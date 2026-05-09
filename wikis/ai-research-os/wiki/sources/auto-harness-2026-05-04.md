---
title: auto-harness — Self-Improving Agentic Systems via Benchmarks and Gating
date_created: '2026-05-05'
date_modified: '2026-05-05'
summary: 'auto-harness is a self-improvement loop for agentic systems: run benchmarks,
  analyze failures, edit the agent implementation, gate against regressions, record
  learnings, and repeat. Its value is that it treats benchmark '
tags:
- self-improving-agents
- harness-engineering
- evaluation
- regression-testing
- benchmarks
- github-repo
type: source
status: final
tags: [wiki, maintenance]
---

# auto-harness — Self-Improving Agentic Systems via Benchmarks and Gating

**Type:** repo  
**Date:** 2026-05-04  
**URL:** https://github.com/neosigmaai/auto-harness  
**Raw file:** [[../raw/repos/auto-harness-2026-05-04.md]]

## Summary
auto-harness is a self-improvement loop for agentic systems: run benchmarks, analyze failures, edit the agent implementation, gate against regressions, record learnings, and repeat. Its value is that it treats benchmark gating and regression tests as the guardrails for autonomous harness edits. Rather than letting a meta-agent freely mutate behavior, the repo steers improvement through PROGRAM.md, benchmark-specific tasks, live eval suites, and persisted results. For Self-OS, this source is a practical reference for overnight agent-maintenance loops that can improve capability while reducing regression risk. It is also useful as a comparison source for deciding which improvement loops should be fully automated and which should require human review before changes land in a production agent harness.

## Key contributions
- Defines a benchmark/analyze/edit/gate/record loop for harness improvement.
- Supports tau-bench, Terminal-Bench, and BIRD-Interact style evaluation targets.
- Emphasizes regression suites and gating before accepting self-improvements.

## Linked concepts and entities
- Concepts: [[concepts/self-improving-agents]], [[concepts/agent-evaluation]], [[concepts/regression-testing]]
- Entities: [[entities/auto-harness-neosigma]]

**Tags:** self-improving-agents, harness-engineering, evaluation, regression-testing, benchmarks, github-repo
