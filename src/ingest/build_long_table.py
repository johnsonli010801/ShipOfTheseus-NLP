import re
from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]  # project root
DATA_RAW = ROOT / "data"
TRAIN_DIR = DATA_RAW / "train_datasets"
TEST_DIR = DATA_RAW / "paraphrased_datasets"
OUT_PATH = ROOT / "data" / "processed" / "theseus_long.csv"


def infer_dataset_name(filename: str) -> str:
    # e.g., "xsum_paraphrased.csv" -> "xsum"
    return filename.split("_")[0].lower()



def parse_version(version):
    if version is None or (isinstance(version, float) and pd.isna(version)):
        return "t0", "none"

    v = str(version).strip().lower()

    # 兼容拼写错误/空串
    if v == "" or v in ["original", "orignal", "t0", "0"]:
        return "t0", "none"

    # 如果有人直接写成 t1/t2/t3
    m = re.fullmatch(r"t(\d+)", v)
    if m:
        it = int(m.group(1))
        return f"t{it}", "unknown"

    # 主逻辑：chatgpt_chatgpt_chatgpt -> 3 次 -> t3
    parts = [p for p in v.split("_") if p]

    # 处理像 "dipper(low)" / "pegasus(full)"，抽 family
    first = parts[0]
    fam = re.match(r"([a-z0-9]+)", first)
    family = fam.group(1) if fam else first

    iteration = f"t{len(parts)}"
    return iteration, family


def load_train_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]

    if "version" not in df.columns:
        df["version"] = "original"

    df["split"] = "train"
    df["iteration"], df["paraphraser"] = zip(*df["version"].map(parse_version))

    return df[["source", "key", "text", "split", "version", "iteration", "paraphraser"]]


def load_test_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    # 统一列名：去空格 + 小写
    df.columns = [c.strip().lower() for c in df.columns]

    # rename 到我们内部用的名字
    df = df.rename(columns={"source": "source", "key": "key"})  # 这行可有可无
    # 关键：确保 Source/Key/text/version 都能对应上
    if "source" not in df.columns and "Source" in df.columns:
        df = df.rename(columns={"Source": "source"})
    if "key" not in df.columns and "Key" in df.columns:
        df = df.rename(columns={"Key": "key"})

    # 兼容你的列名：version_name
    if "version" not in df.columns and "version_name" in df.columns:
        df = df.rename(columns={"version_name": "version"})

    df["split"] = "test"
    df["iteration"], df["paraphraser"] = zip(*df["version"].map(parse_version))

    # 有些 csv 的正文列可能叫 Text 或 content，这里也防一下
    if "text" not in df.columns:
        for alt in ["content", "sentence", "doc", "document"]:
            if alt in df.columns:
                df = df.rename(columns={alt: "text"})
                break

    return df[["source", "key", "text", "split", "version", "iteration", "paraphraser"]]


def main():
    out_dir = OUT_PATH.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    frames = []

    # train
    for p in sorted(TRAIN_DIR.glob("*_train.csv")):
        dataset = infer_dataset_name(p.name)
        df = load_train_csv(p)
        df.insert(0, "dataset", dataset)
        frames.append(df)

    # paraphrased/test
    for p in sorted(TEST_DIR.glob("*_paraphrased.csv")):
        dataset = infer_dataset_name(p.name)
        df = load_test_csv(p)
        df.insert(0, "dataset", dataset)
        frames.append(df)

    all_df = pd.concat(frames, ignore_index=True)

    # A stable doc id (one "ship" chain) is typically (dataset, source, key)
    all_df["doc_id"] = (
        all_df["dataset"].astype(str) + "|" +
        all_df["source"].astype(str) + "|" +
        all_df["key"].astype(str)
    )

    # Basic cleanup
    all_df["text"] = all_df["text"].astype(str).str.replace("\r\n", "\n")

    all_df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")
    print(all_df.head(3).to_string(index=False))
    print("\nCounts by dataset/split/iteration (top):")
    print("\nIteration distribution in TEST:")
    print(all_df[all_df["split"]=="test"]["iteration"].value_counts(dropna=False))

    print("\nTop versions in TEST:")
    print(all_df[all_df["split"]=="test"]["version"].astype(str).value_counts().head(20))


if __name__ == "__main__":
    main()