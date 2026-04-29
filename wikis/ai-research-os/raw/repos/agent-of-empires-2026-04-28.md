---
status: processed
---
# Agent of Empires (AoE): AI Agent Session Manager

**URL:** https://github.com/njbrake/agent-of-empires  
**License:** MIT  
**Author:** Nate Brake ([@natebrake](https://x.com/natebrake)), Machine Learning Engineer at Mozilla.ai  
**Stats:** 1.7k stars · 140 forks · 84 tags · 675 commits · 37 contributors  
**Languages:** Rust 80.2%, TypeScript 15.7%, Astro 1.5%, JavaScript 0.9%

## Overview

> Running one AI agent is easy. Running five of them across different branches, keeping track of which is stuck, which is waiting on input, and which just made a mess of your working tree, becomes a part-time job. AoE makes it a glance: one dashboard, one status column, git worktrees and Docker sandboxes set up for you, and sessions that outlive your terminal.

A session manager for AI coding agents on Linux and macOS. Run multiple agents in parallel across different branches, each in its own isolated session. Access agents from a **TUI**, any **browser**, or the **CLI**.

## Supported Agents

Claude Code · OpenCode · Mistral Vibe · Codex CLI · Gemini CLI · Cursor CLI · Copilot CLI · Pi.dev · Factory Droid · **Hermes**

AoE auto-detects which tools are installed on your system.

## Core Capabilities

- **Multi-interface access**
  - **TUI** (`aoe`): Visual dashboard to create, monitor, and manage sessions.
  - **Web Dashboard (Beta)**: Real xterm.js terminal rendered in the browser; switch sessions, type commands, review diffs. Installable as a PWA. Start with `aoe serve` or press `R` in the TUI.
  - **CLI**: Full command suite (`aoe add`, `aoe status`, etc.) for scripting and integrations like OpenClaw.

- **Session persistence via tmux**
  Each agent runs in its own tmux session. Close the TUI, disconnect SSH, or crash your terminal—agents keep running.
  **Key shortcut:** `Ctrl+b d` detaches from a session and returns to the TUI.

- **Remote phone access**
  Press `R` in the TUI to serve the web dashboard over HTTPS with QR + passphrase auth.
  - Prefers **Tailscale Funnel** for stable URLs (PWA keeps working across restarts).
  - Falls back to **Cloudflare Tunnel**.

- **Claude Session Resume (MVP)**
  Persists Claude session IDs so agents resume after reboot, upgrade, or runtime rotation (`/clear`, `--fork-session`).

- **Git worktrees & Docker sandboxing**
  - Run parallel agents on different branches of the same repo via automatic worktree management.
  - Optional container isolation with shared auth volumes.

- **Agent-aware status detection**
  Detects running, waiting-for-input, idle, and error states using file-based hooks rather than brittle tmux pane parsing.

- **Diff & Edit**
  Review git changes and edit files inline in the TUI without switching contexts.

## Installation

Prerequisites: [tmux](https://github.com/tmux/tmux/wiki) (required), [Docker](https://www.docker.com/) (optional, for sandboxing)

```bash
# Quick install (Linux & macOS)
curl -fsSL \
  https://raw.githubusercontent.com/njbrake/agent-of-empires/main/scripts/install.sh \
  | bash

# Homebrew
brew install aoe

# Nix
nix run github:njbrake/agent-of-empires

# Build from source
git clone https://github.com/njbrake/agent-of-empires
cd agent-of-empires && cargo build --release
```

## Quick Start

```bash
aoe                          # Launch the TUI
aoe add --cmd claude         # Create a session running Claude Code
aoe serve                    # Start the web dashboard
```

In the TUI, press `?` for context-aware keybindings.

## Recent Major Changes

### Hermes Agent Support (#846) — Latest
- Replaced brittle tmux pane-parsing detector with **YAML file-based status hooks** (`~/.hermes/config.yaml`).
- Pre-populates `~/.hermes/shell-hooks-allowlist.json` so registration runs without TTY consent prompts.
- Sets `HERMES_ACCEPT_HOOKS=1` in container env as a bypass for the consent gate.

### Claude Session Resume MVP (#838)
- Adds `ResumeStrategy` enum and `SessionPoller` (fixed-interval thread).
- CLI commands added: `aoe session set-session-id`, `aoe session show --json`.

### Web Dashboard Redesign (#607)
- Complete workspace redesign.

## Why It Matters

AoE is the most complete multi-agent session manager available. It combines tmux persistence, git worktrees, Docker sandboxing, web dashboard (PWA), and remote phone access into one Rust-built tool. The Hermes support is notable — it uses file-based status hooks rather than brittle terminal parsing. Essential for anyone running parallel agent workflows.

## Tags

- agent-session-manager
- multi-agent
- tmux
- git-worktrees
- docker-sandbox
- tui
- web-dashboard
- rust
- claude-code
- codex
- hermes
- parallel-agents
