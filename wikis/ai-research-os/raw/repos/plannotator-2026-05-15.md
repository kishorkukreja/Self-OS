---
source: https://github.com/backnotprop/plannotator
date: 2026-05-15
type: repo
tags: [plannotator, coding-agents, plan-review, code-review, agent-feedback, claude-code, codex, opencode, self-os]
status: processed
---

# backnotprop / plannotator — Visual Plan and Code Review for Coding Agents

## Summary

Plannotator is an interactive visual review layer for AI coding agents. It lets users annotate agent plans, specs, code diffs, files, folders, URLs, and the agent's last response in a browser UI, then send structured feedback back to the agent.

It is highly relevant to Self-OS because it adds a missing human-in-the-loop control surface: fast visual review before an agent moves from plan to implementation, and structured feedback after a diff is produced. This fits the Self-OS preference for durable markdown/Git artifacts plus lightweight review gates rather than opaque autonomous execution.

## Repository metadata

- **Repository:** `backnotprop/plannotator`
- **URL:** https://github.com/backnotprop/plannotator
- **Website:** https://plannotator.ai/
- **Description:** Annotate and review coding agent plans and code diffs visually, share with your team, send feedback to agents with one click.
- **Primary language:** TypeScript
- **Default branch:** `main`
- **Stars at capture:** 5,314
- **Forks at capture:** 369
- **License:** Apache-2.0
- **Created:** 2025-12-28
- **Last pushed:** 2026-05-14
- **Latest release:** `v0.19.16` on 2026-05-13

## Main capabilities

- **Visual plan review:** approve, deny, or annotate implementation plans before coding starts.
- **Plan diff:** see what changed when an agent revises a plan.
- **Code review:** review local diffs or remote PRs; comment on specific code lines.
- **General annotation:** annotate markdown, HTML, URLs, folders, files, specs, and agent responses.
- **Agent feedback loop:** package annotations and send them back to Claude Code, Copilot CLI, Gemini CLI, OpenCode, Pi, or Codex.

## Commands / integration surface

- `/plannotator-review` — view git diffs or remote PRs and package annotations.
- `/plannotator-annotate <file|folder|url>` — annotate arbitrary content.
- `/plannotator-last` — annotate the agent's most recent response.
- Plan-mode hooks can open the UI automatically when an agent exits planning.

## Privacy and collaboration model

- Small shared plans are encoded entirely in the URL hash: no server, no account, and no server-side storage.
- Large shared plans can use an optional paste service.
- Large plans are encrypted in the browser before upload using AES-256-GCM.
- The service stores ciphertext only; the decryption key stays in the URL fragment.
- Hosted pastes auto-delete after 7 days.
- The share/paste system is open source and self-hostable.
- Sharing can be disabled with `PLANNOTATOR_SHARE=disabled`.

## Installation surfaced

```bash
# macOS / Linux / WSL
curl -fsSL https://plannotator.ai/install.sh | bash

# Pin a version
curl -fsSL https://plannotator.ai/install.sh | bash -s -- --version vX.Y.Z
```

Claude Code plugin:

```text
/plugin marketplace add backnotprop/plannotator
/plugin install plannotator@plannotator
```

OpenCode plugin:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["@plannotator/opencode@latest"]
}
```

Codex support uses experimental Stop hooks. The installer can enable hooks automatically when Codex is present; manual setup requires enabling hooks in `~/.codex/config.toml` or `<repo>/.codex/config.toml`, then adding a `hooks.json` that calls `plannotator`.

## Self-OS implications

- **Useful review gate before autonomous implementation:** Plannotator could become the visual layer for approving agent plans generated from Self-OS tasks before workers edit code.
- **Complements markdown planning:** It does not replace markdown plans; it provides a UI for reviewing and annotating them, then feeding structured feedback back to agents.
- **Good match for team/peer review:** Shareable encrypted annotations could let the user or collaborators review a plan asynchronously without granting shell access.
- **Potential Self-OS pattern:** task idea -> agent writes plan -> Plannotator review -> approved plan becomes task artifact -> implementation agent proceeds.
- **Security posture is aligned:** URL-hash storage for small plans and client-side encryption for large plans are reasonable defaults for sensitive planning data, but self-hosting should be considered for private operating loops.
- **Risk:** Any automatic hook that lets an agent proceed after approval must be configured carefully so approval scope is explicit and review feedback is captured in Git/markdown.

## Creative bake-offs

- **Plannotator vs Hermes War Room:** War Room is a mission/agent observability cockpit; Plannotator is a focused review/annotation gate. Self-OS likely needs both shapes but for different moments.
- **Plannotator vs plain PR review:** PR review happens after implementation; Plannotator also reviews the plan before implementation, which can prevent costly wrong turns.
- **Plannotator vs chat feedback:** Visual inline annotations are more precise than a chat paragraph when the artifact is a plan or diff.

## Extraction notes

- `web_extract` captured the GitHub repository summary and raw README.
- Additional docs were extracted from installation and sharing/collaboration pages.
- GitHub API was used for current metadata.
- No credentials or private data were captured.

## Raw README excerpt

```markdown
# Plannotator

Interactive Plan & Code Review for AI Coding Agents. Mark up and refine your plans or code diffs using a visual UI, share for team collaboration, and seamlessly integrate with Claude Code, Copilot CLI, Gemini CLI, OpenCode, Pi, and Codex.
```
