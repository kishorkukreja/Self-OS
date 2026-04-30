---
title: "Claude Code Monitor tool for background tasks"
date_created: 2026-04-30
date_modified: 2026-04-30
summary: "The Claude Code Monitor tool is described as a built-in mechanism for watching background scripts and waking the agent only when action is needed. The user-provided note says this replaces the previous pattern of repeate"
tags: [claude-code, monitor-tool, background-tasks, agent-harnesses, token-efficiency, developer-tools]
type: source
status: final
---

# Claude Code Monitor tool for background tasks

**Type:** resource  
**Date:** 2026-04-29  
**URL:** user-provided Telegram note; related: https://x.com/noahzweben/status/2042332268450963774  
**Raw file:** [[../raw/resources/claude-code-monitor-tool-background-tasks-2026-04-29.md]]

**Summary:** The Claude Code Monitor tool is described as a built-in mechanism for watching background scripts and waking the agent only when action is needed. The user-provided note says this replaces the previous pattern of repeatedly running /loop to poll for errors, which wasted API calls. With Monitor, a single prompt can start a dev server, stream stdout, avoid token burn while healthy, and let Claude respond when stack traces appear.

**Key contributions:**
- Problem: background development tasks in Claude Code previously required repeated polling such as /loop to check whether errors appeared.
- New pattern: ask Claude to start a dev server and use Monitor to watch for errors.
- Example prompt: “Start my dev server and use the Monitor tool to watch for errors.”
- Claimed behavior: Claude runs a background shell script and streams stdout.
- Claimed efficiency: zero tokens are burned while the server is healthy.
- Claimed remediation loop: if a stack trace appears, Claude wakes and fixes the detected issue.

**Tags:** claude-code, monitor-tool, background-tasks, agent-harnesses, token-efficiency, developer-tools
