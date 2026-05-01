---
title: "mattpocock/sandcastle"
date_created: 2026-05-01
date_modified: 2026-05-01
summary: "[[entities/sandcastle]] is a TypeScript toolkit for orchestrating AI coding agents inside isolated sandbox environments."
tags: [sandcastle, coding-agents, sandboxing, claude-code, afk-agents, typescript]
type: source
status: final
---

# mattpocock/sandcastle

**Type:** repo  
**Date:** 2026-04-30  
**URL:** https://github.com/mattpocock/sandcastle  
**Raw file:** [[../raw/repos/sandcastle-2026-04-30.md]]

## Summary

[[entities/sandcastle]] is a TypeScript toolkit for orchestrating AI coding agents inside isolated sandbox environments. Its core API, `sandcastle.run()`, gives developers a programmable control plane for invoking agents such as [[entities/claude-code]] against a repository, running them in Docker, Podman, Vercel Firecracker microVMs, or custom sandboxes, and then managing commits through branch or worktree strategies. The repo turns AFK coding from an ad-hoc chat pattern into a structured workflow with setup, execution, isolation, and merge behavior.

The source is important because it makes [[concepts/sandboxed-coding-agents]] concrete. Sandcastle's value is not simply safer execution; it supports a software-factory model where multiple agents can run in parallel, use separate branches, and feed implementation/review loops without trampling the host checkout. The quick-start path and TypeScript API make it relevant to teams already building custom agent harnesses. It should be tracked alongside coding-agent orchestration, agent verification, context engineering, and automated review pipelines.

## Key contributions
- Sandcastle provides a TypeScript API for running coding agents in isolated Docker, Podman, Vercel, or custom sandboxes.
- It supports branch/worktree strategies so agent commits can be merged or preserved deliberately.
- The repository operationalizes AFK software-factory workflows by treating coding agents as parallel workers with explicit isolation and control-plane logic.

## Concepts and entities

**Concepts:** [[concepts/sandboxed-coding-agents]], [[concepts/software-factory-workflows]], [[concepts/agent-orchestration]], [[concepts/coding-agents]]  
**Entities:** [[entities/sandcastle]], [[entities/matt-pocock]], [[entities/claude-code]]

**Tags:** sandcastle, coding-agents, sandboxing, claude-code, afk-agents, typescript
