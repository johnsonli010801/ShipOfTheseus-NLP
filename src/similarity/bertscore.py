# src/similarity/bertscore.py
from __future__ import annotations
import numpy as np
import pandas as pd
from bert_score import score as bert_score

def compute_bertscore_pairs(
    pairs: pd.DataFrame,
    model_type: str = "distilroberta-base",
    batch_size: int = 64,
    device: str | None = None,
) -> pd.DataFrame:
    cands = pairs["text_tn"].tolist()
    refs  = pairs["text_t0"].tolist()

    P, R, F1 = bert_score(
        cands=cands,
        refs=refs,
        lang="en",
        model_type=model_type,
        rescale_with_baseline=True,
        batch_size=batch_size,
        device=device,
        verbose=True,
    )

    tmp = pairs[["paraphraser","iteration"]].copy()
    tmp["f1"] = F1.cpu().numpy()

    out = (
        tmp.groupby(["paraphraser","iteration"])["f1"]
           .agg(["mean","std","count"])
           .reset_index()
           .rename(columns={"count":"n"})
    )
    out["metric"] = "bertscore_f1"
    return out[["paraphraser","iteration","metric","mean","std","n"]].sort_values(["paraphraser","iteration"])