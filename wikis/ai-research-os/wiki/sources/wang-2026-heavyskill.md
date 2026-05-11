---
title: "HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness"
date_created: 2026-05-11
date_modified: 2026-05-11
summary: "Wang et al. argue that part of the performance attributed to elaborate agentic harnesses may come from a simpler internal skill: parallel reasoning followed by summarization. HeavySkill reframes orchestration as a repeat"
tags: [agent-orchestration, reasoning, reinforcement-learning]
type: source
status: final
---

# HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness

**Type:** paper  
**Date:** 2026-05-04  
**URL:** https://arxiv.org/abs/2605.02396  
**Raw file:** [[../raw/papers/2026-05-04-wang-heavyskill-heavy-thinking-agentic-harness.md]]

**Summary:** Wang et al. argue that part of the performance attributed to elaborate agentic harnesses may come from a simpler internal skill: parallel reasoning followed by summarization. HeavySkill reframes orchestration as a repeatable reasoning primitive that can be scaled in width and depth, benchmarked against Best-of-N baselines, and further improved through reinforcement learning. For Self-OS and Hermes, the paper is a reminder that subagent fan-out, review loops, and Kanban handoffs should be treated as measurable reasoning structures rather than magic infrastructure. The practical implication is to compare orchestration choices against simpler heavy-thinking baselines and to ask whether the skill can be internalized through examples, evaluations, and training-like feedback loops.

**Key contributions:**
- Introduces heavy thinking as parallel reasoning plus summarization inside or beneath agentic harnesses.
- Reports advantages over Best-of-N and suggests stronger models can approach Pass@N behavior.
- Connects orchestration design with reinforcement learning and self-evolving LLM behavior.

**Related:** [[concepts/heavy-thinking]], [[concepts/multi-agent-orchestration]], [[concepts/reinforcement-learning-for-agents]]

**Tags:** agent-orchestration, reasoning, reinforcement-learning
