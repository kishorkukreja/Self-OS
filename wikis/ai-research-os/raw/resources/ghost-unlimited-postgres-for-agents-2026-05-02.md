---
source: https://ghost.build/developers/
date: 2026-05-02
type: resource
tags: [postgres, database-branching, ai-agents, coding-agents, preview-environments, migrations, evals, ghost]
---

# Ghost — Unlimited Postgres for Agents

## Summary

Ghost is a developer database platform positioned around unlimited Postgres databases and forks for AI agents, coding workflows, and rapid experiments. Its main pitch is that coding agents quickly exceed the project limits of conventional hosted Postgres providers, while Ghost makes it cheap and fast to fork, test, compare, and throw away databases. For agentic engineering workflows, Ghost is promising because it turns databases into disposable scratch space for migrations, PR previews, schema experiments, embedding bakeoffs, and safe agent testing against realistic data.

## Key points

- **Positioning:** “Unlimited Postgres for your agents.”
- **Core idea:** give agents and developers unlimited databases and unlimited forks so experiments do not require rationing scarce database projects.
- **Install command:** `curl -fsSL https://install.ghost.build | sh`
- **Free tier claims on page:** unlimited databases, unlimited forks, 100 hrs/month free, 1 TB storage free.
- **Main workflow:** fork a source database, run experiments or migrations in isolated forks, keep/promote the winner, and drop the rest.
- **Agent relevance:** lets Claude/Codex/other agents touch a real database safely by forking first, then deleting bad branches if the agent does something wrong.
- **Database branching use cases:** schema experiments, per-prompt scratch DBs, migration rollback/debugging, PR preview databases, tests against real or sanitized production-like data.
- **Experiment loop:** setup, run, compare, decide — each fork is isolated but shares a common baseline for comparable results.
- **Example:** embedding bakeoff across `all-minilm`, `bge-base`, and `voyage-3`, each tested on a separate database fork before keeping the winner.

## Why it matters

Ghost fits directly into agentic software development and Self-OS/Sandcastle-style workflows. Coding agents often need realistic persistence layers, but real databases are risky, slow to provision, and expensive to duplicate. Ghost’s fork-heavy model suggests a useful pattern: give each agent, prompt, PR, or eval run its own disposable Postgres branch, then compare results and delete failed attempts.

This could be especially useful for:

- AFK/night-shift implementation agents that need database access.
- Sandboxed coding runs where the app needs Postgres.
- Migration testing before touching staging or production.
- PR environments with real schema/data behavior.
- Eval workflows involving embeddings, retrieval, vector extensions, or realistic application state.
- Multi-agent coding setups where each agent needs an isolated database branch.

## Potential Self-OS integration ideas

- Add Ghost as a candidate database backend for agent sandbox workflows.
- Create a pattern where every coding-agent task gets a named Ghost database fork.
- Use database forks for migration validation in PR review.
- Use database forks for eval bakeoffs against shared baseline datasets.
- Pair with Codex/Claude worktrees: one git worktree plus one Ghost DB fork per agent.
- Store Ghost fork metadata in task logs so failed branches can be cleaned up automatically.

## Raw content

# Your agent needs more than 2 projects.

Most Postgres providers cap you at a handful of projects. Agents blow through that in a single task. Ghost gives your agent unlimited databases. Fork, test, throw away.

```bash
curl -fsSL https://install.ghost.build | sh
```

Unlimited databases · Unlimited forks · 100 hrs/mo free · 1TB storage free

## Ghost is unlimited, but here are six ways to use it.

When setting up a database is a two-minute side quest, you only do it when you have to. When it's free and instant, you start using forks like scratch paper.

### 01 — Let Claude touch your database

Fork main before you let your agent run. If it does something weird, drop the fork. If the migration actually worked, keep it. Your real data stays untouched.

> safe vibe-coding with a real db

### 02 — Try two schemas, keep one

Not sure if you need a separate users table or if you can just add columns? Fork it twice. Build both. Ship the one that feels right. Delete the other.

> decisions without commitment

### 03 — A scratch db for every prompt

Prototyping with an LLM? Spin up a throwaway db for each idea. Load sample data. Try stuff. Close the tab when you're done. No cleanup.

> no commitment

### 04 — Undo a bad migration

Ran a migration that broke prod at 11pm? Fork from an hour ago. Point your app at the fork. Debug in the morning. Your users never notice.

> lower-stakes mistakes

### 05 — A real db for every PR

Your collaborator opens a PR with a schema change. Fork main, apply the migration, check that everything still works. No “can you push to staging” Slack messages.

> preview envs that actually work

### 06 — Test locally against real data

Your tests need realistic data but you're tired of seeding fixtures. Fork from prod or a sanitized copy. Run your tests. Drop the fork. Repeat.

> no more fake data

## Fork, run, decide.

Four phases. Each completes in milliseconds. The loop closes faster than most people's Postgres clients connect.

### 01 · setup — Fork three ways

Start from a source database. Create three independent forks, one per hypothesis.

> +184ms total

### 02 · run — Experiment in parallel

Each fork runs in its own isolated Postgres. Nothing leaks between them.

> minutes, not hours

### 03 · compare — Measure against the same baseline

All three forks share a common ancestor, so results are comparable out of the box.

> on your schedule

### 04 · decide — Keep one. Drop the rest.

Promote the winner. Discard the rest. No cleanup, no manual teardown, no ghosted resources.

> 39ms per drop

## Embedding bakeoff example

Fork the source three ways, run the evals in parallel, keep the winner. Three commands, real CLI grammar, no cleanup step.

```bash
# fork the source database three ways
ghost fork docs-main --name eval-small    # 58ms
ghost fork docs-main --name eval-medium   # 61ms
ghost fork docs-main --name eval-large    # 64ms

# run the eval on each fork in parallel
# eval-small: all-minilm · recall 0.71
# eval-medium: bge-base · recall 0.84
# eval-large: voyage-3 · recall 0.92 ✓

# keep the winner, delete the rest
ghost delete eval-small --confirm   # 39ms
ghost delete eval-medium --confirm  # 41ms
```

## Built with Ghost examples

The page links to projects built on Ghost, including:

- PacmanDB — Pac-Man where every pellet eaten is a row in Postgres; ghosts are forks.
- Ghost City — multiplayer city-builder where every player gets their own database; fork to clone a city.
- March Madness — bracket predictor that forks tournament state on every upset.

## Source extraction note

Extracted with Hermes `web_extract` from the developer landing page. Tracking parameters were removed from the canonical source URL.
