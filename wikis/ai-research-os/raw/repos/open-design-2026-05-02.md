---
source: https://github.com/nexu-io/open-design
date: 2026-05-02
type: repo
tags: [open-design, claude-design, design-systems, ai-design, coding-agents, agent-skills, local-first, byok, prototypes, hyperframes, hermes-agent]
status: processed
---

# nexu-io/open-design

**Repository:** https://github.com/nexu-io/open-design  
**Project:** Open Design  
**Owner:** nexu-io  
**License:** Apache-2.0  
**Primary language:** TypeScript  
**Stars:** 15,635  
**Forks:** 1,757  
**Default branch:** main  
**Latest release noted by GitHub summary:** Open Design `0.2.0`  
**Description:** Local-first, open-source alternative to Anthropic's Claude Design. Generates web, desktop, mobile prototypes, slides, images, videos, and HyperFrames; runs on Claude Code, Codex, Cursor, Gemini, OpenCode, Qwen, Copilot, Hermes, Kimi CLI, and other coding-agent runtimes.

## Summary

**Open Design** is a local-first, open-source alternative to Anthropic’s Claude Design. It connects existing coding-agent CLIs to a structured design artifact workflow, allowing users to generate web prototypes, desktop layouts, mobile screens, dashboards, marketing pages, decks, documents, images, videos, and HyperFrames HTML→MP4 motion graphics.

The project’s core claim is that Claude Design demonstrated an artifact-first design loop, but remained closed-source, cloud-only, paid-only, and Anthropic-locked. Open Design aims to reproduce the same mental model without lock-in: self-hostable, BYOK at every layer, deployable, and able to use whichever local coding-agent CLI is installed.

## Core Positioning

> The open-source alternative to Claude Design. Local-first, web-deployable, BYOK at every layer — coding-agent CLIs auto-detected on your `PATH` become the design engine, driven by composable Skills and brand-grade Design Systems.

The README positions Open Design as:

- Local-first and self-hostable
- BYOK / bring-your-own-key
- Compatible with multiple coding-agent CLIs
- Structured around composable design skills and design systems
- Able to export artifacts as HTML, PDF, PPTX, MP4, and related formats
- A sandboxed preview environment for generated design artifacts

## Supported Agent Engines

Open Design does not ship a single proprietary model or agent. Instead, its local daemon scans the user’s `PATH` and can spawn supported CLIs as the design engine.

Supported engines listed include:

- Claude Code
- Codex CLI
- Devin for Terminal
- Cursor Agent
- Gemini CLI
- OpenCode
- Qwen Code
- GitHub Copilot CLI
- Hermes
- Kimi CLI
- Pi
- Kiro CLI
- OpenAI-compatible BYOK proxy fallback

## Key Capabilities

- **Design artifact generation:** web, desktop, mobile, dashboards, marketing pages, slides, reports, images, and video/motion graphics.
- **Design systems:** large library of brand-grade design systems used as machine-readable and human-readable style guidance.
- **Skills:** composable workflow units that can inject prompts, references, side files, templates, and pre-flight instructions into the agent loop.
- **Sandboxed preview:** browser/iframe preview plus artifact linting and saving.
- **Exports:** HTML/PDF/PPTX/MP4 export paths.
- **Import path:** includes a Claude Design import route.
- **BYOK fallback:** OpenAI-compatible streaming proxy if no local CLI is available.

## Prompt Stack

The README describes a prompt stack that layers discovery directives, identity charter, active design system, active skill, project metadata, skill side files, and deck-specific directives.

```text
DISCOVERY directives  (turn-1 form, turn-2 brand branch, TodoWrite, 5-dim critique)
  + identity charter   (OFFICIAL_DESIGNER_PROMPT, anti-AI-slop, junior-pass)
  + active DESIGN.md   (72 systems available)
  + active SKILL.md    (31 skills available)
  + project metadata   (kind, fidelity, speakerNotes, animations, inspiration ids)
  + skill side files   (auto-injected pre-flight: read assets/template.html + references/*.md)
  + (deck kind, no skill seed) DECK_FRAMEWORK_DIRECTIVE   (nav / counter / scroll / print)
```

This is highly relevant to `ai-research-os` because it combines several active themes: agent skills, DESIGN.md-style design tokens, anti-AI-slop design prompts, local-first coding agents, and artifact-first generation.

