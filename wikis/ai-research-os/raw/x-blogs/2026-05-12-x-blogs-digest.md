---
source: X/Twitter daily search
date: 2026-05-12
type: article
tags: [x, twitter, blogs, articles, ai-research, daily-digest]
---

# X/Twitter AI Blogs and Articles — 2026-05-12

## Summary

Daily digest of AI/ML articles, papers, releases, and blog links discovered from X/Twitter-oriented search. `xurl` was not available in the cron environment, so discovery used Hermes `web_search` fallback queries targeting X/Twitter posts and follow-up exact-title searches to recover outbound source links where possible.

Themes surfaced today:

- Agent harnesses, context files, and operational reliability remain a major topic: multiple X results pointed to harness engineering, `AGENTS.md`, and agent reliability work.
- New and recent benchmarks are focusing less on static task success and more on long-horizon, help-seeking, legal-work, reliability, and evaluation-redundancy questions.
- Agent safety discussions are shifting toward persistent state, capability/identity/knowledge poisoning, and specification/governance failure modes.
- Model/infrastructure links included NVIDIA Nemotron 3 Super and OpenForecaster/OpenForesight, both emphasizing specialized agentic or future-reasoning capabilities.

## Top links

### 1. [AI Agents Have Two Souls. You Only Control One.](https://auth0.com/blog/ai-agents-have-two-souls-you-control-only-one/)

- Shared via X: <https://x.com/andychiare/status/2053778390558314587>
- Source/domain: auth0.com
- Author/source: Andrea Chiarelli / Auth0
- Why it matters: Frames agent security around deterministic **agent core** architecture rather than trying to directly control the probabilistic LLM.
- Extracted summary: Agents combine a deterministic software layer and a probabilistic LLM; the article argues security controls should sit in the deterministic agent core, which mediates tools, retrieval, actions, memory, and LLM outputs.
- Signals: Recovered from X search result for “two souls” and confirmed via article extraction.

### 2. [LLM Knowledge Bases](https://academy.dair.ai/blog/llm-knowledge-bases-karpathy)

- Shared via X: <https://x.com/karpathy/status/2039805659525644595>
- Source/domain: academy.dair.ai
- Author/source: Elvis Saravia / DAIR.AI Academy, summarizing Andrej Karpathy’s X post
- Why it matters: Strongly overlaps with Self-OS architecture: raw source ingestion → LLM compilation → interlinked markdown wiki → query/enhancement loops.
- Extracted summary: The post describes using LLMs as compilers for personal knowledge bases, turning raw articles, papers, repos, and notes into structured markdown wikis with indexes, backlinks, concept pages, derived outputs, and linting.
- Signals: X result from Karpathy’s post plus recovered long-form DAIR.AI article.

### 3. [Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)

- Shared via X: <https://x.com/GenAI_is_real/status/2036266930290696599>
- Source/domain: humanlayer.dev
- Author/source: HumanLayer
- Why it matters: Treats coding-agent success as a harness/runtime/configuration problem, not only a model-quality problem.
- Extracted summary: The article defines `coding agent = model(s) + harness`, then surveys configuration levers such as `CLAUDE.md`/`AGENTS.md`, MCP servers, skills, sub-agents, hooks, and verification/back-pressure loops.
- Signals: Recovered from X search phrase “Harness Engineering” and extracted successfully.

### 4. [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html)

- Shared via X: surfaced by X-oriented search results discussing harnesses and progressive disclosure.
- Source/domain: martinfowler.com
- Author/source: Birgitta Böckeler / Thoughtworks
- Why it matters: Gives a software-engineering vocabulary for “outer harnesses” around coding agents: guides, sensors, feedforward controls, and feedback controls.
- Extracted summary: The article argues that teams can reduce supervision and increase confidence in AI-generated code by building harness controls: deterministic tests/linters/codemods, inferential review agents/skills, and feedback loops that let agents self-correct.
- Signals: Follow-up search for “Harness Engineering” recovered the article; extraction confirmed publication and content.

