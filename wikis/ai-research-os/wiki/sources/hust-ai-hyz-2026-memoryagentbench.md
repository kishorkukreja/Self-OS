---
title: "MemoryAgentBench — Evaluating Memory in LLM Agents"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "ICLR 2026 benchmark for agent memory evaluation via incremental multi-turn interactions, testing accurate retrieval, test-time learning, long-range understanding, and conflict resolution."
tags: [agent-memory, benchmark, evaluation, iclr-2026, multi-turn]
type: source
status: final
---

# MemoryAgentBench — Evaluating Memory in LLM Agents

**Type:** repo
**Date:** 2026-04-13
**URL:** https://github.com/HUST-AI-HYZ/MemoryAgentBench
**Raw file:** [[../../raw/repos/memoryagentbench-2026-04-13.md]]

**Summary:** MemoryAgentBench is an ICLR 2026-accepted benchmark designed to evaluate memory capabilities in LLM agents through incremental multi-turn interactions. It assesses four core competencies: Accurate Retrieval (AR), Test-Time Learning (TTL), Long-Range Understanding (LRU), and Conflict Resolution (CR). The benchmark reformulates data from previous benchmarks (RULER, InfBench, HELMET, LongMemEval) into chunks that simulate real multi-turn conversation scenarios, and introduces two new datasets: EventQA and FactConsolidation. A key design philosophy is "inject once, query multiple times," improving evaluation efficiency by mapping one long text to multiple questions.

**Key contributions:**
- Four-competency evaluation framework: AR, TTL, LRU, CR
- Reformatting of existing benchmarks into incremental multi-turn scenarios
- New datasets: EventQA and FactConsolidation
- Efficient "inject once, query multiple times" evaluation design
- Open-source framework with support for custom memory agents

**Tags:** agent-memory, benchmark, evaluation, iclr-2026, multi-turn