## Architecture

Open Design has a browser UI backed by a local daemon. The daemon stores project/conversation state in SQLite, serves static artifacts and frames, exposes APIs for agents/skills/design systems/projects/templates/uploads, and spawns local coding-agent CLIs in per-project workspaces.

```text
┌────────────────────── browser (Next.js 16) ──────────────────────┐
│  chat · file workspace · iframe preview · settings · imports     │
└──────────────┬───────────────────────────────────┬───────────────┘
               │ /api/* (rewritten in dev)          │
               ▼                                    ▼
   ┌──────────────────────────────────┐   /api/proxy/stream (SSE)
   │  Local daemon (Express + SQLite) │   ─→ any OpenAI-compat
   │                                  │       endpoint (BYOK)
   │  /api/agents          /api/skills│       w/ SSRF blocking
   │  /api/design-systems  /api/projects/…
   │  /api/chat (SSE)      /api/proxy/stream (SSE)
   │  /api/templates       /api/import/claude-design
   │  /api/artifacts/save  /api/artifacts/lint
   │  /api/upload          /api/projects/:id/files…
   │  /artifacts (static)  /frames (static)
   │
   │  optional: sidecar IPC at /tmp/open-design/ipc/<ns>/<app>.sock
   │  (STATUS · EVAL · SCREENSHOT · CONSOLE · CLICK · SHUTDOWN)
   └─────────┬────────────────────────┘
             │ spawn(cli, [...], { cwd: .od/projects/<id> })
             ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │  claude · codex · devin (ACP) · gemini · opencode · cursor-agent │
   │  qwen · copilot · hermes (ACP) · kimi (ACP) · pi (RPC) · kiro     │
   │  reads SKILL.md + DESIGN.md, writes artifacts to disk            │
   └──────────────────────────────────────────────────────────────────┘
```

## Runtime Data Layout

```text
.od/
├── app.sqlite                 ← projects · conversations · messages · open tabs
├── artifacts/                 ← one-off "Save to disk" renders (timestamped)
└── projects/<id>/             ← per-project working dir, also the agent's cwd
```

## Quickstart

```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design
corepack enable
corepack pnpm --version   # should print 10.33.2
pnpm install
pnpm tools-dev run web
# open the web URL printed by tools-dev
```

## Why It Matters

Open Design is a notable convergence point for several emerging agentic-development patterns:

1. **Artifact-first AI workflows:** the model produces inspectable design artifacts rather than just prose.
2. **Local-first multi-agent runtime:** existing coding-agent CLIs become interchangeable execution engines.
3. **Skills + DESIGN.md:** reusable skills and design-system specs become the operating layer for design generation.
4. **Anti-lock-in architecture:** the system is self-hostable and can swap providers/agents.
5. **Hermes relevance:** Hermes is explicitly listed as one supported agent runtime, making this directly relevant to Self-OS/Hermes exploration.

## Repository Metadata

```json
{
  "full_name": "nexu-io/open-design",
  "description": "Local-first, open-source alternative to Anthropic's Claude Design. 19 Skills · 71 brand-grade Design Systems · Generate web, desktop, mobile prototypes, slides, images, videos, HyperFrames · Sandboxed preview · HTML/PDF/PPTX/MP4 export · Runs on Claude Code / Codex / Cursor / Gemini / OpenCode / Qwen / Copilot / Hermes / Kimi CLI.",
  "html_url": "https://github.com/nexu-io/open-design",
  "stargazers_count": 15635,
  "forks_count": 1757,
  "watchers_count": 15635,
  "license": "Apache-2.0",
  "language": "TypeScript",
  "created_at": "2026-04-28T04:25:20Z",
  "updated_at": "2026-05-02T21:20:26Z",
  "pushed_at": "2026-05-02T17:00:37Z",
  "homepage": "https://github.com/nexu-io/open-design",
  "topics": [
    "agent-skills",
    "ai-agents",
    "ai-design",
    "byok",
    "claude",
    "claude-code-for-design",
    "claude-design",
    "coding-agents",
    "design-systems",
    "design-tools",
    "desktop-app",
    "figma-alternative",
    "generative-ai",
    "hermes-agent",
    "local-first",
    "nextjs",
    "no-code",
    "prototyping",
    "ui-generator",
    "vibe-coding"
  ],
  "default_branch": "main"
}
```
