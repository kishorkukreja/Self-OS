---
source: telegram note + https://code.claude.com/docs/en/claude-code-on-the-web + https://code.claude.com/docs/en/remote-control
date: 2026-05-12
type: resource
tags: [claude-code, teleport, remote-control, cross-device-workflows, coding-agents, mobile-coding, self-os]
status: processed
---

# Claude Code teleport and remote-control cross-device workflows

## Summary
Claude Code now supports two complementary cross-device session flows. `claude --teleport` pulls a cloud/web/mobile Claude Code session down into a local terminal so the developer can continue with the full session context. `/teleport` is the in-session equivalent. `claude remote-control`, `claude --remote-control`, or `/remote-control` expose a local Claude Code session to claude.ai/code or the Claude mobile app, while the actual process and project environment keep running locally.

## Key commands
```bash
# Pull a cloud Claude Code session down to this machine
claude --teleport
claude --teleport <session-id>

# From inside an active cloud/web/mobile session
/teleport

# Control a local session from phone/browser
claude remote-control
claude --remote-control
claude --rc

# From inside an existing local session
/remote-control
/rc
```

## Why it matters
This closes a practical gap in mobile/desktop AI coding workflows: a developer can start Claude Code from phone/web, then continue locally without copy-pasting prompts or losing context. Conversely, a local session can be monitored and controlled from mobile/web while still retaining local filesystem, tools, MCP servers, and project configuration. For Self-OS, this points toward cross-surface continuity: Telegram/mobile/browser as control planes, local repo/terminal as execution substrate.

## Verified docs notes
From Claude Code web docs:
- Claude Code on the web runs coding tasks on Anthropic-managed cloud infrastructure at `claude.ai/code`.
- `claude --teleport` opens an interactive session picker; `claude --teleport <session-id>` resumes a specific cloud session locally.
- Cloud sessions start from fresh repo clones; committed repo files like `CLAUDE.md`, `.claude/settings.json`, `.mcp.json`, `.claude/rules/`, `.claude/skills/`, `.claude/agents/`, and `.claude/commands/` carry over, but local user config and secrets generally do not.

From Remote Control docs:
- Remote Control connects claude.ai/code or Claude mobile app to a Claude Code session running locally.
- Claude keeps running locally; the web/mobile UI is a remote window into the local session.
- Remote Control requires Claude Code v2.1.51 or later and claude.ai account auth; API keys are not supported.
- Team/Enterprise admins may need to enable the Remote Control toggle.
- Useful modes include server mode (`claude remote-control`), interactive local session with remote access (`claude --remote-control` / `--rc`), and in-session activation (`/remote-control` / `/rc`).
- `--spawn worktree` can create separate git worktrees for remote sessions, reducing conflict risk.

## Self-OS implications
- This strengthens the Self-OS idea of multiple control surfaces: Telegram/browser/mobile for steering, local Git-backed repos for durable execution.
- Cross-device continuity should be considered when designing Hermes/Codex/Claude handoff flows: a session should have a local state artifact, a resumable conversation/session ID, and explicit handoff notes.
- For security, remote-control should be treated as a local-execution exposure, not a generic public tunnel. Prefer trusted accounts, workspace trust checks, and worktree isolation when running multiple sessions.
- The `claude-code` Hermes skill has been updated with Teleport and Remote Control commands.

## User-provided note
```text
Ever start a Claude Code session on your phone and wish you could just pick it back up on your laptop? Right now, you lose your context and end up copy-pasting prompts. Boris Cherny, head of Claude Code at Anthropic, shared the fix on X.

To pull a cloud session down to your machine, run:

claude --teleport
Once you pick a session, your terminal resumes exactly where you left off with full context. You can also use the “/teleport” command from within an active session.

If you want to control a local session from your phone or browser instead, you can run “/remote-control”. The session will then show up in the mobile app and on the web.
```
