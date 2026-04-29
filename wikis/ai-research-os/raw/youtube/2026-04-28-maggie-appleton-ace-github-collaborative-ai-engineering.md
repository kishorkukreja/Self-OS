---
status: processed
---
# Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub

**URL:** https://youtu.be/ClWD8OEYgp8  
**Speaker:** Maggie Appleton, Staff Researcher Engineer (designer background), GitHub Next  
**Context:** AI Engineer Summit  
**Length:** 17:42  
**Prototype:** ACE (Agent Collaboration Environment) — entering technical preview soon

---

## Core Thesis

> *"The hard question is no longer how to build it. It's should we build it."*

Software is a team sport, but today's agentic tools are strictly single-player. Scaling one individual's output without team alignment creates waste, not value. When implementation becomes cheap and fast, **opportunity cost becomes the real cost**—and alignment becomes the primary bottleneck.

---

## The Problem: Solo Agentic Development

### The "One Man, Two Dozen Claudes" Fallacy

Current tools promise that one developer with a fleet of terminal-based agents can replace an entire team. Appleton argues this is flawed:

> *"Believing individual productivity leads to great software is nine women make a baby in one month logic. [...] More individual output doesn't solve problems that require communication and coordination. It makes them worse."*

### How the Process Broke

- **Old workflow:** Planning → Building → Review. Alignment touchpoints (Slack, Zoom, draft PRs, issue comments) happened *alongside* implementation.
- **New workflow:** Implementation time has collapsed. Agents open PRs within minutes of an issue being filed. Most planning touchpoints vanish because "code is so cheap that we don't properly stop to think before we prompt it."
- **Unshared local plans:** Agents generate local plans inside personal CLIs that teammates never see.
- **Result:** All alignment weight shifts to the **pull request**—"after the implementation, when it's too late."

### Consequences of Misalignment

- Duplicate work and hairy merge conflicts (agents touching the same files)
- "Surprise features nobody else agreed to build"
- Giant stacks of context-free PRs to review
- Tossing out finished work after critical post-hoc feedback

### Current Tools Are Obsolete

> *"GitHub, Slack, Jira, Linear, and the like as they currently stand are not designed for the agentic development world. We are funneling masses of agentic outputs into platforms that were built for an outdated way of building software."*

---

## The Solution: ACE (Agent Collaboration Environment)

ACE is a **multiplayer agent environment** from GitHub Next designed to merge planning, context gathering, decision-making, and development into one shared space.

### Architecture: The Session

Each ACE session is three things in one:
1. **Multiplayer chat channel** (Slack-like) with teammates *and* coding agents.
2. **Sandboxed microVM** running in the cloud on its own isolated Git branch.
3. **Shared execution environment** where everyone sees the same terminal, preview, and diff output.

> *"It looks a bit like Slack, GitHub, Copilot, and a bunch of cloud computers had a baby."*

Key behaviors:
- Jump into a teammate's session in one click—no stashing, no pulling branches.
- See the full prompting history that led to the current output.
- Run terminal commands (e.g., `bun install && bun dev`) and share live browser previews.
- Close your laptop; the cloud session stays alive. Teammates (and agents) keep working.

### Truly Multiplayer Agents

Agents can read the entire conversation history as prompt context:

> *"We can talk about things up ahead and just say @Ace, do it. They'll go do it."*

Anyone on the team—not just developers—can prompt the agent. Designers, PMs, and support can participate in real-time feature building without needing a local dev setup.

> *"No one is going to say this doesn't work on my machine."*

### Collaborative Planning

Plans are no longer local, unshareable artifacts. Inside ACE, a plan opens as a **collaborative document** where the team sees each other's cursors, edits together, and validates intent before execution.

Example workflow:
1. Chat about a feature (e.g., adding variable timeframes to the demo app).
2. Ask Ace to write a plan.
3. Teammates suggest changes (e.g., "use a dropdown instead of a segmented control").
4. Update requirements in the shared plan.
5. Return to chat: `@ace do this`—agent runs with approved context.

### Proactive Dashboard & Team Pulse

The ACE dashboard replaces scattered Slack/GitHub/Linear check-ins:

| Section | Function |
|---------|----------|
| **Pick Up** | Resume unfinished sessions/PRs after a weekend with one click. |
| **Recently Completed** | Your recent PRs/issues for quick reference. |
| **Team Pulse** | Summarized activity feed: *"Nate shipped a lobby channel; David fixed access token issues."* |
| **Raw Feed** | Unfiltered recent issues/PRs (optional). |

> *"This dashboard is our first pass at trying to make agents proactive in bringing that social context to you."*

Because agents have access to the conversation history, they can proactively surface relevant team context without manual checking.

---

## Why It Matters

ACE is GitHub Next's answer to the alignment problem in agentic development. The core insight: faster code generation doesn't matter if teams aren't aligned on what to build. The session-based model (chat + cloud VM + shared env + full prompt history) could become the default shape of multiplayer coding. Technical preview coming soon.

## Tags

- ace
- github-next
- multiplayer-coding
- agent-collaboration
- alignment
- team-productivity
- sandboxed-vm
- collaborative-planning
- maggie-appleton
