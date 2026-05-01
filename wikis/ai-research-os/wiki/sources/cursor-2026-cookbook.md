---
title: "cursor/cookbook"
date_created: 2026-05-01
date_modified: 2026-05-01
summary: "[[entities/cursor-cookbook]] is Cursor's public examples repository for building with Cursor's coding-agent SDK."
tags: [cursor, coding-agents, sdk, agent-workflows, examples]
type: source
status: final
---

# cursor/cookbook

**Type:** repo  
**Date:** 2026-04-30  
**URL:** https://github.com/cursor/cookbook  
**Raw file:** [[../raw/repos/cursor-cookbook-2026-04-30.md]]

## Summary

[[entities/cursor-cookbook]] is Cursor's public examples repository for building with Cursor's coding-agent SDK. It shows how to move Cursor from an IDE-only experience into scripts, apps, CLIs, and cloud workflows. The examples include a quickstart for sending a prompt to a local agent and streaming events, an app-builder flow for creating projects in a sandboxed environment, an agent-kanban UI for viewing and creating Cursor Cloud Agents, and a terminal coding-agent CLI.

This source matters for [[concepts/programmable-coding-agents]] because it documents the emerging API surface around coding agents: prompts, models, cancellation, artifacts, conversation state, event streams, cloud agents, and repository selection. It complements Sandcastle rather than replacing it. Sandcastle focuses on the sandbox/control-plane abstraction around agent runs, while Cursor Cookbook shows how a vendor SDK can be embedded into custom developer tools and dashboards. The common pattern is that coding agents are becoming programmable infrastructure components, not just chat windows inside an editor.

## Key contributions
- Cursor Cookbook demonstrates SDK-based integration of Cursor coding agents into apps, scripts, CLIs, and cloud workflows.
- Notable examples include quickstart, app-builder, agent-kanban, and a coding-agent CLI.
- The repository is evidence that coding agents are becoming programmable developer-infrastructure components with event streams, artifacts, prompts, models, and conversation state.

## Concepts and entities

**Concepts:** [[concepts/programmable-coding-agents]], [[concepts/coding-agents]], [[concepts/agent-orchestration]]  
**Entities:** [[entities/cursor]], [[entities/cursor-cookbook]]

**Tags:** cursor, coding-agents, sdk, agent-workflows, examples
