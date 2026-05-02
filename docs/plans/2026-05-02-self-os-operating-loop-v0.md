# Self-OS Operating Loop v0 Implementation Plan

> **For Hermes:** Use `subagent-driven-development` or careful task-by-task execution to implement this plan. Keep raw captures and ops outputs in Git, send summaries to Telegram, and avoid building a dashboard UI until the operating loop proves useful.

**Goal:** Turn Self-OS from a knowledge-capture and automation system into a recurring operating layer that tells Kishor what changed, what needs review, and what agents should do next.

**Architecture:** Build scheduled Hermes skills that collect system state, write markdown operating briefs back into the Self-OS repo, commit/push those briefs, and send the same concise briefing to Telegram. Do not build a dashboard app for v0; treat Telegram as the control surface and the wiki/repo as the durable system of record.

**Tech Stack:** Hermes skills, Hermes cron jobs, Python scripts, Git/GitHub CLI, Self-OS Git repo, markdown wiki outputs, Telegram delivery.

---

## POV / Product Decision

Do **not** build a dashboard first.

A dashboard adds UI surface area, maintenance, and product-design decisions before we know which signals are actually useful. The better v0 is an **operating brief loop**:

1. Collect system state.
2. Save a durable markdown brief into Self-OS.
3. Commit/push it.
4. Send the concise version to Telegram.
5. Let Kishor respond with decisions or tasks.

The operating layer should feel like a daily/weekly chief-of-staff brief, not a web app.

The durable artifact is the markdown file. Telegram is the human interface. Skills and cron are the automation layer.

## Success Criteria for v0

- A morning daily brief runs automatically and posts to Telegram.
- An evening wrap-up runs automatically and posts to Telegram.
- A weekly strategy review runs automatically and posts to Telegram.
- Every run writes a markdown artifact under Self-OS and commits/pushes it.
- Briefs clearly separate:
  - changed since last run,
  - needs Kishor review,
  - safe autonomous agent actions,
  - decisions needed,
  - notable failures or stale workflows.
- The system starts Self-OS-native: Git, wiki, cron, skills, PRs, raw captures, compile/lint/research/newsletter jobs.
- No Gmail/Calendar/Google Workspace integrations in v0.
- No dashboard app in v0.

## Non-goals for v0

- Build a web dashboard.
- Build a TUI.
- Add Gmail/Calendar/ClickUp/Notion.
- Auto-merge PRs.
- Change wiki compile/lint policy.
- Introduce a database.
- Build a generalized personal assistant.

---

## Proposed Information Architecture

### Plan and operating code

- Plan: `/data/Self-OS/docs/plans/2026-05-02-self-os-operating-loop-v0.md`
- System map: `/data/Self-OS/docs/self-os-map.md`
- Collector script: `/data/Self-OS/scripts/generate_self_os_brief.py`
- Optional helper module: `/data/Self-OS/scripts/self_os_state.py`

### Durable operating outputs

Create a new operational raw area in the Self-OS repo:

```text
/data/Self-OS/wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/
  daily/YYYY-MM-DD-morning.md
  daily/YYYY-MM-DD-evening.md
  weekly/YYYY-Www-review.md
```

Rationale:

- These are engineering/project operating artifacts, not AI research sources.
- `coding-projects-os` already owns project plans, sessions, architecture, and reusable engineering patterns.
- The files should remain raw evidence first. A later compile can turn recurring patterns into `wiki/projects/`, `wiki/patterns/`, and `wiki/decisions/`.

### Skills to create

Install these as Hermes skills, not repo-local docs only:

1. `self-os-daily-brief`
   - Morning/evening operational brief.
   - Collects state, writes markdown, commits/pushes, sends Telegram.

2. `self-os-weekly-review`
   - Weekly strategic review.
   - Summarizes what worked, what failed, PRs/branches needing decisions, stale workflows, skill patches needed, and automations to build next.

3. `self-os-tool-map`
   - Maintains `/data/Self-OS/docs/self-os-map.md`.
   - Audits wikis, cron jobs, skills, delivery surfaces, conventions, and known gaps.

