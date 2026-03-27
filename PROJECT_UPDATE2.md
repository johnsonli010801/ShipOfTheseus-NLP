# Project Update 2: Forensic Auditing & Identity Drift

## Overview
This project investigates how iterative AI paraphrasing affects linguistic style and author identity. We analyze text across multiple paraphrasing stages (T0 → T3) and across multiple paraphrasers (ChatGPT, PaLM, Dipper, Pegasus).

Our goal is to measure:
- Linguistic decay (style change)
- Identity drift (embedding shift)
- Content preservation vs distortion
- Paraphraser-specific stylistic fingerprints

---

## Checklist Completion

### 1. Stylometric Profiling (Linguistic Decay)

We measure stylistic drift using:
- POS-tag frequency vectors
- Dependency tree depth

**Findings:**
- Cosine similarity between T0 and later stages consistently decreases across iterations.
- Strong paraphrasers (e.g., Dipper(high)) show the largest POS drift.
- Dependency depth changes indicate increasing syntactic restructuring.

**Interpretation:**
Repeated paraphrasing progressively alters linguistic style, with stronger models inducing more aggressive structural changes.

---

### 2. Identity Trajectory (t-SNE Visualization)

We project POS feature vectors into 2D space using t-SNE, tracking text evolution from T0 → T3.

**Findings:**
- Dipper(high) shows clear trajectory drift:
  - T3 points cluster into a compressed region
  - Indicates strong stylistic convergence toward a "machine-like" style
- Pegasus(slight) and Dipper(low):
  - Minimal movement across stages
  - Strong preservation of original stylistic identity
- ChatGPT, PaLM, Pegasus(full):
  - Moderate drift

**Interpretation:**
Text moves from a diverse human distribution toward a more compressed machine region, with drift strength depending on paraphraser intensity.

---

### 3. The "Point of No Return"

We identify the iteration where original authorship becomes indistinguishable.

**Findings:**
- Significant drop in cosine similarity occurs around T2–T3
- t-SNE shows increasing overlap between stages at later iterations
- Strong paraphrasers (especially Dipper(high)) accelerate this process

**Conclusion:**
The point of no return occurs around T2–T3, where stylistic signals of the original author become difficult to recover.

---

### 4. Paraphraser Fingerprints

We analyze whether paraphrasers produce distinguishable stylistic patterns.

**Findings:**
- Dipper(high):
  - Strongest stylistic drift
  - Produces compressed clusters in embedding space
- Pegasus(slight):
  - Minimal change, preserves structure
- ChatGPT / PaLM / Pegasus(full):
  - Moderate drift
- Dipper(low):
  - Weak drift, similar to Pegasus(slight)

**Conclusion:**
Each paraphraser leaves a distinct stylistic fingerprint, making model identification feasible based on linguistic features.

---

### 5. LMS Preparation

- Drafting of ACL-style report has begun
- Results from Tasks 2 and 3 have been integrated
- Visualizations and quantitative findings are ready for inclusion

---

## Key Outputs

- POS cosine similarity (T0 → T3)
- Entity Recall / Precision metrics
- Dependency depth statistics
- t-SNE visualizations (per model)
- Trajectory summary table

---

## Summary Insight

Repeated paraphrasing pushes text away from its original stylistic identity toward a compressed, machine-like distribution. The rate and severity of this drift depend strongly on the paraphraser used.

---

## Status

- All checklist items completed ✔
- Ready for presentation ✔