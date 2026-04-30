---
source: https://github.com/pbakaus/impeccable
date: 2026-04-30
type: repo
tags: [impeccable, frontend-design, ai-skills, design-systems, cursor, mcp, ui-ux]
---

# pbakaus/impeccable

## Summary

`pbakaus/impeccable` is a frontend design skill and command suite for making AI coding agents better at product UI, visual design, accessibility, responsive behavior, design systems, and UX copy. It builds on Anthropic's `frontend-design` skill and adds a broader design vocabulary, explicit anti-patterns, 7 domain reference files, and 23 `/impeccable` commands. It is designed to reduce generic AI UI output such as reflexive Inter typography, purple gradients, card-on-card layouts, and weak contrast.

## Key points

- Repository: `pbakaus/impeccable`.
- Tagline: "The design language that makes your AI harness better at design."
- Website: https://impeccable.style/
- Created by: Paul Bakaus.
- License: Apache 2.0.
- Latest observed release: `Skill 3.0.6`, Apr 30, 2026.
- Repo stats at capture time: about 23.7k stars, 1.2k forks, 44 watchers, 640 commits, 22 contributors.
- Primary languages: JavaScript, CSS, HTML, small TypeScript component.
- Core promise: 1 skill, 23 commands, and curated anti-patterns for higher-quality frontend design.

## What's included

### The `impeccable` skill

A comprehensive design skill with 7 domain-specific references:

| Reference | Covers |
|---|---|
| `typography` | Type systems, font pairing, modular scales, OpenType, readability |
| `color-and-contrast` | OKLCH, tinted neutrals, dark mode, accessibility, color roles |
| `spatial-design` | Spacing systems, grids, visual hierarchy |
| `motion-design` | Easing curves, staggering, reduced motion |
| `interaction-design` | Forms, focus states, loading patterns |
| `responsive-design` | Mobile-first design, fluid layouts, container queries |
| `ux-writing` | Button labels, error messages, empty states |

### Commands

All commands are accessed through `/impeccable` in supported harnesses.

| Command | Purpose |
|---|---|
| `/impeccable craft` | Full shape-then-build flow with visual iteration |
| `/impeccable teach` | One-time setup to gather design context and write `PRODUCT.md` / `DESIGN.md` |
| `/impeccable document` | Generate `DESIGN.md` from existing code |
| `/impeccable extract` | Pull reusable components and tokens into a design system |
| `/impeccable shape` | Plan UX/UI before code |
| `/impeccable critique` | UX design review: hierarchy, clarity, emotional resonance |
| `/impeccable audit` | Technical quality checks: accessibility, performance, responsive behavior |
| `/impeccable polish` | Final design-system and shipping-readiness pass |
| `/impeccable bolder` | Make bland designs more distinctive |
| `/impeccable quieter` | Tone down overly loud designs |
| `/impeccable distill` | Strip an interface to its essence |
| `/impeccable harden` | Cover error handling, i18n, text overflow, edge cases |
| `/impeccable onboard` | First-run flows, empty states, activation |
| `/impeccable animate` | Add purposeful motion |
| `/impeccable colorize` | Introduce strategic color |
| `/impeccable typeset` | Improve font choices, hierarchy, sizing |
| `/impeccable layout` | Fix layout, spacing, visual rhythm |
| `/impeccable delight` | Add moments of joy |
| `/impeccable overdrive` | Add ambitious, technically extraordinary effects |
| `/impeccable clarify` | Improve unclear UX copy |
| `/impeccable adapt` | Adapt UI for different devices |
| `/impeccable optimize` | Performance improvements |
| `/impeccable live` | Visual variant mode: iterate on elements in the browser |

## Related frontend-debugging pattern: Chrome DevTools MCP

The user also captured a related workflow for frontend debugging in Cursor: use Google's `chrome-devtools-mcp` server to give the coding agent a live Chrome instance, so it can inspect the UI, console, network tab, source-mapped stack traces, and request failures directly instead of guessing from pasted errors or screenshots.

Cursor MCP setup:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

Example prompt:

```text
My checkout button isn't firing. Open localhost:3000, click it, and tell me what's wrong.
```

This pairs naturally with Impeccable: use DevTools MCP for evidence from the running UI, then use Impeccable-style audit/polish/harden workflows for design and implementation quality.

## Why it matters

Impeccable is relevant to AI coding-agent workflows because frontend work fails when the agent lacks design taste, product context, and browser feedback. The combination of Impeccable and Chrome DevTools MCP attacks both problems: Impeccable gives the agent better design vocabulary and anti-pattern awareness, while DevTools MCP gives it live runtime evidence from the page.

## Raw content

Repository extraction summary:

- Project: Impeccable.
- Positioning: "The vocabulary you didn't know you needed. 1 skill, 23 commands, and curated anti-patterns for impeccable frontend design."
- Quick start: visit https://impeccable.style/ to download ready-to-use bundles.
- Built on Anthropic's original `frontend-design` skill.
- Targets common AI-generated UI mistakes, including generic font choices, purple gradients, nested cards, and gray text on colored backgrounds.
- Main skill file: `source/skills/impeccable/SKILL.md`.
- The skill enforces context gathering through `PRODUCT.md` and optionally `DESIGN.md`, with commands like `teach`, `shape`, `craft`, `audit`, and `polish` to move from product context to higher-quality implementation.
