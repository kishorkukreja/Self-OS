---
status: processed
---
     1|---
     2|source: https://www.youtube.com/watch?v=rFGlJ4oIlhw
     3|date: 2026-04-26
     4|type: video
     5|tags: [claude-code, git-worktrees, parallel-agents, coding-workflow, agent-factory, code-review, self-healing]
     6|---
     7|
     8|# Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship
     9|
    10|**Channel:** Cole Medin  
    11|**Length:** 23:53  
    12|**Repo referenced:** [GitHubIssueTriager](https://github.com/coleam00/GitHubIssueTriager)
    13|
    14|---
    15|
    16|## Core Philosophy
    17|
    18|The goal is **10x output, not 2x**, by moving from single-agent coding to a factory system of parallel agents. This requires rebuilding the workflow around isolation and self-sustainability—not just "vibe coding."
    19|
    20|> *"When you go 10x over 2x... it forces you to think differently. For AI coding, it forces us to think about building a system to make our coding agents more self-sustainable."*
    21|
    22|Key mental models:
    23|- **Issue as Spec:** Every implementation starts with a GitHub issue (or Linear/Jira ticket).
    24|- **PR as Validation Input:** The output of implementation is a pull request, which becomes the input for validation.
    25|- **Factory Mindset:** Plan, implement, and validate in separate sessions with isolated contexts.
    26|
    27|---
    28|
    29|## The 5 Pillars
    30|
    31|### Pillar 1: The Issue Spec
    32|Scope individual units of work as GitHub issues. Create issues in batch (often using an AI agent), then fan out to parallel implementation.
    33|
    34|> *"The power of having the issue or the ticket as the input is we already have the individual pieces of work scoped out."*
    35|
    36|**Workflow:** One agent scopes issues → many agents implement in parallel.
    37|
    38|---
    39|
    40|### Pillars 2 & 3: Git Worktrees + Plan/Build/Implement
    41|Each agent works on its own local copy of the codebase using **Git worktrees** to prevent overwrites.
    42|
    43|**Native Claude Code support:**
    44|```bash
    45|claude --worktree issue-10
    46|# or
    47|claude -w issue-10
    48|```
    49|Claude operates inside `.claude/worktrees/issue-10/`, a full duplicate of the codebase.
    50|
    51|> *"Now when our coding agent works on the feature here, it's not going to be overriding other features that other coding agents are building."*
    52|
    53|**Staging:** Plan → Build → Validate, all isolated per worktree. The only variable changing across sessions is the issue number.
    54|
    55|---
    56|
    57|### Pillar 4: Independent Code Review
    58|**Never validate in the same context window as implementation.** The reviewer must never see the writer's chat.
    59|
    60|**Process:**
    61|1. Run `/clear` to wipe the context window.
    62|2. Run `review PR` (custom command) in a **fresh session**.
    63|
    64|The command:
    65|- Data-mines the PR associated with the current branch
    66|- Analyzes git diffs
    67|- Compares changes to the original issue
    68|- Spins up specialized sub-agents for comprehensive review
    69|
    70|**Adversarial Cross-Agent Review:**
    71|Use the [Codex plugin for Claude Code](https://github.com/openai/codex-plugin-cc) for a second opinion:
    72|```bash
    73|/codex adversarial review
    74|```
    75|> *"It's like asking a kid to grade their own homework... they're going to sweep a lot of things under the rug."*
    76|
    77|---
    78|
    79|### Pillar 5: The Self-Healing Layer
    80|When bugs escape into PRs, fix the **system that allowed the bug**, not just the bug itself.
    81|
    82|**Evolve the AI layer:**
    83|- Global rules (`.claude.md`, skills, commands)
    84|- Planning workflows
    85|- Validation processes
    86|
    87|> *"Compare the pull request to the issue... if the coding agent deviated in any kind of way from planning to implementation, it'll be obvious."*
    88|
    89|After each batch, ask: *"What could we fix in our rules, skills, workflows, etc., so that this doesn't happen again?"*
    90|
    91|---
    92|
    93|## Real-World Engineering Challenges
    94|
    95|For agents to handle **end-to-end validation** (actually starting the app and testing it), three isolation problems must be solved:
    96|
    97|### 1. Database Branching & Isolation
    98|Multiple agents hitting the same database will break each other's worktrees.
    99|
   100|**Solution:** Database branching.
   101|- **[Neon](https://get.neon.com/esWDBKR)** (recommended): Instant serverless Postgres branches per worktree. Each branch carries over all tables/data from production.
   102|- **SQLite alternative:** Spin up a local SQLite DB inside each worktree.
   103|
   104|The setup script (`w.sh` / `w.ps1`) creates both the Git worktree and the Neon database branch automatically.
   105|
   106|> *"Not only do we need a worktree for the codebase, but we need something like a worktree for the database as well."*
   107|
   108|### 2. Port Conflicts
   109|Starting multiple app instances simultaneously causes collisions.
   110|
   111|**Solution:** Assign unique ports based on worktree name.
   112|- Base port: `4000`
   113|- Worktree-derived ports: e.g., `4161`, `4107`
   114|- Agents can run `localhost` validation in parallel without collision.
   115|
   116|### 3. Dependency Duplication
   117|Every worktree is a fresh copy of the codebase.
   118|
   119|**Solution:** The worktree setup script installs `node_modules` (or equivalent) **upfront** before the agent begins implementation, keeping the agent focused and speeding up validation.
   120|
   121|> *"If you want to incorporate these ideas... point your coding agent at the repo and say, 'Hey, take these ideas from Cole.'"*
   122|
   123|---
   124|
   125|## Scaling: Tokens & Bottlenecks
   126|
   127|### Token Blowout Mitigation
   128|Longer end-to-end workflows consume more tokens. Use **model tiering:**
   129|
   130|| Task | Recommended Model |
   131||------|------------------|
   132|| High-reasoning coding | Strongest available (e.g., Claude Sonnet 4, o3) |
   133|| Validation & review | Cheaper, fast model (e.g., Claude Haiku, GPT-4o-mini) |
   134|| Simple scaffolding | Cheapest viable model |
   135|
   136|### The 80/20 Rule for Agents
   137|20% of worktree sessions will consume 80% of tokens. Monitor token usage per worktree and optimize the expensive ones.
   138|
   139|---
   140|
   141|## Key Takeaways
   142|
   143|1. **Git worktrees** are the primitive for parallel agent coding — natively supported by Claude Code.
   144|2. **Issue → PR → Review** is the factory pipeline; each stage runs in isolation.
   145|3. **Never review in the same context window** — use adversarial cross-agent review.
   146|4. **Database branching** (Neon) is essential for real end-to-end validation.
   147|5. **Self-healing** means fixing the system (rules, skills, workflows) when bugs escape, not just the bug.
   148|6. **Model tiering** saves tokens — use cheap models for validation, expensive ones for hard coding tasks.
   149|