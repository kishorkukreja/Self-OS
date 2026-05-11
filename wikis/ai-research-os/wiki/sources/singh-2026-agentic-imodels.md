---
title: "Agentic-imodels: Evolving Agentic Interpretability Tools via Autoresearch"
date_created: 2026-05-11
date_modified: 2026-05-11
summary: "Singh et al. introduce Agentic-imodels, an autoresearch loop for evolving data-science models that are interpretable to agents, not only to humans. The key test is whether an LLM can simulate a fitted model from its stri"
tags: [agent-readable-tools, interpretability, autoresearch]
type: source
status: final
---

# Agentic-imodels: Evolving Agentic Interpretability Tools via Autoresearch

**Type:** paper  
**Date:** 2026-05-05  
**URL:** https://arxiv.org/abs/2605.03808  
**Raw file:** [[../raw/papers/2026-05-05-singh-agentic-imodels-agentic-interpretability-tools-autoresearch.md]]

**Summary:** Singh et al. introduce Agentic-imodels, an autoresearch loop for evolving data-science models that are interpretable to agents, not only to humans. The key test is whether an LLM can simulate a fitted model from its string representation and answer questions about behavior. This shifts tool design from human-readable output toward agent-readable artifacts that support downstream reasoning. For Hermes, the idea generalizes beyond tabular models: CLI output, wiki summaries, Kanban tickets, evaluation traces, and daily briefs should be structured so agents can inspect, simulate, and act on them with low ambiguity. The reported gains for Copilot CLI, Claude Code, and Codex reinforce the value of designing tools around the consuming agent.

**Key contributions:**
- Defines an LLM-based interpretability metric for model string representations.
- Shows autoresearch can evolve scikit-learn-compatible models with better predictive and agent-facing properties.
- Provides evidence that agent-readable tools can improve downstream coding/data-science agents.

**Related:** [[concepts/agent-readable-tools]], [[concepts/model-interpretability]], [[entities/claude-code]], [[entities/codex]]

**Tags:** agent-readable-tools, interpretability, autoresearch
