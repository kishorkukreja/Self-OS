---
title: "Learning to Orchestrate Agents in Natural Language with the Conductor"
date_created: 2026-05-11
date_modified: 2026-05-11
summary: "Nielsen et al. introduce a Conductor model trained through reinforcement learning to coordinate pools of LLM workers. Instead of hard-coding one collaboration pattern, the Conductor learns communication topologies and ta"
tags: [agent-orchestration, multi-agent, reinforcement-learning]
type: source
status: final
---

# Learning to Orchestrate Agents in Natural Language with the Conductor

**Type:** paper  
**Date:** 2025-12-04  
**URL:** https://arxiv.org/abs/2512.04388  
**Raw file:** [[../raw/papers/2025-12-04-nielsen-learning-to-orchestrate-agents-conductor.md]]

**Summary:** Nielsen et al. introduce a Conductor model trained through reinforcement learning to coordinate pools of LLM workers. Instead of hard-coding one collaboration pattern, the Conductor learns communication topologies and targeted instructions that exploit worker strengths across reasoning tasks. The result is a concrete example of orchestration as a learnable policy rather than a static wrapper around agents. For Hermes and Self-OS, this points toward future specialist routing where an orchestrator chooses when to fan out, when to recurse, and which worker should receive which prompt. It also gives a research anchor for evaluating fixed Kanban pipelines against adaptive agent-pool selection.

**Key contributions:**
- Shows a small conductor model can learn coordination strategies for heterogeneous LLM workers.
- Uses randomized agent pools and recursive self-selection to support adaptive test-time scaling.
- Supports treating orchestration policy as an optimizable component of agent systems.

**Related:** [[concepts/learned-orchestration]], [[concepts/multi-agent-orchestration]], [[entities/conductor]]

**Tags:** agent-orchestration, multi-agent, reinforcement-learning

**Compile note:** This page is intentionally written as a compact source registry entry rather than a replacement for the raw artifact. The raw file remains the source of truth for wording, figures, and publishing detail; the wiki page captures the durable role the artifact plays in the knowledge base, the operating decisions it supports, and the adjacent pages that should be consulted when the same theme recurs. Reviewers should use the raw link for exact copy or chart production and use this page for navigation, synthesis, and future cross-source analysis.
