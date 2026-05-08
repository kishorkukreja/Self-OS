---
title: "Enterprise RAG Evaluation"
date_created: 2026-05-08
date_modified: 2026-05-08
summary: "Evaluation methods for retrieval systems at realistic enterprise corpus size and noise levels."
tags: [rag, evaluation, enterprise-ai]
type: concept
status: draft
confidence: emerging
source_count: 1
---

# Enterprise RAG Evaluation

**Definition:** Enterprise RAG evaluation measures retrieval quality under production-like document scale, duplication, permissions, and source diversity.

**Why it matters:** The newsletter digest highlights Onyx EnterpriseRAG-Bench as a warning that retrieval that looks strong at 5K documents can degrade sharply at 500K documents. This matters for [[concepts/llm-knowledge-bases]] because internal Slack, Gmail, Jira, Confluence, GitHub, and Drive corpora create near-duplicates and competing evidence that generic vector search may not rank correctly.

**Related:** [[concepts/llm-knowledge-bases]], [[concepts/agent-evaluation]]

**Sources:** [[sources/newsletter-digest-2026-05-07]]

_Last updated: 2026-05-08_
