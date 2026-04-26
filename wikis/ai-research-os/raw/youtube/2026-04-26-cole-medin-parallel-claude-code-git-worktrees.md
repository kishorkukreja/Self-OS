---
source: https://www.youtube.com/watch?v=rFGlJ4oIlhw
date: 2026-04-26
type: video
tags: [claude-code, git-worktrees, parallel-agents, coding-workflow, agent-factory, code-review, self-healing]
---

# Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship

**Channel:** Cole Medin  
**Length:** 23:53  
**Repo referenced:** [GitHubIssueTriager](https://github.com/coleam00/GitHubIssueTriager)

---

## Core Philosophy

The goal is **10x output, not 2x**, by moving from single-agent coding to a factory system of parallel agents. This requires rebuilding the workflow around isolation and self-sustainability—not just "vibe coding."

> *"When you go 10x over 2x... it forces you to think differently. For AI coding, it forces us to think about building a system to make our coding agents more self-sustainable."*

Key mental models:
- **Issue as Spec:** Every implementation starts with a GitHub issue (or Linear/Jira ticket).
- **PR as Validation Input:** The output of implementation is a pull request, which becomes the input for validation.
- **Factory Mindset:** Plan, implement, and validate in separate sessions with isolated contexts.

---

## The 5 Pillars

### Pillar 1: The Issue Spec
Scope individual units of work as GitHub issues. Create issues in batch (often using an AI agent), then fan out to parallel implementation.

> *"The power of having the issue or the ticket as the input is we already have the individual pieces of work scoped out."*

**Workflow:** One agent scopes issues → many agents implement in parallel.

---

### Pillars 2 & 3: Git Worktrees + Plan/Build/Implement
Each agent works on its own local copy of the codebase using **Git worktrees** to prevent overwrites.

**Native Claude Code support:**
```bash
claude --worktree issue-10
# or
claude -w issue-10
```
Claude operates inside `.claude/worktrees/issue-10/`, a full duplicate of the codebase.

> *"Now when our coding agent works on the feature here, it's not going to be overriding other features that other coding agents are building."*

**Staging:** Plan → Build → Validate, all isolated per worktree. The only variable changing across sessions is the issue number.

---

### Pillar 4: Independent Code Review
**Never validate in the same context window as implementation.** The reviewer must never see the writer's chat.

**Process:**
1. Run `/clear` to wipe the context window.
2. Run `review PR` (custom command) in a **fresh session**.

The command:
- Data-mines the PR associated with the current branch
- Analyzes git diffs
- Compares changes to the original issue
- Spins up specialized sub-agents for comprehensive review

**Adversarial Cross-Agent Review:**
Use the [Codex plugin for Claude Code](https://github.com/openai/codex-plugin-cc) for a second opinion:
```bash
/codex adversarial review
```
> *"It's like asking a kid to grade their own homework... they're going to sweep a lot of things under the rug."*

---

### Pillar 5: The Self-Healing Layer
When bugs escape into PRs, fix the **system that allowed the bug**, not just the bug itself.

**Evolve the AI layer:**
- Global rules (`.claude.md`, skills, commands)
- Planning workflows
- Validation processes

> *"Compare the pull request to the issue... if the coding agent deviated in any kind of way from planning to implementation, it'll be obvious."*

After each batch, ask: *"What could we fix in our rules, skills, workflows, etc., so that this doesn't happen again?"*

---

## Real-World Engineering Challenges

For agents to handle **end-to-end validation** (actually starting the app and testing it), three isolation problems must be solved:

### 1. Database Branching & Isolation
Multiple agents hitting the same database will break each other's worktrees.

**Solution:** Database branching.
- **[Neon](https://get.neon.com/esWDBKR)** (recommended): Instant serverless Postgres branches per worktree. Each branch carries over all tables/data from production.
- **SQLite alternative:** Spin up a local SQLite DB inside each worktree.

The setup script (`w.sh` / `w.ps1`) creates both the Git worktree and the Neon database branch automatically.

> *"Not only do we need a worktree for the codebase, but we need something like a worktree for the database as well."*

### 2. Port Conflicts
Starting multiple app instances simultaneously causes collisions.

**Solution:** Assign unique ports based on worktree name.
- Base port: `4000`
- Worktree-derived ports: e.g., `4161`, `4107`
- Agents can run `localhost` validation in parallel without collision.

### 3. Dependency Duplication
Every worktree is a fresh copy of the codebase.

**Solution:** The worktree setup script installs `node_modules` (or equivalent) **upfront** before the agent begins implementation, keeping the agent focused and speeding up validation.

> *"If you want to incorporate these ideas... point your coding agent at the repo and say, 'Hey, take these ideas from Cole.'"*

---

## Scaling: Tokens & Bottlenecks

### Token Blowout Mitigation
Longer end-to-end workflows consume more tokens. Use **model tiering:**

| Task | Recommended Model |
|------|------------------|
| High-reasoning coding | Strongest available (e.g., Claude Sonnet 4, o3) |
| Validation & review | Cheaper, fast model (e.g., Claude Haiku, GPT-4o-mini) |
| Simple scaffolding | Cheapest viable model |

### The 80/20 Rule for Agents
20% of worktree sessions will consume 80% of tokens. Monitor token usage per worktree and optimize the expensive ones.

---

## Key Takeaways

1. **Git worktrees** are the primitive for parallel agent coding — natively supported by Claude Code.
2. **Issue → PR → Review** is the factory pipeline; each stage runs in isolation.
3. **Never review in the same context window** — use adversarial cross-agent review.
4. **Database branching** (Neon) is essential for real end-to-end validation.
5. **Self-healing** means fixing the system (rules, skills, workflows) when bugs escape, not just the bug.
6. **Model tiering** saves tokens — use cheap models for validation, expensive ones for hard coding tasks.
