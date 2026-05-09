# Self-OS Operating Contract

**Purpose:** Define the operating rules agents should follow when running Self-OS. This is not a dashboard, wiki index, or duplicate tool inventory. It is the lightweight routing/policy contract that turns existing wikis, skills, cron jobs, Git branches, and Telegram delivery into a consistent operating loop.

**Primary control surface:** Telegram summaries and user replies.

**Durable system of record:** Markdown artifacts committed to the Self-OS Git repo.

**Default repo:** `/data/Self-OS` on `master`.

---

## 1. Operating Principles

1. **Do not build a dashboard for v0.** Produce markdown briefs and concise Telegram messages first.
2. **Prefer existing Self-OS primitives.** Use wikis, raw captures, wiki compile/lint, skills, cron jobs, branches, PRs, and commits before introducing new infrastructure.
3. **Raw evidence is committed directly.** Source captures and generated operating briefs are durable raw artifacts and may be committed directly to `master`.
4. **Canonical interpretation goes through review.** Wiki compile, wiki lint fixes, and research fulfillments that alter interpreted/canonical knowledge should use a branch + PR unless the user explicitly asks otherwise.
5. **Skills are operational memory.** If a recurring workflow or hard-won extraction rule matters for future runs, patch or create a Hermes skill rather than only saving passive wiki notes.
6. **Telegram is for decisions.** Briefs should tell Kishor what changed, what needs review, what can be delegated, and what decision would unblock the system.

---

## 2. Source Routing Rules

Use these defaults when the user provides a bare link or says “add this,” “save this,” or similar in Self-OS context.

### AI / agents / models / engineering

- GitHub repo → `wikis/ai-research-os/raw/repos/`
- Article/blog/paper/tool page → `wikis/ai-research-os/raw/articles/` or `wikis/ai-research-os/raw/resources/`
- YouTube/video → `wikis/ai-research-os/raw/youtube/`
- X/Twitter thread/post → `wikis/ai-research-os/raw/x-threads/`
- Newsletter-style digest/source bundle → `wikis/ai-research-os/raw/newsletters/`

### Supply chain / logistics / manufacturing / operations

- Source capture → `wikis/supply-chain-os/raw/...`
- Newsletter research and drafts → existing Supply Chain Signals workflow paths.

### Self-OS / implementation / agent operations

- Official plans → `docs/plans/`
- Operating contracts/reference docs → `docs/`
- Daily/weekly operating briefs → `wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/`
- Project implementation sessions → `wikis/coding-projects-os/raw/projects/...`

### Personal / travel / reminders

- Durable user preference or stable personal fact → Hermes memory.
- Personal knowledge artifact → `wikis/personal-os/raw/...` when it should live in Self-OS.
- Time-bound reminder → Hermes cron job, only after the reminder time is known.

---

## 3. Git and Review Policy

### Direct to `master`

Use direct commit + push for:

- Raw URL/repo/video/thread/resource captures.
- Generated daily/evening/weekly Self-OS operating brief artifacts.
- Small docs that clarify operating policy, when requested by the user.
- Skill-independent passive evidence that does not rewrite canonical wiki pages.

### Branch + PR

Use branch + PR for:

- Wiki compile outputs.
- Wiki lint auto-fixes and lint reports.
- Research fulfillment that turns a pending request into interpreted pages/synthesis.
- Any change that rewrites canonical wiki concepts/entities/source pages.
- Any broad refactor or uncertain policy change.

### Push conflict policy

If push is rejected because remote moved:

1. Pull with `git pull origin master --no-rebase` unless a branch workflow is active.
2. Resolve conflicts if any.
3. Push again.
4. Verify with `git status --short` and `git log --oneline -3`.

---

## 4. Extraction and Failure Policy

### Default extraction

- Use `web_extract` first for normal public URLs.
- Use browser/body text fallback for dynamic pages or X/Twitter.
- Use GitHub API/raw README for GitHub repos when useful.

### Known fallbacks

- X/Twitter weak or incomplete extraction → use browser navigation and `document.body.innerText`.
- YouTube transcript blocked by cloud-IP restrictions → stop retrying, use `web_extract` structured summary, and explicitly note transcript limitation.
- Public document URL → use current URL extraction first; use Firecrawl `/scrape` only if primary extraction is weak.
- Local/private PDF/DOCX/XLSX/HTML document bytes → Firecrawl `/parse` is appropriate if available.

