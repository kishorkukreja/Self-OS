---
source: https://cdn.prod.website-files.com/691ef0a011466cf6dc334d6a/69aff666e1120dcc80a632f2_Plurai_Guardrail_Training_ICML.pdf
date: 2026-01-21
type: paper
tags: [guardrails, synthetic-data, ai-safety, llm-evaluation, debate, custom-policy-classifiers, plurai]
---

# BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate

**Authors:** Arnon Mazza, Elad Levi — Plurai Inc.  
**Date:** Preprint, January 21, 2026  
**PDF:** https://cdn.prod.website-files.com/691ef0a011466cf6dc334d6a/69aff666e1120dcc80a632f2_Plurai_Guardrail_Training_ICML.pdf  
**Code:** https://github.com/plurai-ai/BARRED  
**Datasets:** https://huggingface.co/datasets/Plurai/BARRED

## Summary

BARRED — **Boundary Alignment Refinement through REflection and Debate** — is a framework for training custom policy guardrail classifiers from only a task/policy description and a small set of unlabeled examples. The core claim is that custom guardrail deployment is blocked less by model architecture and more by the cost and difficulty of labeled data for application-specific policies. BARRED tries to remove that bottleneck by generating synthetic examples that are both diverse and label-faithful.

The framework decomposes the policy into task-relevant dimensions, samples values along those dimensions, generates boundary-challenging examples with reasoning, and then validates candidate examples through asymmetric multi-agent debate. Rejected samples are refined using debate feedback and re-evaluated. The resulting synthetic training set is used to fine-tune compact classifier models, which the paper reports can outperform generic guardrails and proprietary LLM-as-judge baselines, including reasoning models, on custom policy tasks.

## Key points

- Custom guardrails need to enforce application-specific policies, where a response that is safe in one setting can be a critical failure in another.
- Generic/static guardrails are low-latency but cannot easily adapt to user-defined policies without retraining.
- Dynamic guardrails and prompted LLM-as-judge setups are flexible but have higher latency, inference cost, and inconsistent boundary-case behavior.
- Custom classifiers are accurate and efficient, but normally require expensive labeled data.
- BARRED generates labeled synthetic training data using only a policy description and small unlabeled seed set.
- Diversity comes from dimension decomposition and verbalized sampling.
- Faithfulness comes from multi-agent debate validation plus iterative refinement of rejected samples.
- The paper positions synthetic-data generation as the key lever for turning policy descriptions into cheap, deployable small-model guardrails.

## BARRED pipeline

The paper describes a four-stage pipeline:

1. **Decompose the task** into policy-relevant dimensions using the task description and seed samples.
2. **Sample dimension instantiations and target labels** using verbalized sampling to avoid mode collapse.
3. **Generate boundary-challenging samples** with reasoning for why the example should match the target label.
4. **Validate samples through asymmetric multi-agent debate**, accepting samples that survive debate and refining rejected samples using feedback.

Accepted samples are added to the training set. Rejected samples are refined and re-evaluated until accepted or a retry limit is reached.

## Algorithm excerpt

```text
Algorithm 1 BARRED sample generation algorithm
1: Input: task T, unlabeled seeds S, target size N
2: D ← DECOMPOSEDIMENSIONS(T, S) {sec. 3.1}
3: for d_i ∈ D do
4:     V_i ← VERBALIZEDSAMPLING(d_i, T) {sec. 3.1}
5: end for
6: G ← ∅
7: while |G| < N do
8:     d_i ∼ Uniform(D), v ∼ Uniform(V_i), y ∼ Uniform(Y)
9:     (x, r) ← GENERATESAMPLE(d_i, v, y, T)
10:    {sec. 3.2}
11:    for t = 0, 1, . . . , R_max do
12:        valid, fb ← DEBATEVALIDATION(x, y, r)
13:        {sec 3.3}
14:        if valid then
15:            G ← G ∪ {(x, y, r)}
16:            break
17:        end if
18:        (x, r) ← REFINE(x, y, r, fb) {sec 3.4}
19:    end for
20: end while
21: return G
```

## Why it matters

This is relevant to AI Research OS because it connects several current themes: custom safety policies, LLM-as-judge limitations, synthetic training data, debate-style verification, and small specialized models replacing expensive runtime judging. The practical implication is strong: for high-volume agent or product deployments, a small task-specific guardrail classifier may be cheaper, faster, and more consistent than repeatedly prompting a frontier model to judge policy compliance.

For agentic systems, BARRED also suggests a reusable pattern: use frontier models at training-time to generate and debate data, then distill the resulting boundary knowledge into cheaper runtime components.

## Raw extracted notes

The PDF extraction identified the paper as:

> BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate

Authors: Arnon Mazza and Elad Levi, Plurai Inc.

The abstract states that deploying guardrails for custom policies remains challenging because generic safety models fail to capture task-specific requirements, while prompting LLMs suffers from inconsistent boundary-case performance and high inference costs. Training custom classifiers can achieve both accuracy and efficiency, but demands substantial labeled data that is costly to obtain. BARRED addresses this by generating faithful and diverse synthetic training data from only a task description and a small set of unlabeled examples.

The extracted method description emphasizes:

- **Dimension decomposition:** given task description `T` and seed examples `S = {x1, x2, ..., xk}`, BARRED identifies task-relevant dimensions `D = {d1, d2, ..., dm}`.
- **Verbalized sampling:** for each dimension, it generates possible values `V_i = {v_i,1, v_i,2, ..., v_i,n_i}` to cover the task space and reduce synthetic-data mode collapse.
- **Boundary-challenging generation:** samples are generated near policy decision boundaries, not only obvious positive/negative cases.
- **Debate validation:** multi-agent debate validates whether generated samples and labels are faithful to the policy.
- **Refinement loop:** rejected samples are revised using debate feedback and revalidated.

The paper claims that small language models fine-tuned on BARRED synthetic data consistently outperform state-of-the-art proprietary LLMs, reasoning models, and dedicated guardrail models on several custom policy tasks.
