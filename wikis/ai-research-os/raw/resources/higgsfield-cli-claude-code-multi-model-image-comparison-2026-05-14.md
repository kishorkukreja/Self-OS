---
source: conversation paste + https://higgsfield.ai/cli
date: 2026-05-14
type: resource
tags: [higgsfield, claude-code, ai-image-generation, multi-model-comparison, creative-agents, cli-workflows, product-demo]
---

# Higgsfield CLI + Claude Code — Multi-Model Image Comparison Workflow

## Summary

The Rundown guide describes a workflow for connecting Higgsfield to Claude Code with the Higgsfield CLI, then asking Claude Code to send one image prompt to several AI image models at once. The operational pattern is a **creative model bake-off**: install and authenticate Higgsfield, add the Higgsfield skill to Claude Code, ask Claude Code to verify setup and list available models, run the same prompt across six models, save all outputs in a comparison folder, and generate a `comparison.md` with notes. This is relevant to Self-OS/Hermes as a candidate workflow for systematic creative model evaluation rather than one-off image generation.

## Source context

- **Pasted source:** The Rundown guide snippet supplied by user in Telegram.
- **Companion official page:** https://higgsfield.ai/cli
- **GitHub surfaced by official page:** https://github.com/higgsfield-ai/cli
- **NPM package checked:** `@higgsfield/cli`
- **NPM latest at capture time:** `0.1.40`
- **NPM description:** “Higgsfield AI CLI — generate images and videos from the terminal.”

## User-pasted workflow

The Rundown summary:

> In this guide, you will learn how to connect Higgsfield to Claude Code with the Higgsfield CLI, then use Claude Code to send one image prompt to several AI image models at once.

Step-by-step:

1. Create a new project folder.
2. Install Higgsfield CLI:

   ```bash
   npm install -g @higgsfield/cli
   ```

3. Authenticate:

   ```bash
   higgsfield auth login
   ```

4. Add Higgsfield skill for Claude Code:

   ```bash
   npx skills add higgsfield-ai/skills
   ```

5. Open Claude Code in the same folder and ask it to inspect `higgsfield.ai/cli`, verify the installation, and list available image models.
6. Give Claude Code an image prompt and tell it to run it across six models.
7. Save outputs into a `higgsfield-model-test/` folder.
8. Generate a `comparison.md` file with notes for each result.
9. Pick the best direction.
10. Ask Claude Code to refine the winning prompt or run one more comparison.

Pro tip from the source:

- If setup gets confusing, ask Claude Code to check Node/npm and give a walkthrough.
- Higgsfield also supports video, so the same workflow can be tried for short clips.

Adjacent newsletter item mentioned but not expanded:

- “Claude for Small Business - New tools for payroll, invoices, and campaigns.”

## Official Higgsfield CLI page notes

The official page positions Higgsfield CLI as a way to connect Higgsfield’s AI image/video generation tools to agents including **Claude**, **OpenClaw**, **Hermes**, and **NemoClaw**.

Quickstart from official page:

```bash
npm install -g @higgsfield/cli
higgsfield auth login
npx skills add higgsfield-ai/skills
```

The page frames Higgsfield as “a complete creative studio inside Claude,” with capabilities including:

- Image generation
- Video creation
- Character training
- Asset management
- Marketing Studio workflows
- Brand kit integration
- Multi-model comparisons
- Generation history browsing
- Campaign and content automation

Mentioned media capabilities:

- Static images
- Cinematic videos
- Any aspect ratio
- Any duration
- Up to 4K
- Model and parameter selection

Models mentioned on the page include:

- Soul
- Nano Banana
- Seedance
- Kling
- Veo

## Operational pattern

This is not just an image tool setup; it is a reusable **model-comparison workflow**:

```text
Prompt idea
  → verified CLI + auth + available models
  → run same prompt across N models
  → save outputs in structured folder
  → write comparison.md with notes
  → choose best direction
  → refine prompt or run another comparison
```

Suggested output folder structure:

```text
higgsfield-model-test/
  prompt.md
  outputs/
    model-1.png
    model-2.png
    model-3.png
    model-4.png
    model-5.png
    model-6.png
  comparison.md
```

A stronger comparison file should include:

- Prompt used
- Model name
- Output path
- Visual strengths
- Visual weaknesses
- Prompt adherence
- Style fit
- Artifact / anatomy / text-rendering issues
- Recommended next prompt refinement
- Winner and rationale

## Why it matters

For creative workflows, this turns subjective “try an image model” exploration into a small evaluation harness. Instead of asking an agent to generate one image and hoping it works, the workflow creates comparable artifacts, written judgments, and a clear refinement loop. That is more aligned with Self-OS’ preference for evidence and QA than pure vibe-based creative generation.

## Self-OS / Hermes implications

- **Potential product-demo/image skill candidate:** This could become a Hermes-native skill after manual validation, especially for comparing image models before producing final product-demo assets.
- **Keep outputs outside Self-OS:** If used for actual generations, the generated images/video should go in a separate product demos or creative experiments directory, not inside `/data/Self-OS`, unless explicitly requested.
- **Comparison-first creative work:** The workflow matches the user’s preference for grounding recommendations in genuine findings: generate multiple outputs, compare them, then refine.
- **Need credential and cost controls:** Authentication, paid model usage, and generated media storage should be explicit before automating this through Hermes or cron.
- **Video extension:** Since Higgsfield supports video, the same comparison harness could be extended to short clip generation, but image comparison should be validated first.
- **Agent portability:** Official Higgsfield positioning mentions Hermes, suggesting this may not need to remain Claude Code-only; however, exact Hermes integration should be tested before relying on it.

## Verification notes

- `web_extract` successfully extracted https://higgsfield.ai/cli.
- `npm view @higgsfield/cli` verified the package exists and latest version is `0.1.40` at capture time.
- No live Higgsfield authentication or generation was run during this capture.
- The guide text was supplied by the user; no original newsletter URL was included.

## Raw pasted text

```text
The Rundown: In this guide, you will learn how to connect Higgsfield to Claude Code with the Higgsfield CLI, then use Claude Code to send one image prompt to several AI image models at once.

Step-by-step:

Create a new project folder, install Higgsfield CLI (npm install -g @higgsfield/cli), authenticate (higgsfield auth login), and add Higgsfield skill (npx skills add higgsfield-ai/skills) for Claude Code

Open Claude Code in the same folder and ask it to inspect higgsfield.ai/cli, verify the installation, and list available image models

Give Claude Code an image prompt and tell it to run it across six models, save outputs into a higgsfield-model-test folder, and generate a comparison.md file with notes for each result

Pick the best direction, then ask Claude Code to refine the winning prompt or run one more comparison

Pro tip: If setup gets confusing, ask Claude Code to check Node/npm and give a walkthrough. Higgsfield also supports video, so you can also try this for short clips

🏪 Claude for Small Business - New tools for payroll, invoices, and campaigns
```
