---
title: "Full Walkthrough: Workflow for AI Coding from Planning to Production"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Matt Pocock's complete workflow for AI coding: human-in-the-loop planning with Grill Me, PRD and Kanban issue slicing, then AFK agent implementation via the Ralph loop."
tags: [ai-coding, workflow, planning, prd, kanban, agent-workflow]
type: source
status: final
---

# Full Walkthrough: Workflow for AI Coding from Planning to Production

**Type:** video
**Date:** 2026-04-26
**URL:** https://www.youtube.com/watch?v=-QFHIoCo-Ko
**Speaker:** Matt Pocock
**Raw file:** [[../../raw/youtube/2026-04-26-matt-pocock-workflow-ai-coding-planning-production.md]]

**Summary:** Matt Pocock details a production-ready workflow for AI-assisted software engineering built on two constraints: LLMs have a "smart zone" (~100k tokens) and suffer from the "Memento problem" (context resets). The workflow separates human-in-the-loop planning from AFK implementation. Planning begins with the **"Grill Me"** skill — adversarial interviewing that produces a shared design concept through 40–100 questions. This feeds a **PRD** (destination document) and a **Kanban board** of vertically sliced issues (journey document). Vertical slices (tracer bullets) cross all layers (schema, API, minimal UI) to provide immediate integration feedback, unlike horizontal layer-by-layer coding. Implementation uses the **"Ralph loop"** — an AFK agent picking unblocked issues, implementing in focused passes, running tests, committing, and repeating. The key discipline: planning is human, implementation is automated; code remains the battleground.

**Key contributions:**
- Smart zone concept: tasks sized under ~100k tokens to preserve LLM reasoning quality
- Memento problem: deterministic context clears preferred over compaction for predictable resets
- Grill Me → PRD → Kanban with vertical slices workflow
- Ralph loop: autonomous issue-by-issue implementation with test-and-commit cycles
- Clear separation: planning = human-in-the-loop; implementation = AFK agent

**Tags:** ai-coding, workflow, planning, prd, kanban, agent-workflow
