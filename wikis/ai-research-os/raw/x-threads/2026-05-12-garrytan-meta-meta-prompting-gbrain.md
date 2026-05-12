---
source: https://x.com/garrytan/status/2053127519872614419?s=20
date: 2026-05-12
type: thread
tags: [gbrain, garry-tan, personal-ai, skillify, fat-skills, thin-harness, openclaw, hermes-agent, knowledge-graph, self-os]
---

# Garry Tan: Meta-Meta-Prompting — The Secret to Making AI Agents Work

## Summary
Garry Tan describes his personal AI stack as a compounding operating system rather than a chat interface. The core pattern is “fat skills, fat code, thin harness”: OpenClaw/Hermes route messages through a thin runtime, while detailed Markdown skills and a large structured brain repo carry the operational knowledge. GBrain acts as the knowledge infrastructure: pages for people, companies, meetings, books, articles, and ideas; entity propagation; retrieval; graph links; and recurring cron jobs. The article's practical starting advice is to pick a harness, start a brain with GBrain, do real work, then run Skillify to convert repeated workflows into reusable skills.

## Key points
- Personal AI becomes powerful when it is treated as an operating system with state, skills, retrieval, and background jobs — not as a stateless chatbot.
- GBrain is described as a 100,000-page structured personal knowledge base with compiled truth, append-only timelines, and raw sidecars.
- “Book mirror” is the flagship example: extract a book chapter-by-chapter, summarize the author's ideas, and map them to Garry's actual life/context using brain retrieval.
- The system improved through iteration: fact-checking, cross-modal eval, deep retrieval, and per-section brain searches were added after failures.
- Skillify is the recursive meta-skill: it extracts repeatable workflows into tested skills with triggers and edge cases, then registers them in the resolver.
- Skills compose: book-mirror can call brain-ops, enrich, cross-modal-eval, and pdf-generation.
- Models are treated as interchangeable engines; the durable value is in skills, code, and data.
- The linked open-source stack includes GStack, GBrain, OpenClaw, and Hermes Agent.

## Why it matters
This is one of the clearest external articulations of the same direction as Self-OS: a personal operating system made of durable knowledge, procedural skills, scheduled agents, and thin routing harnesses. The useful finding is that “memory” is not a single vector DB feature. It is a full operating architecture: source-of-truth Markdown, compiled truth, timelines, entity propagation, skillification, evaluation, and cron-driven maintenance.

## Self-OS implications
- GBrain should be evaluated as a possible backend or companion for Self-OS knowledge retrieval, especially around hybrid search, entity pages, and skillpacks.
- The “How to Start” section maps cleanly onto Self-OS:
  1. Pick a thin harness: Hermes Agent is already the default.
  2. Start a brain with GBrain.
  3. Do one real workflow, not abstract architecture planning.
  4. Use Skillify to extract the repeated pattern.
  5. Run resolver checks and evaluation so the skill compounds safely.
- This should connect to existing notes on harness engineering, SkillOS, GoalBuddy, the 12-rule CLAUDE.md contract, and auto-improving software loops.

## Links
- X article: https://x.com/garrytan/status/2053127519872614419?s=20
- GBrain repo mentioned in the article: https://github.com/garrytan/gbrain
- Agent install instructions mentioned by GBrain README: https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
- AGENTS.md fallback: https://raw.githubusercontent.com/garrytan/gbrain/master/AGENTS.md

## How to Start excerpt
The article's “How to Start” section says:

1. **Pick a harness.** Use OpenClaw, Hermes Agent, or build your own from scratch with Pi. Keep it thin; the harness is just the router. Host on a spare home computer with Tailscale, or use Render/Railway.
2. **Start a brain with GBrain.** Inspired by Karpathy's LLM Wiki, implemented in OpenClaw, and extended into GBrain. The article claims 97.6% recall on LongMemEval, no LLM in the retrieval loop, and 39 installable skills.
3. **Do something interesting.** Do not start by planning the skill architecture. Do a real thing: write a report, research a person, build a model, analyze a portfolio, etc.
4. **Skillify the workflow.** After a successful/manual workflow, run Skillify to extract the pattern into a reusable skill.
5. **Run `check_resolvable`.** Verify the new skill is wired into the resolver.
6. **Keep using and evaluating it.** Use cross-modal eval when outputs are wrong; bake fixes into the skill so every future run improves.

## Raw content notes
The post/article includes examples of:
- Book mirrors that map each chapter of a book to the user's real life/context.
- Meeting prep for Demis Hassabis using accumulated person pages, biography notes, public beliefs, and the user's own prior positions.
- A 100,000-page personal brain with pages for people, companies, meetings, books, articles, and ideas.
- Entity propagation after meetings so every person/company mentioned gets updated.
- Skills such as meeting-ingestion, enrich, media-ingest, and perplexity-research.
- More than 100 daily/background jobs/crons in the author's personal system.
