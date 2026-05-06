---
source: https://github.com/yizhiyanhua-ai/fireworks-tech-graph
date: 2026-05-06
type: repo
tags: [technical-diagrams, svg, png, ai-agents, architecture-diagrams, claude-code-skills, rag, multi-agent-systems]
---

# fireworks-tech-graph

## Summary
`fireworks-tech-graph` is a GitHub repository by `yizhiyanhua-ai` for generating production-quality technical diagrams from natural language. It is packaged as a Claude Code skill / diagram-generation system that converts plain English or Chinese descriptions into polished SVG diagrams and high-resolution PNG exports using `rsvg-convert`.

The repo is especially relevant to AI/agent documentation because it includes built-in patterns for RAG pipelines, agentic RAG, agentic search, Mem0-style memory systems, multi-agent collaboration, and tool-call loops. It can be used to turn system descriptions into architecture diagrams, data-flow diagrams, sequence diagrams, concept maps, and other technical visuals.

## Repository
- GitHub: https://github.com/yizhiyanhua-ai/fireworks-tech-graph
- NPM package: https://www.npmjs.com/package/@yizhiyanhua-ai/fireworks-tech-graph
- License: MIT
- Approximate GitHub stats at capture: ~5.6k stars, ~505 forks
- Primary language: Python
- Requirements: `rsvg-convert` from `librsvg` for PNG export

## Key points
- Generates editable SVG and high-resolution PNG diagrams from natural language.
- Supports English and Chinese prompts.
- Includes multiple visual styles, including flat icon, dark terminal, blueprint, Notion clean, glassmorphism, Claude-style, and OpenAI-style aesthetics.
- Supports UML-style diagrams and AI/agent workflow patterns.
- Built-in architecture patterns include RAG, agentic RAG, agentic search, Mem0 memory layers, multi-agent collaboration, and tool-call loops.
- Designed for technical documentation, README diagrams, engineering blogs, slides, and agent architecture docs.
- Uses local SVG generation and `rsvg-convert`, avoiding dependency on external CDNs/fonts for output rendering.

## Installation

Install as a Claude Code skill:

```bash
npx skills add yizhiyanhua-ai/fireworks-tech-graph
```

Update:

```bash
npx skills add yizhiyanhua-ai/fireworks-tech-graph --force -g -y
```

Clone directly:

```bash
git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git ~/.claude/skills/fireworks-tech-graph
```

Install PNG export dependency:

```bash
# macOS
brew install librsvg

# Ubuntu/Debian
sudo apt install librsvg2-bin

# Verify
rsvg-convert --version
```

## Example prompts

```text
Draw a RAG pipeline flowchart
```

```text
Generate an Agentic Search architecture diagram
```

```text
Generate a Mem0 memory architecture diagram, dark style
```

```text
Draw a multi-agent collaboration diagram --style glassmorphism
```

```text
Create a tool call flow diagram --output /tmp/diagrams/
```

## Visual styles mentioned by the README
- Flat Icon — white background; useful for blogs, slides, docs.
- Dark Terminal — dark developer aesthetic; useful for READMEs and technical articles.
- Blueprint — architecture/engineering look.
- Notion Clean — clean white documentation style.
- Glassmorphism — product/keynote style.
- Claude Official — warm Anthropic-like aesthetic.
- OpenAI Official — clean modern OpenAI-like aesthetic.

## Why it matters
This is useful for Self-OS and AI research documentation because architecture ideas often arrive as text descriptions before they become diagrams. A reusable skill that turns system descriptions into SVG + PNG can make agent architectures more legible in briefs, PRDs, README files, slide decks, and wiki pages. Its built-in knowledge of agent patterns means it can avoid generic flowcharts and instead produce diagrams that reflect real AI system structures: retrieval layers, memory stores, planner/executor loops, tool calls, and multi-agent handoffs.

## Raw content

GitHub repository summary extracted from the live repository page:

- Repository: `yizhiyanhua-ai/fireworks-tech-graph`
- Title: Generate production-quality SVG+PNG technical diagrams from natural language. 7 styles, UML support, and AI/Agent workflow patterns.
- Core pitch: Stop drawing diagrams by hand. Describe your system in English or Chinese and get publication-ready SVG + PNG technical diagrams in seconds.
- Example workflow: User asks for a Mem0 memory architecture diagram in dark style; the skill classifies the diagram as a memory architecture diagram, generates an SVG with swim lanes, cylinders, semantic arrows, and exports a 1920px PNG.
- Key capabilities: natural-language diagram generation, editable SVG, 1920px PNG, `rsvg-convert` export, multiple visual styles, UML diagram types, AI/agent workflow patterns, semantic shapes, arrows, swim lanes, and product icons.
