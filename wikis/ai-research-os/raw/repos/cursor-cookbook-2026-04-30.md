---
source: https://github.com/cursor/cookbook
date: 2026-04-30
type: repo
tags: [cursor, coding-agents, sdk, agent-workflows, examples]
---

# cursor/cookbook

## Summary

`cursor/cookbook` is Cursor's public examples repository for building with Cursor, especially the Cursor SDK. It contains small TypeScript examples showing how to run Cursor's coding agent from apps, scripts, CLIs, and cloud workflows. The repository is useful as a practical reference for integrating Cursor Cloud Agents into custom developer tools, dashboards, and autonomous coding pipelines.

## Key points

- Public GitHub repo: `cursor/cookbook`.
- Purpose: small examples for building with Cursor.
- Primary focus: Cursor SDK, the TypeScript API for running Cursor's coding agent from code.
- Primary language: TypeScript.
- Repository stats at capture time: about 2.6k stars, 287 forks, 6 commits.
- Latest observed commit: `df5f5a0` by `leerob`, message `Migrate coding agent CLI to OpenTUI (#1)`, dated Apr 29, 2026.
- Setup requires a Cursor API key from the Cursor integrations dashboard exposed as `CURSOR_API_KEY`.
- Official SDK docs: https://cursor.com/docs/api/sdk/typescript

## Notable examples

### `sdk/quickstart`

Minimal Node.js example that creates a local Cursor agent, sends one prompt, and streams the response.

### `sdk/app-builder`

A web app for spinning up Cursor agents to scaffold new projects and iterate on ideas in a sandboxed cloud environment.

### `sdk/agent-kanban`

A kanban-style interface for Cursor Cloud Agents. It supports viewing agents, grouping by status or repository, previewing artifacts, and creating new cloud agents from a repository and prompt.

### `sdk/coding-agent-cli`

A minimal terminal-based interface for spawning Cursor agents.

## Why it matters

This is a strong implementation reference for moving Cursor from an IDE-only workflow into programmable agent orchestration. The examples map directly onto the user's interest in segmented coding-agent workflows, dashboards for agent state, and automated implementation/review pipelines.

## Raw content

Source extraction summary from GitHub:

- Repository: `cursor/cookbook`
- Visibility: public
- Purpose: small examples for building with Cursor.
- Cursor SDK overview: the TypeScript API for running Cursor's coding agent from apps, scripts, and workflows. It supports the same agent across local workspaces and cloud runtimes, streams agent events as runs progress, and lets callers manage prompts, models, cancellation, artifacts, and conversation state from code.
- Setup: create a Cursor API key from the Cursor integrations dashboard and set `CURSOR_API_KEY`.
- Contents:
  - `sdk/quickstart`
  - `sdk/app-builder`
  - `sdk/agent-kanban`
  - `sdk/coding-agent-cli`
  - `README.md`
- Contributors observed: `ericzakariasson`, `leerob`, `cursoragent`, `rwashburne`.
