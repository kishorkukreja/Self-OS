---
title: "Computer-Use Agent Verification"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Methods and benchmarks for reliably verifying whether autonomous computer-use agents have succeeded on web and GUI tasks."
tags: ['computer-use-agents', 'verification', 'process-reward', 'outcome-verification']
type: concept
status: draft
confidence: emerging
source_count: 2
---

# Computer-Use Agent Verification

**Computer-use agent (CUA) verification** addresses the challenge of determining whether an agent trajectory actually achieved the user goal, a prerequisite for both benchmarking and training. The [[Universal Verifier]] introduces four principles: specific non-overlapping rubrics, separation of process and outcome rewards, distinguishing controllable from uncontrollable failures, and structured screenshot context management.

Key signals:
- **Process reward:** Fine-grained score reflecting execution quality across sub-goals.
- **Outcome reward:** Binary judgment on whether the user goal was achieved.
- **Cascading-error-free scoring:** Penalizes failures proportionally rather than compounding upstream errors.

_Last updated: 2026-04-27_