Later, only if needed:

4. `self-os-onboarding`
   - Creates a mini-OS pattern for new domains/projects.

---

## Operating Brief Shape

Every daily brief should use this structure:

```markdown
# Self-OS Morning Brief — YYYY-MM-DD

## TL;DR
- One-line state of the system.
- Top 1–3 things needing attention.

## Changed Since Last Brief
- Raw captures added.
- Compiled wiki pages changed.
- PRs opened/merged/updated.
- Cron jobs completed/failed.
- New research/newsletter outputs.

## Needs Kishor Review
- PRs needing merge/close/review.
- Ambiguous research or content decisions.
- Skill changes that need approval.

## Safe Agent Actions
- Tasks agents can do without more human judgment.
- Example: compile latest raw captures, lint stale links, summarize new captures, draft newsletter section.

## Decisions Needed
- Explicit yes/no or multiple-choice decisions.

## Health / Failures
- Failed cron jobs.
- Divergent git state.
- Stuck branches.
- Missing secrets/config.

## Next Suggested Prompt
A copy-pasteable prompt Kishor can send next.
```

The Telegram version should be a shorter version of the same content, optimized for quick reading.

---

## Data Sources for v0

### Git / repository

Commands:

```bash
cd /data/Self-OS
git status --short
git log --oneline --since='24 hours ago'
git branch -r --list 'origin/wiki-compile/*'
git branch -r --list 'origin/wiki-lint/*'
git branch -r --list 'origin/research/*'
```

### GitHub PRs

Preferred:

```bash
gh pr list --state open --json number,title,headRefName,updatedAt,url,author
```

Fallback:

```bash
curl -s -H "Authorization: token $GITHUB_PAT" \
  https://api.github.com/repos/kishorkukreja/Self-OS/pulls
```

### Recent raw captures

Find files modified in the last 24 hours:

```bash
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timedelta
root = Path('/data/Self-OS/wikis')
cutoff = datetime.now().timestamp() - 24*3600
for p in root.glob('*/raw/**/*.md'):
    if p.stat().st_mtime >= cutoff:
        print(p)
PY
```

### Pending research requests

Search:

```bash
grep -R "status: pending" /data/Self-OS/wikis/*/raw/requests /data/Self-OS/wikis/*/raw/**/requests 2>/dev/null || true
```

Implementation should use Python filesystem traversal rather than shell glob fragility.

### Compile/lint state

Read:

- `wikis/*/wiki/ingest-log.md`
- `wikis/*/wiki/log.md`
- open PRs with `wiki-compile/` and `wiki-lint/` branches
- raw files not mentioned in ingest logs

### Cron state

Use Hermes `cronjob(action='list')` when running interactively or as a Hermes cron. If the future scheduled skill cannot call the cron tool directly, use the Hermes CLI if available:

```bash
hermes cron list
```

The brief should include:

- job name,
- schedule,
- last run status,
- next run,
- failures/staleness.

---

## Implementation Tasks

### Task 1: Create the Self-OS map

**Objective:** Create a canonical inventory of the current Self-OS system.

**Files:**
- Create: `/data/Self-OS/docs/self-os-map.md`

**Content sections:**

```markdown
# Self-OS Map

## Purpose

## Knowledge Stores
- ai-research-os
- supply-chain-os
- coding-projects-os
- personal-os

## Automation Jobs
- wiki compile
- wiki lint
- research poll
- x/blog ingestion
- GitHub trending ingestion
- supply-chain signals
- daily profile news digest

## Interaction Surfaces
- Telegram
- GitHub PRs
- Self-OS repo
- wiki raw/compiled pages

## Capabilities
- URL ingest
- wiki compile
- wiki lint
- research request
- daily/weekly operating briefs
- newsletter generation
- deck generation
- stock analysis
- agent delegation

## Conventions
- raw captures direct to master
- compiled/interpreted outputs via PR
- operational brief outputs direct to master as raw project artifacts

## Known Gaps
```

