---
title: "HyperFrames by HeyGen"
date_created: 2026-04-29
date_modified: 2026-04-29
summary: "HyperFrames by HeyGen captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and desi"
tags: [ai-tools]
type: source
status: final
---

# HyperFrames by HeyGen

**Type:** repo  
**Date:** 2026-04-27  
**URL:** The Unwind AI newsletter  
**Raw file:** [[../../raw/repos/hyperframes-2026-04-27.md]]

**Summary:** HyperFrames by HeyGen captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and design trade-offs that can be compared against the rest of the AI Research OS corpus. "Write HTML. Render video. Built for agents." HyperFrames is an open-source, HTML-native video rendering framework. Compositions are plain HTML files with data attributes — no React, no proprietary DSL. HyperFrames' bet is HTML; Remotion's bet is React components. - HTML-native authoring — Paste and animate arbitrary HTML/CSS passthrough - Deterministic rendering — same input = identical output - AI-first workflows — CLI is non-interactive by default; designed for agent-driven pipelines - Frame Adapter pattern — Bring your own animation runtime (GSAP, Lottie, CSS, Three.js) - Library-clock animations — GSAP et al. are seekable/frame-accurate during render (not wall-clock) Authoring  HTML + CSS + GSAP  React components (TSX) Build step  None; index.html plays as-is  Required (bundler) Library-clock animations  Seekable, frame-accurate  Plays at wall-clock during render Distributed rendering  Single-machine today  Lambda, production-ready License  Apache 2.0 (fully OSS)  Source-available/custom license

**Key contributions:**
- "Write HTML. Render video. Built for agents."
- HyperFrames is an open-source, HTML-native video rendering framework. Compositions are plain HTML files with data attributes — no React, no proprietary DSL.
- HyperFrames' bet is HTML; Remotion's bet is React components.
- - HTML-native authoring — Paste and animate arbitrary HTML/CSS passthrough
- - Deterministic rendering — same input = identical output

**Related concepts:** [[concepts/ai-tools]]  
**Primary entity:** [[entities/hyperframes-by-heygen]]

**Tags:** ai-tools
