from rouge_score import rouge_scorer
import numpy as np
import pandas as pd

def compute_rougel_pairs(pairs: pd.DataFrame) -> pd.DataFrame:
    scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)

    rows = []
    for (paraphraser, iteration), g in pairs.groupby(["paraphraser", "iteration"], sort=False):
        scores = [
            scorer.score(a, b)["rougeL"].fmeasure
            for a, b in zip(g["text_t0"], g["text_tn"])
        ]
        rows.append({
            "paraphraser": paraphraser,
            "iteration": iteration,
            "metric": "rougeL_f",
            "mean": float(np.mean(scores)),
            "std": float(np.std(scores)),
            "n": int(len(scores)),
        })
    return pd.DataFrame(rows).sort_values(["paraphraser", "iteration"])