---
status: processed
---
     1|---
     2|source: https://github.com/mattpocock/skills
     3|date: 2026-04-26
     4|type: repo
     5|tags: [claude-code, skills, agent-workflow, matt-pocock, planning, tdd, refactoring]
     6|---
     7|
     8|# mattpocock/skills: Agent Skills for Real Engineers
     9|
    10|**Repo:** `github.com/mattpocock/skills` · **Stars:** 22.9k · **Forks:** 1.9k · **License:** MIT  
    11|**Origin:** Straight from Matt Pocock's `.claude` directory.
    12|
    13|> "My agent skills that I use every day to do real engineering - not vibe coding."
    14|
    15|---
    16|
    17|## Installation Pattern
    18|
    19|All skills install via the `skills` CLI:
    20|
    21|```bash
    22|npx skills@latest add mattpocock/skills/<skill-name>
    23|```
    24|
    25|---
    26|
    27|## Skills Catalog
    28|
    29|### Planning & Design
    30|
    31|- **`to-prd`** — Turn conversation context into a PRD and submit it as a GitHub issue.
    32|- **`to-issues`** — Break any plan, spec, or PRD into independently-grabbable GitHub issues using **vertical slices**.
    33|- **`grill-me`** — Get relentlessly interviewed about a plan or design until every branch of the decision tree is resolved.
    34|- **`design-an-interface`** — Generate multiple radically different interface designs for a module using parallel sub-agents.
    35|- **`request-refactor-plan`** — Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue.
    36|
    37|### Development
    38|
    39|- **`tdd`** — Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one **vertical slice** at a time.
    40|- **`triage-issue`** — Investigate a bug by exploring the codebase, identify the root cause, and file a GitHub issue with a TDD-based fix plan.
    41|- **`improve-codebase-architecture`** — Find deepening opportunities, informed by domain language in `CONTEXT.md` and decisions in `docs/adr/`.
    42|- **`migrate-to-shoehorn`** — Migrate test files from `as` type assertions to `@total-typescript/shoehorn`.
    43|- **`scaffold-exercises`** — Create exercise directory structures with sections, problems, solutions, and explainers.
    44|
    45|### Tooling & Setup
    46|
    47|- **`setup-pre-commit`** — Set up Husky pre-commit hooks with lint-staged, Prettier, type checking, and tests.
    48|- **`git-guardrails-claude-code`** — Set up Claude Code hooks to block dangerous git commands before execution.
    49|
    50|### Writing & Knowledge
    51|
    52|- **`write-a-skill`** — Create new skills with proper structure, progressive disclosure, and bundled resources.
    53|- **`edit-article`** — Edit and improve articles by restructuring sections, improving clarity, and tightening prose.
    54|- **`ubiquitous-language`** — Extract a DDD-style ubiquitous language glossary from the current conversation.
    55|- **`obsidian-vault`** — Search, create, and manage notes in an Obsidian vault with wikilinks and index notes.
    56|
    57|### Additional Skills
    58|
    59|- **`caveman`** — Simplified approach alongside domain-model
    60|- **`domain-model`** — Maintains `CONTEXT-FORMAT.md` for defining domain concepts
    61|- **`github-triage`** — Uses `/domain-model` session terminology
    62|- **`qa`** — Breaks reports into issues with blocking relationships for parallelism
    63|- **`zoom-out`** — High-level perspective skill
    64|