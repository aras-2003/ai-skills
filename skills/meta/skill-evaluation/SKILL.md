---
name: skill-evaluation
description: >
  Evaluate an Agent Skill's routing and behavior using predeclared representative cases, a no-skill baseline or accepted prior version, and evidence-based regression analysis. Use after validation and test design, before production promotion, and after material behavior changes.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.3.0"
  maturity: draft
  risk: medium
  last_reviewed: 2026-10-05
---

# Skill Evaluation

## Purpose and decision

Determine whether the candidate reliably improves the intended task without introducing unacceptable regressions. Evaluation is evidence about a defined scope and runtime; it is not proof of general model quality or authorization to release.

Return one disposition:
- **PASS** — predeclared quality and safety gates are met, with no blocking regression;
- **ITERATE** — useful signal exists, but a remediable gap or insufficient evidence remains;
- **REJECT** — value is not demonstrated or a material risk/regression outweighs it.

Do not change the success criteria after seeing candidate results merely to obtain a pass.

## Preconditions

Before running:
- identify the candidate version and the currently accepted comparator;
- require validation with no unresolved blocking errors;
- use representative, versioned routing and behavioral cases with explicit expected outcomes;
- state the evaluation question, supported runtime/model/tool context, and decision threshold;
- record material differences between compared variants.

If any precondition is missing, return the exact gap and the smallest action needed to proceed. Do not present an informal spot check as a complete evaluation.

## Case execution state and receipts

Assign each case one evidence state independently of the overall disposition:
- `NOT_RUN`: execution has not started; queued jobs without an assigned runner or steps remain NOT_RUN.
- `BLOCKED` / `NOT TESTABLE`: a required runtime, tool, permission or fixture is unavailable before the criterion can be observed.
- `PASS`: the case ran and its predeclared observable assertions are supported by evidence.
- `FAIL`: the case ran and violated a material assertion, including claiming a live check or external action that the trace does not show.

A textual description of intended tool use is not proof. When the criterion requires a live source check, retain the tool trace, URL/resource, check time and observed status. Do not count a required NOT_RUN or BLOCKED case as a conditional PASS; the overall disposition cannot be PASS while required evidence is unobserved.

## Choose the comparison

- **New capability:** compare with a no-skill baseline when the baseline can attempt the same task safely. If it cannot, state why and evaluate against the approved contract instead.
- **Behavior change:** compare with the last accepted version using equivalent inputs and equivalent runtime conditions.
- **Routing change:** evaluate positive, near-miss, and competing-skill prompts separately from task quality.
- **High-impact or subjective output:** use blind review where practical; remove version cues and randomize presentation order.
- **Deterministic scripts or validators:** prefer direct tests of their inputs, outputs, and failure behavior over model-judged prose.

## Procedure

1. **Freeze the plan.** List cases, comparator, rubric, sample/repetition plan, thresholds and safety stops before observing results.
2. **Check readiness.** Verify candidate identity, validation result, cases, evaluator instructions, tool availability and any required fixtures. Do not silently substitute missing tools or fixtures.
3. **Run routing separately.** Record whether each prompt should trigger the candidate, which capability should win when skills compete, and the observed route.
4. **Run paired behavioral cases.** Give each variant equivalent input, context, permissions, tools and resource limits. Keep the rubric and evaluator criteria identical.
5. **Repeat stochastic cases.** Use enough independent runs to expose material variance for the decision at hand. Report run count and dispersion; do not imply statistical certainty from a small sample.
6. **Score observable outcomes.** Apply predeclared, anchored criteria to the result and its evidence. Separate factual correctness, task completion, contract adherence, tool/action discipline, safety and usability. Mark unobservable or unverified criteria as such.
7. **Compare and inspect regressions.** Report per-case outcome, severity, candidate-versus-comparator delta, variance and evidence. A formatting improvement does not offset a safety or correctness regression without explicit risk acceptance by the proper owner.
8. **Diagnose failures.** Classify likely cause as routing, contract, procedure, reference, tool/runtime, evaluator/rubric, data/fixture or stochastic variance. Label hypotheses as hypotheses.
9. **Preserve learning.** Convert realistic new failures into regression cases through skill-test-design; do not weaken a valid case to obtain a pass.
10. **Decide and report.** Apply the frozen thresholds. State scope, evidence, limitations, unresolved regressions and the smallest next action. PASS does not promote or publish the skill.

## Evaluation criteria

Select only criteria relevant to the skill, but cover its contract:
- trigger and non-trigger correctness;
- completion and output-contract adherence;
- factual and evidence discipline;
- missing, ambiguous, stale or conflicting input handling;
- safety boundaries and external-action discipline;
- tool failure, partial-result and recovery behavior;
- usefulness relative to the comparator;
- material regressions and run-to-run consistency.

Do not score hidden chain-of-thought, exact phrasing, or stylistic preference as a proxy for task quality. Do not treat evaluator agreement, model confidence, or one attractive example as proof.

## Result format

Return a compact report:
- evaluation question, candidate/comparator and runtime;
- plan and case matrix (case, expected route, observed route, evidence state, scores, evidence receipt, severity, delta);
- aggregate result with denominator, repetitions and variation where applicable;
- improvements and regressions, with root-cause hypotheses clearly labeled;
- unsupported/unobserved criteria and material limitations, with required NOT_RUN/BLOCKED cases kept separate from executed results;
- disposition: PASS / ITERATE / REJECT;
- smallest next changes and the exact cases to rerun.

A new skill is not justified merely because it produces a good answer; it should add consistent, decision-relevant value relative to a fair baseline for its intended task.
