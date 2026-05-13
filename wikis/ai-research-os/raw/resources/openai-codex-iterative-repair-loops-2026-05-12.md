---
source: https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex
date: 2026-05-12
type: resource
tags: [openai, codex, iterative-repair, validation-loops, agent-workflows, notebooks, qa, self-os]
status: processed
---

# OpenAI Cookbook — Build iterative repair loops with Codex

## Summary

This OpenAI Cookbook example demonstrates closed-loop Codex workflows where an agent reviews an artifact, repairs it, validates the result, and feeds failures into the next pass. The example repairs stale API/SDK notebooks, but the pattern applies to any agent output with trustworthy feedback.

## Core loop

The workflow has three phases:

1. **Review** — inspect the artifact and return structured findings without editing.
2. **Repair** — apply focused edits to a copied artifact using findings and validation feedback.
3. **Validate** — run relevant checks, report remaining issues, and feed failures into the next repair pass.

Key principle: validation closes the loop. The repaired artifact must satisfy checks that matter; remaining issues become the next repair input.

## Setup notes

- Uses Codex CLI in headless mode so repair steps can run from Python.
- Installs a pinned CLI version: `npm install -g @openai/codex@0.130.0`.
- Requires `OPENAI_API_KEY`.
- Optional environment variables include:
  - `REPAIR_MODEL`, defaulting to `gpt-5.4-mini` in the example.
  - `COOKBOOK_CHAT_MODEL`, defaulting to `gpt-5.5`.
  - `REPAIR_REASONING_EFFORT`, defaulting to `low`.
  - `CODEX_REPAIR_RUNS_DIR` to control output directory.

## Example artifacts

The notebook repairs three intentionally stale notebooks:

- Qdrant embeddings/search notebook — expected to pass in iteration 1.
- Getting started with evals notebook — expected to pass in iteration 2.
- Knowledge retrieval notebook — expected to pass in iteration 3.

## Quality contract

The cookbook defines business rules before asking Codex to review or repair, including:

- Prefer current APIs and models.
- Modernize stale API patterns.
- Make fresh-environment setup explicit.
- Keep examples runnable with local data where possible.
- Remove brittle manual placeholders.
- State runtime prerequisites and side effects before execution.
- Preserve the original teaching goal while modernizing implementation.

## Why it matters

This is a reusable agent reliability pattern: do not ask an agent to “fix it” in one shot. Give it a measured loop with a business contract, validation signal, and bounded repair passes.

## Self-OS implications

- Night Shift agents should be launched with explicit review/repair/validate loops, not open-ended implementation prompts.
- taskOS specs should include a `validation contract` section.
- Wiki/source modernization, notebook repair, and code refactors can all use the same loop shape.
- Pairs naturally with Crabbox: run validation in clean remote sandboxes, then feed failures back to Codex/Hermes.

## Related captures

- `wikis/ai-research-os/raw/x-threads/2026-05-12-steipete-codex-crabbox-bug-repair.md`
- `wikis/ai-research-os/raw/resources/crabbox-remote-agent-workspaces-2026-05-12.md`
