---
title: "Agent Memory"
date_created: 2026-04-27
date_modified: 2026-05-01
summary: "Systems that enable agents to store, retrieve, and learn from historical experiences to improve future reasoning and planning."
tags: ['agent-memory', 'deep-research', 'parametric-memory', 'memory-system']
type: concept
status: draft
confidence: emerging
source_count: 3
---

# Agent Memory

**Agent memory** encompasses both non-parametric (retrieval-based) and parametric (model-weight-based) mechanisms for leveraging historical experience. In deep research agents, memory must capture not only factual results but also process knowledge: how tasks were solved, what strategies succeeded or failed, and how plans were adapted. [[MIA]] proposes a Manager-Planner-Executor architecture that explicitly separates episodic memory storage from parametric planning, enabling test-time learning without interrupting inference.

Key dimensions:
- **Non-parametric memory:** Stored trajectories retrieved by similarity, quality, and frequency.
- **Parametric memory:** Knowledge distilled into model weights via reinforcement learning.
- **Bidirectional conversion:** Trajectories are compressed into workflows, which are then used to update the Planner's policy.

_Last updated: 2026-04-27_

## Update — 2026-05-01
Architectures and benchmarks for retaining, retrieving, and evaluating persistent context across agent interactions. New supporting source: [[sources/x-blogs-digest-2026-04-30]].

_Last updated: 2026-05-01_
