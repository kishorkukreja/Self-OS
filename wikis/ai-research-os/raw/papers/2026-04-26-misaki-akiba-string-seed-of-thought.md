---
status: processed
---
     1|---
     2|source: https://arxiv.org/abs/2510.21150
     3|date: 2026-04-26
     4|type: paper
     5|tags: [prompting, llm, diversity, probabilistic-instruction-following, generation, iclr-2026]
     6|---
     7|
     8|# String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation
     9|
    10|**arXiv ID:** [2510.21150](https://arxiv.org/abs/2510.21150) (cs.AI)  
    11|**Authors:** Kou Misaki, Takuya Akiba  
    12|**Venue:** **Accepted to ICLR 2026**
    13|
    14|---
    15|
    16|## Core Contribution
    17|
    18|> We introduce **String Seed of Thought (SSoT)**, a novel prompting method for LLMs that improves **Probabilistic Instruction Following (PIF)**. We define PIF as a task requiring an LLM to select its answer from a predefined set of options, each associated with a specific probability, such that the empirical distribution of the generated answers aligns with the target distribution when prompted multiple times.
    19|
    20|---
    21|
    22|## Problem: Why PIF Matters
    23|
    24|LLMs excel at deterministic tasks but fail at **Probabilistic Instruction Following (PIF)**, causing critical issues:
    25|
    26|- **Bias in non-deterministic behaviors** — problematic for:
    27|  - Human-behavior simulation
    28|  - Content diversification
    29|  - Multiplayer games
    30|- **Diversity collapse** — outputs collapse into a limited set of answers
    31|- **Harm to test-time scaling** — reduced diversity undermines performance gains from increased inference-time computation
    32|
    33|---
    34|
    35|## Method: How SSoT Works
    36|
    37|SSoT is a **simple prompting method** that operates in two stages:
    38|
    39|1. **Entropy Generation:** Instructs the LLM to first output a **random string** to generate sufficient entropy
    40|2. **Constrained Derivation:** Instructs the LLM to **extract randomness by manipulating this string** to derive a final answer
    41|
    42|**Key Property:** Preserves diversity while adhering to specific constraints.
    43|
    44|---
    45|
    46|## Key Results
    47|
    48|- **PIF Performance:** SSoT significantly improves PIF performance, approaching the **ideal performance of a pseudo-random number generator**
    49|- **Generalization beyond closed-set tasks:** Experiments on **NoveltyBench** demonstrate benefits extend to **open-ended tasks** by enhancing response diversity
    50|
    51|---
    52|
    53|## Access Paper
    54|
    55|- **[View PDF](https://arxiv.org/pdf/2510.21150)**
    56|- **[HTML (experimental)](https://arxiv.org/html/2510.21150v3)**
    57|