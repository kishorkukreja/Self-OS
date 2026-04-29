---
status: processed
---
# OpenAI Symphony

**URL:** https://github.com/openai/symphony  
**License:** Apache 2.0  
**Status:** Public, low-key engineering preview  
**Stars:** 17.8k | **Forks:** 1.5k | **Watchers:** 139 | **Commits:** 12 | **Contributors:** 6

**Announcement:** https://openai.com/index/open-source-codex-orchestration-symphony/

## Overview

> **Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents.**

Symphony is an open-source orchestration framework that monitors work sources (e.g., a Linear board), spawns autonomous coding agents to handle tasks, and manages the full implementation lifecycle. Agents provide proof of work—CI status, PR review feedback, complexity analysis, and walkthrough videos—and can land PRs safely when accepted. Engineers manage work at a higher level rather than supervising Codex directly.

## Important Status

> **Warning:** Symphony is a low-key engineering preview for testing in trusted environments.

## Getting Started

### Requirements
Symphony works best in codebases that have adopted [harness engineering](https://openai.com/index/harness-engineering/). It is designed as the next step after harness engineering—moving from managing coding agents to managing work that needs to get done.

### Implementation Options

**Option 1: Build Your Own**
> Implement Symphony according to the following spec: https://github.com/openai/symphony/blob/main/SPEC.md

**Option 2: Experimental Reference Implementation**
An Elixir-based reference implementation is provided. Setup instructions in `elixir/README.md`.

## Key Files & Structure

| Path | Description |
|------|-------------|
| `SPEC.md` | Service specification (normative service contract for porting/implementing Symphony) |
| `elixir/` | Experimental reference implementation (Elixir 95.5%) |
| `.codex/` | Codex-related configuration |
| `.github/` | GitHub Actions workflows |

## Recent Notable Commits

- **fix(elixir): configure Codex app-server model via config** (Apr 27, 2026)
  - Changed default Symphony Codex command to select `gpt-5.5` via `--config model` instead of root `--model` flag. Aligns with Codex app-server behavior.
- **Clarify Symphony service specification (#61)** (Apr 27, 2026)
  - Tightened ambiguous conformance language in `SPEC.md` with normative RFC 2119 terminology (MUST, SHOULD, MAY).
  - Moved extension config ownership to extension sections. Points Codex protocol details at targeted app-server spec.
- **[codex] Pin GitHub Actions workflow references (#57)** (Mar 27, 2026)
  - Pinned all floating external GitHub Actions workflow references to immutable SHAs for supply-chain security.

## Contributors

- @frantic-openai, @codex, @kevinw-openai, @hintz-openai, @mstrautmann-oai, @tiago-oai

## Why It Matters

Symphony represents OpenAI's official take on "always-on agent systems"—turning issue trackers into autonomous implementation pipelines. The Elixir reference implementation is notable (95.5% Elixir), and the spec-first approach means it can be reimplemented in any language. Key paradigm shift: manage *work*, not agents.

## Tags

- codex-orchestration
- openai
- agent-orchestration
- elixir
- harness-engineering
- autonomous-coding
- linear-integration
- proof-of-work
- spec-first
