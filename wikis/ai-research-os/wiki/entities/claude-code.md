---
title: "Claude Code"
date_created: 2026-04-12
date_modified: 2026-04-12
summary: "Anthropic's official CLI for Claude enabling agentic coding sessions with file system access, tool use, hooks, and skills — the primary interface for Self OS on the laptop."
tags: [tool, claude-code, cli, agentic, self-os]
type: entity
status: final
---

# Claude Code

**Type:** tool

**Description:** Anthropic's official CLI for Claude that enables agentic coding sessions with file system access, tool use, hooks, and skills — the primary interface for Self OS on the laptop.

**Key facts:**
- CLI invoked as `claude` in terminal
- Supports custom skills (slash commands) stored as `.md` files in `~/.claude/commands/`
- Hooks system: session-start, session-end, pre-compact, post-tool — configured in `settings.json`
- Manages context window with automatic compaction
- Used in Self OS for: wiki-ingest, wiki-query, wiki-lint, notebooklm-research, wrap-up

**Relationships:** [[concepts/claude-code-hooks]], [[entities/anthropic]], [[concepts/wiki-agent-memory]]

**Sources:** [[sources/cole-medin-self-evolving-claude-memory-2026]], [[sources/hooeem-extend-claude-sessions-2026]]

_Last updated: 2026-04-12_
