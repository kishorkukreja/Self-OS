---
title: "BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate"
date_created: 2026-04-30
date_modified: 2026-04-30
summary: "BARRED — Boundary Alignment Refinement through REflection and Debate — is a framework for training custom policy guardrail classifiers from only a task/policy description and a small set of unlabeled examples. The core c"
tags: [guardrails, synthetic-data, ai-safety, llm-evaluation, debate, custom-policy-classifiers, plurai]
type: source
status: final
---

# BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate

**Type:** paper  
**Date:** 2026-01-21  
**URL:** https://cdn.prod.website-files.com/691ef0a011466cf6dc334d6a/69aff666e1120dcc80a632f2_Plurai_Guardrail_Training_ICML.pdf  
**Raw file:** [[../raw/papers/2026-04-29-mazza-barred-synthetic-training-custom-policy-guardrails.md]]

**Summary:** BARRED — Boundary Alignment Refinement through REflection and Debate — is a framework for training custom policy guardrail classifiers from only a task/policy description and a small set of unlabeled examples. The core claim is that custom guardrail deployment is blocked less by model architecture and more by the cost and difficulty of labeled data for application-specific policies. BARRED tries to remove that bottleneck by generating synthetic examples that are both diverse and label-faithful.
The framework decomposes the policy into task-relevant dimensions, samples values along those dimensions, generates boundary-challenging examples with reasoning, and then validates candidate examples through asymmetric multi-agent debate. Rejected samples are refined using debate feedback and re-evaluated. The resulting synthetic training set is used to fine-tune compact classifier models, which the paper reports can outperform generic guardrails and proprietary LLM-as-judge baselines, including reasoning models, on custom policy tasks.

**Key contributions:**
- Custom guardrails need to enforce application-specific policies, where a response that is safe in one setting can be a critical failure in another.
- Generic/static guardrails are low-latency but cannot easily adapt to user-defined policies without retraining.
- Dynamic guardrails and prompted LLM-as-judge setups are flexible but have higher latency, inference cost, and inconsistent boundary-case behavior.
- Custom classifiers are accurate and efficient, but normally require expensive labeled data.
- BARRED generates labeled synthetic training data using only a policy description and small unlabeled seed set.
- Diversity comes from dimension decomposition and verbalized sampling.

**Tags:** guardrails, synthetic-data, ai-safety, llm-evaluation, debate, custom-policy-classifiers, plurai
