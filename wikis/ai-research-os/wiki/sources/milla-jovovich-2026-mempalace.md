---
title: "MemPalace — Local AI Memory System"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Local-first AI memory system using a palace architecture (wings, rooms, halls, drawers) to organise conversations and projects, achieving 96.6% R@5 on LongMemEval with zero API calls."
tags: [agent-memory, long-term-memory, chromadb, verbatim-storage, mcp, longmemeval]
type: source
status: final
---

# MemPalace — Local AI Memory System

**Type:** repo
**Date:** 2026-04-13
**URL:** https://github.com/MemPalace/mempalace
**Raw file:** [[../../raw/repos/mempalace-2026-04-13.md]]

**Summary:** MemPalace is a local-first AI memory system that stores raw verbatim conversations and project data in ChromaDB without LLM summarisation. It organises memories into a navigable "palace" structure: wings (people/projects), rooms (topics), halls (memory types), and drawers (original files). This metadata-driven architecture provides a 34% retrieval improvement over unfiltered search. MemPalace achieves 96.6% R@5 on LongMemEval in raw mode with zero API calls, making it one of the highest-scoring memory systems benchmarked. Additional features include a temporal knowledge graph (SQLite), specialist agent diaries, the experimental AAAK compression dialect, and 19 MCP tools.

**Key contributions:**
- Palace architecture delivering structured retrieval without LLM preprocessing
- 96.6% LongMemEval R@5 in raw verbatim mode (zero API calls)
- Temporal knowledge graph with validity windows and invalidation
- Four-layer memory stack (L0 identity, L1 critical facts, L2 room recall, L3 deep search)
- 19 MCP tools for palace navigation, knowledge graph, and agent diaries

**Tags:** agent-memory, long-term-memory, chromadb, verbatim-storage, mcp, longmemeval, knowledge-graph