### Secrets policy

Never persist or print API keys, tokens, passwords, bot tokens, database URLs, or connection strings. Replace any discovered value with `[REDACTED]`.

---

## 5. Skill-Patching and Promotion Rules

Patch or create skills when operational behavior should improve future runs.

### Patch an existing skill when

- A source changes how an existing workflow should operate.
- A fallback rule prevents repeated failure.
- A repo/resource becomes directly usable in an existing workflow.
- The user corrects a workflow or preference.

Examples:

- Firecrawl `/parse` belongs in `knowledge-base-operations` extraction fallback rules.
- Refero Styles belongs in `design-md` as a design reference, not as a separate passive wiki-only item.
- Codex `/goal` belongs in the `codex` skill with cost/token cautions.

### Create a new skill when

- A workflow repeats or is expected to recur.
- It requires 5+ steps or multiple tools.
- It has non-obvious pitfalls.
- It should be schedulable via cron.

### Do not create a skill when

- The item is merely passive reference material.
- It duplicates an existing skill.
- The workflow has not yet proven useful manually.

---

## 6. Daily Brief Contract

A daily brief should be generated from current system state and saved as markdown before or alongside Telegram delivery.

### Required durable output path

```text
wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/daily/YYYY-MM-DD-{morning|evening|manual}.md
```

### Required sections

1. **TL;DR** — one-line system status and the top things needing attention.
2. **Changed Since Last Brief** — recent commits, raw captures, generated outputs, merged PRs.
3. **Needs Kishor Review** — PRs, decisions, ambiguous workflow changes, stuck items.
4. **Safe Agent Actions** — things agents can do without additional judgment.
5. **Decisions Needed** — explicit decision prompts.
6. **Health / Failures** — failed cron jobs, git divergence, extraction failures, missing config.
7. **Thinking Loop** — connections between recent captures and older notes, the strongest pattern, and one non-task question.
8. **Next Suggested Prompt** — one copy-pasteable prompt for the user.

### Feedback-loop routing

Each daily brief should push at least one insight toward an explicit route:

- Passive knowledge → wiki synthesis or wait for wiki compile.
- Operational workflow → patch/create a Hermes skill.
- Implementation idea → Kanban/taskOS task.
- Needs decision → concise Telegram question for Kishor.
- Needs code/repo work → branch/PR workflow unless it is a raw/generated operating artifact.

### Telegram version

Telegram should be shorter than the markdown artifact. It should emphasize:

- what changed,
- what needs review,
- the top recommended next action,
- any failure needing attention.

---

## 7. Weekly Review Contract

A weekly review should summarize operating-loop quality, not just content volume. It must also be saved as a markdown artifact before or alongside Telegram delivery.

### Required durable output path

```text
wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/weekly/YYYY-Www-review.md
```

Required sections:

- Major changes this week.
- Repeated captures/themes.
- Open PRs and stale branches.
- Cron reliability.
- Skills patched or needing patches.
- Workflows that should be automated next.
- Decisions Kishor should make.
- Proposed next week operating priorities.

The weekly Telegram version should be short: the emerging thesis, activity counts, cron reliability, the top health issue, and the one recommended action.

---

## 8. Human Review Triggers

Escalate to Kishor instead of acting autonomously when:

- A change would alter canonical wiki interpretation or delete existing knowledge.
- A new cron job would send recurring messages to Telegram.
- A workflow needs external credentials or exposes possible secrets.
- There are multiple plausible target wikis and the wrong choice would matter.
- A PR should be merged or closed.
- A source contains legal, financial, medical, or personally sensitive implications.

---

## 9. First Implementation Scope

The first implementation should stay intentionally narrow:

1. Generate a manual daily brief from Git, recent raw files, PRs if available, and known cron status.
2. Save it under `coding-projects-os/raw/projects/self-os-operating-loop/ops/daily/`.
3. Commit/push the contract, script, and first brief.
4. Do not schedule cron until the manual brief format proves useful.
5. Do not create a dashboard.

---

## 10. Maintenance Rule

If this contract conflicts with a more specific wiki `CLAUDE.md` or Hermes skill, follow the more specific operational instruction for that workflow, then update this contract if the conflict reveals a durable Self-OS rule.
