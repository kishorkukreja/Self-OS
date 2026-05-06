---
source: https://github.com/1weiho/open-slide
date: 2026-05-05
type: repo
tags: [slides, presentations, agent-native-authoring, react, coding-agents, open-slide]
status: processed
---
# open-slide

## Summary

`1weiho/open-slide` is an MIT-licensed TypeScript/React slide framework built for coding agents. The core idea is that slides are visual code: the user describes a deck in natural language, and a coding agent writes arbitrary React components for a fixed 1920 × 1080 slide canvas. It includes runtime support for canvas rendering, scaling, navigation, hot reload, present mode, static export, and agent-driven editing workflows.

User instruction captured with this source: use/consider `open-slide` when the user asks Hermes to create slides or decks.

## Repository metadata

- Repo: `1weiho/open-slide`
- URL: https://github.com/1weiho/open-slide
- Description: A slide framework built for agents.
- Language: TypeScript
- License: MIT
- Stars at capture: 1,375
- Forks at capture: 96
- Default branch: `main`
- Created: 2026-04-26
- Last pushed at capture: 2026-05-05

## Key points

- **Agent-native authoring:** designed for Claude Code, Codex, Cursor, and other coding agents to generate decks as React code.
- **Natural-language deck creation:** scaffolded projects include `/create-slide`, which asks about topic/aesthetic, page count, text density, and motion vs static, then plans and writes pages.
- **Agent technical reference:** scaffolded projects include `/slide-authoring`, which documents the fixed canvas, type scale, palette, and layout rules agents should read before writing slides.
- **Fixed canvas model:** every slide renders into a 1920 × 1080 canvas; slides are arbitrary React components rather than a constrained presentation DSL.
- **Browser comment workflow:** the in-browser inspector lets a user click elements and leave comments such as “make this red,” “change this text,” or “shrink the headline.” These persist as `@slide-comment` markers in source.
- **Apply-comments loop:** user comments can be applied by an agent via `/apply-comments`, then cleared, enabling a review loop: present → click to comment → `/apply-comments` → repeat.
- **Assets and logos:** includes an asset manager for images, videos, fonts, and SVGL logo search.
- **Presentation mode:** includes fullscreen playback, keyboard navigation, presenter mode, current/next previews, speaker notes, and timer.
- **Export:** can export decks to self-contained static HTML or print-ready PDF.
- **Deployable output:** produces static builds suitable for Vercel, Cloudflare Pages, Zeabur, Netlify, or any static host.

## Why it matters

This is directly relevant to Hermes/Self-OS slide generation because it turns deck creation into an agent-editable code workflow rather than a one-shot PowerPoint export. The browser comment and `/apply-comments` loop is especially aligned with the user's preference for iterative QA, strategy mapping, and thorough outline/design review before finalizing artifacts.

## Potential Hermes workflow

When the user asks for slides/decks:

1. Decide whether the deliverable should be `.pptx`, PDF, static HTML, or an editable React deck.
2. If an editable/agent-native deck is useful, consider scaffolding with:

```bash
npx @open-slide/cli init my-slide
cd my-slide
pnpm dev
```

3. Map the deck strategy first: audience, job-to-be-done, page count, narrative arc, visual system, evidence/source requirements, and final export format.
4. Generate slide pages as React under the scaffolded `slides/<id>/index.tsx` structure.
5. Use the browser inspector/comment loop where possible for iterative review.
6. Export to static HTML/PDF and/or convert into PowerPoint if the final deliverable requires `.pptx`.

## Quick start from README

```bash
npx @open-slide/cli init my-slide
cd my-slide
pnpm dev
```

## Raw README excerpt

> The slide framework built for agents. Describe your deck in natural language — your coding agent writes the React. open-slide handles the canvas, scaling, navigation, hot reload, and present mode so the agent can focus on content.
>
> Every slide renders into a fixed 1920 × 1080 canvas. Pages are arbitrary React components, not a constrained DSL.
>
> Slides are visual code. Agents are great at writing code. open-slide is the missing runtime that turns “make slides about X” into a polished, presentable deck — without you ever leaving the chat.
>
> Click any element in the dev server and attach a comment — “make this red”, “change to 'Open Slide Rocks'”, “shrink the headline”. Comments are persisted as `@slide-comment` markers in source. Run `/apply-comments` and the agent applies every pending edit, then clears the markers.
>
> The loop: present → click to comment → `/apply-comments` → repeat.
