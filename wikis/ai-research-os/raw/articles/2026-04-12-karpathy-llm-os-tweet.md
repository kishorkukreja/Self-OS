---
source: https://x.com/karpathy/status/1907193941248381031
date: 2026-04-02
type: article
tags: [llm, knowledge-base, karpathy, workflow]
status: processed
---

# Karpathy on LLM Knowledge Bases (April 2026)

Karpathy tweeted about a personal workflow for managing knowledge with LLMs. The core pattern:

- Keep a `raw/` folder for unprocessed inputs (articles, notes, dumps)
- Keep a `wiki/` folder for LLM-curated, synthesised knowledge
- Run a Claude Code command to ingest raw → wiki on demand
- The wiki becomes a queryable knowledge base that grows over time

Key insight: the wiki is not written by hand. It's maintained by the LLM, which reads raw inputs and updates structured wiki entries. Humans drop things into raw/ and query the wiki. The LLM does the synthesis work.

This pattern scales well because:
1. Raw inputs don't need to be structured — dump anything
2. Wiki entries are always LLM-curated summaries, not raw notes
3. Contradiction detection happens at ingest time, not later
4. The wiki is always queryable, even mid-ingest

Karpathy described this as the "LLM OS" concept — using an LLM as the operating layer for personal knowledge management, rather than a search tool or chatbot.
