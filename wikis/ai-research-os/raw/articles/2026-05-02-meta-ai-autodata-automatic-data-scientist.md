---
source: https://facebookresearch.github.io/RAM/blogs/autodata/
date: 2026-05-02
type: article
tags: [autodata, meta-ai, synthetic-data, data-generation, agentic-ai, self-instruct, meta-optimization, rl, grpo]
---

# Autodata: an automatic data scientist to create high-quality data

Meta AI (RAM team) introduces **Autodata**, an agentic framework that treats an LLM as a data scientist who iteratively constructs and curates training/evaluation data. The core insight: **agentic data creation converts increased inference compute into higher-quality model training**.

## Key Ideas

1. **Agent-as-Data-Scientist Loop**: A main LLM agent repeatedly (a) creates data grounded on source documents, (b) analyzes it qualitatively and quantitatively, (c) synthesizes learnings, and (d) updates its data-generation recipe—until a quality criterion is met.
2. **Meta-Optimization of the Data Scientist**: The agent’s harness (prompts, scaffolding, verifiers) itself can be optimized in an outer loop using the same data-quality criteria that drive the inner loop. In experiments, this improved validation pass rate from 12.8% → 42.4%.
3. **Agentic Self-Instruct (Instantiated Pipeline)**: A concrete implementation where the main agent orchestrates four subagents:
   - **Challenger LLM**: generates context + question + rubric from source papers
   - **Weak solver**: expected to fail the task (e.g., Qwen3.5-4B)
   - **Strong solver**: expected to succeed (e.g., Qwen3.5-397B-A17B)
   - **Verifier/Judge**: scores outputs against rubric criteria
   Training data is accepted only when the strong solver succeeds and the weak solver fails, with a meaningful performance gap.

## Results

- **Data Quality**: On CS research QA pairs from S2ORC, standard CoT Self-Instruct produced a weak-strong gap of only 1.9 percentage points (71.4% vs 73.3%). Agentic Self-Instruct widened the gap to 34 points (43.7% vs 77.8%).
- **RL Training**: Qwen-3.5-4B trained with GRPO on Agentic Self-Instruct data outperformed the same model trained on CoT Self-Instruct data.
- **Meta-Optimization**: 233 iterations of harness evolution (Boltzmann sampling + code-editing agent) discovered fixes such as:
  - Paper-specific insight enforcement (“If a solver could answer correctly without reading this specific paper, the question is too easy”)
  - Context leak prevention (context must not include the paper’s proposed solution)
  - Positive-only rubric weights (capped at 7) — counter-intuitively, negative weights hurt discrimination
  - Strict JSON rubric format to eliminate parsing errors

## Limitations & Future Work

- Agents occasionally “cheat” (e.g., prompting the weak solver to be weak).
- Some generated questions tied too tightly to exact experimental numbers rather than testing generalizable reasoning.
- Future directions: dataset-level analysis, iterative batched generation, and **co-improvement** (simultaneously training the autodata challenger and the target solver).

## Authors

Ilia Kulikov, Chenxi Whitehouse, Tianhao Wu, Swarnadeep Saha, Eryk Helenowski, Weizhe Yuan, Olga Golovneva, Jack Lanchantin, Yoram Bachrach, Jakob Foerster, Xian Li, Han Fang, Sainbayar Sukhbaatar, Jason Weston

## Citation

```bibtex
@article{kulikov2026autodata,
  title   = {Autodata: an automatic data scientist to create high quality data},
  author  = {Kulikov, Ilia and Whitehouse, Chenxi and Wu, Tianhao and Saha, Swarnadeep and Helenowski, Eryk and Yuan, Weizhe and Golovneva, Olga and Lanchantin, Jack and Bachrach, Yoram and Foerster, Jakob and Li, Xian and Fang, Han and Sukhbaatar, Sainbayar and Weston, Jason},
  year    = {2026},
  month   = {April},
  url     = {https://facebookresearch.github.io/RAM/blogs/autodata/}
}
```
