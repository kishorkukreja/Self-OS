---
source: https://arxiv.org/abs/2605.03808
date: 2026-05-05
type: paper
tags: [agentic-data-science, interpretability, autoresearch, tabular-ml, agent-tools, ai-agents]
---

# Agentic-imodels: Evolving agentic interpretability tools via autoresearch

## Source metadata

- **arXiv ID:** 2605.03808v1
- **URL:** https://arxiv.org/abs/2605.03808
- **PDF:** https://arxiv.org/pdf/2605.03808
- **Authors:** Chandan Singh, Yan Shuo Tan, Weijia Xu, Zelalem Gero, Weiwei Yang, Michel Galley, Jianfeng Gao
- **Published:** 2026-05-05
- **Categories:** cs.AI, cs.CL, cs.LG
- **Comment:** Not specified

## Abstract summary

Agentic data science systems are improving at autonomously analyzing, fitting, and interpreting data, but current ADS systems use statistical tools designed for humans rather than agents. This paper introduces Agentic-imodels, an agentic autoresearch loop that evolves data-science tools designed to be interpretable by agents. It develops scikit-learn-compatible regressors for tabular data optimized for both predictive performance and an LLM-based interpretability metric. The metric tests whether a fitted model's string representation is simulatable by an LLM: can the LLM answer questions about the model's behavior from the string output alone? The evolved models improve predictive performance and agent-facing interpretability, generalize to new datasets and tests, and improve downstream agentic data science performance for Copilot CLI, Claude Code, and Codex on BLADE by up to 73%.

## Why this matters for Self-OS / Hermes

This is directly relevant to agent tooling design. The key shift is from human-interpretable artifacts to agent-interpretable artifacts. For Self-OS/Hermes, that principle applies beyond tabular models: CLI outputs, Kanban task summaries, wiki source captures, mission files, reward-cycle notes, and eval results should be designed so agents can simulate and reason over them reliably.

## Notes for later synthesis

- Treat this as a raw paper capture; compile can later promote it into source summaries and concepts.
- Cross-link candidates: agent orchestration, agent memory, multi-agent coordination, agentic harnesses, agent-readable tools, reward/evaluation loops.
- Useful for future work on Hermes Kanban, goal loops, task graph design, skill consolidation, and Self-OS operating memory.
