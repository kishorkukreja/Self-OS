---
title: "Vectorless RAG"
date_created: 2026-05-08
date_modified: 2026-05-08
summary: "Retrieval-augmented generation that navigates document structure and relevance reasoning without embedding chunk search as the primary mechanism."
tags: [rag, retrieval, document-ai]
type: concept
status: draft
confidence: emerging
source_count: 1
---

# Vectorless RAG

**Definition:** Vectorless RAG retrieves evidence through explicit document structure, tree search, or reasoning steps instead of nearest-neighbour vector similarity over chunks.

**Why it matters:** PageIndex is a concrete example of the pattern. It argues that professional documents often require relevance reasoning over sections rather than semantic similarity over arbitrary chunks, making it relevant to [[concepts/llm-knowledge-bases]] and due-diligence workflows that need citations.

**Related:** [[concepts/llm-knowledge-bases]], [[concepts/document-parsing]]

**Sources:** [[sources/pageindex-2026-vectorless-rag]]

_Last updated: 2026-05-08_
