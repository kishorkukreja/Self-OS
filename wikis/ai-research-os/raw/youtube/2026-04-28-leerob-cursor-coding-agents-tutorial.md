---
status: processed
---
# Cursor: Coding Agents Tutorial (2026) — Lee Robinson

**URL:** https://youtu.be/kF2WQgk1LtY  
**Channel:** @leerob (Lee Robinson, Vercel)  
**Published:** April 15, 2026 | **Length:** 31:42

---

## How Coding Agents Work: The Harness

A Cursor coding agent runs inside a **harness** made of three components:
1. **Instructions** — System prompts and behavioral rules
2. **Tools** — File editing, codebase search, terminal commands, etc.
3. **Model** — The frontier LLM you select

> "You don't really need to think about those details. Cursor is going to take care of that for you. What's more important is that you learn how to effectively use these models."

---

## Prompting Strategy

- **Vague prompts** force the agent to guess layouts, components, and styling.
- **Detailed prompts** that reference existing patterns, logs, and specific intent produce dramatically better results.

> "The intent you provide the models through prompting really makes a difference in the quality that you get out."

---

## Context Management

Your conversation with an agent builds up a "working memory" of messages, tool calls, and file reads.

**Best practices:**
- **Start a new conversation** when beginning a new feature.
- **Start a new conversation** if the agent goes off track or starts making mistakes.
- Tag specific files manually when you know exactly what you need; otherwise, modern agents are good at auto-retrieving relevant files via search tools.

---

## Searching & Understanding Your Codebase

Cursor arms agents with layered search tools:

| Method | Purpose |
|--------|---------|
| **Exact Match (Grep)** | Find precise strings, functions, or variables |
| **Instant Grep** | Cursor-optimized recursive search for large codebases |
| **Semantic Search** | Find code by *meaning* even without literal keyword matches |

**How semantic search works:**
> "Cursor transforms your codebase into these searchable vectors using an embedding model... cursor has this understanding of your entire codebase and all the symbols and then maps that back to the natural language that you use."

- **Sub-agents:** The built-in **explore sub-agent** searches in its own isolated context window and returns only its findings. Use this for large/unfamiliar codebases to avoid bloating the main conversation with tokens.
- **Architecture diagrams:** Ask agents to generate **Mermaid diagrams** to visualize data flow and onboard faster.

**Critical warning:**
> "A common mistake I see all the time is when developers ask the agents to change code, but they don't really understand exactly how that code works yet... Your intent really matters here. The coding agent will take your request very literally."

---

## Developing New Features with Plan Mode

**Recommended workflow:**
1. **Enter plan mode** (Shift+Tab) and describe the feature.
2. The agent spawns sub-agents to explore the codebase and returns an **interactive markdown plan**.
3. **Review and edit** the plan; the agent asks clarifying questions.
4. Click **Build** to generate code.

**Iterating:**
- Start the dev server and let the agent read errors directly; paste compiler/linter errors back to the agent for quick fixes.
- Paste **screenshots** of the UI for visual/design feedback.
- Use **voice mode** for rapid tweaks.
- Continue until the output is shippable.

> "This workflow of starting with a plan and then going back and forth with the agent to iterate on the design details is how I build most new things."

---

## Debugging Systematically

### Core Debugging Principles
Apply these whether a human or agent is debugging:
1. **Reproduce** the issue reliably
2. **Minimize** the test case
3. **Isolate** variables (change one thing at a time)
4. Form a **specific hypothesis** on root cause
5. **Instrument** code with logging or a debugger
6. **Write tests** after fixing to prevent regressions

### Handling Bugs by Severity
- **Simple bugs:** Paste the error or stack trace directly. Agents usually fix these immediately.
- **Complex/systematic bugs:** Use **Debug Mode** in Cursor:
  1. Generates hypotheses
  2. Instruments code with targeted logging
  3. Asks you to reproduce the issue
  4. Reads and analyzes the logs
  5. Makes a targeted fix based on collected evidence

### Advanced Debugging Tips
- **Multi-model approach:** Ask several models to fix the same bug and compare their solutions.
- **Gather evidence:** Ask agents to investigate slow queries (`EXPLAIN ANALYZE`), check logs, or analyze traces.
- **Use MCP servers:** Pull in external data (e.g., Sentry MCP for production runtime errors).
- **Understand the fix:** Never merge a fix you don't fully understand. Watch for band-aid solutions (e.g., adding `any` in TypeScript).
> "It's up to you to develop this conviction that you actually have the correct code to fix the issue."

---

## Code Review & Testing

### Review Standards
> "Your standards for what gets merged should be the same whether it was written by an agent or a human."

### Testing
- Running `git diff` is the review — if it passes your bar, approve.
- Agents can also go back and edit PRs after the fact based on review comments.

---

## Why It Matters

This is the definitive 2026 tutorial on using Cursor's agentic features effectively. Key takeaways: detailed prompting > vague prompts, plan mode before building, sub-agents for exploration, systematic debugging (not just pasting errors), and maintaining the same merge bar for agent-written code.

## Tags

- cursor
- coding-agents
- agentic-workflow
- prompting
- plan-mode
- debugging
- code-review
- leerob
- vercel
