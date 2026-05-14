---
title: "Ashpreet Bedi — Auto-Improving Software"
date_created: 2026-05-14
date_modified: 2026-05-14
summary: "Ashpreet Bedi's thread describes an agent-platform architecture designed so coding agents can improve the agents running on the platform. The important design move is colocation: a"
tags: [auto-improving-software, agent-platforms, evals, claude-code]
type: source
status: final
---

# Ashpreet Bedi — Auto-Improving Software

**Type:** thread
**Date:** 2026-05-13
**URL:** https://x.com/ashpreetbedi/status/2053885390717890757?utm_source=tldrai
**Raw file:** [[../raw/x-threads/2026-05-13-ashpreetbedi-auto-improving-agent-platform.md]]

## Summary

Ashpreet Bedi's thread describes an agent-platform architecture designed so coding agents can improve the agents running on the platform. The important design move is colocation: agent code, instructions, live runtime, logs, traces, sessions, and eval cases are all close enough that Claude Code can create probes, run them against a container, inspect the results, edit the agent, and rerun failures. The thread names five lifecycle prompts—create, improve, extend, hill climb, and review—that turn a platform from a deployment target into an agent-operable development loop.

The strongest contribution is the Improve → Hill Climb loop. Rather than treating evals as an external reporting layer, the platform exposes eval execution and trace inspection through APIs and local logs. That lets a coding agent derive tests from the agent spec, identify PASS/FAIL cases, patch behavior, and stop when probes pass or iteration limits are reached. For the wiki, this is a concrete example of [[concepts/auto-improving-software.md]] and [[concepts/agent-platforms.md]] becoming practical through observability, API access, and tight feedback cycles.

## Key contributions
- Defines a practical lifecycle for agents that create, improve, extend, hill-climb, and review other agents.
- Shows why colocated traces, logs, evals, and runtime APIs are prerequisites for auto-improvement.
- Connects Claude Code workflows with platform architecture rather than treating coding agents as external assistants.

**Tags:** auto-improving-software, agent-platforms, evals, claude-code
