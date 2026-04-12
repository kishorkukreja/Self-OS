---
title: "Knowledge Compounding"
date_created: 2026-04-12
date_modified: 2026-04-12
summary: "Property of an LLM knowledge base where each new input and query answer enriches the base, compounding rather than resetting."
tags: [llm, knowledge-base, compounding, workflow]
type: concept
status: final
---

# Knowledge Compounding

**Definition:** The property of an LLM knowledge base where each new input and each query answer enriches the base, making future queries more accurate and complete — compounding rather than resetting.

**Why it matters:** Most AI interactions are stateless: you ask, you get an answer, nothing accumulates. Knowledge compounding flips this. When query answers are filed back into the wiki and new sources are synthesised against existing content, the base grows in depth and interconnection. After weeks of use, a topic-specific wiki can answer questions that no individual source could.

**Mechanisms:**
1. **Ingest compounding** — new raw files are synthesised against existing wiki content, not in isolation. Connections and contradictions are found automatically.
2. **Query compounding** — answers to questions are saved as synthesis files, available to future queries.
3. **Health check compounding** — periodic contradiction and gap detection keeps the wiki accurate as knowledge evolves.

**Related:** [[llm-knowledge-base]], [[raw-wiki-pattern]]

**Sources:** [[sources/hooeem-llm-knowledge-base-guide-2026]]

_Last updated: 2026-04-12_
