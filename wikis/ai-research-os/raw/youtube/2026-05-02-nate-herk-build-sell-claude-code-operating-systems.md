---
source: https://youtu.be/bCljOfCH8Ms?si=vGjFaJfxuPKG5fi4
date: 2026-05-02
type: video
tags: [ai-operating-system, claude-code, self-os, automation, skills, routines, dashboards, google-workspace, clickup, llm-wiki, personal-os, agentic-workflows]
status: processed
---

# Build & Sell Claude Code Operating Systems (2+ Hour Course)

**Source:** YouTube — Nate Herk | AI Automation  
**URL:** https://youtu.be/bCljOfCH8Ms  
**Length:** 02:33:21  
**Published:** 2026-05-01  
**Views at capture:** 57,042  
**Likes at capture:** 2,141  

> Note: `web_extract` returned a rich structured summary and metadata. A direct transcript fetch via `youtube-transcript-api` failed because YouTube blocked cloud-provider IP requests, so this raw capture preserves the extracted summary and implementation-relevant details rather than a full timestamped transcript.

## Summary

Nate Herk frames a Claude Code-based **AI Operating System** as a persistent working environment that can see business files, communications, priorities, tasks, and data; interact with external tools through APIs, CLIs, MCPs, browser automation, and scripts; run reusable skills and routines; produce dashboards; and eventually act like a 24/7 AI employee or executive assistant.

The core idea is to move away from brittle, app-specific automation and instead build a durable, tool-agnostic operating layer around Claude Code. The OS should survive rapid tool churn by encoding reusable methods, skills, cadences, and source-system integrations rather than depending on one SaaS workflow product. The course emphasizes that adoption has an initial productivity dip while skills and routines are built, followed by compounding returns as the system becomes more capable.

## Course Timestamps

```text
0:00 Intro
3:30 The Three Ms of AI
11:30 The Four Cs of an AIOS
15:00 Mapping Your Tools
20:30 Cloning the Repo & VS Code Setup
29:00 The Onboarding Skill
36:30 Connecting ClickUp
47:30 Audit & Level Up Skills
51:30 Google Workspace CLI
1:06:00 Capabilities & Building Skills
1:25:30 Live Skill Build
1:35:30 Cadence & Cloud Routines
1:56:30 Loop & Reminders
2:05:00 Karpathy's LLM Wiki
2:23:30 Dashboards with Artifacts
2:27:30 Daily Loop & Success Criteria
2:32:00 Final Thoughts
```

## Key Concepts

### AIOS Definition

An AI Operating System is a Claude Code-centered environment that can:

- Read from business files, project-management systems, calendars, docs, email, and spreadsheets.
- Interact with tools using APIs, CLIs, MCPs, browser automation, or scripts.
- Run workflows as named skills rather than ad hoc prompts.
- Schedule recurring routines, reminders, audits, and dashboards.
- Act as a durable coordination layer across tools that may change every few months.

### Three Ms of AI

Nate presents three layers for using AI effectively:

1. **Mindset** — Before doing any manual task, ask how AI could do it or at least do 30% of it.
2. **Method** — Break roles into functions and tasks, then automate reusable chunks.
3. **Machine** — Use Claude Code and connected tools as the operating environment where those methods become executable.

Important quote from the course:

> “The question is never will AI do this for me. The question is to what extent can I leverage AI here?”

### Function Breakdown

Instead of asking whether AI can handle an entire job, decompose work into repeatable functions. Example: YouTube production can be decomposed into ideation, scripting, slides, title/thumbnail packaging, description writing, comment replies, and analytics review. Each function can become a capability, skill, or recurring routine.

### Four Cs of an AIOS

The extracted course summary identifies the AIOS as being organized around four implementation dimensions:

- **Context** — The system can read the user’s files, docs, tasks, priorities, and communications.
- **Capabilities** — The system has reusable skills and integrations for acting on tools and data.
- **Cadence** — The system runs routines on predictable loops: daily planning, hourly checks, weekly audits, reminders.
- **Control / Coordination** — The system centralizes work and decision-making while keeping the human in control.

### Mapping Tools

The OS begins by mapping the user’s existing tools, data sources, and workflows. Relevant source systems include:

- Project management tools such as ClickUp
- Google Workspace: Gmail, Calendar, Drive, Docs, Sheets
- Local files and repository docs
- Dashboards and business metrics
- LLM Wiki / knowledge-base systems
- Reminders and cloud routines

### Skills as Capabilities

The course emphasizes building reusable skills rather than one-off prompts. Skills should encode:

- Trigger phrases / when to use
- Inputs required
- Source systems to inspect
- Steps to execute
- Output format
- Verification / success criteria

This maps closely to Hermes/Self-OS skill architecture: persistent procedural memory, explicit triggers, tool usage, and verifiable outputs.

### Cadence and Cloud Routines

A useful AIOS should not only respond to prompts; it should run recurring routines:

- Morning planning loop
- Daily priority check
- Hourly urgent update check
- Weekly audit and level-up routines
- Reminders and follow-ups
- Dashboard refreshes

### Karpathy-style LLM Wiki

The course points to Karpathy’s LLM Wiki as a way to structure knowledge so the AIOS can retrieve, reason over, and update a durable knowledge base. This is especially relevant to Self-OS because the existing `/data/Self-OS/wikis/*` structure already implements a raw-to-compiled wiki workflow.

### Dashboards with Artifacts

The AIOS should produce dashboards from live or semi-live data sources. Artifacts can summarize priorities, metrics, active work, blockers, and system health. The dashboard becomes the user-facing control surface rather than another static report.

## Why It Matters for Self-OS

This video directly overlaps with the current Self-OS direction. Self-OS already has several pieces of an AI operating system:

- GitHub-backed wikis for durable context (`ai-research-os`, `supply-chain-os`, etc.)
- Hermes skills for reusable workflows
- Cron jobs for recurring research/newsletter routines
- Tool integrations for web, files, GitHub, messaging, and scheduled jobs
- A raw capture → compile → reviewed knowledge pipeline

The next step is to formalize these into an OS architecture with explicit contexts, capabilities, cadences, dashboards, and success criteria.

## Implementation-Relevant Takeaways

- Treat Claude/Hermes as an **operating layer**, not just a chat assistant.
- Start by mapping tools and workflows before adding more automation.
- Convert recurring prompts into skills.
- Convert recurring checks into cron routines.
- Make a dashboard/control surface that shows priorities, pending work, recent captures, cron health, PRs, and next actions.
- Keep the system tool-agnostic: APIs/CLIs/MCPs/scripts are replaceable adapters.
- Expect a temporary productivity dip while the OS is configured.
- Define success criteria for the daily loop: user knows what to focus on, what changed, what needs review, and what the AI already handled.
