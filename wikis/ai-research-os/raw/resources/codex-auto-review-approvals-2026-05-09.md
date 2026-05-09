---
source: conversation
source_detail: "User-provided note about Codex auto-review approvals"
date: 2026-05-09
type: resource
tags: [codex, coding-agents, agent-permissions, auto-review, developer-tooling]
---

# Codex Auto-Review Approvals

## Summary

OpenAI has reportedly made **auto-review** the default approval flow for Codex internally. Instead of pausing a Codex session until a human approves script execution or network access, Codex can delegate each approval request to a separate reviewer agent that evaluates the action against a risk policy. This is meant to remove the frequent approval stalls that made background Codex sessions difficult to run unattended.

The reported impact is a roughly **200x reduction in user prompts**. The TUI still shows each reviewer decision in real time, so operators can audit what was approved or rejected.

## Configuration

Add the following to `~/.codex/config.toml`:

```toml
approvals_reviewer = "auto_review"
```

Then restart Codex.

## Key points

- Problem: Codex sessions can stall every few minutes waiting for permission to run scripts or access the network.
- Fix: enable `approvals_reviewer = "auto_review"` so a separate reviewer agent handles approval decisions.
- Safety model: the reviewer checks the requested action against a risk policy before allowing it.
- Operator visibility: the TUI shows each decision in real time.
- Claimed impact: approximately 200x fewer user approval prompts.

## Why it matters

This is directly relevant to long-running coding-agent workflows and background sessions. It suggests a useful pattern for Hermes/Self-OS agent operations: separate the *executor* from a lightweight *risk reviewer* so autonomy can increase without removing auditability.

## Self-OS / Hermes implications

- For Codex-backed implementation sessions, this setting should be considered when stalls are caused by repeated permission prompts.
- For future Hermes agent orchestration, this is a concrete example of an approval-reviewer subagent pattern: execution agent proposes action, reviewer agent checks risk policy, system logs the decision.
- This may belong in future agent-operation runbooks alongside sandbox, network, and approval-policy defaults.

## Raw note

Codex used to stall every few minutes, waiting for permission to run scripts or access the network. These constant interruptions made background sessions nearly impossible because the agent would sit idle until someone clicked approve.

OpenAI's head of Codex just shared a fix. Auto-review is now the default inside OpenAI and delegates each approval to a separate agent that vets the action against a risk policy before letting it run. The shift reportedly cuts user prompts by roughly 200x. To enable it, add this to your `~/.codex/config.toml`:

```toml
approvals_reviewer = "auto_review"
```

Restart Codex, and the reviewer takes over. The TUI shows each decision in real time, so you can still see what the reviewer approved or rejected.
