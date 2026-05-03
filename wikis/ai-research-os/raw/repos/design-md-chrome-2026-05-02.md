---
source: https://github.com/bergside/design-md-chrome
date: 2026-05-02
type: repo
tags: [design-md, chrome-extension, design-systems, typeui, frontend, skills, design-tokens]
status: processed
---

# design-md-chrome (TypeUI DESIGN.md Extractor)

## Summary

A Chrome extension by Bergside that extracts visual styles and design tokens from any website and generates a `DESIGN.md` or `SKILL.md` file. The output follows the open-source TypeUI DESIGN.md format and can be used with tools such as Google Stitch, Claude Code, and Codex as a blueprint for recreating a site's design system.

## Key points

- **Auto-extract**: reads typography, colors, spacing, radius, shadows, and motion from the active tab.
- **Generate DESIGN.md**: produces design-system documentation markdown from extracted signals.
- **Generate SKILL.md**: produces agent-ready skill markdown for AI coding tools.
- **Refresh**: re-runs extraction for the current page state.
- **Download**: saves generated output as `DESIGN.md` or `SKILL.md`.
- **Explain**: shows how the file was generated, with TypeUI reference.

## Generated file structure

The generated markdown follows a standard TypeUI DESIGN.md structure with sections covering Mission, Brand, Style Foundations, Accessibility, Writing Tone, Rules (Do/Don't), Guideline Authoring Workflow, Required Output Structure, Component Rule Expectations, and Quality Gates.

## Installation

1. Download the extension source.
2. Open `chrome://extensions`
3. Enable **Developer mode**
4. Click **Load unpacked**
5. Select the project folder.

## Related links

- **Repository**: https://github.com/bergside/design-md-chrome
- **Curated design skills**: https://www.typeui.sh/design-skills
- **TypeUI DESIGN.md format**: https://www.typeui.sh/design-md
- **DESIGN.md concept** (Google project): https://github.com/google-labs-code/design.md

## Why it matters

For SelfOS and agentic frontend workflows, this is a fast way to reverse-engineer a site's design system into a machine-readable `DESIGN.md`. It complements manual design review and can be paired with Hermes' `design-md` skill for authoring and validating DESIGN.md specs.

## Raw content

Extracted README via `web_extract`.

The README describes a Chrome extension that extracts styles and information from any given site and generates a `DESIGN.md` or `SKILL.md` file that you can use with tools such as Google Stitch, Claude Code, Codex, and others to build websites with a given design system blueprint. The file is based on the open-source TypeUI DESIGN.md format.

Available actions include Auto-extract, Generate DESIGN.md, Generate SKILL.md, Refresh, Download, and Explain. The generated markdown covers Mission, Brand, Style Foundations, Accessibility, Writing Tone, Rules (Do/Don't), Guideline Authoring Workflow, Required Output Structure, Component Rule Expectations, and Quality Gates.
