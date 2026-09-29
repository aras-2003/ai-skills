---
name: skill-evaluation
description: >
  Evaluate a candidate Agent Skill against representative eval cases, a no-skill baseline or previous version, and diagnose routing or behavioral regressions. Use after validation and test design, before production promotion, and after material behavior changes.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: draft
  risk: medium
  last_reviewed: 2026-09-29
---

# Skill Evaluation

## Preconditions

Require:
- candidate skill;
- validation result without blockers;
- representative eval cases.

## Evaluation modes

### New skill
Compare candidate with a no-skill baseline when useful to prove the skill adds value.

### Existing skill change
Compare candidate with the current accepted version.

### Subjective/high-value output
When feasible, use blind A/B review so the evaluator does not know which version produced which output.

## Procedure

1. Run routing tests separately from behavior tests.
2. For each behavioral case, preserve equivalent inputs across variants.
3. Evaluate only observable behavior and output.
4. Record:
   - pass/fail;
   - severity;
   - failure category;
   - whether candidate improved, regressed or is neutral.
5. Diagnose cause:
   - description/routing;
   - procedure;
   - conflicting instruction;
   - missing reference;
   - script/tool issue;
   - bad test.
6. Do not weaken a valid test to obtain a pass.
7. Add newly discovered realistic failures to the regression suite.

## Evaluation criteria

At minimum:
- trigger correctness;
- completion of intended task;
- factual/evidence discipline;
- handling of missing information;
- output contract adherence;
- tool/action discipline;
- context efficiency;
- absence of new severe regressions.

## Result

Return:
- overall disposition: PASS / ITERATE / REJECT;
- case matrix;
- regressions;
- improvements;
- root-cause hypotheses;
- smallest next changes;
- tests to rerun.

A new skill is not justified merely because it produces a good answer; it should add consistent value relative to the baseline for the intended task.
