---
source: https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/new-hire-onboarding
date: 2026-05-15
type: repo
tags: [google-adk, long-running-agents, durable-agent-state, event-driven-agents, human-in-the-loop, multi-agent-orchestration, self-os]
status: processed
---

# GoogleCloudPlatform/generative-ai — ADK New Hire Onboarding

## Summary

This repository directory is a Google Cloud ADK example for a **long-running New Hire Onboarding Coordinator Agent**. It demonstrates how to move beyond stateless chatbot demos toward durable background workflows that can pause for human actions, resume from external events, delegate to sub-agents, and survive delays or infrastructure restarts. The example uses Google Agent Development Kit (ADK), Gemini Flash-Lite, FastAPI, a React demo UI, persistent sessions, and a strict onboarding state machine.

The core design point is that long-running agents should not preserve continuity by replaying raw chat history. Instead, they should maintain an explicit, durable, lightweight workflow state — for example an enum-based state machine — and wake up only when real external events occur.

## Key points

- Demonstrates a **time-agnostic, multi-day agent workflow** for HR onboarding.
- Uses **Google ADK** and a ReAct-style coordinator agent powered by Gemini Flash-Lite.
- Models progress through a strict state machine rather than inferring progress from conversation history.
- Supports human-in-the-loop pause/resume gates: document signature and hardware delivery.
- Includes a FastAPI + React live onboarding cockpit with an HR command center and employee portal.
- The UI intentionally does not fake progress: state advances only after backend ADK resume turns complete.
- Includes tests and evaluation/linting dependencies, making it closer to a production demo than a pure notebook.

## Architecture pattern

### Durable background agent, not chatbot

The README frames the problem as a shift from raw conversation memory to durable workflow memory. Dumping long histories into vector stores or prompts causes:

- prompt-context pollution,
- rising token costs,
- stale intermediate state,
- hallucinated reasoning after idle time,
- and risk of skipping real-world gates.

The alternative is explicit state. The onboarding flow tracks progress through steps such as welcome packet sent, documents signed, IT provisioned, hardware delivered, and completed.

### Event-driven dormancy

The agent is expected to pause at points where the real world is the bottleneck. Instead of polling or blocking threads for days, it waits for webhook-like resume events from user actions such as signing a packet or confirming laptop delivery.

### Multi-agent delegation

The coordinator does not need to own every tool and domain concern. It can delegate specialized sub-workflows, such as IT provisioning, to a more focused sub-agent and then regain control when the sub-agent completes.

## Demo flow

1. Start a fresh onboarding case.
2. Review the unsigned onboarding packet.
3. Sign the packet in the employee portal.
4. Wait for the backend ADK signature resume turn to complete.
5. Review the signed packet.
6. Confirm laptop delivery.
7. Wait for the hardware resume turn to complete.
8. See the hardware receipt and day-one schedule.

## Local run commands

```bash
gcloud auth application-default login
gcloud config set project <your-project-id>
uv sync
uv run uvicorn app.fast_api_app:app --host 127.0.0.1 --port 8000
```

Open:

```text
http://127.0.0.1:8000/live-onboarding/
```

If changing the frontend:

```bash
cd frontend/live-onboarding
npm install
npm run build
```

The React build is written into `app/static/live-onboarding`, which FastAPI serves.

## Notable repository metadata

- Parent repository: `GoogleCloudPlatform/generative-ai`
- Directory: `agents/adk/new-hire-onboarding`
- Stars at capture: about 16.9k on parent repository, according to extraction
- Forks at capture: about 4.2k on parent repository, according to extraction
- Python: `>=3.11,<3.14`
- Main dependency: `google-adk>=1.15.0,<2.0.0`
- Other relevant dependencies: OpenTelemetry Google GenAI instrumentation, Google Cloud Logging, Vertex AI agent engines/evaluation, pytest, ruff, ty, codespell

## Why it matters

This is a concrete reference implementation for **durable agent workflows**: agents as background process coordinators rather than ephemeral chat sessions. It is relevant to Self-OS because many useful personal/operational workflows are naturally long-running: research requests, procurement/supply-chain monitoring, newsletter production, coding-agent handoffs, PR review, and recurring operating briefs.

## Self-OS / Hermes implications

- Treat long-running Hermes jobs as **explicit state machines**, not as giant replayed transcripts.
- For workflows like wiki research, newsletter production, Night Shift coding, and daily operating loops, persist compact state: current phase, blockers, artifacts, review gates, and next event needed.
- Prefer event-driven wakeups where possible: PR opened, artifact written, cron completed, external data changed, human approved, etc.
- Avoid optimistic UI/status updates in dashboards or Telegram summaries; report only state confirmed by backend files, git status, cron state, or verified tool output.
- Model human-in-the-loop gates as first-class states instead of vague “waiting” notes.

## Raw content notes

The README and tutorial emphasize the same architectural thesis:

> Most chatbot tutorials rely on dumping massive conversation history JSON blobs into a vector database to “remember” past turns. However, over multi-day workflows, this unstructured approach introduces severe prompt context pollution, high token costs, and reasoning hallucinations.

The tutorial frames the build as an iterative coding-agent playbook and identifies three axes of change:

1. **From stateless to durable:** serialize agent state to a persistent database so it survives restarts and idle periods.
2. **From active polling to event-driven resumption:** pause dormant workflows and wake them only when external events arrive.
3. **From single-agent monoliths to multi-agent delegation:** delegate specialized sub-workflows to focused sub-agents.

The tutorial’s scaffold prompt asks a coding agent to create an ADK onboarding project with persistent session and memory bank settings from the start. The second prompt asks for a strict enum state machine with stages such as `START`, `WELCOME_SENT`, `DOCUMENTS_SIGNED`, `IT_PROVISIONED`, `HARDWARE_DELIVERED`, and `COMPLETED`.
