---
url: https://x.com/dani_avila7/status/2048486242321662189
author: Daniel San (@dani_avila7)
saved: 2026-04-27
source: codenewsletter.ai
status: processed
---
# Keep your Claude Code context clean with Subagents

> "Long Claude Code sessions get messy fast. Every grep, find, and ls stays in your context, taking up space you'll never read again. Subagents fix this: they run work in their own window and return only the result."

## What is a Subagent

A subagent is a specialized assistant that runs in its own context window, with its own system prompt, tools, and permissions.

The main agent calls it, the subagent does the work in isolation, and returns a summary.

### Creating a Subagent

You create one with a Markdown file and frontmatter in `.claude/agents/<name>.md`:

```markdown
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability. Use after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer. When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Start the review immediately
```

Claude Code picks it up automatically and invokes it when the description matches the task.

## Where Subagents Live

Priority (highest to lowest):

1. `.claude/agents/` — **Project scope** (check into version control, share with team)
2. `~/.claude/agents/` — **Personal scope** (available everywhere)
3. Claude Code built-ins — **Global scope**

When two subagents share the same name, the higher-priority location wins.

For most cases, use `.claude/agents/` (team-shared) or `~/.claude/agents/` (personal).

## The Problem: One Window for Everything

Without subagents, the main agent does it all in a single context. You ask it to review a controller, find a pattern, validate something. It fires grep, find, ls, glob, cd, more grep, another find — every call stays in your context, burning tokens you'll never re-read.

## Built-in Subagents

Claude Code ships with several built-in subagents:

- **Code reviewer** — Reviews code for quality and security
- **Test writer** — Generates tests for changed code
- **Documentation writer** — Updates docs for API changes
- **Refactoring assistant** — Suggests structural improvements
- **Security auditor** — Scans for vulnerabilities
- **Performance optimizer** — Identifies bottlenecks

## Forking Context

Set `CLAUDE_CODE_FORK_SUBAGENT=1` to fork the main agent's context into a subagent:

```bash
CLAUDE_CODE_FORK_SUBAGENT=1 claude
```

This lets the subagent inherit the current state but run independently, then return a condensed result.

## Why It Matters

Subagents keep the main context window clean. Instead of cramming every tool call and intermediate result into the main agent's context, work is delegated to specialized agents that return only what matters. This is especially critical for long sessions or complex multi-step tasks.

## Related

- Claude Code Hook — Context Timeline (visualizes subagent activity in real time)
- WUPHF — multi-agent "office" where subagent patterns are fundamental
- Hermes Labyrinth — observability for tracking subagent crossings
