# Project Update 1 – The "First Planks"
## Ship of Theseus: Data & Baseline Similarity Analysis

---

## Overview

This update establishes the baseline similarity framework for analyzing iterative paraphrasing in the Ship of Theseus corpus.

We compare lexical and semantic similarity between original human-written texts (T0) and three iterative paraphrasing stages (T1–T3).

The core research question:

Does semantic meaning (the “hull”) remain intact while lexical and stylistic elements (the “planks”) gradually change?

---

## Dataset

Corpus: Ship of Theseus (processed version)

Subsets analyzed:

- yelp
- xsum
- sci_gen
- cmv
- tldr
- wp
- elis

We restricted evaluation to the `test` split for consistency.

Iterations included:

- T0 (Original Human Text)
- T1
- T2
- T3

Paraphrasers:

- ChatGPT
- Dipper
- PaLM
- Pegasus

---

## Data Processing

1. Loaded processed iteration files using `load_processed_iteration`
2. Filtered for `split="test"`
3. Created unique `doc_id = dataset|key`
4. Merged T0 with T1, T2, T3
5. Constructed aligned T0–Tn comparison pairs
6. Trimmed text length to reduce memory usage
7. Removed empty candidate sentences
8. Enabled GPU acceleration for semantic similarity computation

Final dataset size:
~400,000 aligned T0–Tn pairs

---

## Baseline Similarity Metrics

### Lexical Metrics

- ROUGE-L
- ROUGE-1

These measure surface word overlap.

### Semantic Metric

- BERTScore-F1 (distilroberta-base)

This measures contextual embedding similarity.

---

## Key Findings

1. ROUGE decreases steadily from T1 to T3.
2. BERTScore declines more gradually.
3. Semantic similarity is more stable than lexical overlap.
4. Pegasus maintains relatively high semantic preservation.
5. Dipper shows stronger lexical erosion.

Interpretation:

Lexical form changes more rapidly than semantic content.

This supports the "Hull vs Planks" hypothesis:
Meaning remains relatively stable while stylistic identity erodes.

---

## Technical Stack

- Python 3.12
- PyTorch with CUDA (RTX 3070 GPU)
- transformers
- bert_score
- rouge_score
- pandas
- pathlib
- Jupyter Notebook

Optimization techniques:

- GPU acceleration
- Batch embedding computation
- Memory trimming
- Efficient group-level aggregation

---

## Next Phase: Stylometric Audit

Planned analyses:

- Dependency tree depth
- POS distribution comparison
- Sentence complexity metrics
- Function word frequency tracking
- Stylometric clustering across iterations

Goal:

Quantify the degradation of authorial identity beyond lexical similarity.

---

## Deliverables

1. Slide Deck (10-minute team presentation)
2. Baseline Python Notebook
3. ACM-format Project Report (max 5 pages)

---