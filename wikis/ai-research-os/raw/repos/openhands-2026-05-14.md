---
source: https://github.com/OpenHands/OpenHands
date: 2026-05-14
type: repo
tags: [ai-agents, coding-agents, developer-tools, open-source, agent-platforms, self-os]
status: processed
---

# OpenHands / OpenHands — AI-Driven Development

## Summary

OpenHands is a large open-source AI-driven development project that packages coding-agent capabilities across several usage modes: a composable Python Software Agent SDK, a Claude Code/Codex-like CLI, a local GUI with REST API + React frontend, a hosted cloud product, and enterprise self-hosted deployment. The repository frames OpenHands less as a single coding assistant and more as a developer-agent platform spanning local, cloud, and enterprise execution. It is especially relevant to Self-OS as a reference point for how mature agent systems separate SDK/runtime, CLI control surface, GUI/API layer, hosted operations, integrations, and enterprise governance.

## Repository metadata

- **Repository:** `OpenHands/OpenHands`
- **URL:** https://github.com/OpenHands/OpenHands
- **Homepage:** https://openhands.dev
- **Description:** 🙌 OpenHands: AI-Driven Development
- **Primary language:** Python
- **Default branch:** `main`
- **Stars:** 73,543
- **Forks:** 9,290
- **Open issues:** 422
- **Created:** 2024-03-13
- **Last pushed:** 2026-05-14
- **Latest release surfaced by extraction:** `1.7.0` on 2026-05-01
- **License:** README states MIT for core work, except `enterprise/`; GitHub API reports `NOASSERTION`, likely because of mixed licensing / enterprise directory.
- **Topics:** `agent`, `artificial-intelligence`, `chatgpt`, `claude-ai`, `cli`, `developer-tools`, `gpt`, `llm`, `openai`

## Key points

- **Multiple product surfaces:** OpenHands can be used via SDK, CLI, local GUI, cloud, or enterprise self-hosted deployment.
- **SDK as engine:** The Software Agent SDK is described as a composable Python library containing the agentic technology that powers the rest of the platform.
- **CLI parity with modern coding agents:** The CLI is positioned as familiar to Claude Code or Codex users and can be powered by Claude, GPT, or other LLMs.
- **Local GUI:** The local GUI runs on a laptop and includes a REST API plus single-page React application, with a user experience compared to Devin or Jules.
- **Hosted cloud:** OpenHands Cloud includes integrations with Slack, Jira, and Linear, plus multi-user support, RBAC, permissions, and collaboration features.
- **Enterprise deployment:** OpenHands Enterprise supports self-hosting in a company VPC via Kubernetes and is source-available under separate licensing.
- **Adjacent assets:** README links to evaluation infrastructure, a Chrome extension, and a Theory-of-Mind module for SWE.

## Why it matters

OpenHands is useful as a mature reference architecture for agentic software development systems. For Self-OS/Hermes, the interesting pattern is the separation of **agent SDK/runtime**, **CLI interface**, **local GUI/API**, **cloud execution**, **enterprise governance**, and **integrations**. That decomposition maps directly onto the question of how Self-OS should evolve without collapsing everything into a single dashboard or monolithic agent.

## Self-OS implications

- **Hermes should stay control-surface agnostic:** OpenHands’ split between SDK, CLI, GUI, cloud, and enterprise reinforces the Self-OS principle that Telegram, CLI, dashboards, and scheduled skills should be separate surfaces over the same underlying operating loop.
- **SDK/runtime separation matters:** The OpenHands SDK framing is a reminder that durable workflows should live in reusable skills/scripts/runtimes, not only in chat prompts.
- **Agent governance is a first-class layer:** RBAC, permissions, integrations, and enterprise deployment are not just SaaS features; they point to future Self-OS needs around connector control, review gates, identity, and audit trails.
- **Evaluation infrastructure should be treated as part of the platform:** The linked OpenHands benchmarks repo is worth separately reviewing if Self-OS expands its coding-agent QA and Night Shift review loops.
- **Avoid premature GUI gravity:** OpenHands has a GUI, but its architecture still exposes CLI/SDK/API paths. For Self-OS v0, this supports continuing to prioritize Telegram + markdown + skills before building a dashboard.

## Links surfaced

- OpenHands docs: https://docs.openhands.dev
- SDK docs: https://docs.openhands.dev/sdk
- SDK source: https://github.com/OpenHands/software-agent-sdk/
- CLI docs: https://docs.openhands.dev/openhands/usage/run-openhands/cli-mode
- CLI source: https://github.com/OpenHands/OpenHands-CLI
- Local setup docs: https://docs.openhands.dev/openhands/usage/run-openhands/local-setup
- Cloud app: https://app.all-hands.dev/
- Enterprise: https://openhands.dev/enterprise
- Roadmap: https://github.com/orgs/openhands/projects/1
- Benchmarks: https://github.com/OpenHands/benchmarks
- Chrome extension: https://github.com/OpenHands/openhands-chrome-extension/
- Theory-of-Mind module: https://github.com/OpenHands/ToM-SWE
- Tech report linked from README: https://arxiv.org/abs/2511.03690

