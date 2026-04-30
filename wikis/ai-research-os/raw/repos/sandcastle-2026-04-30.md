---
source: https://github.com/mattpocock/sandcastle
date: 2026-04-30
type: repo
tags: [sandcastle, coding-agents, sandboxing, claude-code, afk-agents, typescript]
---

# mattpocock/sandcastle

## Summary

Sandcastle is a TypeScript toolkit for orchestrating AI coding agents inside isolated sandbox environments. It provides a programmatic API, centered on `sandcastle.run()`, for invoking agents such as Claude Code against a repository, letting them work on branches or worktrees, and then merging or preserving their commits according to the configured strategy. It is designed for AFK software-factory workflows where multiple coding agents can implement, review, and iterate in parallel with stronger isolation than running everything directly on the host.

## Key points

- Repository: `mattpocock/sandcastle`.
- Package: `@ai-hero/sandcastle`.
- License: MIT.
- Language: TypeScript.
- Latest observed release: `v0.5.6`, Apr 29, 2026.
- Repo stats at capture time: about 2.1k stars, 174 forks, 26 releases, 889 commits.
- Core API: `run()` / `sandcastle.run()`.
- Main use case: orchestrating AI coding agents in isolated sandboxes.
- Built-in sandbox providers: Docker, Podman, Vercel Firecracker microVMs via `@vercel/sandbox`, plus custom providers.
- Supports branch/worktree strategies for agent commits and merges.

## Quick start

```bash
npm install --save-dev @ai-hero/sandcastle
npx sandcastle init
cp .sandcastle/.env.example .sandcastle/.env
npx tsx .sandcastle/main.ts
```

Environment setup commonly includes `ANTHROPIC_API_KEY` for Claude Code workflows. The repo also points to GitHub issue `#191` for using a Claude subscription instead of an API key.

## Minimal API example

```ts
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

await run({
  agent: claudeCode("claude-opus-4-6"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
});
```

## Sandbox providers

| Provider | Import path | Type | Notes |
|---|---|---|---|
| Docker | `@ai-hero/sandcastle/sandboxes/docker` | Bind mount | Works with `run()`, `createSandbox()`, and `interactive()` |
| Podman | `@ai-hero/sandcastle/sandboxes/podman` | Bind mount | Docker alternative |
| Vercel | `@ai-hero/sandcastle/sandboxes/vercel` | Isolated | Uses Vercel sandbox / Firecracker microVM infrastructure |
| No-sandbox | `@ai-hero/sandcastle/sandboxes/no-sandbox` | None | Interactive-only, runs directly on host |

## Why it matters

Sandcastle operationalizes a major pattern in modern AI engineering: treating coding agents as parallel workers rather than chat assistants. It is especially relevant to workflows with planning, isolated implementation, automated review, and controlled merge gates. Compared with ad-hoc agent runs, Sandcastle gives the workflow a reusable TypeScript control plane and explicit sandbox abstraction.

## Related source

- X announcement: https://x.com/mattpocockuk/status/2049506712801935611?s=2
- Companion video discovered during ingest: https://www.youtube.com/watch?v=E5-QK3CDVQM

## Raw content

Extracted repository facts:

- Title: GitHub - `mattpocock/sandcastle`: Orchestrate sandboxed coding agents in TypeScript with `sandcastle.run()`.
- Description: A TypeScript library for orchestrating AI coding agents in isolated sandboxes.
- Workflow:
  1. Invoke agents with a single `sandcastle.run()`.
  2. Run the agent in a sandbox using a configurable branch strategy.
  3. Merge or preserve commits according to the selected strategy.
- Prerequisites:
  - Git
  - Docker Desktop, Podman, Vercel sandbox, or a custom sandbox provider.
- Common use cases:
  - Running multiple AFK coding agents in parallel.
  - Building implementation/review pipelines.
  - Orchestrating custom agent workflows.
  - Running agents safely against isolated branches/worktrees.
