---
url: https://github.com/heygen-com/hyperframes
repo: heygen-com/hyperframes
saved: 2026-04-27
source: The Unwind AI newsletter
stars: 11.9k
license: Apache 2.0
language: TypeScript 97.4%
status: processed
---
# HyperFrames by HeyGen

> "Write HTML. Render video. Built for agents."

HyperFrames is an open-source, HTML-native video rendering framework. Compositions are plain HTML files with data attributes — no React, no proprietary DSL.

## Core Premise

HyperFrames' bet is **HTML**; Remotion's bet is React components.

## Key Capabilities

- **HTML-native authoring** — Paste and animate arbitrary HTML/CSS passthrough
- **Deterministic rendering** — same input = identical output
- **AI-first workflows** — CLI is non-interactive by default; designed for agent-driven pipelines
- **Frame Adapter pattern** — Bring your own animation runtime (GSAP, Lottie, CSS, Three.js)
- **Library-clock animations** — GSAP et al. are seekable/frame-accurate during render (not wall-clock)

## HyperFrames vs Remotion

| Dimension | HyperFrames | Remotion |
|-----------|-------------|----------|
| Authoring | HTML + CSS + GSAP | React components (TSX) |
| Build step | **None**; `index.html` plays as-is | Required (bundler) |
| Library-clock animations | Seekable, frame-accurate | Plays at wall-clock during render |
| Distributed rendering | Single-machine today | Lambda, production-ready |
| License | **Apache 2.0** (fully OSS) | Source-available/custom license |

## Quick Start

### AI Agent (Recommended)
```bash
npx skills add heygen-com/hyperframes
```
Registers slash commands:
- `/hyperframes` — Author compositions
- `/hyperframes-cli` — CLI commands
- `/gsap` — Animation help

### Manual
```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview   # live-reload browser preview
npx hyperframes render    # MP4 output
npx hyperframes lint      # validate composition
npx hyperframes doctor    # environment diagnostics
```

### Requirements
- Node.js ≥ 22
- FFmpeg

## Architecture & Packages

| Package | Path | Description |
|---------|------|-------------|
| `hyperframes` | `packages/cli` | Init, preview, lint, render, transcribe, TTS, doctor |
| `@hyperframes/core` | `packages/core` | Types, parsers, generators, linter, runtime, frame adapters |
| `@hyperframes/engine` | `packages/engine` | Seekable page-to-video capture engine (Puppeteer + FFmpeg) |
| `@hyperframes/producer` | `packages/producer` | Full rendering pipeline (capture + encode + audio mix) |
| `@hyperframes/studio` | `packages/studio` | Browser-based composition editor UI (React + Hono) |
| `@hyperframes/player` | `packages/player` | Embeddable `<hyperframes-player>` web component |
| `@hyperframes/shader-transitions` | `packages/shader-transitions` | WebGL shader transitions |

## AI Agent Plugin Ecosystem

Packaged as a **single source of truth** for multiple agent marketplaces:

- **Claude Code** — `.claude-plugin/plugin.json`; auto-discovers `skills/` directory
- **Cursor** — `.cursor-plugin/plugin.json`; available via Cursor Marketplace or sideload
- **Codex** — `.codex-plugin/plugin.json`; sparse-install supported
- **Claude Design** — `docs/guides/claude-design-hyperframes.md` produces valid first drafts

### Bundled Skills (`skills/`)

| Skill | Scope |
|-------|-------|
| `hyperframes` | HTML composition authoring, captions, TTS, audio-reactive animation, transitions |
| `hyperframes-cli` | CLI workflow guidance (init, lint, preview, render, doctor) |
| `hyperframes-registry` | Block/component installation via `hyperframes add` |
| `website-to-hyperframes` | Capture a URL → design system → video production pipeline |
| `gsap` | GSAP API, timelines, easing, ScrollTrigger, performance |

## Catalog & Registry

50+ ready-to-use blocks and components (shader transitions, social overlays, data viz):

```bash
npx hyperframes add flash-through-white   # shader transition
npx hyperframes add instagram-follow      # social overlay
npx hyperframes add data-chart            # animated chart
```

Browse: [hyperframes.heygen.com/catalog](https://hyperframes.heygen.com/catalog)

## Why It Matters

HyperFrames lowers the barrier for AI agents to produce professional video by authoring in plain HTML/CSS rather than learning a React component DSL. The Apache 2.0 license, agent-first CLI design, and multi-marketplace skill packaging make it a strong reference for agentic video generation pipelines.