### 5. [HiL-Bench (Human-in-Loop Benchmark)](https://labs.scale.com/leaderboard/hil)

- Shared via X: <https://x.com/cwolferesearch/status/2052040103422226555>
- Source/domain: labs.scale.com
- Author/source: Scale AI
- Why it matters: Evaluates whether agents know when to stop guessing and ask humans targeted questions.
- Extracted summary: HiL-Bench tests selective escalation across software-engineering and text-to-SQL tasks with hidden missing, ambiguous, or contradictory blockers. It measures whether agents use `ask_human()` at the right time instead of confidently failing.
- Signals: X result explicitly mentioned HIL-Bench; extracted benchmark page and arXiv paper were consistent.

### 6. [HiL-Bench: Do Agents Know When to Ask for Help?](https://arxiv.org/html/2604.09408v3)

- Shared via X: <https://x.com/cwolferesearch/status/2051756934097973248>
- Source/domain: arxiv.org
- Author/source: Tu Trinh et al. / Scale AI
- Why it matters: Paper version of the benchmark gives dataset design, blocker taxonomy, and a “confident failure” framing for agent evaluation.
- Extracted summary: The paper argues current benchmarks are blind to agents that should ask for help but instead guess. It introduces 300 tasks with 1,131 blockers spanning missing information, ambiguity, and contradictions.
- Signals: X search plus exact title follow-up; extracted arXiv HTML.

### 7. [Introducing Harvey’s Legal Agent Benchmark](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)

- Shared via X: <https://x.com/NVIDIAAI/status/2052469248975671524>
- Source/domain: harvey.ai
- Author/source: Harvey
- Why it matters: Extends long-horizon agent benchmarking into legal work, with rubrics and realistic client-matter assignments.
- Extracted summary: Harvey LAB is an open-source legal-agent benchmark with 1,250 tasks, 24 practice areas, and 75,000+ expert-written rubric criteria. It focuses on planning, retrieval, synthesis, and reviewable legal work products rather than short Q&A.
- Signals: X result described an open-source benchmark for legal-agent capabilities; source article extracted successfully.

### 8. [Towards a Science of AI Agent Reliability](https://arxiv.org/abs/2602.16666)

- Shared via X: <https://x.com/random_walker/status/2026384543700115870>
- Source/domain: arxiv.org
- Author/source: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan
- Why it matters: Pushes agent evaluation beyond average success rate into reliability profiles that matter for deployment.
- Extracted summary: The paper proposes twelve reliability metrics across consistency, robustness, predictability, and safety. It evaluates 14 models and argues recent capability gains have produced only small reliability improvements.
- Signals: X search result for paper title; arXiv extraction successful.

### 9. [New Paper: Towards a science of AI agent reliability](https://www.normaltech.ai/p/new-paper-towards-a-science-of-ai)

- Shared via X: <https://x.com/random_walker/status/2026384543700115870>
- Source/domain: normaltech.ai
- Author/source: Sayash Kapoor & Arvind Narayanan
- Why it matters: Accessible blog companion to the agent reliability paper, with practical analogies from safety-critical engineering.
- Extracted summary: The post explains the “capability-reliability gap” and reports experiments across GAIA and TauBench, including repeated runs, paraphrased instructions, tool faults, confidence estimation, and 500 benchmark runs.
- Signals: Recovered as the official-looking blog companion for the X-posted paper.

### 10. [NVIDIA Nemotron 3 Super](https://research.nvidia.com/labs/nemotron/Nemotron-3-Super/)

- Shared via X: <https://x.com/kwindla/status/2031777618274763095>
- Source/domain: research.nvidia.com
- Author/source: NVIDIA Research
- Why it matters: Open model release positioned for high-throughput agentic and long-context workflows.
- Extracted summary: NVIDIA describes Nemotron 3 Super as a 120B-total/12B-active hybrid Mamba-Transformer MoE model with up to 1M context, NVFP4 checkpoints, multi-token prediction, and released weights/data/recipes.
- Signals: X search surfaced Nemotron 3 Super launch; source page and NVIDIA blog extracted.

