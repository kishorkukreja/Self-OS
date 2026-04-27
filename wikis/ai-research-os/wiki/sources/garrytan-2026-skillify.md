---
title: "How to really stop your agents from making the same mistakes"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Garry Tan's Skillify pattern: every agent failure becomes a permanent structural fix with tests, resolver routing, and daily evals via the 10-step Skillify checklist."
tags: [skillify, agent-reliability, testing, skills, openclaw, gbrain]
type: source
status: final
---

# How to really stop your agents from making the same mistakes

**Type:** thread
**Date:** 2026-04-26
**URL:** https://x.com/garrytan/status/2046876981711769720
**Author:** Garry Tan (@garrytan)
**Raw file:** [[../../raw/x-threads/2026-04-26-garrytan-skillify-stop-agents-making-same-mistakes.md]]

**Summary:** Garry Tan argues that most agent "reliability" is vibes-based and decays under complexity. The alternative is **Skillify**: every agent failure becomes a permanent structural fix — a skill with tests that run daily, forever. Tan critiques frameworks like LangChain for providing testing primitives without opinionated workflows. The 10-step Skillify checklist mandates: SKILL.md contract, deterministic code scripts, unit tests, integration tests, LLM evals, resolver trigger, resolver eval, check-resolvable + DRY audit, E2E smoke test, and brain filing rules. Two illustrative failures show deterministic work being done in latent LLM space instead of code space (calendar lookup, timezone math). GBrain is Tan's open-source engine managing brain repos, evals, and quality gates. The core insight: in healthy engineering teams every bug gets a test; AI agents should work the same way.

**Key contributions:**
- Skillify as a verb: prototype → "skillify it" → durable infrastructure with tests and routing
- 10-step checklist from SKILL.md through E2E smoke test to brain filing rules
- GBrain: open-source knowledge engine with `gbrain doctor --fix` and portable SkillPacks
- Deterministic-code principle: what code can do, code should do — not LLM reasoning
- Resolver evals and check-resolvable audits revealing dark skills (15% unreachable in first audit)

**Tags:** skillify, agent-reliability, testing, skills, openclaw, gbrain
