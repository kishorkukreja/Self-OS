---
source: https://x.com/GoogleCloudTech/status/2047567704807346675
date: 2026-05-02
type: thread
tags: [agent-harness, warp, agent-architecture, orchestration, multi-agent-systems, a2a, mcp, google-cloud, gemini-enterprise, agent-interoperability]
---

# Harness vs Warp (Agent Architecture Overview)

> Capture note: the user supplied the neutral Harness vs Warp summary below and attached the X URL as context/source. Browser extraction of the linked X post surfaced a Google Cloud Tech article about A2A + MCP integration patterns; both are preserved here because they are adjacent concepts in agent architecture and orchestration.

## User-Supplied Wiki Summary

### Key Concepts

#### Agent harness (e.g. Cursor SDK)

A **harness** is the control layer around an agent:

- manages the agent loop
- handles tool execution
- controls context and memory
- enables subagents and delegation

It turns a model into a fully functioning, programmable agent.

---

#### Warp (agentic environment + orchestrator)

**Warp** is a terminal-based environment with built-in agents and orchestration:

- runs agents locally or in the cloud (via its backend, “Oz”)
- supports multi-agent workflows
- integrates with codebases and tools
- provides a UI + execution layer

---

### Relationship Between Them

A harness and Warp operate at different layers:

- **Harness:** Defines how an agent works — loop, tools, reasoning.
- **Warp:** Defines how agents are run and coordinated.

---

### What Works in Practice

You can:

- build a custom agent using a harness
- run it independently, locally or as a service
- invoke it from Warp workflows

---

### What Does Not Happen (Currently)

Warp does not:

- act as a neutral host for arbitrary harnesses
- fully adopt external agent runtimes
- expose its internal agent loop for replacement

---

### Correct Mental Model

> Harness builds agents.  
> Warp orchestrates and interacts with agents.

More precisely:

```text
Custom Agent (with harness)
        ↓
Runs independently
        ↓
Warp can call / coordinate it
```

---

### Bottom Line

Harnesses and Warp are complementary, not interchangeable.

- **Harness:** agent construction layer
- **Warp:** agent execution + orchestration environment

## Extracted X / Google Cloud Tech Context

**Post:** Google Cloud Tech, Apr 24 2026  
**Visible engagement at capture:** 17 replies, 91 reposts, 475 likes, 636 bookmarks, 43.6K views

The linked X post is a Google Cloud Tech article titled:

> How A2A and MCP work together: five integration patterns for building multi-agent systems

The article argues that organizations will not build every agent from scratch. Instead, value comes from discovering and coordinating agents built by different teams, languages, and organizations. It frames **A2A** as the protocol for agent-to-agent communication and **MCP** as the protocol for agent-to-tool communication.

### Five Integration Patterns

#### 1. Agent Card Discovery

Before an agent can delegate to another agent, it must know that agent exists, what it can do, and how to communicate with it. A2A uses **Agent Cards**: JSON documents published at well-known URLs describing capabilities, authentication requirements, and rate limits. The article compares Agent Cards to OpenAPI specs, but for agent-to-agent interaction.

Google's Agent Development Kit (ADK) can expose an agent as an A2A server and generate the Agent Card from the agent definition. Remote agents can then be consumed through `RemoteA2aAgent`, which handles authentication, serialization, errors, and streaming.

#### 2. Delegated Specialization

The most common pattern is delegation: a coordinator agent hands off specialized tasks to other agents. The specialists can be built by different teams, in different languages, and deployed independently, as long as they speak A2A.

Example: a customer onboarding coordinator delegates identity verification to a security agent, credit assessment to a risk agent, account provisioning to a platform agent, compliance documentation to legal, and welcome communication to marketing.

The article compares this to the microservices principle: independent deployment, scaling, and evolution, with A2A acting as the service contract for agents.

#### 3. Tool Bridge (Model Context Protocol)

A2A connects agents to agents; **MCP** connects agents to tools and data. The Tool Bridge pattern uses MCP to give agents secure access to APIs, databases, and enterprise systems without custom connectors for each backend.

The article cites ADK's integration ecosystem, MCP Toolbox for Databases, and Apigee API Hub as examples of making tools and APIs available through governed MCP interfaces.

#### 4. Cross-Organization Federation

A2A enables agents from different organizations to collaborate without sharing internal implementation details or assuming a common framework, language, or cloud provider.

Google's example is Agent Gallery in Gemini Enterprise, with validated partner agents from companies such as Adobe, ServiceNow, Workday, and Salesforce. Governance remains separate: each organization enforces its own data-sharing, authorization, and security boundaries.

#### 5. Ambient Event Mesh

The final pattern combines A2A with event-driven architecture. Ambient agents listen to streams or database changes, process events, delegate to specialists, or escalate to humans.

The article describes Batch and Event-Driven Agents in Gemini Enterprise Agent Platform connecting to BigQuery tables and Pub/Sub streams. Adding a new specialist agent requires registering it in Agent Registry and updating routing logic.

### Why It Matters

This X article is useful alongside the Harness vs Warp note because it reinforces a layered mental model for agent systems:

- **Harnesses** define how a single agent works internally.
- **Agent runtimes/environments** such as Warp provide execution and orchestration surfaces.
- **A2A** defines agent-to-agent interoperability.
- **MCP** defines agent-to-tool interoperability.
- **Registries / gateways / observability** provide enterprise-scale governance.

The combined takeaway: modern agent architecture is becoming layered, with separable construction, execution, orchestration, interoperability, and governance planes.

## Links Mentioned in X Article

- A2A + MCP codelab: https://codelabs.developers.google.com/instavibe-adk-multi-agents
- ADK samples: https://github.com/google/adk-samples
- ADK: https://adk.dev
- Gemini Enterprise Agent Platform: https://cloud.google.com/products/gemini-enterprise-agent-platform