### 11. [New NVIDIA Nemotron 3 Super Delivers 5x Higher Throughput for Agentic AI](https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/)

- Shared via X: <https://x.com/kwindla/status/2031777618274763095>
- Source/domain: blogs.nvidia.com
- Author/source: NVIDIA Blog
- Why it matters: Explains NVIDIA’s agentic-AI positioning: context explosion, thinking tax, long context, and throughput constraints for multi-agent systems.
- Extracted summary: The blog says Nemotron 3 Super uses hybrid MoE, Mamba layers, LatentMoE, multi-token prediction, and NVFP4 optimization to improve throughput and accuracy for autonomous agent systems.
- Signals: Companion source recovered from exact Nemotron search and extracted.

### 12. [You Don’t Need to Run Every Eval](https://dimitrisp.substack.com/p/you-dont-need-to-run-every-eval)

- Shared via X: <https://x.com/arafatkatze/status/2027428568717005033>
- Source/domain: dimitrisp.substack.com
- Author/source: Dimitris Papailiopoulos
- Why it matters: Challenges eval-suite sprawl by arguing many LLM benchmark scores can be predicted from a small subset.
- Extracted summary: The post introduces BenchPress, claiming LLM benchmark matrices are low-rank enough that five benchmarks can predict many others within a few points. It uses sparse regression and rank-2 SVD matrix completion over 83 models and 49 benchmarks.
- Signals: X result quoted “LLM evals are so low-rank”; exact phrase search found the Substack.

### 13. [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988)

- Shared via X: <https://x.com/omarsar0/status/2027025932339278029>
- Source/domain: arxiv.org
- Author/source: Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev
- Why it matters: Empirical caution for agent instruction files: more context can increase cost and reduce task success if it adds unnecessary requirements.
- Extracted summary: Across multiple coding agents and LLMs, repository-level context files tended to reduce task success compared with no context file and increased inference cost by over 20%; the paper recommends minimal human-written requirements.
- Signals: X result surfaced trending AGENTS.md paper; arXiv extracted.

### 14. [Scaling Open-Ended Reasoning To Predict the Future](https://arxiv.org/html/2512.25070v1)

- Shared via X: <https://x.com/ShashwatGoel7/status/2008589506492932466>
- Source/domain: arxiv.org
- Author/source: Nikhil Chandak, Shashwat Goel, Ameya Prabhu, Moritz Hardt, Jonas Geiping
- Why it matters: Shows a specialized route for training LLMs to produce calibrated open-ended forecasts rather than only binary predictions.
- Extracted summary: The paper releases OpenForesight, a ~52K-question open-ended forecasting dataset generated from global news, and trains OpenForecaster8B via RL with accuracy plus adapted Brier-score rewards.
- Signals: X search surfaced OpenForesight/OpenForecaster announcement; arXiv extraction successful.

### 15. [OpenForecaster-8B](https://huggingface.co/nikhilchandak/OpenForecaster-8B)

- Shared via X: <https://x.com/ShashwatGoel7/status/2008589506492932466>
- Source/domain: huggingface.co
- Author/source: Nikhil Chandak et al.
- Why it matters: Provides a concrete model artifact for open-ended forecasting experiments.
- Extracted summary: OpenForecaster-8B is post-trained from Qwen3-8B on OpenForesight with GRPO and a joint accuracy/Brier reward. The model card emphasizes calibrated confidence and retrieval for recent events beyond its cutoff.
- Signals: Companion artifact recovered through exact OpenForesight search.

### 16. [The Specification Trap](https://arxiv.org/html/2512.03048v5)

