---
source: https://youtu.be/rIs802-bXDY?si=7OdzYUm_fDprjvL4
date: 2026-05-10
type: video
tags: [ai-agents, coding-agents, codex, hermes-agent, goals, goal-buddy, mission-md, long-running-agents, rewards-loop, self-os]
---

# AI Jason — I used /goals command wrong... Here are all tips & mistakes

## Source metadata

- **URL:** https://youtu.be/rIs802-bXDY?si=7OdzYUm_fDprjvL4
- **Video title:** I used /goals command wrong... Here are all tips & mistakes
- **Channel:** AI Jason
- **Uploaded:** 2026-05-09
- **Length:** 12:17
- **Category:** Science & Technology
- **Extraction note:** `youtube-transcript-api` was blocked by YouTube IP restrictions from this environment. This capture uses `web_extract` metadata and summary rather than a full transcript.

## Why this matters

This video is useful for Self-OS and Hermes because it frames `/goal` as a practical mechanism for keeping coding agents moving on large objectives instead of stopping after the first plausible partial answer. The important idea is not simply "run the agent longer." It is to define a standing goal, keep artifacts on disk, judge completion against a definition of done, and resume the next concrete step when the work is incomplete.

That maps directly onto several Self-OS themes:

- longer agent loops for implementation and research work;
- goal-buddy style companion processes that keep the primary agent honest;
- `mission.md` as a durable task contract;
- artifacts as evidence rather than chat-only progress;
- reward/evaluation cycles that can continue across recurring steps.

## Video outline

Timestamps surfaced by extraction:

- **0:00** — What the `/goal` feature is
- **1:44** — How it works
- **4:20** — How to set it up
- **5:35** — How to prompt goals
- **8:45** — Goal-buddy
- **10:00** — `/Mission` exploration and long horizontal tasks

## Core idea

The video describes OpenAI Codex's experimental `/goal` feature and compares it with similar long-running goal persistence in Hermes Agent. The basic problem is familiar: coding agents can do well-scoped tickets, but on larger or ambiguous work they often stop too early, claim success prematurely, or require repeated human nudges.

The proposed pattern is a standing goal loop:

1. The user gives the agent a goal.
2. The agent works toward it.
3. When the agent stops, the system checks whether the goal is actually complete.
4. If the goal is incomplete, the agent receives a continuation prompt.
5. The loop repeats until the goal is complete or the run is stopped.

The useful distinction is between a dumb loop and a judged loop. A rough loop can simply re-run an agent a fixed number of times. A goal loop should assess whether the objective is satisfied, whether proxy signals are misleading, and what concrete next step should happen next.

## Practical takeaways

### 1. Use `/goal` for work that is too large for a single agent turn

Good candidates include:

- fixing a broad set of failing tests;
- migrations and refactors;
- reducing Docker image size or improving performance;
- converting codebases from one language or framework shape to another;
- prompt optimization against an eval set;
- building a prototype from a PRD or plan file;
- debugging tasks where progress can be measured with repeated checks.

The pattern is less useful for small tasks that already have a clear one-shot completion boundary.

### 2. Avoid proxy completion

A goal loop should not accept weak signals such as "tests passed once" or "the agent says done" as proof. The completion check should look for the actual objective:

- Were all required artifacts created?
- Did the relevant tests/evals pass?
- Was the definition of done satisfied?
- Are there remaining TODOs, failing commands, or unverified assumptions?
- Does the final state match the original goal, not just a nearby easier goal?

### 3. Give the agent a concrete mission file

The video's `/Mission` discussion is especially relevant for Self-OS. A long-running task should have a file like `mission.md` that records:

- the objective;
- the definition of done;
- constraints and non-goals;
- required artifacts;
- verification commands;
- reward/evaluation criteria;
- current state and next step.

This gives the loop an external memory substrate. The agent can resume from files instead of relying only on chat history.

### 4. Goal-buddy as an accountability layer

The goal-buddy idea is to pair the working agent with a companion/judge role. The buddy should not do the implementation work. Its job is to check whether the agent is drifting, stopping early, accepting proxy signals, or failing to update artifacts.

A Hermes/Self-OS version could use:

- a primary implementation agent;
- a goal-buddy reviewer/coach;
- `mission.md` as the shared contract;
- an artifacts folder for logs, diffs, eval results, screenshots, and notes;
- recurring checkpoints scheduled after some time.

## Self-OS implications

This should become an experiment rather than just a saved reference. The likely experiment:

1. Pick a small but real task with measurable output.
2. Create a `mission.md` file and `artifacts/` folder.
3. Run a goal-style loop with a primary agent.
4. Add a goal-buddy review step that checks for premature completion.
5. Add a longer reward/evaluation cycle that revisits the mission after some time, inspects artifacts, and decides whether to continue, revise the goal, or close it.

The key test is whether this produces better long-running work than the current pattern of isolated agent runs plus human follow-up.

## Open questions

- What is the smallest Self-OS task that can test this without creating operational noise?
- Should `mission.md` live in `/data/taskOS/tasks/<slug>/`, in a repo worktree, or in a temporary Kanban workspace?
- Should the goal-buddy be a Kanban reviewer task, a standing Hermes goal, or a recurring cron check?
- How should reward criteria be represented: tests, eval score, artifact checklist, human rubric, or a combination?
- How long should the first recurring checkpoint wait before re-entering the loop?

## Links mentioned in video description

- AI Builder Club workshop: https://www.aibuilderclub.com/
- Crewlet early access: http://crewlet.io/
- Superdesign: http://superdesign.dev/
- AI Jason on X: https://twitter.com/jasonzhou1993
