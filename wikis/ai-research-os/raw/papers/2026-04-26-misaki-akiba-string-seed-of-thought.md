---
source: https://arxiv.org/abs/2510.21150
date: 2026-04-26
type: paper
tags: [prompting, llm, diversity, probabilistic-instruction-following, generation, iclr-2026]
---

# String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation

**arXiv ID:** [2510.21150](https://arxiv.org/abs/2510.21150) (cs.AI)  
**Authors:** Kou Misaki, Takuya Akiba  
**Venue:** **Accepted to ICLR 2026**

---

## Core Contribution

> We introduce **String Seed of Thought (SSoT)**, a novel prompting method for LLMs that improves **Probabilistic Instruction Following (PIF)**. We define PIF as a task requiring an LLM to select its answer from a predefined set of options, each associated with a specific probability, such that the empirical distribution of the generated answers aligns with the target distribution when prompted multiple times.

---

## Problem: Why PIF Matters

LLMs excel at deterministic tasks but fail at **Probabilistic Instruction Following (PIF)**, causing critical issues:

- **Bias in non-deterministic behaviors** — problematic for:
  - Human-behavior simulation
  - Content diversification
  - Multiplayer games
- **Diversity collapse** — outputs collapse into a limited set of answers
- **Harm to test-time scaling** — reduced diversity undermines performance gains from increased inference-time computation

---

## Method: How SSoT Works

SSoT is a **simple prompting method** that operates in two stages:

1. **Entropy Generation:** Instructs the LLM to first output a **random string** to generate sufficient entropy
2. **Constrained Derivation:** Instructs the LLM to **extract randomness by manipulating this string** to derive a final answer

**Key Property:** Preserves diversity while adhering to specific constraints.

---

## Key Results

- **PIF Performance:** SSoT significantly improves PIF performance, approaching the **ideal performance of a pseudo-random number generator**
- **Generalization beyond closed-set tasks:** Experiments on **NoveltyBench** demonstrate benefits extend to **open-ended tasks** by enhancing response diversity

---

## Access Paper

- **[View PDF](https://arxiv.org/pdf/2510.21150)**
- **[HTML (experimental)](https://arxiv.org/html/2510.21150v3)**
