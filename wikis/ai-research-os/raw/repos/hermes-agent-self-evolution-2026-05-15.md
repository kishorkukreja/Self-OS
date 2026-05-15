---
source: https://github.com/NousResearch/hermes-agent-self-evolution
date: 2026-05-15
type: repo
tags: [hermes-agent, self-evolution, dspy, gepa, skill-optimization, prompt-optimization, agent-evaluation, self-os]
status: processed
---

# NousResearch / hermes-agent-self-evolution — External Evolution Loop for Hermes

## Summary

`NousResearch/hermes-agent-self-evolution` is a standalone optimisation pipeline for improving Hermes Agent artifacts through evolutionary search. It targets skills, tool descriptions, system prompt sections, and eventually tool implementation code using DSPy + GEPA as the primary engine, with Darwinian Evolver planned for code-level evolution.

The repository matters for Self-OS because it formalises a feedback loop that turns real agent traces and evaluation datasets into improved operating procedures. This is directly aligned with keeping high-value Self-OS workflows as living skills rather than static notes.

## Repository metadata

- **Repository:** `NousResearch/hermes-agent-self-evolution`
- **URL:** https://github.com/NousResearch/hermes-agent-self-evolution
- **Description:** Evolutionary self-improvement for Hermes Agent — optimise skills, prompts, and code using DSPy + GEPA
- **Primary language:** Python
- **Default branch:** `main`
- **Stars at capture:** 3,191
- **Forks at capture:** 344
- **License surfaced by GitHub API:** none
- **Created:** 2026-03-09
- **Last pushed:** 2026-03-29
- **Latest release:** none surfaced by GitHub API

## Core architecture

```text
Read current skill/prompt/tool
  -> Generate evaluation dataset
  -> Run GEPA optimiser using execution traces
  -> Produce candidate variants
  -> Evaluate variants against constraints and benchmarks
  -> Select best variant
  -> Create PR / review-gated update against Hermes Agent
```

## What it optimises

- **Phase 1 — Skill files:** `SKILL.md` optimisation using DSPy + GEPA. Implemented.
- **Phase 2 — Tool descriptions:** evolve short tool schema descriptions to improve tool-choice accuracy. Planned.
- **Phase 3 — System prompt sections:** evolve persona, tool-use policy, and formatting guidance offline. Planned.
- **Phase 4 — Tool implementation code:** use Darwinian Evolver for code mutation, guarded by tests. Planned.
- **Phase 5 — Continuous improvement loop:** automated pipeline for ongoing improvement. Planned.

## Key principles

- **No GPU training required:** optimisation happens through API calls over text/code artifacts, not weight updates.
- **GEPA is trace-aware:** it reads execution traces to understand why attempts failed, then proposes targeted mutations.
- **Start with low-risk text artifacts:** skills are the best first target because they are measurable, reviewable, and reversible.
- **Human review remains mandatory:** the repo describes PR-based deployment rather than direct mutation of the live agent.

## Guardrails surfaced

- Full test suite must pass: `pytest tests/ -q`.
- Skills must remain under a size limit around 15KB.
- Tool descriptions should stay compact, around 500 characters.
- Prompt caching must not be broken by mid-conversation changes.
- Evolved artifacts must preserve original semantics.
- Changes should go through review rather than direct commit.

## Self-OS implications

- **Skill quality can become measurable.** Self-OS should preserve enough examples, expected outputs, and failure cases for important workflows so skills can be optimised later.
- **Raw ingests can seed eval datasets.** Notes like this should not only describe tools; they should record candidate metrics and edge cases for future skill evaluation.
- **Use review-gated evolution.** Self-OS can adopt GEPA-style improvement for skills, but evolved skill changes should land as diffs with tests or smoke checks.
- **Do not optimise everything.** Start with repeatable, high-frequency skills where success criteria are observable: newsletter production, wiki ingest, code review, research synthesis, TradingAgents analysis.
- **Keep operational skill specs small.** The 15KB guardrail is a useful constraint for avoiding bloated skills that degrade prompt caching and comprehension.

## Quickstart surfaced

```bash
git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
cd hermes-agent-self-evolution
pip install -e ".[dev]"

export HERMES_AGENT_REPO=~/.hermes/hermes-agent

python -m evolution.skills.evolve_skill \
  --skill github-code-review \
  --iterations 10 \
  --eval-source synthetic

python -m evolution.skills.evolve_skill \
  --skill github-code-review \
  --iterations 10 \
  --eval-source sessiondb
```

## Extraction notes

- `web_extract` captured GitHub repository summary plus raw README.
- GitHub API was used for current metadata.
- Raw `PLAN.md` was also extracted to capture the phased architecture and guardrails.
- No credentials or private data were captured.

## Raw README excerpt

```markdown
# 🧬 Hermes Agent Self-Evolution

Evolutionary self-improvement for Hermes Agent.

Hermes Agent Self-Evolution uses DSPy + GEPA (Genetic-Pareto Prompt Evolution) to automatically evolve and optimize Hermes Agent's skills, tool descriptions, system prompts, and code — producing measurably better versions through reflective evolutionary search.

No GPU training required. Everything operates via API calls — mutating text, evaluating results, and selecting the best variants. ~$2-10 per optimization run.
```
