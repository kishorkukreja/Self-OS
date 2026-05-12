---
title: Claude Code
date_created: 2026-04-12
date_modified: 2026-05-12
summary: Anthropic's official CLI for Claude enabling agentic coding sessions with
  file system access, tool use, hooks, and skills — the primary interface for Self
  OS on the laptop.
tags:
- tool
- claude-code
- cli
- agentic
- self-os
type: entity
status: final
tags: [wiki, maintenance]
---
# Claude Code

**Type:** tool

**Description:** Anthropic's official CLI for Claude that enables agentic coding sessions with file system access, tool use, hooks, and skills — the primary interface for Self OS on the laptop.

**Key facts:**
- CLI invoked as `claude` in terminal
- Supports custom skills (slash commands) stored as `.md` files in `~/.claude/commands/`
- Hooks system: session-start, session-end, pre-compact, post-tool — configured in `settings.json`
- Manages context window with automatic compaction
- Memory is project-scoped via `CLAUDE.md` and auto-memory in `~/.claude/projects/<name>/memory/` (25 KB limit)
- Can orchestrate subagents but skills do not self-evolve; manual curation required
- Used in Self OS for: wiki-ingest, wiki-query, wiki-lint, notebooklm-research, wrap-up

**Relationships:** [[concepts/claude-code-hooks]], [[entities/anthropic]], [[concepts/wiki-agent-memory]]

**Sources:** [[sources/cole-medin-self-evolving-claude-memory-2026]], [[sources/hooeem-extend-claude-sessions-2026]]

_Last updated: 2026-05-09_
- 2026-04-30: Added evidence from [[sources/context-mode-2026]].
- 2026-04-30: Added evidence from [[sources/claude-code-monitor-tool-background-tasks-2026]].

## Update — 2026-05-01
- Claude Code is referenced by this source and tracked as a wiki entity. Supporting source: [[sources/mattpocock-2026-sandcastle]].

_Last updated: 2026-05-09_

## Update — 2026-05-02

[[sources/alphasignal-2026-claude-code-setup-plugin]] adds Anthropic's `claude-code-setup` plugin as evidence that Claude Code is becoming a configurable project runtime. The plugin scans a repo read-only and recommends targeted MCP servers, skills, hooks, subagents, and slash commands suited to the current codebase.

## 2026-05-03 update

This page was linked from [[sources/claude-code-game-studios-2026-05-02]]. Claude Code is an entity referenced by Donchitos/Claude-Code-Game-Studios.

**Sources:** [[sources/claude-code-game-studios-2026-05-02]]

## 2026-05-03 update

This page was linked from [[sources/github-trending-weekly-2026-05-02]]. Claude Code is an entity referenced by GitHub Trending Weekly Repositories — 2026-05-02.

**Sources:** [[sources/github-trending-weekly-2026-05-02]]

## 2026-05-03 update

This page was linked from [[sources/nate-herk-build-sell-claude-code-operating-systems-2026]]. Claude Code is an entity referenced by Build & Sell Claude Code Operating Systems (2+ Hour Course).

**Sources:** [[sources/nate-herk-build-sell-claude-code-operating-systems-2026]]

## 2026-05-04 update

Referenced by [[sources/2026-05-03-x-blogs-digest]].

## 2026-05-06 update

This page was linked from [[sources/open-slide-2026-05-05]]. Claude Code is an entity referenced by open-slide.

**Sources:** [[sources/open-slide-2026-05-05]]

## 2026-05-09 — Daily compile update

The 2026-05-08 AI newsletter sources add this entity to the current agent-platform signal set, alongside voice APIs, coding-agent workflows, office integration, and review/routine automation.

**Sources:** [[sources/newsletter-digest-2026-05-08]], [[sources/the-code-2026-05-08]], [[sources/claire-vo-2026-claude-code-agent-platform]]


## Update — 2026-05-10
- Claude Code is referenced in [[sources/2026-05-09-how-to-build-an-agent-platform]] as part of the latest compiled source set.


## Update — 2026-05-10
- Claude Code is referenced in [[sources/newsletter-digest-2026-05-09]] as part of the latest compiled source set.


## Update — 2026-05-10
- Claude Code is referenced in [[sources/github-trending-weekly-2026-05-09]] as part of the latest compiled source set.


## Update — 2026-05-10
- Claude Code is referenced in [[sources/2026-05-09-trq212-unreasonable-effectiveness-html]] as part of the latest compiled source set.

## Compile update — 2026-05-12

**Type:** tool or organization

**Sources:** [[sources/mnilax-2026-12-rule-claude-md-template]]

This entity was referenced by Mnilax Thread — 12-Rule CLAUDE.md Template.

## Compile update — 2026-05-12

**Type:** tool or organization

**Sources:** [[sources/auto-improving-software-2026-05-11]]

This entity was referenced by Auto-Improving Software.
