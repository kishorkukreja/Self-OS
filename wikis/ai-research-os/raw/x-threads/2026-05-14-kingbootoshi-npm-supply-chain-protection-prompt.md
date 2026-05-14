---
source: https://x.com/KingBootoshi/status/2054025614798295530
date: 2026-05-14
type: thread
tags: [software-supply-chain, npm, package-security, coding-agents, claude-code, codex, developer-workflows]
---

# BOOTOSHI — NPM supply-chain protection prompt for Codex/Claude Code

## Source metadata

- Author: BOOTOSHI 👑 / `@KingBootoshi`
- Original post date: 2026-05-12 02:27
- Captured: 2026-05-14
- Source URL: https://x.com/KingBootoshi/status/2054025614798295530
- Visible metrics at capture: 44 replies, 139 reposts, ~1.4K likes, ~3.2K bookmarks, ~127.5K views

## Raw post text

> USE THE PROMPT BELOW IN CODEX/CC TO PROTECT YOUR SYSTEM AND CODEBASE FROM NPM SUPPLY CHAIN ATTACKS (LIKE TANSTACK TODAY):
>
> """
> set up npm supply-chain protection on this machine. do all four steps.
>
> 1. edit `~/.npmrc`. keep every existing line (auth tokens etc), append:
>
> ```ini
> min-release-age=7
> minimum-release-age=10080
> save-exact=true
> ```
>
> 2. edit `~/.bunfig.toml` (create if missing). keep existing content, append:
>
> ```toml
> [install]
> minimumReleaseAge = 604800
> ```
>
> 3. in this project, open `package.json` and pin every dependency:
>
> strip `^` and `~` from every version under `dependencies`, `devDependencies`, and `peerDependencies`. exact versions only.
>
> 4. commit the lockfile (`bun.lock` / `package-lock.json` / `pnpm-lock.yaml`) so the resolved tree is locked in git. then report: files changed, deps pinned, anything unexpected.
> """
>
> the cooldown makes every package manager refuse any version published in the last 7 days. attack chains usually only last a couple hours, but this protects you long term and for any future attacks... which at this rate will keep happening

## Why it matters

This is a compact operational pattern for reducing exposure to fast-moving package compromise events in JavaScript/TypeScript projects. The key idea is to make the coding agent apply four defensive defaults before or during dependency work:

1. NPM release-age cooldowns.
2. Bun release-age cooldowns.
3. Exact dependency version pins rather than floating semver ranges.
4. Lockfile commitment so the resolved dependency tree is reviewable and reproducible.

The post is especially relevant to agentic coding workflows because dependency updates, package installs, and boilerplate generation are common areas where agents may introduce unreviewed transitive-risk surface.

## Self-OS / Hermes implications

- Candidate addition to coding-agent safety checklists: before Night Shift or AFK implementation runs touch JS/TS dependencies, ensure release-age gates and lockfile discipline are explicit in the task contract.
- Could become a reusable Hermes/Claude Code skill or checklist step for `software-project-workflows`: verify package-manager config, pin dependency ranges intentionally, and report any unexpected dependency tree changes.
- Treat this as a defensive default, not a universal rule: exact pins and cooldowns improve reproducibility and supply-chain safety but can require process decisions for libraries/apps with existing dependency policies.

## Extraction notes

Browser extraction succeeded on the public X post. The post includes an attached image, but the core operational instructions were present in the visible post text and captured above.
