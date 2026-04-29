---
source: user-provided Telegram note; related: https://x.com/noahzweben/status/2042332268450963774
date: 2026-04-29
type: resource
tags: [claude-code, monitor-tool, background-tasks, agent-harnesses, token-efficiency, developer-tools]
---

# Claude Code Monitor tool for background tasks

## Summary
The Claude Code Monitor tool is described as a built-in mechanism for watching background scripts and waking the agent only when action is needed. The user-provided note says this replaces the previous pattern of repeatedly running `/loop` to poll for errors, which wasted API calls. With Monitor, a single prompt can start a dev server, stream stdout, avoid token burn while healthy, and let Claude respond when stack traces appear.

## Key points
- Problem: background development tasks in Claude Code previously required repeated polling such as `/loop` to check whether errors appeared.
- New pattern: ask Claude to start a dev server and use Monitor to watch for errors.
- Example prompt: “Start my dev server and use the Monitor tool to watch for errors.”
- Claimed behavior: Claude runs a background shell script and streams stdout.
- Claimed efficiency: zero tokens are burned while the server is healthy.
- Claimed remediation loop: if a stack trace appears, Claude wakes and fixes the detected issue.
- Search corroboration found a Noah Zweben/X post described as announcing a Monitor tool that lets Claude create background scripts that wake the agent when needed.

## Why it matters
This is a useful agent-harness primitive: it replaces wasteful polling loops with event-driven monitoring. It is relevant to long-running coding agents, local dev servers, CI watching, PR monitoring, and token-efficient background supervision.

## Raw content
User-provided note:

> Tracking background tasks in Claude Code used to be a hassle. Users had to keep running “/loop” just to check for errors, which ended up wasting a lot of API calls. To streamline this, Claude Code PM Noah Zweben swapped out that clunky workaround for a built-in Monitor tool.
>
> Now, a single prompt automates the process.
>
> Start my dev server and use the Monitor tool to watch for errors.
>
> Claude runs a background shell script and streams stdout. It burns zero tokens while the server is healthy, but instantly fixes any stack traces it detects.

Related search result: `https://x.com/noahzweben/status/2042332268450963774`, titled “Thrilled to announce the Monitor tool which lets Claude create ...”, described as “Thrilled to announce the Monitor tool which lets Claude create background scripts that wake the agent up when needed.”

Other search results summarized the same feature as real-time log tracking, error detection, scheduled script polling of pull request status, background scripts that trigger agents based on conditions, and reduced token consumption/costs.
