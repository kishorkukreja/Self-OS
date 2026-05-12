---
source: https://github.com/walkinglabs/learn-harness-engineering
date: 2026-05-12
type: repo
tags: [harness-engineering, coding-agents, agent-reliability, claude-code, ai-engineering, verification, self-os]
---

# walkinglabs/learn-harness-engineering

## Summary
`walkinglabs/learn-harness-engineering` is a project-based course for learning how to build the environment around AI coding agents so they can complete real engineering work reliably. The repository frames failures in AI coding work as harness failures rather than purely model failures: missing instructions, missing state, weak verification, loose scope, and poor session lifecycle management. The repo includes a VitePress documentation site, multilingual READMEs, hands-on TypeScript/Electron projects, and harness artifacts such as `AGENTS.md`, `CLAUDE.md`, `feature_list.json`, `init.sh`, and `claude-progress.md` inside project roots.

## Metadata
- Repository: `https://github.com/walkinglabs/learn-harness-engineering`
- Documentation site: `https://walkinglabs.github.io/learn-harness-engineering/`
- Description: Harness engineering official style beginner tutorial, from 0 to 1
- Main language: TypeScript
- Stars at capture: ~4,032
- Forks at capture: 388
- Default branch: `main`
- License: none detected via GitHub API
- Last pushed at capture: 2026-05-11T03:40:20Z

## Key points
- Core thesis: **the model is smart; the harness makes it reliable**.
- Harness engineering is not prompt engineering alone; it is the design of the working environment the agent operates inside.
- The course defines five harness subsystems: instructions, state, verification, scope, and session lifecycle.
- The README cites an Anthropic-style comparison where the same model and prompt produced poor output without a harness but useful output with a planner/generator/evaluator harness.
- The repo structure itself is a teaching artifact: docs, lectures, projects, solutions, skills, and progressive project stages.

## Why it matters
This is highly aligned with Self-OS/Hermes because it provides an explicit curriculum for turning AI coding agents from prompt responders into reliable engineering workers. The useful finding is that reliability comes from the *surrounding system*: local state, restartable sessions, verification gates, scoped feature slices, and lifecycle handoffs. That overlaps with taskOS, Hermes Kanban, Mission-Oriented Workspaces, Goal Buddy-style `goal.md` + `state.yaml`, and the user's preference for real engineering rather than vibe coding.

## Self-OS implications
- Connect this source to the existing **agent harness / harness engineering** concept cluster.
- Treat the five-subsystem model as a candidate rubric for Self-OS agent workspaces:
  - Instructions → `CLAUDE.md`, `AGENTS.md`, skills, operating contract.
  - State → `task-state.md`, `state.yaml`, Kanban cards, progress logs.
  - Verification → tests, lint, evals, smoke runs, reviewer receipts.
  - Scope → vertical slices, one feature at a time, acceptance criteria.
  - Session lifecycle → initialization, checkpoints, handoff notes, clean restart state.
- The repo should inform any future `harness-engineering` Hermes skill or taskOS template for coding-agent projects.
- Strong candidate for wiki compile into a fuller concept page on `harness-engineering` and links to Goal Buddy, 12-rule `CLAUDE.md`, and auto-improving software loops.

## Repository structure captured
```text
.github/
.gitignore
CLAUDE.md
README-CN.md
README-KO.md
README.md
docs/
get_anthropic_logo.js
package-lock.json
package.json
projects/
scripts/
skills/
```

Top-level `docs/` entries:
```text
.vitepress/
en/
index.md
ko/
public/
ru/
uz/
vi/
zh/
```

Top-level `skills/` entries:
```text
README.md
README-CN.md
README-KO.md
harness-creator/
```

Projects:
```text
project-01/
project-02/
project-03/
project-04/
project-05/
project-06/
shared/
```

## Raw README summary
The course is a project-based guide to building reliable coding environments for AI agents. Its core claim is that strong models alone are insufficient: "The strongest model in the world will still fail on real engineering tasks if you don't build a proper environment around it." The repo argues that many failures are harness failures — missing structure, state, verification, scoping, and lifecycle control.

A harness has five subsystems:
1. Instructions — what to do, what to read, and in what order; ideally with progressive disclosure.
2. State — persisted records of what has been done, what is in progress, and what comes next.
3. Verification — runnable proof such as tests, lint, type-checks, smoke runs, or e2e checks.
4. Scope — one feature at a time, with a definition of done and no hidden overreach.
5. Session lifecycle — init at start, clean state at end, and a handoff path for the next session.

The model decides what code to write. The harness governs when, where, and how it writes it. The harness does not make the model smarter; it makes the model's output reliable.

## Captured CLAUDE.md details
The repository's own `CLAUDE.md` says this is a VitePress documentation site plus hands-on project code. Main commands include:

```bash
npm install
npm run docs:dev
npm run docs:build
npm run docs:preview

# Project Electron apps, from each project directory
npm install
npm run dev
npm run check
npm run test
npm run test:watch
```

Architecture notes:
- The course revolves around an Electron knowledge-base desktop app evolving across six projects.
- Main process: window management, IPC handlers, service initialization.
- Preload: `contextBridge` exposing typed API to renderer.
- Renderer: React UI with document list, Q&A panel, status bar.
- Services: DocumentService, IndexingService, QaService, PersistenceService.
- Shared types: cross-boundary interfaces and IPC channel constants.
- Harness files in project roots include `AGENTS.md`, `CLAUDE.md`, `feature_list.json`, `init.sh`, and `claude-progress.md`.
