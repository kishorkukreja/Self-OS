---
source: https://arxiv.org/abs/2512.04388
date: 2025-12-04
type: paper
tags: [multi-agent-systems, agent-orchestration, reinforcement-learning, conductor-model, test-time-scaling, ai-agents]
status: processed
---

# Learning to Orchestrate Agents in Natural Language with the Conductor

## Source metadata

- **arXiv ID:** 2512.04388v5
- **URL:** https://arxiv.org/abs/2512.04388
- **PDF:** https://arxiv.org/pdf/2512.04388
- **Authors:** Stefan Nielsen, Edoardo Cetin, Peter Schwendeman, Qi Sun, Jinglue Xu, Yujin Tang
- **Published:** 2025-12-04
- **Categories:** cs.LG
- **Comment:** To appear at ICLR 2026

## Abstract summary

Powerful large language models from different providers have been trained and finetuned to specialize across domains. This work introduces a Conductor model trained with reinforcement learning to discover coordination strategies among LLMs. The Conductor learns targeted communication topologies for agent collaboration and prompt-engineers focused instructions to leverage individual worker capabilities. A 7B Conductor achieves performance gains beyond any individual worker on reasoning benchmarks including LiveCodeBench and GPQA. Training with randomized agent pools helps it adapt to arbitrary sets of open- and closed-source agents. Allowing the Conductor to select itself as a worker creates recursive topologies and a form of dynamic test-time scaling through online iterative adaptation.

## Why this matters for Self-OS / Hermes

This is a strong conceptual match for Hermes Kanban and future multi-profile orchestration. It suggests the orchestrator role itself can be learned and optimized, not just hand-coded. For Self-OS, the paper is relevant to task graph design, specialist profile routing, agent pool selection, and whether an orchestrator should dynamically choose communication topology instead of always using fixed researcher → analyst → writer pipelines.

## Notes for later synthesis

- Treat this as a raw paper capture; compile can later promote it into source summaries and concepts.
- Cross-link candidates: agent orchestration, agent memory, multi-agent coordination, agentic harnesses, agent-readable tools, reward/evaluation loops.
- Useful for future work on Hermes Kanban, goal loops, task graph design, skill consolidation, and Self-OS operating memory.
