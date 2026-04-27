---
title: "DESIGN.md — Google Labs Format Specification"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Alpha-format specification from Google Labs for describing visual design systems to coding agents using machine-readable YAML tokens combined with human-readable Markdown rationale."
tags: [design-system, agent-tooling, google-labs, format-spec, coding-agents]
type: source
status: final
---

# DESIGN.md — Google Labs Format Specification

**Type:** repo
**Date:** 2026-04-26
**URL:** https://github.com/google-labs-code/design.md
**Raw file:** [[../../raw/repos/design-md-2026-04-26.md]]

**Summary:** DESIGN.md is an alpha format specification that gives coding agents a persistent, structured understanding of a design system. It combines machine-readable design tokens (YAML front matter) with human-readable design rationale (Markdown prose). The specification defines a canonical token schema covering colors, typography, spacing, rounded corners, and component properties, along with a canonical section order from Overview through Do's and Don'ts. A companion CLI toolkit (`@google/design.md`) provides linting, diffing, and validation capabilities.

**Key contributions:**
- Standardised token schema for design systems targeting agent consumption
- Canonical section order ensuring predictable agent parsing
- Component token support with variant states (hover, active, pressed)
- Consumer behaviour specification for graceful handling of unknown content
- CLI tools for validation and regression detection between design versions

**Tags:** design-system, agent-tooling, google-labs, format-spec, coding-agents
