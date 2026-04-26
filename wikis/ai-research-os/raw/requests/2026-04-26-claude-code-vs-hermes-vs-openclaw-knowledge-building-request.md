---
source: internal
date: 2026-04-26
type: request
tags: [self-learning-agents, knowledge-building, claude-code, hermes, openclaw, comparison, agent-memory]
status: processed
---

# Research Request: Self-Learning AI Tools for Autonomous Knowledge Building

## Research Question
Which self-learning AI tools are better for autonomous knowledge building: Claude Code, Hermes Agent, or OpenClaw?

## Scope
Evaluate each platform on:
1. **Skill acquisition & evolution** — how the agent learns new procedures and improves existing ones over time
2. **Persistent memory architecture** — cross-session recall of user preferences, environment details, and lessons learned
3. **Knowledge compounding** — whether each interaction enriches the base and produces compounding returns
4. **Self-directed improvement** — ability to refactor its own memory, skills, or prompts without human intervention
5. **Knowledge export & interoperability** — how learned knowledge can be shared, versioned, or reused across contexts

## Context
All three tools are autonomous CLI agents that can read/write files, run shell commands, and use tools. However, their approaches to self-directed knowledge building differ significantly:

- **Claude Code** (Anthropic) relies on `CLAUDE.md` project files, custom slash commands, and `settings.json` hooks. Memory is project-scoped; cross-project learning requires manual porting of CLAUDE.md files. No built-in skill marketplace or automatic skill generation.

- **Hermes Agent** (Nous Research) uses a formal **skills** system (`~/.hermes/skills/`) where successful workflows are persisted as reusable SKILL.md documents. It has pluggable memory backends (built-in, Honcho, Mem0) and accumulates environment conventions across sessions. Skills can be published, shared, and auto-loaded.

- **OpenClaw** (open-source community) maintains persistent memory via markdown files in its workspace (`AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `TOOLS.md`, `USER.md`). It can **write its own skills** and hot-reload them. Local-first, runs on owned hardware, and has a community skill registry (Clawhub). Featured by NVIDIA as a local autonomous agent runtime.

## Deliverables
- Comparative synthesis (500–1,500 words) filed in `wiki/syntheses/`
- Updated entity pages for Hermes Agent and OpenClaw (Claude Code already exists)
- Relevant concept pages if cross-cutting themes emerge (e.g., self-learning AI agent, skill evolution)

## Source Leads
- https://openclaw.ai/ — Official site, capabilities, community testimonials
- https://www.lennysnewsletter.com/p/openclaw-the-complete-guide-to-building — Claire Vo’s comprehensive setup guide
- https://github.com/NousResearch/hermes-agent — Hermes Agent source and documentation
- https://code.claude.com/docs — Claude Code CLI reference
- Raw papers already in `raw/papers/` mentioning OpenClaw skill ecosystems: `2026-04-12-ma-skillclaw.md`, `2026-04-13-liu-graph-of-skills.md`