**Verification:**

```bash
test -f /data/Self-OS/docs/self-os-map.md
```

**Commit:**

```bash
cd /data/Self-OS
git add docs/self-os-map.md
git commit -m "docs: add Self-OS system map"
```

### Task 2: Create the brief generator script skeleton

**Objective:** Create a Python script that can generate a markdown operating brief without sending it yet.

**Files:**
- Create: `/data/Self-OS/scripts/generate_self_os_brief.py`

**CLI shape:**

```bash
python3 scripts/generate_self_os_brief.py --mode morning --write
python3 scripts/generate_self_os_brief.py --mode evening --write
python3 scripts/generate_self_os_brief.py --mode weekly --write
```

**Implementation requirements:**

- Use only Python standard library in v0.
- Run from `/data/Self-OS`.
- Gather git state via `subprocess.run`.
- Gather recent files via `pathlib` and modification timestamps.
- Gather open PRs via `gh pr list` if available; otherwise mark PR collection unavailable.
- Write markdown into:
  - morning/evening: `wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/daily/YYYY-MM-DD-{mode}.md`
  - weekly: `wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/weekly/YYYY-Www-review.md`
- Do not commit inside this script yet.

**Verification:**

```bash
cd /data/Self-OS
python3 scripts/generate_self_os_brief.py --mode morning --write
python3 scripts/generate_self_os_brief.py --mode evening --write
```

Expected: two markdown files are created under the ops folder.

**Commit:**

```bash
git add scripts/generate_self_os_brief.py wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/
git commit -m "feat: generate Self-OS operating briefs"
```

### Task 3: Add commit/push wrapper behavior

**Objective:** Add an optional `--commit` flag that commits generated briefs.

**Files:**
- Modify: `/data/Self-OS/scripts/generate_self_os_brief.py`

**CLI shape:**

```bash
python3 scripts/generate_self_os_brief.py --mode morning --write --commit
```

**Rules:**

- Pull `origin master --no-rebase` before writing if `--commit` is set.
- Only add generated operating brief files and `docs/self-os-map.md` if modified intentionally.
- Commit message:
  - morning: `ops: add Self-OS morning brief YYYY-MM-DD`
  - evening: `ops: add Self-OS evening brief YYYY-MM-DD`
  - weekly: `ops: add Self-OS weekly review YYYY-Www`
- Push to `origin master`.
- If push is rejected, pull with `--no-rebase` once and retry.

**Verification:**

```bash
cd /data/Self-OS
python3 scripts/generate_self_os_brief.py --mode morning --write --commit
```

Expected: generated file committed and pushed to master.

### Task 4: Create the `self-os-daily-brief` Hermes skill

**Objective:** Make the daily brief loop reusable and schedulable.

**Skill name:** `self-os-daily-brief`

**Skill content must include:**

- Trigger conditions.
- Required repo path: `/data/Self-OS`.
- Morning vs evening modes.
- Commands to run the generator.
- How to summarize the markdown for Telegram.
- Failure handling.
- Verification checklist.

**Core instruction:**

```text
Run the Self-OS daily brief generator, commit/push the generated markdown artifact, then send a concise Telegram summary with TL;DR, needs review, safe agent actions, decisions needed, and failures.
```

**Verification:**

- Load the skill with `skill_view(name='self-os-daily-brief')`.
- Run manually once for morning mode.
- Confirm the markdown artifact exists.
- Confirm the Telegram message is sent.

### Task 5: Create the `self-os-weekly-review` Hermes skill

**Objective:** Produce weekly strategic review artifacts.

**Skill name:** `self-os-weekly-review`

**Output sections:**

- What worked this week.
- What failed or got stuck.
- PRs/branches needing review.
- Raw captures not yet compiled.
- Research requests pending/processed.
- Skills created/updated/stale.
- Automations to build next.
- Decisions for Kishor.

**Verification:**

- Run manually once.
- Confirm weekly markdown artifact is written and committed.
- Confirm Telegram summary is sent.

