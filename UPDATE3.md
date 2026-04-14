# 🧠 Final Project: The Paradox of Authorial Identity — Checklist Responses

## 1. Final Synthesis of Decay (RQ1 & RQ2)

### Which features are replaced first?

Our analysis shows that **stylistic features decay first**, while **semantic content remains relatively stable**.

Evidence:
- POS-tag distributions and syntactic structures change significantly across iterations (T0 → T3)
- t-SNE visualization shows rapid movement away from the human region
- Semantic metrics (BERTScore, BLEU, ROUGE) decline more slowly
- Named Entity Recognition (NER) indicates that core entities are partially preserved

Conclusion:
> The "planks" of style are replaced early, while the semantic "hull" remains intact longer.

---

### Does the "Ship" survive to T3?

Partially.

- The **meaning of the text survives**
- The **stylistic identity of the author is lost**

Conclusion:
> The ship survives in meaning, but not in stylistic identity.

---

### Point of No Return (RQ2)

We observe that the **point of no return occurs between T1 and T2**.

- Stylometric features diverge strongly after T1
- t-SNE shows convergence toward machine-like clusters
- Strong paraphrasers (e.g., Dipper-high) cause identity loss as early as T1

Conclusion:
> The original author’s stylistic DNA becomes undetectable after T2 for most models, and even earlier for aggressive paraphrasers.

---

## 2. Multi-Modal Audit Results

### Structural vs Lexical Analysis

We compare:
- Structural features (syntax, dependency)
- Lexical features (word choice, BLEU/ROUGE)

Findings:

- Vocabulary (lexical "skin") changes the fastest
- Syntax (structural "skeleton") is more stable but still degrades
- Semantic meaning remains the most stable

Conclusion:
> The "skin" (words) changes first, followed by the "skeleton" (syntax), while meaning persists the longest.

---

## 3. "Decay" Dashboard

We implemented a visualization-based analysis pipeline that allows comparison across iterations:

- t-SNE identity trajectory
- Semantic decay curves (BERTScore, BLEU, ROUGE)
- Entity retention curves (NER)

These components collectively simulate a **"style-drift dashboard"**, enabling users to observe how text evolves from T0 to T3.

---

## 4. Forensic Conclusions

### Core Question

If every linguistic marker is replaced by an AI, but meaning remains — who is the author?

---

### Findings

- Stylistic identity is rapidly replaced by machine-generated patterns
- Semantic intent is partially preserved across iterations
- Different models produce distinct stylistic transformations

---

### Interpretation

> Authorship becomes ambiguous once stylistic features are replaced.

> While the original semantic intent may persist, the linguistic realization is fully controlled by the paraphrasing model.

---

### Final Insight

> The author of the meaning may remain human, but the author of the expression becomes the machine.

> This reveals the paradox: identity is tied more to style than meaning.

---

## 5. Deliverables Confirmation

We have completed all required deliverables:

- Stylometric analysis (POS, syntax)
- Semantic similarity analysis (BERTScore, BLEU, ROUGE)
- Identity trajectory visualization (t-SNE)
- Named entity analysis (NER)
- Paraphraser fingerprint analysis
- Fully reproducible code pipeline

---

## 📊 Key Takeaways

1. Style decays faster than content
2. Meaning survives multiple paraphrasing iterations
3. Strong paraphrasers erase identity earlier
4. Each model leaves a distinct fingerprint
5. Authorship becomes ambiguous once style is replaced