---
source: https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex?utm_source=tldrai
date: 2026-05-14
type: resource
tags: [openai, codex, coding-agents, iterative-repair, validation-loops, notebooks, agent-workflows, qa]
status: processed
---

# OpenAI Cookbook — Build iterative repair loops with Codex

## Source metadata

- Source: OpenAI Cookbook
- Title: "Build iterative repair loops with Codex"
- Author: Shreekant Agrawal
- Published: 2026-05-11
- Captured: 2026-05-14
- URL: https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex?utm_source=tldrai

## Core idea

The cookbook demonstrates a closed-loop coding-agent workflow where Codex repeatedly improves an artifact using explicit validation feedback. The example repairs stale OpenAI Cookbook notebooks, but the broader pattern applies to any artifact where the agent output can be checked by trustworthy tests, linters, schemas, or domain-specific validators.

The loop is:

1. **Review:** inspect the current artifact and produce structured findings without editing files.
2. **Repair:** apply focused edits to a copied artifact using the review findings and previous validation feedback.
3. **Validate:** run checks, summarize remaining issues, and feed those issues into the next pass.

The key architectural point is that validation closes the loop: the agent does not merely claim the repair is complete; the repaired artifact must satisfy the checks that matter, and any remaining failures become the next repair input.

## Setup pattern

The example runs Codex CLI in headless mode from Python notebook cells rather than an interactive chat UI.

Requirements noted in the cookbook:

- Install Codex CLI.
- Set `OPENAI_API_KEY`.
- Optionally configure repair model and reasoning effort.
- Ensure the sample artifacts exist locally under `data/docs/`.

The cookbook pins Codex CLI for reproducibility:

```python
!npm install -g @openai/codex@0.130.0
```

Example configuration variables:

```python
MODEL = os.getenv("REPAIR_MODEL", "gpt-5.4-mini")
COOKBOOK_CHAT_MODEL = os.getenv("COOKBOOK_CHAT_MODEL", "gpt-5.5")
REPAIR_REASONING_EFFORT = os.getenv("REPAIR_REASONING_EFFORT", "low")
```

## Sample artifacts

The worked example repairs three intentionally stale notebooks:

```python
NOTEBOOKS = [
    DATA_DIR / "qdrant_embeddings_search_pre_repair.ipynb",
    DATA_DIR / "getting_started_evals_pre_repair.ipynb",
    DATA_DIR / "knowledge_retrieval_pre_repair.ipynb",
]
```

The notebooks are designed to exercise increasing repair depth:

- `qdrant_embeddings_search_pre_repair.ipynb` — one-pass cleanup; modernize the local Qdrant query path and clarify sample fixture framing.
- `getting_started_evals_pre_repair.ipynb` — two-pass cleanup; modernize stale Evals flow, then use validation feedback to remove brittle result-log behavior.
- `knowledge_retrieval_pre_repair.ipynb` — three-pass cleanup; modernize model/API shape, tighten local setup, then restore the full retrieval teaching flow.

## Business rules and issue taxonomy

Before review or repair, Codex receives a shared contract defining what “good” means. The cookbook’s rules focus the loop on:

- current OpenAI API patterns;
- clear setup instructions;
- runnable local examples;
- preservation of original teaching goals;
- removal of stale or brittle instructions.

Examples of modernization rules include:

- `client.chat.completions.create` → `client.responses.create`;
- legacy function-calling schemas → current tools schema;
- `qdrant.search` → `qdrant.query_points`;
- `oaieval` CLI examples → current Evals API workflow.

This is important because the repair loop is only as good as the contract and validators that constrain it. The business rules prevent the agent from making generic “cleanup” edits while losing the teaching purpose of the artifact.

## Operational pattern

The reusable pattern is:

1. Preserve the original artifact.
2. Copy it into a repair workspace.
3. Run a no-edit review pass that emits structured issues.
4. Run a focused edit pass against the copy.
5. Run validators.
6. Feed validator failures and review findings into the next iteration.
7. Stop only when validation passes or a bounded iteration limit is reached.
8. Produce an evidence-backed final report: files changed, issues fixed, validation results, remaining risks.

For production agent workflows, this pattern should be bounded by:

- maximum iteration count;
- strict artifact scope;
- explicit business rules;
- deterministic validation commands;
- a final human-review or PR-review checkpoint for interpreted changes.

## Why it matters

This is a concrete OpenAI reference implementation for “repair loops” rather than single-pass vibe coding. It aligns strongly with real-engineering agent workflows:

- agents need objective feedback, not just instruction-following;
- repair should happen against copies or branches, preserving the original;
- validation output should become structured input to the next agent pass;
- completion should be evidence-based, not confidence-based;
- business rules are part of the executable task contract.

## Self-OS / Hermes implications

This should influence Hermes/Codex workflows for Night Shift and AFK implementation:

- Add an explicit **review → repair → validate → iterate** loop to Codex task contracts where validation exists.
- Prefer bounded loops over open-ended “fix everything” prompts.
- Store repair artifacts under mission/workspace folders when experiments are long-running: original artifact, repaired copy, validation logs, and final report.
- Use this as a pattern for wiki compile, notebook repair, generated code repair, eval repair, and documentation modernization tasks.
- Pair well with existing Self-OS handoff/task-state patterns: each iteration updates the evidence state, while durable memory only records stable lessons.

## Candidate Hermes skill update

This source is operational enough to patch the local `codex` skill with an “iterative repair loop” section: no-edit review, copy/branch repair, validation feedback, bounded iteration, and evidence-backed final report.

## Extraction notes

`web_extract` successfully retrieved a structured summary of the OpenAI Cookbook page. The capture preserves the high-level workflow, setup requirements, examples, business-rule framing, and Self-OS implications rather than copying the full notebook implementation verbatim.
