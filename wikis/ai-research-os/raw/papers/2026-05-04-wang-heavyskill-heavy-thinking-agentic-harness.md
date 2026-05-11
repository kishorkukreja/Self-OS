---
source: https://arxiv.org/abs/2605.02396
date: 2026-05-04
type: paper
tags: [agentic-harness, heavy-thinking, multi-agent-reasoning, reinforcement-learning, self-evolving-llms, ai-agents]
status: processed
---

# HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness

## Source metadata

- **arXiv ID:** 2605.02396v1
- **URL:** https://arxiv.org/abs/2605.02396
- **PDF:** https://arxiv.org/pdf/2605.02396
- **Authors:** Jianing Wang, Linsen Guo, Zhengyu Chen, Qi Guo, Hongyu Zang, Wenjie Shi, Haoxiang Ma, Xiangyu Xi, Xiaoyu Li, Wei Wang, Xunliang Cai
- **Published:** 2026-05-04
- **Categories:** cs.AI
- **Comment:** 18 pages, 10 figures

## Abstract summary

Recent advances in agentic harness with orchestration frameworks that coordinate multiple agents with memory, skills, and tool use have achieved remarkable success in complex reasoning tasks. However, the underlying mechanism that truly drives performance remains obscured behind intricate system designs. In this paper, we propose HeavySkill, a perspective that views heavy thinking not only as a minimal execution unit in orchestration harness but also as an inner skill internalized within the model's parameters that drives the orchestrator to solve complex tasks. We identify this skill as a two-stage pipeline, i.e., parallel reasoning then summarization, which can operate beneath any agentic harness. We present a systematic empirical study of HeavySkill across diverse domains. Our results show that this inner skill consistently outperforms traditional Best-of-N (BoN) strategies; notably, stronger LLMs can even approach Pass@N performance. Crucially, we demonstrate that the depth and width of heavy thinking, as a learnable skill, can be further scaled via reinforcement learning, offering a promising path toward self-evolving LLMs that internalize complex reasoning without relying on brittle orchestration layers.

## Why this matters for Self-OS / Hermes

This is directly relevant to Hermes/Self-OS because it questions whether complex external orchestration is always the real source of gains. The paper frames heavy thinking itself as an internal skill: parallel reasoning followed by summarization. That maps onto current Hermes patterns such as subagent fan-out/fan-in, Kanban researcher-to-analyst pipelines, and goal-buddy review loops. The useful lesson is to treat orchestration not as magic infrastructure but as a repeatable reasoning primitive that can be benchmarked, trained, and possibly internalized.

## Notes for later synthesis

- Treat this as a raw paper capture; compile can later promote it into source summaries and concepts.
- Cross-link candidates: agent orchestration, agent memory, multi-agent coordination, agentic harnesses, agent-readable tools, reward/evaluation loops.
- Useful for future work on Hermes Kanban, goal loops, task graph design, skill consolidation, and Self-OS operating memory.