## Extraction notes

- User supplied a LinkedIn safety redirect URL; canonical source resolved to `https://github.com/OpenHands/OpenHands`.
- `web_extract` successfully extracted a repository summary and repository snapshot.
- GitHub API was used for current metadata.
- Raw README was fetched from `https://raw.githubusercontent.com/OpenHands/OpenHands/main/README.md`.

## Raw content

```markdown
<a name="readme-top"></a>

<div align="center">
  <img src="https://raw.githubusercontent.com/OpenHands/docs/main/openhands/static/img/logo.png" alt="Logo" width="200">
  <h1 align="center" style="border-bottom: none">OpenHands: AI-Driven Development</h1>
</div>

<div align="center">
  <a href="https://github.com/OpenHands/OpenHands/blob/main/LICENSE"><img src="https://img.shields.io/badge/LICENSE-MIT-20B2AA?style=for-the-badge" alt="MIT License"></a>
  <a href="https://docs.google.com/spreadsheets/d/1wOUdFCMyY6Nt0AIqF705KN4JKOWgeI4wUGUP60krXXs/edit?gid=811504672#gid=811504672"><img src="https://img.shields.io/badge/SWEBench-77.6-00cc00?logoColor=FFE165&style=for-the-badge" alt="Benchmark Score"></a>
  <br/>
  <a href="https://docs.openhands.dev/sdk"><img src="https://img.shields.io/badge/Documentation-000?logo=googledocs&logoColor=FFE165&style=for-the-badge" alt="Check out the documentation"></a>
  <a href="https://arxiv.org/abs/2511.03690"><img src="https://img.shields.io/badge/Paper-000?logoColor=FFE165&logo=arxiv&style=for-the-badge" alt="Tech Report"></a>
</div>

<hr>

🙌 Welcome to OpenHands, a [community](COMMUNITY.md) focused on AI-driven development. We’d love for you to [join us on Slack](https://dub.sh/openhands).

There are a few ways to work with OpenHands:

### OpenHands Software Agent SDK
The SDK is a composable Python library that contains all of our agentic tech. It's the engine that powers everything else below.

Define agents in code, then run them locally, or scale to 1000s of agents in the cloud.

[Check out the docs](https://docs.openhands.dev/sdk) or [view the source](https://github.com/OpenHands/software-agent-sdk/)

### OpenHands CLI
The CLI is the easiest way to start using OpenHands. The experience will be familiar to anyone who has worked
with e.g. Claude Code or Codex. You can power it with Claude, GPT, or any other LLM.

[Check out the docs](https://docs.openhands.dev/openhands/usage/run-openhands/cli-mode) or [view the source](https://github.com/OpenHands/OpenHands-CLI)

### OpenHands Local GUI
Use the Local GUI for running agents on your laptop. It comes with a REST API and a single-page React application.
The experience will be familiar to anyone who has used Devin or Jules.

[Check out the docs](https://docs.openhands.dev/openhands/usage/run-openhands/local-setup) or view the source in this repo.

### OpenHands Cloud
This is a deployment of OpenHands GUI, running on hosted infrastructure.

You can try it for free using the Minimax model by [signing in with your GitHub or GitLab account](https://app.all-hands.dev).

OpenHands Cloud comes with source-available features and integrations:
- Integrations with Slack, Jira, and Linear
- Multi-user support
- RBAC and permissions
- Collaboration features (e.g., conversation sharing)

### OpenHands Enterprise
Large enterprises can work with us to self-host OpenHands Cloud in their own VPC, via Kubernetes.
OpenHands Enterprise can also work with the CLI and SDK above.

OpenHands Enterprise is source-available--you can see all the source code here in the enterprise/ directory,
but you'll need to purchase a license if you want to run it for more than one month.

Enterprise contracts also come with extended support and access to our research team.

Learn more at [openhands.dev/enterprise](https://openhands.dev/enterprise)

### Everything Else

Check out our [Product Roadmap](https://github.com/orgs/openhands/projects/1), and feel free to
[open up an issue](https://github.com/OpenHands/OpenHands/issues) if there's something you'd like to see!

You might also be interested in our [evaluation infrastructure](https://github.com/OpenHands/benchmarks), our [chrome extension](https://github.com/OpenHands/openhands-chrome-extension/), or our [Theory-of-Mind module](https://github.com/OpenHands/ToM-SWE).

All our work is available under the MIT license, except for the `enterprise/` directory in this repository (see the [enterprise license](enterprise/LICENSE) for details).
The core `openhands` and `agent-server` Docker images are fully MIT-licensed as well.

If you need help with anything, or just want to chat, [come find us on Slack](https://dub.sh/openhands).
```
