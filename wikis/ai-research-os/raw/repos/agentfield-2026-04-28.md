---
status: processed
---
# AgentField

**URL:** https://github.com/Agent-Field/agentfield  
**License:** Apache 2.0 | **Stars:** 1.5k | **Forks:** 251 | **Contributors:** 32  
**Languages:** Go (50.0%), TypeScript (30.1%), Python (18.9%)  
**Latest Release:** v0.1.71 (Apr 21, 2026); v0.1.72-rc.8 (Apr 28, 2026)

## Overview

AgentField is an open-source control plane that makes AI agents callable by any service—frontends, backends, other agents, cron jobs—just like any other API. You write agent logic in Python, Go, or TypeScript. AgentField turns it into production infrastructure: routing, coordination, memory, async execution, and cryptographic audit trails. Every function becomes a REST endpoint, every agent gets a cryptographic identity, and every decision is traceable.

> "AI has outgrown chatbots and prompt orchestrators. Backend agents need backend infrastructure."

## Core Capabilities

### Build
- **Reasoners & Skills** — `@app.reasoner()` for AI judgment; `@app.skill()` for deterministic code.
- **Structured AI** — `app.ai(schema=MyModel)` returns typed Pydantic/Zod output via LiteLLM (100+ LLMs).
- **Harness** — `app.harness("task", provider="claude-code")` dispatches multi-turn coding tasks to Claude Code, Codex, Gemini CLI, or OpenCode.
- **Cross-Agent Calls** — `app.call("other-agent.func")` routes through the control plane with tracing.
- **Discovery** — `app.discover(tags=["ml*"])` finds agents across the mesh; `tools="discover"` lets LLMs auto-invoke them.
- **Memory** — KV + vector search across four scopes (global, agent, session, run). No Redis required.

### Run
- **Async Execution** — Fire-and-forget with HMAC-SHA256 signed webhooks, SSE streaming, retries. No timeout limits.
- **Human-in-the-Loop** — `app.pause()` suspends execution for approval; crash-safe and durable.
- **Canary Deployments** — Traffic weight routing (5% → 50% → 100%), A/B testing, blue-green deploys.
- **Observability** — Auto workflow DAGs, Prometheus `/metrics`, structured logs, execution timelines.

### Govern
- **Cryptographic Identity** — Auto-generated W3C DID + Ed25519 keys per agent; signature-based auth instead of shared API keys.
- **Verifiable Credentials** — Tamper-proof receipt per execution; offline-verifiable via `af vc verify audit.json`.
- **Policy Enforcement** — Tag-based access policies enforced by infrastructure, not prompts.

## Quick Start

```bash
# Install
curl -fsSL https://agentfield.ai/install.sh | bash

# Python (default)
af init my-agent --defaults
cd my-agent && pip install -r requirements.txt
af server          # Terminal 1 → Dashboard at http://localhost:8080
python main.py     # Terminal 2 → Agent auto-registers
```

### Python Example
```python
from agentfield import Agent, AIConfig
from pydantic import BaseModel

app = Agent(
    node_id="claims-processor",
    version="2.1.0",
    ai_config=AIConfig(model="anthropic/claude-sonnet-4-20250514"),
)

class Decision(BaseModel):
    action: str
    confidence: float
    reasoning: str

@app.reasoner(tags=["insurance", "critical"])
async def evaluate_claim(claim: dict) -> dict:
    decision = await app.ai(
        system="Insurance claims adjuster. Evaluate and decide.",
        user=f"Claim #{claim['id']}: {claim['description']}",
        schema=Decision,
    )
    if decision.confidence < 0.85:
        await app.pause(approval_request_id=f"claim-{claim['id']}", ...)
    await app.call("notifier.send_decision", input={"claim_id": claim["id"], "decision": decision.model_dump()})
    return decision.model_dump()

app.run()
# Exposes: POST /api/v1/execute/claims-processor.evaluate_claim
```

## Architecture

- **Stateless Go Control Plane** — routes calls, tracks execution DAGs, enforces policies.
- **Agent Mesh** — Agents connect from anywhere (laptop, Docker, Kubernetes) and auto-register.
- **Storage** — PostgreSQL for production queue/state; SQLite/BoltDB for local dev.
- **Web UI** — React-based dashboard with real-time DAGs, execution traces, and fleet management.

## Why It Matters

AgentField is one of the most production-ready "agent control planes" available—cryptographic identity, canary deploys, built-in observability, and harness dispatch to Claude Code / Codex. Treats agents as infrastructure, not scripts.

## Tags

- agent-control-plane
- agent-orchestration
- production-ai
- go
- typescript
- python
- harness-engineering
- observability
- governance
- self-hostable
