---
source: https://crabbox.sh/
date: 2026-05-12
type: resource
tags: [crabbox, remote-execution, agent-workspaces, sandboxing, ci-hydration, parallel-agents, verification-loops, self-os]
status: processed
---

# Crabbox — remote agent workspaces and warm boxes

## Summary

Crabbox is a shared agent workspace control plane for keeping the local developer loop while running compute-heavy commands on remote machines. Its tagline is: **"Warm a box, sync the diff, run the suite."** A local CLI leases or reuses a remote target, syncs tracked and nonignored files, runs commands remotely, streams stdout/stderr back, and releases the target.

## Key points

- Keeps the normal local workflow: editor, Git, CLI commands, dirty checkout.
- Moves execution to remote capacity: brokered cloud machines, static SSH hosts, or sandbox providers.
- Uses a Cloudflare Worker + Durable Object broker to manage provider credentials, leases, cleanup, usage tracking, and cost guardrails.
- The CLI carries only a bearer token; provider credentials are not distributed to local machines or runners.
- Supports warm machines via `crabbox warmup`, reusable with `--id` across runs, SSH sessions, and CI hydration.
- Supports multiple runner/provider shapes: Hetzner, AWS, Azure, E2B, Daytona, Blacksmith, Semaphore, static SSH, Linux, Windows, and macOS.
- Can hydrate remote workspaces from GitHub Actions setup steps so local remote runs match CI setup.
- Provides browser desktop access through `crabbox webvnc` for UI testing, screenshots, and shared sessions.
- Can collect run evidence and artifacts: screenshots, videos, JUnit summaries, logs, and lease metadata.

## Architecture

Crabbox consists of:

- Local Go CLI.
- Cloudflare Worker.
- Fleet Durable Object that tracks leases and cost state.
- Remote cloud or SSH-backed runners.

Simplified flow:

```text
your laptop -> HTTPS -> Cloudflare Worker / Fleet Durable Object -> cloud provider
     |                                                           |
     +------------- SSH + rsync to leased runner ----------------+
```

## Why it matters

Crabbox is useful for AI-assisted engineering because it makes expensive or state-sensitive validation cheap to run remotely. It is especially relevant for big test suites, UI tests, multi-agent bug repair, and cases where local machine state may hide or create failures.

## Self-OS implications

- Night Shift agents should run risky or expensive validation in isolated remote workspaces, not only on the Hermes host.
- Crabbox-like artifacts could become evidence attached to PR reviews: logs, screenshots, JUnit, metadata.
- Warm boxes are a natural fit for repeated `test → patch → test` loops during big refactors.
- A Self-OS implementation pattern could be: taskOS spec → isolated worktree → Crabbox run → artifact bundle → PR review summary.

## Related source

Peter Steinberger's X post describes using Codex with ephemeral Crabboxes to reproduce bugs, verify failures, fix, and verify fixes across 10 parallel sessions.
