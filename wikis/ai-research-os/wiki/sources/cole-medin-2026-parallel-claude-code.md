---
title: "Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Cole Medin's factory system for parallel agent coding using Git worktrees, database branching, adversarial review, and self-healing workflows to achieve 10x output."
tags: [claude-code, git-worktrees, parallel-agents, coding-workflow, agent-factory, self-healing]
type: source
status: final
---

# Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship

**Type:** video
**Date:** 2026-04-26
**URL:** https://www.youtube.com/watch?v=rFGlJ4oIlhw
**Channel:** Cole Medin
**Raw file:** [[../../raw/youtube/2026-04-26-cole-medin-parallel-claude-code-git-worktrees.md]]

**Summary:** Cole Medin presents a factory system for parallel AI coding designed for 10x rather than 2x output. The architecture rests on five pillars: (1) **Issue as Spec** — GitHub issues scope individual units of work; (2) **Git Worktrees** — each agent works in an isolated codebase copy via Claude Code's native `--worktree` flag; (3) **Plan/Build/Implement** — staged development within each worktree; (4) **Independent Code Review** — validation never occurs in the same context window as implementation, using adversarial cross-agent review (including the Codex plugin for Claude Code); and (5) **Self-Healing** — when bugs escape, fix the system (rules, skills, workflows) not just the bug. Real-world challenges require database branching (Neon serverless Postgres), unique port assignment per worktree, and upfront dependency installation. Model tiering saves tokens: strongest models for coding, cheaper models for validation.

**Key contributions:**
- Git worktrees as the primitive for parallel agent isolation, natively supported by Claude Code
- Database branching (Neon) solving multi-agent database collision
- Adversarial cross-agent review preventing "grading your own homework"
- Self-healing layer: systematic improvement of rules and workflows from escaped defects
- Model tiering strategy for token efficiency across reasoning and validation tasks

**Tags:** claude-code, git-worktrees, parallel-agents, coding-workflow, agent-factory, self-healing
