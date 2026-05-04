# Compound Engineering Methodology for Self-OS

Created: 2026-05-04
Source: https://github.com/EveryInc/compound-engineering-plugin/tree/main/plugins/compound-engineering
Status: captured for Self-OS adoption

## Why this matters

The Every Inc compound-engineering plugin is useful because it frames engineering work as a compounding loop, not a collection of one-off prompts. The strongest pattern to adapt into Self-OS is:

**Strategy → Ideate → Brainstorm → Plan → Review → Work → Verify → Compound → Pulse**

For Self-OS, this should become the default methodology for turning raw ideas, links, screenshots, repos, and user requests into durable tasks, reviewed plans, implementation work, verification artifacts, and compounding knowledge.

## Self-OS adaptation

Self-OS should not blindly copy the plugin. Instead, it should adapt the loop to Kishor's operating model:

- Telegram is the primary control surface.
- Git-backed Markdown is the durable system of record.
- taskOS stores future implementation tasks.
- Self-OS stores operating contracts, methods, daily/weekly reports, and knowledge artifacts.
- GitHub PR UI remains the preferred code review surface.
- Day Shift handles strategy, planning, review, and QA.
- Night Shift handles sandboxed implementation and execution.
- Skills and cron jobs make recurring procedures operator-grade.

## Canonical loop

### 1. Strategy

Define or update the operating strategy before creating scattered tasks.

Outputs:

- `docs/self-os-strategy.md` or equivalent strategy section.
- Active tracks of work.
- Key metrics.
- Non-goals and constraints.

Questions:

- What problem are we solving?
- Who/what is the system serving?
- What is the current operating thesis?
- What should agents not do?

### 2. Ideate

Generate and evaluate possible directions grounded in the strategy.

Outputs:

- Idea shortlist.
- Evaluation criteria.
- Recommended next idea to explore.

Questions:

- Which idea best advances the strategy?
- What is high-leverage versus merely interesting?
- What should be deferred?

### 3. Brainstorm

Turn a promising idea into a concrete requirements direction through focused Q&A.

Outputs:

- Problem framing.
- Requirements draft.
- Scope boundaries.
- Open questions.

Questions:

- What does success look like?
- What is the smallest useful version?
- What constraints must the implementation obey?

### 4. Plan

Break the requirements into a structured implementation or operational plan.

Outputs:

- Plan document.
- Task graph.
- Dependencies.
- Acceptance criteria.
- Suggested agents/profiles.

Questions:

- What should be done first?
- What can run in parallel?
- Which steps require human review?

### 5. Review

Stress-test the plan before execution.

Review lenses:

- Scope guardian.
- Architecture reviewer.
- Security/reliability reviewer.
- Product usefulness reviewer.
- Testability reviewer.
- Simplicity reviewer.

Outputs:

- Must-fix issues.
- Should-fix issues.
- Open questions.
- Ready/not-ready verdict.

### 6. Work

Execute the reviewed plan through the right worker model: Hermes, Codex, Claude Code, Kanban worker, or taskOS/GitHub issue workflow.

Outputs:

- Code/docs/config changes.
- Commits/branches/PRs.
- Implementation notes.

Rules:

- Use branch + PR for interpreted implementation work.
- Keep raw captures direct-to-master when appropriate.
- Do not let unconstrained agents implement vague ideas.

### 7. Verify

Prove the work behaves correctly before declaring completion.

Outputs:

- Test results.
- Smoke checks.
- Screenshots or demo reels where useful.
- Reviewer notes.
- Failure notes if blocked.

Questions:

- What evidence proves this works?
- What was not tested?
- What needs manual review?

### 8. Compound

Capture reusable learning after the work is done.

Outputs:

- Skill update or new skill.
- Memory entry if durable and compact.
- Wiki note if it is research/knowledge.
- taskOS follow-up if more implementation is needed.
- Updated operating contract if the workflow changed.

Questions:

- What did we learn that should make future work easier?
- Does an existing skill need patching?
- Did the system discover a new pattern or pitfall?

### 9. Pulse

Periodically report system health and user outcomes.

Outputs:

- Daily/weekly Self-OS pulse report.
- Cron health.
- PR/task status.
- Wiki capture summary.
- Skill drift/staleness warnings.
- Suggested next actions.

Questions:

- What changed?
- What matters?
- What is stuck?
- What should the user review next?

## Skills to add/adapt

These are the Self-OS skill candidates derived from the compound-engineering plugin and the current Self-OS operating model.

### Core methodology skills

