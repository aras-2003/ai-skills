# OAF Core Validation — 2026-09-30

## Environment

- Runtime: ChatGPT Work
- Model class: Luna
- Case: `evals/oaf-health-check/case-001-enterprise-it.md`
- Evaluation style: explicit skill invocation + workflow synthesis

## Result summary

| Component | Result | Notes |
|---|---|---|
| oaf-health-check initial diagnosis | PASS | Selected relevant domains, deferred design skills, preserved uncertainty |
| decision-rights-review | PASS | Deepened formal/actual ownership, escalation and authority/resource diagnosis |
| portfolio-prioritization | PASS | Refused false scoring, separated mandatory work, capacity and dependencies |
| operating-model-review | PASS | Preserved centralisation/autonomy trade-off and interface diagnosis |
| architecture-review | PASS | Separated organisational decision-system causes from unproven technology defects |
| evidence-loop-review | PASS | Diagnosed reporting-to-action weakness without generating a KPI catalogue |
| oaf-health-check synthesis | PASS+ | Updated confidence selectively and converged on an integrated evidence exercise |

## Validated behavior

The tested core supports:
- structured diagnosis;
- specialist review;
- evidence/inference separation;
- diagnose-before-design gating;
- cross-domain synthesis;
- explicit unknowns;
- bounded next diagnostic action.

## Model-class evidence

Luna was adequate for the tested structured-diagnosis cases.

This does **not** validate Luna for:
- target operating-model design;
- target-state architecture design;
- enterprise-wide transformation design;
- highly contested executive evidence;
- high-impact global/local redesign.

## Regression expectations captured from tests

### Decision rights
- Escalation is not a decision mechanism unless destination, trigger, timeframe and authority are explicit.
- Prioritisation authority without funding/capacity authority may be nominal.
- Do not prescribe a new owner when evidence only proves the current owner is unknown.

### Portfolio
- Do not score when initiative evidence is not comparable.
- Mandatory work remains outside ordinary value ranking.
- Capacity and dependencies may override nominal rank.
- Criteria examples are not universal OAF defaults.

### Operating model
- Local optimisation can be rational while enterprise outcomes remain weak.
- Forums should not compensate for unclear ownership.
- Centralisation versus autonomy is a design trade-off, not a default answer.

### Architecture
- Organisational symptoms are not evidence of technology-estate defects.
- Architecture responsibility without investment/delivery authority is primarily a governance issue.
- Target architecture must wait for adequate estate evidence.

### Evidence loops
- Reporting-to-action failure does not prove KPI quality is the root cause.
- Evidence requires an owner, cadence, threshold, decision authority and response mechanism.

## Promotion decision

Promote to production:
- `decision-rights-review`
- `portfolio-prioritization`
- `operating-model-review`
- `architecture-review`
- `evidence-loop-review`
- runtime workflow entrypoint `oaf-health-check`

Keep candidate:
- `strategy-to-execution-diagnostic`
- `capability-map-review`
- `governance-design`
- `transformation-blueprint`
- all wave-2 additions until independent runtime evaluation.
