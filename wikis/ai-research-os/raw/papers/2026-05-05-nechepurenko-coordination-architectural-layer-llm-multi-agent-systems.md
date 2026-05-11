---
source: https://arxiv.org/abs/2605.03310
date: 2026-05-05
type: paper
tags: [multi-agent-systems, coordination, architecture, prediction-markets, agent-failures, ai-agents]
status: processed
---

# Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems

## Source metadata

- **arXiv ID:** 2605.03310v1
- **URL:** https://arxiv.org/abs/2605.03310
- **PDF:** https://arxiv.org/pdf/2605.03310
- **Authors:** Maksym Nechepurenko, Pavel Shuvalov
- **Published:** 2026-05-05
- **Categories:** cs.MA, cs.LG, q-fin.TR
- **Comment:** 31 pages, 7 figures, 4 tables. Code, traces, and production agents publicly released; see Appendix B for repository pinning

## Abstract summary

The paper argues that multi-agent LLM systems often fail because of coordination defects rather than base-model capability. It treats coordination as a configurable architectural layer, separable from agent logic and information access. The authors instantiate this using prediction markets: a single LLM, fixed tools, fixed output cap, and fixed prompt template across five coordination configurations. Using Murphy decomposition of Brier score, they show different coordination configurations leave distinguishable signatures even when aggregate scores coincide. The study reports results on 100 Polymarket binary markets resolved after the model training cutoff and deploys the same configurations as live agents on Foresight Arena as a replication channel.

## Why this matters for Self-OS / Hermes

This paper gives Self-OS a more rigorous vocabulary for agent architecture. Instead of treating Kanban, delegation, cron, and goal loops as implementation conveniences, it suggests coordination should be measured as a layer with failure signatures, cost-quality Pareto behavior, and task-conditioned performance. This is especially relevant for future Hermes work on orchestration diagnostics, task graph choices, and production failure analysis.

## Notes for later synthesis

- Treat this as a raw paper capture; compile can later promote it into source summaries and concepts.
- Cross-link candidates: agent orchestration, agent memory, multi-agent coordination, agentic harnesses, agent-readable tools, reward/evaluation loops.
- Useful for future work on Hermes Kanban, goal loops, task graph design, skill consolidation, and Self-OS operating memory.