1. `self-os-strategy`
   - Adapted from `ce-strategy`.
   - Maintains Self-OS strategy, tracks, metrics, constraints, and non-goals.

2. `self-os-ideate`
   - Adapted from `ce-ideate`.
   - Generates and evaluates grounded ideas before deeper brainstorming.

3. `self-os-brainstorm-to-prd`
   - Adapted from `ce-brainstorm`.
   - Converts vague ideas into requirements/PRD-ready docs.

4. `self-os-plan`
   - Adapted from `ce-plan`.
   - Produces task graphs, dependencies, acceptance criteria, and implementation plans.

5. `self-os-plan-review`
   - Adapted from `ce-doc-review` and `ce-code-review`.
   - Runs multi-lens review before work begins.

6. `self-os-work`
   - Adapted from `ce-work`.
   - Executes reviewed work via the right agent/tooling path.

7. `self-os-verify`
   - Adapted from verification patterns across `ce-work`, `ce-demo-reel`, `ce-test-browser`, and `ce-code-review`.
   - Collects proof that work is done.

8. `self-os-compound-learning`
   - Adapted from `ce-compound`.
   - Turns solved problems into skills, memories, wiki notes, or taskOS follow-ups.

9. `self-os-product-pulse`
   - Adapted from `ce-product-pulse`.
   - Creates Self-OS operating pulse reports.

### Supporting skills

10. `self-os-session-research`
    - Adapted from `ce-sessions`, `ce-session-inventory`, and `ce-session-extract`.
    - Finds decisions, attempts, and unresolved context across prior agent sessions.

11. `self-os-pr-feedback-resolver`
    - Adapted from `ce-resolve-pr-feedback`.
    - Resolves PR review comments systematically.

12. `self-os-demo-reel`
    - Adapted from `ce-demo-reel`.
    - Creates visual proof for UI/CLI/product changes, storing media outside Self-OS unless explicitly requested.

13. `self-os-optimize-loop`
    - Adapted from `ce-optimize`.
    - Runs metric-driven prompt/workflow/system optimization loops.

14. `agent-native-architecture-review`
    - Adapted from `ce-agent-native-architecture` and `ce-agent-native-audit`.
    - Reviews whether Self-OS and related systems are truly agent-native.

15. `self-os-simplify-code`
    - Adapted from `ce-simplify-code`.
    - Simplifies recently changed code while preserving behavior.

## Default routing rule

Any substantial new Self-OS task should move through the methodology unless it is a trivial raw capture:

1. If the request is vague: start at Strategy/Ideate/Brainstorm.
2. If the request is already scoped: start at Plan.
3. If a plan exists: Review before Work.
4. If work is done: Verify before reporting done.
5. If a reusable lesson appears: Compound.
6. Periodically: Pulse.

## Relationship to taskOS

For taskOS, this methodology means task folders should not be only one-line TODOs. A captured task should preserve enough context that later agents can convert it into:

- `docs/spec.md`
- `docs/prd.md`
- `docs/issues.md`
- `docs/implementation-plan.md`

The taskOS task captured from this document should explicitly ask future implementers to create tasks using the methodology:

**strategy → ideate → brainstorm → plan → review → work → verify → compound → pulse**

## Initial implementation recommendation

First build the skills in this order:

1. `self-os-strategy`
2. `self-os-brainstorm-to-prd`
3. `self-os-plan`
4. `self-os-plan-review`
5. `self-os-product-pulse`
6. `self-os-compound-learning`

Then add:

7. `self-os-session-research`
8. `self-os-verify`
9. `self-os-work`
10. `self-os-ideate`
11. `self-os-pr-feedback-resolver`
12. `self-os-demo-reel`
13. `self-os-optimize-loop`
14. `agent-native-architecture-review`
15. `self-os-simplify-code`

## Source repo notes

The source plugin includes skills such as:

- `ce-strategy`
- `ce-ideate`
- `ce-brainstorm`
- `ce-plan`
- `ce-code-review`
- `ce-work`
- `ce-debug`
- `ce-compound`
- `ce-compound-refresh`
- `ce-optimize`
- `ce-product-pulse`
- `ce-sessions`
- `ce-doc-review`
- `ce-demo-reel`
- `ce-resolve-pr-feedback`
- `ce-agent-native-architecture`
- `ce-agent-native-audit`
- `ce-simplify-code`

The adaptation target is not a generic engineering plugin; it is a Self-OS operating methodology that keeps tasks constrained, reviewable, verifiable, and compounding.
