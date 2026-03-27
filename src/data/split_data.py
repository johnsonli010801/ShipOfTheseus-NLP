from __future__ import annotations
from pathlib import Path
import re, json
import pandas as pd

# -------- parsing helpers --------

def _normalize_cols(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    # unify version col name
    if "version" not in df.columns and "version_name" in df.columns:
        df = df.rename(columns={"version_name": "version"})
    # unify required cols
    needed = ["source", "key", "text", "version"]
    missing = [c for c in needed if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns {missing}. Got columns={df.columns.tolist()}")
    # strip strings
    for c in ["source", "key", "text", "version"]:
        df[c] = df[c].astype(str)
    df["source"] = df["source"].str.strip()
    df["key"] = df["key"].str.strip()
    df["version"] = df["version"].str.strip()
    return df

def _paraphraser_family(version: str) -> str:
    v = (version or "").strip().lower()
    if v in ["", "original", "nan", "none"]:
        return "none"
    # take first token before '_' and remove modifiers like "(full)" "(slight)" "(low)" "(high)"
    first = v.split("_")[0]
    m = re.match(r"([a-z0-9]+)", first)
    base = m.group(1) if m else first

    # collapse variants to the 4 required paraphrasers
    if base.startswith("dipper"):
        return "dipper"
    if base.startswith("pegasus"):
        return "pegasus"
    if base.startswith("chatgpt"):
        return "chatgpt"
    if base.startswith("palm"):
        return "palm"
    return base  # fallback

def _iteration_from_version(version: str) -> str:
    v = (version or "").strip().lower()
    if v in ["", "original", "nan", "none"]:
        return "t0"
    # count steps by number of tokens separated by "_"
    parts = [p for p in v.split("_") if p]
    return f"t{len(parts)}"

# -------- main export --------

def export_processed_from_raw(root: Path) -> None:
    raw_train = root / "data" / "raw" / "train_datasets"
    raw_para  = root / "data" / "raw" / "paraphrased_datasets"

    if not raw_train.exists() or not raw_para.exists():
        raise FileNotFoundError(
            "Expected raw folders:\n"
            "  data/raw/train_datasets/\n"
            "  data/raw/paraphrased_datasets/\n"
        )

    out_base = root / "data" / "processed"
    out_dirs = {
        "t0": out_base / "t0_human",
        "t1": out_base / "t1_paraphrased",
        "t2": out_base / "t2_paraphrased",
        "t3": out_base / "t3_paraphrased",
    }
    for d in out_dirs.values():
        d.mkdir(parents=True, exist_ok=True)

    meta_dir = root / "data" / "metadata"
    meta_dir.mkdir(parents=True, exist_ok=True)

    datasets = []
    split_stats = {}

    # We build t0..t3 from paraphrased_datasets (it contains Human + paraphrasers + versions)
    for p in sorted(raw_para.glob("*_paraphrased.csv")):
        dataset = p.name.replace("_paraphrased.csv", "")
        datasets.append(dataset)

        df = _normalize_cols(pd.read_csv(p))

        # derive fields
        df["dataset"] = dataset
        df["version"] = df["version"].astype(str)
        df["iteration"] = df["version"].map(_iteration_from_version)
        df["paraphraser"] = df["version"].map(_paraphraser_family)

        # doc_id aligns all iterations of the same original item
        df["doc_id"] = df["dataset"] + "|" + df["key"].astype(str)

        # define split: these paraphrased files are our "test" chain material
        df["split"] = "test"

        # ----- export t0_human -----
        t0 = df[(df["iteration"] == "t0") & (df["source"].str.lower() == "human")].copy()

        # Some datasets may have t0 duplicated across sources; enforce one per key
        t0 = t0.drop_duplicates(subset=["doc_id"], keep="first")

        # ----- export t1/t2/t3 paraphrased -----
        tn = df[df["iteration"].isin(["t1", "t2", "t3"])].copy()
        # keep only the 4 paraphrasers required for Update1
        tn = tn[tn["paraphraser"].isin(["chatgpt", "palm", "pegasus", "dipper"])]

        # columns to save (clean & consistent)
        cols_t0 = ["dataset","doc_id","key","text","source","version","iteration","paraphraser","split"]
        cols_tn = ["dataset","doc_id","key","text","source","version","iteration","paraphraser","split"]

        (out_dirs["t0"] / f"{dataset}.csv").write_text("")  # ensure file exists even if empty

        t0[cols_t0].to_csv(out_dirs["t0"] / f"{dataset}.csv", index=False)

        for it in ["t1","t2","t3"]:
            part = tn[tn["iteration"] == it][cols_tn]
            part.to_csv(out_dirs[it] / f"{dataset}.csv", index=False)

        split_stats[dataset] = {
            "t0_human": int(len(t0)),
            "t1": int((tn["iteration"]=="t1").sum()),
            "t2": int((tn["iteration"]=="t2").sum()),
            "t3": int((tn["iteration"]=="t3").sum()),
        }

    datasets = sorted(set(datasets))

    # paraphraser labels metadata (fixed 4)
    with open(meta_dir / "paraphraser_labels.json", "w", encoding="utf-8") as f:
        json.dump({"paraphrasers": ["chatgpt","palm","pegasus","dipper"]}, f, indent=2)

    with open(meta_dir / "dataset_splits.json", "w", encoding="utf-8") as f:
        json.dump({"datasets": datasets, "counts": split_stats}, f, indent=2)

    print("Done. Exported to data/processed/t0_human..t3_paraphrased and data/metadata/")

if __name__ == "__main__":
    ROOT = Path(__file__).resolve().parents[2]
    export_processed_from_raw(ROOT)