### Task 6: Create the `self-os-tool-map` Hermes skill

**Objective:** Maintain the system inventory.

**Skill name:** `self-os-tool-map`

**Behavior:**

- Inspect repo structure.
- Inspect available Hermes skills.
- Inspect cron jobs.
- Inspect wiki conventions.
- Update `/data/Self-OS/docs/self-os-map.md`.
- Commit/push only if map changed.

**Verification:**

- Run skill manually.
- Confirm map updates are meaningful and non-noisy.

### Task 7: Register cron jobs

**Objective:** Schedule recurring briefs.

**Recommended schedules:**

- Morning brief: `0 8 * * *` UK-local intent.
- Evening wrap-up: `0 21 * * *` UK-local intent.
- Weekly review: `0 10 * * 0` UK-local intent.

Because cron scheduling uses system/UTC interpretation unless explicitly handled, use the same BST/GMT care as existing newsletter jobs. If Hermes cron cannot specify timezone directly, create separate GMT/BST jobs or choose UTC times deliberately.

**Job prompts must be self-contained.** Example morning prompt:

```text
Run the self-os-daily-brief workflow in morning mode for /data/Self-OS. Generate the markdown operating brief, commit and push it to master, then send a concise Telegram summary back to this chat. Do not ask questions. If anything fails, write the failure into the brief and report it.
```

**Verification:**

- List cron jobs after creation.
- Manually run each once.
- Confirm output file and Telegram delivery.

### Task 8: Add first feedback loop

**Objective:** Use outputs to improve the system.

After the first 3 daily runs, review:

- Which sections were useful?
- Which sections were noisy?
- Which missing signals caused follow-up questions?
- Which agent actions were safe enough to automate?
- Which skills need patching?

Then patch `self-os-daily-brief` and the generator.

---

## Telegram Output Format

Use concise Telegram-friendly markdown. No tables.

```markdown
## Self-OS Morning Brief — YYYY-MM-DD

**TL;DR:** ...

**Needs review**
- ...

**Safe agent actions**
- ...

**Decisions needed**
- ...

**Health**
- ...

Saved: `wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/daily/YYYY-MM-DD-morning.md`
Commit: `abc1234`
```

---

## Operating Policy

### Direct-to-master allowed

- Generated operating brief markdown under raw ops folders.
- System map updates.
- Skill docs after explicit approval or when maintaining a skill already in use.

### Branch + PR required

- Compiled/interpreted wiki pages.
- Major changes to wiki schemas.
- New canonical project/entity/concept pages generated from raw evidence.
- Risky automation changes.

### Human judgment required

- Merge/close PR decisions.
- Deleting old branches.
- Changing schedule cadence.
- Adding personal data integrations.
- Auto-triggering coding agents with write access.

---

## First Implementation Sequence

1. Create `/data/Self-OS/docs/self-os-map.md`.
2. Create `/data/Self-OS/scripts/generate_self_os_brief.py` skeleton.
3. Generate first morning/evening brief manually.
4. Create `self-os-daily-brief` skill.
5. Run manually and send Telegram output.
6. Create `self-os-weekly-review` skill.
7. Create `self-os-tool-map` skill.
8. Schedule morning/evening/weekly cron jobs.
9. After three daily runs, revise signal/noise.

---

## Open Decisions

1. **Ops artifact location:** Default recommendation is `wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/`. If this becomes central enough, create a dedicated `self-os-ops` wiki later.
2. **Morning/evening times:** Need final UK-local schedule.
3. **Telegram verbosity:** Start compact, then expand only if useful.
4. **Agent autonomy level:** v0 should recommend actions, not auto-launch coding agents unless explicitly asked.
5. **Cron timezone handling:** Match existing BST/GMT split pattern if necessary.

## Recommendation

Start with skills + markdown briefs + Telegram. Defer dashboards entirely.

The core product is not “a dashboard”; it is **a recurring decision loop**. If the loop becomes valuable, a dashboard can emerge later as a read-only visualization of already-useful brief data.
