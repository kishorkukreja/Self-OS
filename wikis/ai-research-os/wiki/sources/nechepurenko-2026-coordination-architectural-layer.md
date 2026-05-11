---
title: "Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems"
date_created: 2026-05-11
date_modified: 2026-05-11
summary: "Nechepurenko and Shuvalov argue that multi-agent systems often fail because of coordination choices, not because the underlying model lacks capability. Their prediction-market experiment isolates coordination as a config"
tags: [multi-agent, coordination, agent-evaluation]
type: source
status: final
---

# Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems

**Type:** paper  
**Date:** 2026-05-05  
**URL:** https://arxiv.org/abs/2605.03310  
**Raw file:** [[../raw/papers/2026-05-05-nechepurenko-coordination-architectural-layer-llm-multi-agent-systems.md]]

**Summary:** Nechepurenko and Shuvalov argue that multi-agent systems often fail because of coordination choices, not because the underlying model lacks capability. Their prediction-market experiment isolates coordination as a configurable architectural layer while holding the model, tools, prompt template, and output budget constant. By using Brier-score decomposition, the paper shows that different coordination configurations can leave different calibration and resolution signatures even when aggregate scores look similar. For Self-OS, this offers a useful engineering lens: delegation, Kanban topology, cron loops, and review stages should be measured as architectural choices with cost-quality tradeoffs and identifiable failure modes.

**Key contributions:**
- Treats coordination as a separable layer in LLM multi-agent architecture.
- Uses prediction markets and Brier-score decomposition to reveal coordination signatures.
- Suggests production agent systems need diagnostics for coordination defects, not just model upgrades.

**Related:** [[concepts/multi-agent-coordination]], [[concepts/agent-evaluation]], [[concepts/multi-agent-orchestration]]

**Tags:** multi-agent, coordination, agent-evaluation

**Compile note:** This page is intentionally written as a compact source registry entry rather than a replacement for the raw artifact. The raw file remains the source of truth for wording, figures, and publishing detail; the wiki page captures the durable role the artifact plays in the knowledge base, the operating decisions it supports, and the adjacent pages that should be consulted when the same theme recurs. Reviewers should use the raw link for exact copy or chart production and use this page for navigation, synthesis, and future cross-source analysis.
