# Runtime evaluation protocol

## Goal

Test skills and workflows in the actual runtime without leaking evaluator expectations into the executor.

Static CI proves repository/package integrity. Runtime evidence proves behavior.

## Isolation boundary

Every runtime case registered in `evals/runtime-fixtures.yaml` has:
- a stable case ID;
- an execution mode: `explicit` or `natural-routing`;
- an executor-only `.input.md`;
- an evaluator-only `.rubric.yaml`.

The executor may receive the input, the intended runtime catalog, tools and ordinary project context required by the case. It must not receive the rubric, expected routing, PASS/FAIL criteria, expected answer or evaluator notes.

The Lab packager copies only executor inputs into `references/evals/`. Run:

```bash
python scripts/eval/validate_isolation.py --artifact plugins/arek-ai-skills-lab
```

to check the registry and built artifact.

## Evidence receipts

Narrative validation summaries are historical context, not evidence receipts for a changed component version.

A runtime receipt records:
- case ID plus input/rubric digests;
- component version/content digest and source revision;
- exact provider/model/reasoning settings;
- available catalog and prompt;
- actual output and relevant tool/resource trace;
- reviewer and assisted/unassisted state;
- explicit status.

`NOT_RUN` is required when runtime/model access is unavailable. An assisted run cannot be recorded as PASS.

Use:

```bash
python scripts/eval/receipt.py create ...
python scripts/eval/receipt.py validate evals/results/<record>.json
```

Provider adapters are deliberately separate from this minimum harness.

## Evaluation modes

### Explicit behavior

The executor is explicitly asked to use a named skill/workflow. This tests procedure adherence, evidence discipline, stop conditions and output contract. It does not prove natural routing.

### Natural routing

The user intent does not name a skill. The recorded runtime catalog is part of the receipt. This mode tests capability selection separately from task quality.

### Real-use evidence

Real work can supplement synthetic evals. Store only safe/redacted inputs or a controlled reference plus digest. Do not commit secrets or private CV/material.

## Evaluation sequence

1. Validate source and package integrity.
2. Validate rubric isolation.
3. Run explicit behavior cases.
4. Run near-miss / missing / conflicting-evidence cases.
5. Run natural-routing cases where routing matters.
6. Evaluate actual output against the evaluator-only rubric.
7. Record the receipt and any regression.
8. Promote only after the required evidence matches the exact component version.

## Current migration status

Critical OAF and Commerce runtime fixtures have been split into executor inputs and evaluator rubrics. Historical PASS/PASS++ summaries remain historical only.

Fresh unassisted runtime execution is pending where no current receipt exists. See `evals/results/runtime-status.yaml`.

## Promotion rule

Do not report runtime PASS merely because:
- static validation passed;
- a previous version passed;
- a narrative summary says PASS;
- the model produced plausible prose.

Promotion requires the evidence policy defined for the component/maturity and no unresolved high-severity failure.
