---
title: "ReMe — Memory Management Toolkit for AI Agents"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Memory management framework offering file-based and vector-based systems with context compaction, hybrid retrieval, and SOTA results on LoCoMo and HaluMem benchmarks."
tags: [agent-memory, memory-management, vector-memory, file-memory, stateless-sessions]
type: source
status: final
---

# ReMe — Memory Management Toolkit for AI Agents

**Type:** repo
**Date:** 2026-04-13
**URL:** https://github.com/agentscope-ai/ReMe
**Raw file:** [[../../raw/repos/reme-2026-04-13.md]]

**Summary:** ReMe is a memory management framework for AI agents providing both file-based (ReMeLight) and vector-based memory systems. It addresses limited context windows and stateless sessions by automatically compacting conversations, persistently storing important information, and recalling relevant context in future interactions. ReMeLight uses markdown files (MEMORY.md, daily journals, dialog logs) with a ReActAgent-powered compactor and summariser, plus hybrid vector + BM25 retrieval. The vector-based system manages personal, procedural, and tool memory types. ReMe achieves state-of-the-art results on LoCoMo (86.23% overall) and HaluMem benchmarks, and integrates with QwenPaw and OpenClaw.

**Key contributions:**
- Dual memory systems: file-based ReMeLight and vector-based ReMe
- ReActAgent-powered context compaction with structured summaries (Goal, Constraints, Progress, Key Decisions, Next Steps)
- Hybrid retrieval (vector + BM25) for file-based memories
- Three vector memory types: personal, procedural, and tool memory
- SOTA on LoCoMo and HaluMem; AppWorld and BFCL-V3 improvements reported

**Tags:** agent-memory, memory-management, vector-memory, file-memory, stateless-sessions, openclaw