- Shared via X: <https://x.com/KanikaBK/status/2053868195258495274>
- Source/domain: arxiv.org
- Author/source: Austin Spizzirri
- Why it matters: Connects alignment and governance to an “open specification” model rather than fixed value targets for increasingly autonomous systems.
- Extracted summary: The paper argues static content-based value alignment is insufficient under capability scaling, distributional shift, and autonomy. It defines the specification trap as what happens when a value specification becomes closed and no longer updates from the process it governs.
- Signals: X search result mentioned the paper and date; exact title search recovered arXiv.

### 17. [Your Agent, Their Asset: A Real-World Safety Analysis of OpenClaw](https://www.researchgate.net/publication/403562849_Your_Agent_Their_Asset_A_Real-World_Safety_Analysis_of_OpenClaw)

- Shared via X: <https://x.com/KanikaBK/status/2052055386870726782>
- Source/domain: researchgate.net / arXiv preprint metadata
- Author/source: Zijun Wang et al.
- Why it matters: Directly relevant to personal AI operating systems because it studies attacks against persistent agent state and local capabilities.
- Extracted summary: The paper evaluates OpenClaw, a local personal AI agent with Gmail, Stripe, and filesystem access. It introduces the CIK taxonomy—Capability, Identity, Knowledge—and reports that poisoning persistent state can substantially increase attack success rates.
- Signals: X result surfaced paper title; exact title search recovered ResearchGate/arXiv metadata.

## Raw candidates / notes

### Search environment

- `xurl` check: `command -v xurl` returned missing in the cron environment.
- Because `xurl` was unavailable, no X API auth check or direct engagement metrics were available.
- Fallback used Hermes `web_search` against X/Twitter-oriented queries and exact phrase/title searches to recover outbound article URLs.

### Fallback X/Twitter-oriented queries run

- `site:x.com AI LLM agents blog article today`
- `site:x.com AI research paper blog lang en`
- `site:x.com LLM agents evals benchmark article`
- `site:x.com machine learning blog post AI tools`
- `AI LLM agents blog article X Twitter today`
- `site:x.com LLM inference training benchmark release blog`
- `site:x.com AI agents newsletter paper release`

### Exact-title / recovery searches run

- `"two souls" "AI agent" blog`
- `"LLM Knowledge Bases" Karpathy`
- `"Harness Engineering" AI agents blog`
- `"progressive disclosure" "working agents" harness article`
- `"HIL-Bench" LLM benchmark`
- `"Harvey" open-source benchmark agent capabilities legal work`
- `"Your Agent, Their Asset" paper April 2026`
- `"The Specification Trap" paper April 2026`
- `"Towards a Science of AI Agent Reliability"`
- `"CAD" disaggregated approach accelerate long context LLM training`
- `"OpenForesight" 52k forecasting questions dataset`
- `"NVIDIA Nemotron 3 Super"`
- `"LLM evals are so low-rank" 5 benchmarks 44`
- `"AGENTS.md" coding agents benchmark paper`
- `"Ollama, vLLM, SGLang, and LLaMA.cpp Server"`

### Additional candidates seen but not promoted

- [Efficient Long-context Language Model Training by Core Attention Disaggregation](https://arxiv.org/pdf/2510.18121) — surfaced via X result about CAD for long-context LLM training; not promoted because extraction was not completed in this run.
- Hyperbolic posts about LLM serving frameworks — X snippets mentioned Ollama, vLLM, SGLang, and LLaMA.cpp Server; outbound long-form URL was not visible in fallback search results.
- Malware-reversing agents overview — X snippet appeared relevant but no source URL was recovered quickly.
- General X/Twitter growth-agent articles — excluded as lower relevance to AI/ML research and more marketing/tooling oriented.

### Extraction notes

- `web_extract` successfully summarized most non-X URLs used in the digest.
- One batched extraction attempt over many URLs timed out; extraction was retried in smaller batches successfully.
- X post pages themselves were not extracted; snippets from `web_search` were used only as discovery signals, and the digest prefers recovered outbound sources.
