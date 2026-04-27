---
title: "SimpleMem — Efficient Lifelong Memory for LLM Agents"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Memory framework for LLM agents based on semantic lossless compression, achieving SOTA on LoCoMo and Mem-Gallery benchmarks with minimal token cost via a three-stage pipeline."
tags: [agent-memory, lifelong-memory, semantic-compression, multimodal, llm-agents]
type: source
status: final
---

# SimpleMem — Efficient Lifelong Memory for LLM Agents

**Type:** repo
**Date:** 2026-04-13
**URL:** https://github.com/aiming-lab/SimpleMem
**Raw file:** [[../../raw/repos/simplemem-2026-04-13.md]]

**Summary:** SimpleMem is a family of efficient memory frameworks for LLM agents addressing the fundamental challenge of long-term memory through semantic lossless compression. Its three-stage pipeline—semantic structured compression, online semantic synthesis, and intent-aware retrieval planning—maximises information density while minimising token cost. The framework indexes memories through three complementary representations (semantic dense vectors, lexical BM25, and symbolic metadata) and supports parallel multi-view retrieval. Omni-SimpleMem extends this to multimodal memory (text, image, audio, video), achieving new SOTA on LoCoMo (F1=0.613, +47%) and Mem-Gallery (F1=0.810, +51%). The system integrates with Claude, Cursor, LM Studio, and other platforms via MCP or Python.

**Key contributions:**
- Three-stage pipeline: semantic structured compression → online synthesis → intent-aware retrieval
- Multi-view indexing (dense vector + BM25 + symbolic metadata) with parallel retrieval
- Cross-session memory with persistent conversation continuity
- Omni-SimpleMem multimodal support (text, image, audio, video)
- MCP server and PyPI package for broad integration

**Tags:** agent-memory, lifelong-memory, semantic-compression, multimodal, mcp, llm-agents
