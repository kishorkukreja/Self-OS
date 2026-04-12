---
title: "I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases"
date_created: 2026-04-12
date_modified: 2026-04-12
summary: "Applies Karpathy's raw→wiki pattern to internal coding session data using Claude Code hooks and Agent SDK — creating self-evolving memory that compounds with every session."
tags: [claude-code, claude-code-hooks, session-memory, knowledge-base, compounding-loop, agent-sdk]
type: source
status: final
---

# I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases

**Type:** video
**Date:** 2026-04-06
**URL:** https://www.youtube.com/watch?v=7huCP6RkcY4
**Author:** Cole Medin
**Raw file:** [[../../raw/youtube/I Built Self-Evolving Claude Code Memory w Karpathy's LLM Knowledge Bases.md]]

**Summary:** Cole Medin applied Karpathy's external-data raw→wiki pattern to internal coding session data. Claude Code hooks (session-start, pre-compact, session-end) automatically capture session transcripts into daily logs (the raw/ equivalent), the Claude Agent SDK runs a flush process to promote logs into a structured wiki, and queries are answered against the wiki at session start. Result: Claude Code memory that evolves with the codebase without any manual maintenance.

**Key contributions:**
- Internal vs external variant: session logs as raw/ input instead of web articles
- Claude Code hooks architecture: session-start loads agents.md + index.md; session-end + pre-compact trigger Agent SDK summarisation
- Flush process (daily): Agent SDK promotes daily logs → structured wiki concepts/connections
- Compounding loop: query answers filed back → wiki grows → future queries get better answers
- No RAG needed: agent navigates via index.md file tree; no vector DB, no semantic search
- Self-contained system: Claude Code itself can modify its own memory prompts via agents.md

**Tags:** claude-code, claude-code-hooks, session-memory, knowledge-base, compounding-loop, agent-sdk, internal-knowledge
