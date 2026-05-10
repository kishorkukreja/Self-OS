# Hermes Agent Experiment Workspaces

Created: 2026-05-10

## Purpose

Self-OS uses Hermes for wiki captures, cron jobs, Telegram delivery, Kanban execution, taskOS backlog work, and longer-running agent experiments. This note defines the canonical place for experiment artifacts so future runs do not scatter `mission.md`, logs, reviews, and temporary outputs across wiki raw folders or ad hoc directories.

## Current environment snapshot

Verified on 2026-05-10:

- Active Hermes profile: `default`.
- Hermes config path: `/root/.hermes/config.yaml`.
- Kanban board: default SQLite board at `/root/.hermes/kanban.db`.
- Gateway: system service running and hosting the embedded Kanban dispatcher.
- Cron: existing Self-OS/wiki/newsletter jobs are registered; no new cron job was created for this workspace setup.

Decision: keep using the `default` Hermes profile for now. Add named profiles only when there is real operational pain: different models/tools, separate memory, safety boundaries, or distinct always-on workers.

## Canonical locations

Use this routing table before creating files:

| Need | Location | Notes |
| --- | --- | --- |
| Durable external source capture | `/data/Self-OS/wikis/<wiki>/raw/...` | Articles, repos, videos, threads, newsletters. |
| Self-OS operating policy/runbooks | `/data/Self-OS/docs/` | Compact policies that future agents should read. |
| Early implementation idea | `/data/Self-OS/wikis/coding-projects-os/raw/ideas/` | Lightweight, not execution-ready. |
| Shaped implementation backlog | `/data/taskOS/tasks/<slug>/` | `README.md` + `docs/idea.md`; suitable for PRD/issues later. |
| Execution/audit trail | Hermes Kanban (`~/.hermes/kanban.db`) | Task state, dependencies, handoffs, blockers. |
| Agent experiment workspace | `/data/Self-OS/workspaces/hermes-experiments/<slug>/` | Mission files, run logs, reviews, curated artifacts. |
| Bulky/private temporary outputs | outside Git or an experiment-local ignored folder | Summarize findings back into the experiment workspace. |

Do not put runtime experiment artifacts directly into wiki raw folders. Wiki raw is for source captures and generated operating briefs, not scratch logs.

## Workspace layout

Each experiment should use:

```text
/data/Self-OS/workspaces/hermes-experiments/<slug>/
  README.md
  mission.md
  reward-cycle.md
  artifacts/
    README.md
  runs/
    README.md
  reviews/
    README.md
```

Recommended meaning:

- `README.md` — short orientation, owner/task IDs, current status, and file map.
- `mission.md` — objective, definition of done, constraints, evaluation criteria, and current next step.
- `reward-cycle.md` — checkpoint cadence, reward/eval signals, continue/stop criteria, and recurring review prompt.
- `artifacts/` — curated outputs worth preserving: scripts, eval JSON, screenshots, prompt contracts, result summaries.
- `runs/` — dated run logs and command transcripts. Keep concise; redact secrets.
- `reviews/` — goal-buddy, human, or independent-agent reviews against `mission.md`.

Use the committed `_template/` folder as the starting shape for new experiments.

## When to use taskOS instead

Use `/data/taskOS/tasks/<slug>/` when the item is a backlog work item that should become a spec, PRD, issue set, or implementation plan. The completed goal-loop experiment currently lives there because it started as a taskOS-style implementation experiment:

```text
/data/taskOS/tasks/goal-loop-mission-reward-experiment/
```

For future agent-workflow experiments, prefer the Self-OS experiment workspace unless the output is primarily a backlog item.

## Kanban workflow convention

For Kanban-backed experiments:

1. Create/claim a Kanban card for the execution unit.
2. Put the experiment slug and workspace path in the card body or completion metadata.
3. Keep `mission.md` as the durable task contract.
4. Save run evidence under `runs/` and curated outputs under `artifacts/`.
5. Save independent review under `reviews/`.
6. Complete the Kanban card with `changed_files`, `workspace_path`, `tests_run` or verification commands, and any next card IDs.

Kanban remains the execution/audit trail. The workspace is the file artifact store. The wiki is not the scratchpad.

## Verification commands

Use these checks before handing off a workspace setup:

```bash
cd /data/Self-OS
git status --short
hermes profile list
hermes gateway status
hermes cron list --all
```

When an experiment creates code or scripts, add project-specific checks in that experiment's `README.md` and record results in the Kanban completion metadata.

## Next steps

- Reuse `_template/` for the next `/goal` / goal-buddy / reward-cycle experiment.
- If experiments become frequent and the `default` profile becomes noisy, create a dedicated Hermes profile such as `self-os-lab`; do not do this before there is a concrete reason.
- If a workspace pattern proves reusable across multiple experiments, promote the workflow into a Hermes skill rather than only expanding this note.
