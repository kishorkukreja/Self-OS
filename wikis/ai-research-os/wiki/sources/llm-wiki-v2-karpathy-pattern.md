# LLM Wiki v2 — Extending Karpathy's Pattern with Agent Memory

**Type:** repo
**Date:** 2026-04-12
**URL:** https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2
**Raw file:** [[../../raw/repos/llm-wiki-v2-karpathy-pattern.md]]

**Summary:** Extends Karpathy's raw→wiki pattern by adding agent memory lifecycle hooks: load context on session start, compress and file insights on session end, check contradiction and trigger supersession on memory write, and run periodic lint/consolidation on schedule. The key insight is that the bookkeeping that causes wikis to be abandoned should be fully automated, with humans only handling curation and direction.

**Key contributions:**
- Lifecycle hooks for agent memory (session start/end, query, memory write, schedule)
- Contradiction detection and knowledge supersession as automated processes
- Retention decay concept: old knowledge that's never accessed degrades in priority
- Quality threshold for filing back query answers: only high-value answers get persisted
- Human stays in the loop for direction; bookkeeping is fully automated

**Tags:** llm, knowledge-base, agent-memory, wiki, automation, session-lifecycle
