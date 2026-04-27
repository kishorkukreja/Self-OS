---
title: "CADAM — Open Source Text-to-CAD Web App"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Browser-based text-to-CAD tool generating parametric 3D models via OpenSCAD WebAssembly with real-time previews and interactive parameter sliders."
tags: [text-to-cad, 3d-modeling, openscad, generative-ai, web-app, claude-api]
type: source
status: final
---

# CADAM — Open Source Text-to-CAD Web App

**Type:** repo
**Date:** 2026-04-26
**URL:** https://github.com/Adam-CAD/CADAM
**Raw file:** [[../../raw/repos/cadam-2026-04-26.md]]

**Summary:** CADAM is an open-source text-to-CAD web application that transforms natural language descriptions and images into parametric 3D models directly in the browser. It generates OpenSCAD code and renders it via WebAssembly, allowing real-time parameter adjustments without re-invoking AI generation. The tool supports multiple export formats (.STL and .SCAD), includes BOSL, BOSL2, and MCAD libraries, and features a React 18 + TypeScript frontend with Three.js rendering. The backend uses Supabase (PostgreSQL + Edge Functions) and the Claude API via OpenRouter for generation.

**Key contributions:**
- Natural language and image-to-3D model generation in the browser
- Parametric controls with interactive sliders for instant dimension adjustments
- OpenSCAD WebAssembly engine for client-side rendering
- Real-time preview via Three.js + React Three Fiber
- Smart updates that change parameters without AI re-generation

**Tags:** text-to-cad, 3d-modeling, openscad, generative-ai, web-app, claude-api
