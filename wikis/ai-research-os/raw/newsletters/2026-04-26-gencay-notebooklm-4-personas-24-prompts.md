---
source: Gencay newsletter (Substack)
date: 2026-04-26
type: newsletter
tags: [notebooklm, prompting, personas, marketing, studying, research, design, content-generation]
status: processed
---

# I Built 4 NotebookLM Personas With 24 Prompts (Steal All)

**Author:** Gencay  
**Source:** Substack newsletter  
**Date:** Apr 26, 2026

---

> "NotebookLM is the most underused tool in your stack. Most people upload three PDFs, generate one podcast, and never come back. That is a waste."

**The trick:** NotebookLM is not a summarizer. It is a **persona engine**. Same notebook, four voices: Marketer, Student, Researcher, Designer.

**Rule:** Four separate notebooks beat one mega-notebook. NotebookLM scrambles when sources span unrelated domains.

---

## Persona Structure (All 4)

Each persona follows the same three-part structure:
1. **Sources** you upload (URLs, PDFs, or NotebookLM Deep Research)
2. **Setup prompt** that defines the role and rules
3. **Six working prompts** tied to a specific Studio button

Studio buttons: Data Table, Reports, Audio Overview, Slide Deck, Video Overview, Infographic, Flash Cards, Quiz

---

## Persona 1: Marketer

**Setup Prompt:**
```
You are a senior B2B marketer auditing a SaaS-style content business. 
Tone: direct, no jargon, no marketing fluff. Cite source location after 
every factual claim like (Source 1, "What You Get" section). If a source 
does not state something, write "not in sources" and stop. Never infer 
positioning, pricing, or audience from generic SaaS knowledge. Output 
markdown tables when data is comparable, prose only when narrative is 
required.
```

**Prompt 1: Competitor Intel Table** (Data Table)
Build a competitive intel table comparing learnaiwme.com against godofprompt.ai and promptbase.com. Columns: Brand, One-Sentence Promise, Pricing Model, Target Buyer, Distinctive Feature, Visible Weakness.

**Prompt 2: Positioning Brief** (Reports)
Distill the positioning into: one-sentence promise, buyer's status quo, the shift this site creates, three proof points pulled directly from sources.

**Prompt 3: Copy Audit Line by Line** (Reports)
Audit homepage copy line by line. For each weak line: quote it, name failure mode, rewrite in 12 words or fewer.

**Prompt 4: ICP Profile From Documented Behavior** (Reports)
Profile the ideal customer using only behaviors and language the sources document.

**Prompt 5: 8 Campaign Angles With Forced Emotion Diversity** (Data Table)
Generate 8 distinct campaign angles. Each: hook headline, target emotion (from 8 options), source-backed proof point, buyer objection it dissolves.

**Prompt 6: Audio Overview Brief for Top 3 Objections** (Audio Overview)
Generate a 4-minute script with two hosts focused on top 3 buyer objections.

---

## Persona 2: Student

**Setup Prompt:**
```
You are a patient study partner who has read every source in this 
notebook end to end. Tone: clear, no academic jargon unless the source 
uses it first. Cite source location after every factual claim like 
(Source 2, p.4). If a concept is not covered, say "not in sources" 
and stop. Default to plain language first, technical language second. 
Default to active recall over passive review.
```

**Prompt 1: Concept Breakdown** (Reports)
Break down {concept}: plain-language definition, why it exists, three components, one worked example, most common misunderstanding.

**Prompt 2: Feynman Explanation** (Reports)
Explain {concept} as if teaching a smart 12-year-old. No jargon, one concrete analogy, max 200 words.

**Prompt 3: Active Recall Flashcards** (Flashcards)
Generate recall flashcards: front = retrieval question, back = answer in 25 words or fewer. Mix 3 difficulty levels.

**Prompt 4: Gap Finder** (Reports)
Identify weak spots: 10 questions that require connecting 2+ sections, testing conceptual understanding.

**Prompt 5: Exam Prep Brief** (Main Chat)
Build exam prep: 5 highest-yield concepts, 3 commonly confused concepts, 10 terms, 3 worked-problem patterns.

**Prompt 6: Connection Map** (Audio Overview)
6-minute script mapping how concepts connect, for commute listening.

---

## Persona 3: Researcher

**Setup Prompt:**
```
You are a senior research assistant trained in critical reading. Tone: 
precise, skeptical, no hedging. Cite source location after every claim. 
When sources disagree, surface the disagreement. If a question cannot 
be answered, say "not in sources" and name what additional source 
would be needed. Output structured prose, not bullet soup.
```

**Prompt 1: Literature Synthesis** (Reports)
Synthesize what sources collectively say: core consensus, active debate, settled questions, unanswered questions.

**Prompt 2: Gap Analysis** (Reports)
Identify research gaps: 5 unanswered questions, 3 methodological gaps, 2 contradictions, 1 untested assumption.

**Prompt 3: Methodology Critique** (Reports)
Critique each source's methodology: method, sample, strongest/weakest design choice, alternative approach.

**Prompt 4: Citation Web** (Infographic)
Map citation relationships between sources as a network.

**Prompt 5: Contradiction Finder** (Reports)
Find every contradiction: claim, Source A position, Source B position, reason for disagreement, stronger evidence side.

**Prompt 6: Hypothesis Generator** (Audio Overview)
5-minute script generating 3 testable hypotheses from gaps and contradictions.

---

## Persona 4: Designer

**Prompt 1: Infographic Brief** (Reports)
Build a complete infographic brief: key insight, information hierarchy, visual metaphor, layout type, color logic, typography pairing, three things to NOT include.

**Prompt 2: Concept Infographic** (Infographic)
Visualize {topic} with one statistic as focal point + 4 supporting facts from different sources.

**Prompt 3: Visual Hierarchy Audit** (Slide Deck)
Generate a slide deck: each slide has title (max 6 words), 3 bullets (max 10 words), speaker notes.

**Prompt 4: Brand Voice Extract** (Video Overview)
Immersive tour of how AI educators visually communicate complex ideas.

**Prompt 5: Comparison Infographic** (Infographic)
Comparison visualization with source-backed data.

**Prompt 6: Design System Audit** (Reports)
Audit visual patterns across sources: color palettes, typography, layout rhythms, icon styles.

---

## Key Takeaways

- **Persona engine, not summarizer** — same sources, different outputs
- **One notebook per persona** — no mixing domains
- **Studio button matters** — wrong button breaks output
- **Scalable pattern** — same skeleton, new voice (copywriter, lawyer, startup advisor, etc.)
