---
title: AutoAgent — Autonomous Harness Engineering
date_created: '2026-05-05'
date_modified: '2026-05-05'
summary: AutoAgent is a compact framework for autonomous harness engineering. A human
  writes program.md, while a meta-agent edits agent.py, runs Harbor benchmark tasks,
  checks scores, and iterates. Its significance is the clean s
tags:
- autonomous-agents
- harness-engineering
- harbor
- evaluation
- self-improving-agents
- github-repo
type: source
status: final
---

# AutoAgent — Autonomous Harness Engineering

**Type:** repo  
**Date:** 2026-05-04  
**URL:** https://github.com/kevinrgu/autoagent  
**Raw file:** [[../raw/repos/autoagent-2026-05-04.md]]

## Summary
AutoAgent is a compact framework for autonomous harness engineering. A human writes program.md, while a meta-agent edits agent.py, runs Harbor benchmark tasks, checks scores, and iterates. Its significance is the clean separation between human intent, editable harness implementation, and benchmark feedback. For Self-OS, it is a lightweight companion to HALO and auto-harness: all three point toward systems where the model is not retrained, but the harness is repeatedly improved under objective or semi-objective tests. AutoAgent is especially useful as a minimal pattern for “program the loop, evaluate the loop, let the meta-agent edit the loop.” The repository also keeps the conceptual surface area small, making it a useful baseline when comparing heavier trace-driven or multi-benchmark harness-improvement systems.

## Key contributions
- Uses program.md as the human control surface for autonomous harness edits.
- Treats agent.py as the editable harness target with fixed benchmark adapter boundaries.
- Runs Harbor-format tasks and hill-climbs on score as the feedback signal.

## Linked concepts and entities
- Concepts: [[concepts/autonomous-harness-engineering]], [[concepts/self-improving-agents]], [[concepts/agent-evaluation]]
- Entities: [[entities/autoagent]]

**Tags:** autonomous-agents, harness-engineering, harbor, evaluation, self-improving-agents, github-repo
