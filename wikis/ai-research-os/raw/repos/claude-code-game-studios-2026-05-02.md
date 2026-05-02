---
source: https://github.com/Donchitos/Claude-Code-Game-Studios
date: 2026-05-02
type: repo
tags: [claude-code, game-development, ai-agents, agentic-workflows, skills, hooks, templates, gamedev, multi-agent-systems]
---

# Donchitos/Claude-Code-Game-Studios

**Repository:** https://github.com/Donchitos/Claude-Code-Game-Studios  
**Owner:** Donchitos  
**License:** MIT  
**Language:** Shell  
**Stars:** 16,939  
**Forks:** 2,464  
**Default branch:** main  
**Latest release noted by GitHub summary:** v1.0.0-beta — Apr 7, 2026  
**Description:** Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.

## Summary

**Claude Code Game Studios** is a Claude Code project template for turning a single Claude Code session into a structured game-development “studio.” It packages a large set of specialist agents, workflow slash commands/skills, hooks, rules, templates, and coordination protocols modeled on a real game studio hierarchy.

The repo’s central claim is that solo AI-assisted game development becomes more reliable when the AI session has explicit production structure: directors to guard vision, department leads to own domains, specialists for implementation, hooks for validation, and templates for design/production artifacts. The system is framed as collaborative rather than fully autonomous: the human remains final decision-maker, while the agent organization asks better questions, catches mistakes earlier, and keeps the project disciplined from brainstorm to launch.

## What It Includes

- **49 agents** across design, programming, art, audio, narrative, QA, production, engine support, live ops, security, analytics, accessibility, and community roles.
- **72 skills / slash-command workflows** such as `/start`, `/help`, `/design-system`, `/create-epics`, `/create-stories`, `/dev-story`, `/story-done`, `/qa-plan`, `/release-checklist`, and `/hotfix`.
- **12 hooks** for validation around commits, pushes, assets, sessions, skill edits, and audit trails.
- **11 path-scoped rules** for gameplay, engine, AI, UI, networking, tests, prototypes, and design docs.
- **39 templates** for GDDs, UX specs, ADRs, sprint plans, HUD designs, accessibility docs, and other studio artifacts.

## Studio Hierarchy

```text
Tier 1 — Directors (Opus)
  creative-director    technical-director    producer

Tier 2 — Department Leads (Sonnet)
  game-designer        lead-programmer       art-director
  audio-director       narrative-director    qa-lead
  release-manager      localization-lead

Tier 3 — Specialists (Sonnet/Haiku)
  gameplay-programmer  engine-programmer     ai-programmer
  network-programmer   tools-programmer      ui-programmer
  systems-designer     level-designer        economy-designer
  technical-artist     sound-designer        writer
  world-builder        ux-designer           prototyper
  performance-analyst  devops-engineer       analytics-engineer
  security-engineer    qa-tester             accessibility-specialist
  live-ops-designer    community-manager
```

## Engine Coverage

The template includes specialist agent support for the three major game engines:

- **Godot 4:** `godot-specialist`, plus GDScript, shaders, and GDExtension specialists.
- **Unity:** `unity-specialist`, plus DOTS/ECS, shaders/VFX, Addressables, and UI Toolkit specialists.
- **Unreal Engine 5:** `unreal-specialist`, plus GAS, Blueprints, Replication, and UMG/CommonUI specialists.

## Project Structure

```text
CLAUDE.md                           # Master configuration
.claude/
  settings.json                     # Hooks, permissions, safety rules
  agents/                           # 49 agent definitions
  skills/                           # 72 slash commands / workflows
  hooks/                            # 12 hook scripts
  rules/                            # 11 path-scoped coding standards
  statusline.sh                     # Status line: context %, model, stage, epic breadcrumb
  docs/
    workflow-catalog.yaml           # 7-phase pipeline definition
    templates/                      # 39 document templates
src/                                # Game source code
assets/                             # Art, audio, VFX, shaders, data files
design/                             # GDDs, narrative docs, level designs
docs/                               # Technical documentation and ADRs
tests/                              # Unit, integration, performance, playtest tests
tools/                              # Build and pipeline tools
prototypes/                         # Throwaway prototypes isolated from src/
production/                         # Sprint plans, milestones, release tracking
```

## Notable Workflow Pattern

The repo maps game production into a slash-command-driven lifecycle:

- **Onboarding:** `/start`, `/help`, `/project-stage-detect`, `/setup-engine`, `/adopt`
- **Design:** `/brainstorm`, `/map-systems`, `/design-system`, `/quick-design`, `/review-all-gdds`
- **Architecture:** `/create-architecture`, `/architecture-decision`, `/architecture-review`, `/create-control-manifest`
- **Planning:** `/create-epics`, `/create-stories`, `/sprint-plan`, `/story-readiness`, `/estimate`
- **Implementation:** `/dev-story`, `/story-done`
- **Reviews:** `/design-review`, `/code-review`, `/balance-check`, `/content-audit`, `/scope-check`, `/gate-check`
- **QA:** `/qa-plan`, `/smoke-check`, `/regression-suite`, `/test-evidence-review`, `/test-flakiness`
- **Release:** `/release-checklist`, `/launch-checklist`, `/changelog`, `/patch-notes`, `/hotfix`

## Why It Matters

This repo is a concrete example of the emerging pattern where Claude Code is treated less like a single coding assistant and more like a **role-structured operating environment**. It combines several themes relevant to `ai-research-os`: multi-agent orchestration, skills as reusable workflows, software-production guardrails, hooks for validation, and domain-specialized agent hierarchies.

It is also notable because the domain is game development, where quality requires coordination across engineering, design, art, narrative, UX, performance, QA, and production. The template therefore acts as a stress test for whether agentic coding systems can encode not just coding tasks, but a broader studio process.

## Installation / Usage

```bash
git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game
cd my-game
claude
```

Then start the workflow inside Claude Code:

```text
/start
```

## Repository Metadata

```json
{
  "full_name": "Donchitos/Claude-Code-Game-Studios",
  "description": "Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.",
  "html_url": "https://github.com/Donchitos/Claude-Code-Game-Studios",
  "stargazers_count": 16939,
  "forks_count": 2464,
  "watchers_count": 16939,
  "license": "MIT",
  "language": "Shell",
  "created_at": "2026-02-12T05:21:38Z",
  "updated_at": "2026-05-02T20:22:14Z",
  "pushed_at": "2026-05-02T10:47:53Z",
  "topics": [
    "ai-agents",
    "ai-assisted-development",
    "anthropic",
    "claude",
    "claude-code",
    "game-design",
    "game-development",
    "gamedev",
    "godot",
    "indie-game-dev",
    "unity",
    "unreal-engine"
  ]
}
```
