# 🧠 Ship of Theseus: Computational Forensics of Authorial Identity

## 📌 Project Overview

This project investigates the "Ship of Theseus" Paradox in the context of text paraphrasing.  
Using the Ship of Theseus Paraphrased Corpus, we analyze how a human-authored document evolves through multiple rounds of AI paraphrasing:

T0 (Human) → T1 → T2 → T3

Each iteration replaces parts of the text’s stylistic identity ("planks") while attempting to preserve its semantic meaning ("hull").

We aim to quantify:

- How quickly style decays
- Whether meaning survives
- When authorship identity is lost
- Whether different paraphrasers leave detectable fingerprints

---

## 🎯 Research Questions

### RQ1 — Style vs. Content Decay  
Which features are replaced first?

- Stylistic Features  
  - POS-tag distributions  
  - Dependency structure  

- Semantic Content  
  - BERTScore  
  - BLEU / ROUGE  
  - Named Entities (NER)

---

### RQ2 — Point of No Return  
At what iteration does the original author’s identity become undetectable?

- Measured using:
  - Stylometric drift
  - Embedding trajectory (t-SNE)
  - Feature collapse

---

### RQ3 — Paraphraser Fingerprints  
Can we identify which model generated the paraphrase?

- Models analyzed:
  - ChatGPT  
  - PaLM  
  - Pegasus (slight / full)  
  - Dipper (low / high)

---

## ⚙️ Methodology

### 1. Data Processing
- Parsed the paraphrased corpus into a long-format table
- Each document tracked across:
  - T0, T1, T2, T3
  - paraphraser model
  - dataset source

---

### 2. Stylometric Analysis (Structure / Style)

We extracted:

- POS-tag frequency distributions
- Dependency tree depth
- Sentence structure features

Observation:  
Stylistic features shift significantly from T0 → T3, indicating rapid loss of authorial style.

---

### 3. Semantic Analysis (Content)

We measured similarity between T0 and later stages:

- BERTScore (F1)
- BLEU / ROUGE

Observation:  
Semantic similarity decreases gradually, but remains relatively high compared to stylistic features.

---

### 4. Named Entity Retention (NER)

We extracted entities using spaCy and computed:

- Recall (T0 vs Tx)
- Precision
- Jaccard similarity

Key Finding:

- Entity retention decreases slowly
- Indicates content preservation even when style is lost
- Strong paraphrasers (e.g., Dipper-high) aggressively rewrite entities

---

### 5. Identity Trajectory (t-SNE)

We visualized text representations across iterations using t-SNE.

Observation:

- T0 points are more diverse (human region)
- T3 points are more compressed (machine region)
- Indicates convergence toward a uniform AI style

---

### 6. Paraphraser Behavior Analysis

Each model exhibits distinct patterns:

- ChatGPT → moderate rewriting
- PaLM → moderate rewriting
- Pegasus (slight) → high content preservation
- Pegasus (full) → balanced rewriting
- Dipper (low) → moderate rewriting
- Dipper (high) → aggressive rewriting

---

## 📊 Key Findings

### ✔ Linguistic Decay
- Style decays faster than content
- POS and syntax drift rapidly across iterations

---

### ✔ Identity Trajectory
- Text shifts from a diverse human region
- Toward a compressed machine-like cluster

---

### ✔ Point of No Return
- Occurs around T2 for strong paraphrasers
- Original stylistic identity becomes indistinguishable

---

### ✔ Paraphraser Fingerprints
- Models are distinguishable based on:
  - Entity retention
  - Structural drift
  - Semantic preservation

---

## 🧠 Interpretation: The Paradox

Even when:

- Most stylistic features are replaced  
- Syntax is transformed  
- Vocabulary is rewritten  

The semantic core (meaning) often remains intact.

This leads to the central paradox:

"If every linguistic marker is replaced, but meaning survives — who is the author?"

---

## 📁 Repository Structure

.
├── data/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_baseline_similarity.ipynb
│   ├── 03_stylometry_analysis.ipynb
│   ├── update2.ipynb
│   └── final_update_ner.ipynb
├── figures/
├── src/
├── README.md

---

## 🧪 Reproducibility

To reproduce results:

pip install -r requirements.txt

Run notebooks in order:

1. Data ingestion  
2. Similarity baseline  
3. Stylometric analysis  
4. Identity trajectory  
5. NER analysis  

---

## 🧑‍🤝‍🧑 Team Roles

- Lead Architect — Data pipeline & repo structure  
- Linguistic Scientist — Stylometric features  
- Similarity Analyst — BERTScore / semantic analysis  
- Forensics Lead — Attribution & drift  
- Technical Editor — ACL paper & formatting  

---

## 📦 Deliverables

- Stylometric analysis  
- Semantic similarity analysis  
- Identity trajectory visualization  
- Paraphraser fingerprint analysis  
- Reproducible code pipeline  

---

## 🚀 Conclusion

This project demonstrates that:

- Style is fragile and easily replaced  
- Meaning is resilient across paraphrasing  
- AI paraphrasing creates a convergent machine identity space  

Ultimately, the Ship of Theseus paradox extends to language:

A text can lose all traces of its original author — yet still remain "the same" in meaning.