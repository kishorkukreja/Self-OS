---
title: "Scaling Test-Time Compute for Agentic Coding"
date_created: 2026-04-29
date_modified: 2026-04-29
summary: "Scaling Test-Time Compute for Agentic Coding captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, "
tags: [coding-agents, agent-orchestration]
type: source
status: final
---

# Scaling Test-Time Compute for Agentic Coding

**Type:** repo  
**Date:** 2026-04-28  
**URL:** https://arxiv.org/abs/2604.16529  
**Raw file:** [[../../raw/repos/scaling-test-time-compute-agentic-coding-2026-04-28.md]]

**Summary:** Scaling Test-Time Compute for Agentic Coding captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and design trade-offs that can be compared against the rest of the AI Research OS corpus. Scaling Test-Time Compute for Agentic Coding Joongwon Kim, Wannan Yang, Kelvin Niu, Hongming Zhang, Yun Zhu, Eryk Helenowski, Ruan Silva, Zhengxing Chen, Srinivasan Iyer, Manzil Zaheer, Daniel Fried, Hannaneh Hajishirzi, Sanjeev Arora, Gabriel Synnaeve, Ruslan Salakhutdinov, Anirudh Goyal Test-time scaling has become a powerful way to improve large language models. However, existing methods are best suited to short, bounded outputs that can be directly compared, ranked or refined. Long-horizon coding agents violate this premise: each attempt produces an extended trajectory of actions, observations, errors, and partial progress taken by the agent. In this setting, the main challenge is no longer generating more attempts, but representing prior experience in a form that can be effectively selected from and reused. We propose a test-time scaling framework for agentic coding based on compact representations of rollout trajectories. Our framework converts each rollout into a structured summary that preserves its salient hypotheses, progress, and…

**Key contributions:**
- Scaling Test-Time Compute for Agentic Coding
- In this setting, the main challenge is no longer generating more attempts, but representing prior experience in a form that can be effectively selected from and reused.
- Two Complementary Forms of Inference-Time Scaling
- 1. Parallel Scaling: Recursive Tournament Voting (RTV)
- Recursively narrows a population of rollout summaries through small-group comparisons.

**Related concepts:** [[concepts/coding-agents]], [[concepts/agent-orchestration]]  
**Primary entity:** [[entities/scaling-test-time-compute-for-agentic-coding]]

**Tags:** coding-agents, agent-orchestration
