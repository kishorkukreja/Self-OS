---
title: "PageIndex — Vectorless, Reasoning-based RAG"
date_created: 2026-05-08
date_modified: 2026-05-08
summary: "VectifyAI PageIndex repository capture for a vectorless, tree-indexed, reasoning-based RAG framework over long professional documents."
tags: [rag, retrieval, document-ai, agents]
type: source
status: final
---

# PageIndex — Vectorless, Reasoning-based RAG

**Type:** repo
**Date:** 2026-05-07
**URL/Source:** https://github.com/VectifyAI/PageIndex
**Raw file:** [[../raw/repos/pageindex-2026-05-07.md]]
**Concepts:** [[concepts/vectorless-rag]], [[concepts/tree-indexed-document-memory]], [[concepts/llm-knowledge-bases]], [[concepts/agentic-memory]]
**Entities:** [[entities/pageindex]], [[entities/vectifyai]]

## Summary

PageIndex is a Python framework from VectifyAI that proposes [[concepts/vectorless-rag]] for long professional documents. Instead of chunking files into embeddings and asking a vector database for semantically similar fragments, PageIndex builds a table-of-contents-like hierarchy and uses LLM reasoning or tree search to identify the sections most relevant to a question. The captured repository positions this as closer to how a human expert scans complex financial reports, legal documents, manuals, or academic textbooks: start from structure, narrow to likely sections, then inspect evidence with section and page traceability.

The source matters because it complements two recurring Self-OS themes: [[concepts/llm-knowledge-bases]] and [[concepts/agentic-memory]]. For knowledge work, the point is not merely higher recall; it is explainable retrieval over documents where similarity does not equal relevance. The README also surfaces an agentic vectorless RAG demo with the OpenAI Agents SDK, a PageIndex File System layer for multi-document corpora, MCP/API integrations, and commercial/on-prem deployment paths. Claims such as FinanceBench performance should be treated as project claims until independently verified, but the architectural pattern is valuable: preserve document hierarchy, make retrieval decisions inspectable, and use agents to reason over a structured index before reading raw text.

## Key takeaways

- The source adds a dated signal to the AI wiki rather than replacing the raw capture.
- Claims that originate in vendor or newsletter summaries should be traced back to the original linked source before use in formal synthesis.
- The strongest durable value is the connection between agent capability and operational infrastructure: evaluation, memory, retrieval, compute, and workflow design.

## Compilation notes

Compiled from `raw/repos/pageindex-2026-05-07.md` during the 2026-05-08 wiki compile. The raw capture remains canonical for exact excerpts, links, figures, and code.
