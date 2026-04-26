---
source: https://github.com/mattpocock/skills
date: 2026-04-26
type: repo
tags: [claude-code, skills, agent-workflow, matt-pocock, planning, tdd, refactoring]
---

# mattpocock/skills: Agent Skills for Real Engineers

**Repo:** `github.com/mattpocock/skills` · **Stars:** 22.9k · **Forks:** 1.9k · **License:** MIT  
**Origin:** Straight from Matt Pocock's `.claude` directory.

> "My agent skills that I use every day to do real engineering - not vibe coding."

---

## Installation Pattern

All skills install via the `skills` CLI:

```bash
npx skills@latest add mattpocock/skills/<skill-name>
```

---

## Skills Catalog

### Planning & Design

- **`to-prd`** — Turn conversation context into a PRD and submit it as a GitHub issue.
- **`to-issues`** — Break any plan, spec, or PRD into independently-grabbable GitHub issues using **vertical slices**.
- **`grill-me`** — Get relentlessly interviewed about a plan or design until every branch of the decision tree is resolved.
- **`design-an-interface`** — Generate multiple radically different interface designs for a module using parallel sub-agents.
- **`request-refactor-plan`** — Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue.

### Development

- **`tdd`** — Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one **vertical slice** at a time.
- **`triage-issue`** — Investigate a bug by exploring the codebase, identify the root cause, and file a GitHub issue with a TDD-based fix plan.
- **`improve-codebase-architecture`** — Find deepening opportunities, informed by domain language in `CONTEXT.md` and decisions in `docs/adr/`.
- **`migrate-to-shoehorn`** — Migrate test files from `as` type assertions to `@total-typescript/shoehorn`.
- **`scaffold-exercises`** — Create exercise directory structures with sections, problems, solutions, and explainers.

### Tooling & Setup

- **`setup-pre-commit`** — Set up Husky pre-commit hooks with lint-staged, Prettier, type checking, and tests.
- **`git-guardrails-claude-code`** — Set up Claude Code hooks to block dangerous git commands before execution.

### Writing & Knowledge

- **`write-a-skill`** — Create new skills with proper structure, progressive disclosure, and bundled resources.
- **`edit-article`** — Edit and improve articles by restructuring sections, improving clarity, and tightening prose.
- **`ubiquitous-language`** — Extract a DDD-style ubiquitous language glossary from the current conversation.
- **`obsidian-vault`** — Search, create, and manage notes in an Obsidian vault with wikilinks and index notes.

### Additional Skills

- **`caveman`** — Simplified approach alongside domain-model
- **`domain-model`** — Maintains `CONTEXT-FORMAT.md` for defining domain concepts
- **`github-triage`** — Uses `/domain-model` session terminology
- **`qa`** — Breaks reports into issues with blocking relationships for parallelism
- **`zoom-out`** — High-level perspective skill
