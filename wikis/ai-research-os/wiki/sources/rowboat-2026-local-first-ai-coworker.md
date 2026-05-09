---
title: "Rowboat — Open-Source AI Coworker with Memory"
date_created: 2026-05-09
date_modified: 2026-05-09
summary: "Rowboat is a local-first AI coworker that turns work data into an editable Markdown knowledge graph and uses it to generate practical artifacts."
tags: [rowboat, agent-memory, ai-operating-system]
type: source
status: final
---

# Rowboat — Open-Source AI Coworker with Memory

**Type:** repo
**Date:** 2026-05-09
**URL/Source:** https://github.com/rowboatlabs/rowboat
**Raw file:** [[../raw/repos/rowboat-2026-05-09.md]]
**Concepts:** [[concepts/agent-memory]], [[concepts/local-first-agent-memory]], [[concepts/ai-operating-system]], [[concepts/knowledge-graph-memory]]
**Entities:** [[entities/rowboat]], [[entities/obsidian]]

## Summary

Rowboat is a high-signal reference implementation for local-first agent memory. The project connects to work data such as email, calendar, Drive, meeting notes, and voice memos, then turns that context into an editable knowledge graph. Its core architectural choice is to store working memory as an Obsidian-compatible Markdown vault with backlinks rather than hiding state in a hosted model or opaque vector database. That makes user memory inspectable, editable, portable, and deletable.

For [[concepts/agent-memory]], Rowboat demonstrates a product pattern where context accumulation becomes the basis for action. It remembers people, projects, decisions, commitments, and topics; retrieves relevant context for meetings or writing tasks; and generates briefs, emails, documents, plans, summaries, voice-note outputs, and PDF decks. This overlaps strongly with Self-OS themes: raw captures, compiled wiki pages, durable local state, and transparent agent workflows.

The most useful distinction is that Rowboat appears productized around desktop coworker workflows and SaaS connectors, while Self-OS is Git-backed and automation-first through Hermes cron jobs, wiki compiles, Telegram control, and agent/Kanban operations. The source should be used as a comparison point for user-owned memory, knowledge-graph editing, and AI operating-system UX. It also suggests a useful product boundary: memory tools should separate raw capture, curated graph state, generated artifacts, and explicit actions so users can audit how a coworker reached a recommendation.

## Key takeaways

- Rowboat treats Markdown as the user-owned memory substrate for an AI coworker.
- The project turns accumulated context into action artifacts rather than simple retrieval answers.
- It is a useful benchmark for local-first memory, knowledge graphs, Obsidian-compatible storage, and personal AI operating-system design.
