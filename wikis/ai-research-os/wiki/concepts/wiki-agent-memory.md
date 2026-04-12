---
title: "Wiki Agent Memory"
date_created: 2026-04-12
date_modified: 2026-04-12
summary: "Pattern of giving an LLM agent lifecycle hooks into a knowledge wiki — loading context on session start, filing insights on session end, and running maintenance on schedule."
tags: [llm, agent-memory, session-lifecycle, hooks]
type: concept
status: final
---

# Wiki Agent Memory

**Definition:** The pattern of giving an LLM agent lifecycle hooks into a knowledge wiki — loading context on session start, filing insights on session end, and running maintenance automatically on schedule.

**Why it matters:** The reason personal wikis get abandoned is bookkeeping burden. Wiki agent memory automates the bookkeeping: the agent handles loading, filing, contradiction-checking, and retention decay. The human only provides direction and curation — the parts that require judgement.

**Lifecycle hooks:**
- **Session start:** Load relevant wiki context based on recent activity and current task
- **Session end:** Compress session into observations, file insights above quality threshold
- **Query:** Check if answer is worth filing back (quality score > threshold)
- **Memory write:** Check for contradictions with existing knowledge, trigger supersession
- **Scheduled:** Periodic lint, consolidation, retention decay

**Key concepts:**
- **Supersession:** When a new insight contradicts an old one, the old entry is marked superseded rather than deleted — history preserved, current view updated
- **Retention decay:** Knowledge that's never accessed or referenced degrades in priority, surfacing what's active vs stale
- **Quality threshold:** Not all query answers deserve to be filed — only insights above a usefulness threshold go into the wiki

**Related:** [[llm-knowledge-base]], [[raw-wiki-pattern]], [[knowledge-compounding]]

**Sources:** [[sources/llm-wiki-v2-karpathy-pattern]]

_Last updated: 2026-04-12_
