---
title: "LLM Wiki v2 — extending Karpathy's LLM Wiki pattern with lessons from building agentmemory"
source: "https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2"
author:
published:
created: 2026-04-12
description: "LLM Wiki v2 — extending Karpathy's LLM Wiki pattern with lessons from building agentmemory - llm-wiki.md"
tags:
  - "clippings"
status: processed
---
- **On session start**: load relevant context from the wiki based on recent activity
- **On session end**: compress the session into observations, file insights
- **On query**: check if the answer is worth filing back (quality score > threshold)
- **On memory write**: check for contradictions with existing knowledge, trigger supersession
- **On schedule**: periodic lint, consolidation, retention decay

The human should still be in the loop for curation and direction. But the bookkeeping, the part that makes people abandon wikis, should be fully automated.