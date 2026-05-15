---
source: https://softwaredoug.com/blog/2026/05/11/the-new-agentic-search-models.html?utm_source=tldrai
date: 2026-05-14
type: article
tags: [agentic-search, information-retrieval, search-systems, retrieval, llms, domain-adaptation, query-understanding, self-os]
status: processed
---

# Doug Turnbull — Agentic search models

## Source metadata

- Author: Doug Turnbull / SoftwareDoug
- Title: "Agentic search models"
- Published: 2026-05-11
- Captured: 2026-05-14
- Source URL: https://softwaredoug.com/blog/2026/05/11/the-new-agentic-search-models.html?utm_source=tldrai

## Core thesis

Doug Turnbull argues that search is moving from manually assembled, monolithic retrieval pipelines toward **agentic search models**: LLMs trained specifically to control and orchestrate search tasks.

The shift is not simply “add an LLM to search.” It is a proposed architectural change from thick, bespoke, manually tuned pipelines toward smaller domain-tuned models that understand the end-to-end search process and can coordinate simpler backend retrieval tools.

Key quoted framing from the extracted article:

> “But a new power is rising: agentic search models. LLMs trained specifically on controlling the search task.”

> “Unlike the traditional stack, the agent sees the whole process.”

> “We need agents trained to reason and orchestrate simpler retrieval systems.”

## Traditional search stack

The article describes the current dominant pattern as a thick search monolith assembled from multiple narrow components:

- embeddings;
- BM25;
- rerankers;
- query understanding;
- query classifiers;
- business rules;
- multiple retrieval backends;
- post-processing;
- ranking and reranking layers.

This stack is powerful but highly manual, programmatic, and bespoke. Each part optimizes a local slice of the problem. The embedding model handles similarity; the query classifier categorizes intent; the reranker scores candidates; business rules patch edge cases. No single component sees the whole user task.

Doug’s critique is that this style has dominated for one to two decades, but becomes increasingly awkward as users expect search systems to behave like assistants rather than keyword boxes.

## What agentic search changes

Agentic search reframes retrieval as orchestration. Instead of forcing every query through a fixed linear pipeline, an agent can:

- interpret user intent;
- select among retrieval tools;
- choose whether to use lexical, vector, hybrid, filtered, or domain-specific retrieval;
- inspect and refine candidate results;
- use product taxonomy, business context, or local conventions;
- call subagents or knowledge-base tools;
- guide the user when the query is underspecified.

The underlying retrieval tools still matter. The difference is that they become thinner primitives coordinated by a model that understands the larger objective.

## Why frontier models are not enough

Doug argues that frontier models such as GPT-5 or Claude Sonnet can handle the broad 80% case, but often miss the domain-specific last 20% that determines whether search is actually good.

That last 20% includes:

- company-specific vocabulary;
- user behavior patterns;
- implicit relevance signals;
- product taxonomy;
- local meanings;
- category-specific user expectations;
- business constraints and merchandising logic.

Examples from the article:

- A furniture-store query for “bistro tables” likely means small outdoor tables, not restaurant equipment.
- In fashion search, users may prefer dark or plain patterns over complex ones in certain contexts.

The problem is that general models may treat “search” as web search. Real site, product, enterprise, and domain search are usually narrower, noisier, less complete, and more dependent on local conventions than Google-like web search.

## Current workaround: context engineering

The current workaround is to surround general models with constraints and context:

- retrieval-specific prompts;
- domain instructions;
- validation checks;
- query rewriting rules;
- taxonomies;
- examples of good and bad relevance;
- guardrails around available search tools.

Doug frames this as useful but transitional. Long term, the argument is for models trained specifically to reason over domain search systems and orchestrate simpler retrieval backends.

## Why it matters

The article is important because it shifts the conversation from “which retrieval component should we add?” to “who or what controls the retrieval process?”

For AI systems, this is a meaningful architecture distinction:

- Retrieval quality is not only an embedding/reranker problem.
- Search intent is often local and domain-specific.
- LLMs can coordinate retrieval steps, but generic web-search priors can mislead them.
- Good search agents need domain training, business rules, and validation loops — not just tool access.

This overlaps with the broader agentic workflow pattern: the agent is not replacing all infrastructure; it is becoming the orchestration layer over simpler, more inspectable primitives.

## Self-OS / Hermes implications

This has direct implications for Self-OS search and wiki retrieval:

1. **Self-OS search should not pretend to be web search.** The system is a personal operating memory with local conventions, project names, recurring workflows, and implicit priorities.
2. **Domain-tuned retrieval agents matter.** Separate search behaviors may be needed for ai-research-os, supply-chain-os, coding-projects-os, taskOS, and daily operating briefs.
3. **Search quality should include local intent.** A query like “handoff,” “night shift,” “signal translation,” or “Ralph loop” has Self-OS-specific meaning that generic embeddings may not capture.
4. **Retrieval should become an agentic loop.** Query understanding, source selection, result inspection, follow-up retrieval, and answer synthesis should be orchestrated rather than treated as a single vector search call.
5. **Validation is still necessary.** Agentic search can hallucinate relevance unless grounded in file paths, source excerpts, dates, and wiki links.

A useful Self-OS experiment would be a small “agentic wiki search” prototype that routes a query across named wikis, taskOS, memory, and recent sessions, then returns evidence-backed results with explicit source paths and confidence.

## Candidate operational follow-up

Potential future taskOS idea:

- Build a minimal agentic search prototype for Self-OS:
  - input: user query from Telegram;
  - classify domain: AI research, supply chain, coding projects, operations, task backlog, memory;
  - select retrieval tools: ripgrep/file search, wiki index, session_search, taskOS search;
  - inspect top results;
  - return evidence-backed answer with paths, dates, and confidence;
  - log failed queries for search improvement.

This should start as a small manual experiment before becoming a scheduled or reusable Hermes skill.

## Extraction notes

`web_extract` successfully retrieved a structured summary of the article. The capture preserves the thesis, architectural pattern, examples, and Self-OS implications rather than copying the full article verbatim.
