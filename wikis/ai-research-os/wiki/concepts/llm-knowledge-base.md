# LLM Knowledge Base

**Definition:** A structured, LLM-maintained knowledge repository where an AI reads raw inputs and writes synthesised wiki entries, enabling compounding knowledge accumulation over time.

**Why it matters:** Traditional note-taking and search systems index information but don't synthesise it. An LLM knowledge base turns raw material into connected, queryable knowledge that compounds — each new input enriches the existing structure rather than sitting in a pile. The system gets more useful the more you feed it.

**The core loop:**
1. Collect raw material into `raw/` (articles, papers, threads, transcripts)
2. LLM reads and synthesises into `wiki/` (concepts, entities, sources, syntheses)
3. Queries are run against the compiled wiki, not the raw material
4. Query answers get filed back into the wiki
5. Periodic health checks catch contradictions and gaps

**Related:** [[raw-wiki-pattern]], [[knowledge-compounding]], [[entities/andrej-karpathy]]

**Sources:** [[sources/karpathy-llm-os-tweet-2026]], [[sources/hooeem-llm-knowledge-base-guide-2026]]

_Last updated: 2026-04-12_
