---
url: https://arxiv.org/abs/2604.16529
saved: 2026-04-28
paper_title: Scaling Test-Time Compute for Agentic Coding
arXiv: 2604.16529 (v1, submitted 16 Apr 2026)
license: CC BY-NC-SA 4.0
pages: 70 pages, 26 figures, 12 tables
status: processed
---
# Scaling Test-Time Compute for Agentic Coding

## Authors
Joongwon Kim, Wannan Yang, Kelvin Niu, Hongming Zhang, Yun Zhu, Eryk Helenowski, Ruan Silva, Zhengxing Chen, Srinivasan Iyer, Manzil Zaheer, Daniel Fried, Hannaneh Hajishirzi, Sanjeev Arora, Gabriel Synnaeve, Ruslan Salakhutdinov, Anirudh Goyal

## Abstract

Test-time scaling has become a powerful way to improve large language models. However, existing methods are best suited to short, bounded outputs that can be directly compared, ranked or refined. Long-horizon coding agents violate this premise: each attempt produces an extended trajectory of actions, observations, errors, and partial progress taken by the agent.

In this setting, the main challenge is **no longer generating more attempts, but representing prior experience in a form that can be effectively selected from and reused**.

We propose a test-time scaling framework for agentic coding based on **compact representations of rollout trajectories**. Our framework converts each rollout into a structured summary that preserves its salient hypotheses, progress, and failure modes while discarding low-signal trace details.

## Two Complementary Forms of Inference-Time Scaling

### 1. Parallel Scaling: Recursive Tournament Voting (RTV)

Recursively narrows a population of rollout summaries through small-group comparisons.

### 2. Sequential Scaling: Parallel-Distill-Refine (PDR)

Adapted to the agentic setting by conditioning new rollouts on summaries distilled from prior attempts.

## Results

**Claude-4.5-Opus gains on SWE-Bench Verified (mini-SWE-agent):**
- Baseline: **70.9%** → With RTV/PDR: **77.6%**

**Claude-4.5-Opus gains on Terminal-Bench v2.0 (Terminus 1):**
- Baseline: **46.9%** → With RTV/PDR: **59.1%**

## Key Insight

> "Test-time scaling for long-horizon agents is fundamentally a problem of **representation, selection, and reuse** — not just generating more attempts."

## Why It Matters

This paper directly addresses a core challenge in agentic coding: brute-force test-time compute (generating more rollouts) hits diminishing returns when each rollout is a long, stateful trajectory. By compressing trajectories into reusable structured summaries, RTV and PDR enable genuine scaling — where more compute translates to better selection and refinement rather than just more noise. Essential reading for anyone building autonomous coding agents.

## Categories

- cs.SE (Software Engineering)
- cs.AI (Artificial Intelligence)
- cs.CL (Computation and Language)
- cs.LG (Machine Learning)

## Citation

```bibtex
@misc{kim2026scalingtesttimecomputeagentic,
      title={Scaling Test-Time Compute for Agentic Coding},
      author={Joongwon Kim and Wannan Yang and Kelvin Niu and Hongming Zhang and Yun Zhu and Eryk Helenowski and Ruan Silva and Zhengxing Chen and Srinivasan Iyer and Manzil Zaheer and Daniel Fried and Hannaneh Hajishirzi and Sanjeev Arora and Gabriel Synnaeve and Ruslan Salakhutdinov and Anirudh Goyal},
      year={2026},
      eprint={2604.16529},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2604.16529},
}
```
