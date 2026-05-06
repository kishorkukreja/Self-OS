---
source: https://github.com/Manavarya09/design-extract
date: 2026-05-06
type: repo
tags: [design-systems, design-tokens, frontend-tooling, agent-tools, figma, tailwind, shadcn, mcp]
---

# Designlang / design-extract

## Summary
`designlang` / `design-extract` is a GitHub repository by Manavarya09 for extracting a website's complete design system from the live DOM. It uses a headless browser to inspect real rendered pages and emits a broad design-system package: DTCG tokens, Tailwind config, shadcn/ui theme, Figma variables, CSS variables, motion tokens, typed component anatomy, brand voice, page-intent labels, design report cards, and prompt packs for tools such as v0, Lovable, Cursor, and Claude Artifacts.

The repo is notable because it treats websites as inspectable source-of-truth design systems rather than just screenshots or pages to clone. For Self-OS, this belongs in the design/frontend tooling cluster alongside design-md, Refero Styles, shadcn, Tailwind, and agent-native UI generation workflows.

## Repository
- GitHub: https://github.com/Manavarya09/design-extract
- Package / product name: `designlang`
- Websites: https://designlang.manavaryasingh.com / https://www.designlang.app
- License: MIT
- Runtime: Node 20+, Playwright / headless Chromium
- Approximate GitHub stats at capture: ~2.2k stars, ~202 forks
- Primary language: JavaScript

## Key points
- Extracts live DOM design signals with one command, instead of relying only on static screenshots or hand-written brand guidelines.
- Emits 17+ output files including DTCG design tokens, Tailwind config, shadcn theme, Figma variables, CSS custom properties, component anatomy, motion tokens, brand voice, and AI prompt packs.
- Includes deeper design analysis: layout patterns, responsive behavior across multiple breakpoints, hover/focus/active states, WCAG contrast scoring, multi-page consistency, drift checks, visual diffs, and shareable graded report cards.
- Supports downstream platform emitters for web, iOS SwiftUI, Android Compose, Flutter, and WordPress.
- Includes an MCP / agent-facing workflow for Claude Code, Cursor, Windsurf, and other coding agents.

## Example commands

```bash
npx designlang https://stripe.com
npx designlang pack stripe.com
npx designlang remix stripe.com --as cyberpunk
npx designlang grade https://stripe.com --badge
npx designlang battle stripe.com vercel.com
npx designlang clone https://stripe.com
npx designlang --full https://stripe.com
```

Install globally:

```bash
npm i -g designlang
```

Install as an agent skill:

```bash
npx skills add Manavarya09/design-extract
```

Agent command:

```text
/extract-design <url>
```

## Output files mentioned by the README
- `*-design-language.md` — 19-section AI-ready markdown spec for recreating the design.
- `*-design-tokens.json` — W3C / DTCG tokens with primitive, semantic, and composite layers.
- `*-tailwind.config.js` — drop-in Tailwind theme.
- `*-shadcn-theme.css` — shadcn/ui globals variables.
- `*-figma-variables.json` — Figma variables import, including light and dark support.
- `*-variables.css` — CSS custom properties.
- `*-anatomy.tsx` — typed React stubs for detected components and variants.
- `*-motion-tokens.json` — durations, easings, springs, and scroll-linked motion flags.
- `*-voice.json` — brand voice: tone, pronoun posture, CTA verbs.
- `*-prompts/` — prompt packs for v0, Lovable, Cursor, and Claude Artifacts.
- `*-mcp.json` — disk-backed MCP payload.
- `*-grade.html` / `*-grade.svg` — report card and badge.
- `*-battle.html` — head-to-head design-system comparison card.
- `*-remix.<vocab>.html` — restyled site variants.

## Why it matters
This is operationally useful for agent-assisted design because it converts an existing live website into structured design-system artifacts agents can actually consume. It bridges visual inspiration, design token extraction, Figma variable import, Tailwind/shadcn implementation, and prompt-pack generation. In Self-OS terms, this could become part of a design ingestion workflow: capture a reference site, extract its tokens and interaction language, then feed those outputs into UI generation, design review, or `DESIGN.md`-style specs.

## Raw content

GitHub repository summary extracted from the live repository page:

- Repository: `Manavarya09/design-extract`
- Product/package: `designlang`
- About: Extract any website's complete design system with one command. DTCG tokens, semantic + primitive + composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters, Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension.
- Core README pitch: `designlang` points a headless browser at any URL and reads the design system off the live DOM. One command emits 17+ files — DTCG tokens, Tailwind config, shadcn theme, Figma variables, motion tokens, typed component anatomy, brand voice, page-intent labels, and a paste-ready prompt pack for v0 / Lovable / Cursor / Claude Artifacts.
- It also captures layout patterns, responsive behavior across four breakpoints, hover/focus/active states, WCAG contrast scoring, multi-page consistency, drift checks against a live source of truth, visual diffs, and a shareable graded report card.
