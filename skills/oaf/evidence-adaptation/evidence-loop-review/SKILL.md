---
name: evidence-loop-review
description: >
  Review whether organisational KPIs, outcomes, reviews and feedback loops actually inform decisions and adaptation. Use when governance produces reporting but weak learning; do not use as a generic KPI-design task.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.0.0"
  maturity: production
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
    validated_models:
      luna:
        status: pass
        validated_on: 2026-09-30
        validated_use:
          - reporting-to-action diagnosis
          - specialist review
---

# Evidence Loop Review

## Purpose
Test whether evidence changes decisions rather than merely producing reports.

## Procedure
1. Identify the key decisions and expected outcomes.
2. Map the measures/evidence used before and after those decisions.
3. Review metric quality, timeliness, ownership and interpretability.
4. Review cadence against the decision and outcome time horizon.
5. Check whether action thresholds are explicit.
6. Check whether the person reviewing evidence has authority to change priorities, funding, scope or resources.
7. Distinguish activity metrics from outcome evidence.
8. Trace whether review forums trigger explicit decisions and corrective actions.
9. Identify the smallest sample of recent review cycles needed to isolate the dominant failure mode.

## Decision rules
- A KPI without a linked decision or action threshold has limited governance value.
- More metrics are not automatically better.
- Activity metrics are not inherently invalid; they are weak when used as substitutes for outcomes.
- Feedback loops need evidence, cadence, owner, decision authority and response mechanism.
- Do not assume metric quality is the root cause when the case only proves reporting-to-action failure.
- Do not create a generic KPI catalogue unless explicitly requested.

## Output contract
Decision/outcome | evidence | owner | cadence | action threshold | observed response | gap | smallest improvement.

Then:
- evidence vs inference;
- activity vs outcome evidence;
- failure modes to test: metric quality / ownership / cadence / interpretation / action mechanism;
- smallest next diagnostic step.

## Model guidance
Default: **standard**.
Validated on Luna for reporting-to-action diagnosis.
Escalate where evidence quality is highly contested or the task becomes enterprise performance-system design.

## Quality checks
- [ ] Evidence linked to decisions.
- [ ] Activity vs outcome metrics distinguished.
- [ ] Action mechanism explicit.
- [ ] Metric quality not assumed without evidence.
- [ ] No generic KPI catalogue generated.
