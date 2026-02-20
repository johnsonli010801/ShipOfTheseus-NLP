from __future__ import annotations
from pathlib import Path
import pandas as pd

def load_processed_iteration(root: Path, iteration_dir: str, dataset: str) -> pd.DataFrame:
    path = root / "data" / "processed" / iteration_dir / f"{dataset}.csv"
    return pd.read_csv(path)

def list_datasets(root: Path) -> list[str]:
    d = root / "data" / "processed" / "t0_human"
    return sorted([p.stem for p in d.glob("*.csv")])