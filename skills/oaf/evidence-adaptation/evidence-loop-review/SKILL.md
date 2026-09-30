---
name: evidence-loop-review
description: >
  Review whether organisational KPIs, outcomes, reviews and feedback loops actually inform decisions and adaptation. Use when governance produces reporting but weak learning; do not use as a generic KPI-design task.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Evidence Loop Review

## Purpose
Test whether evidence changes decisions rather than merely producing reports.

## Procedure
1. Identify key decisions and expected outcomes.
2. Map the measures/evidence used before and after decisions.
3. Review data timeliness, ownership, quality and interpretability.
4. Check whether review forums trigger explicit decisions or corrective actions.
5. Identify vanity/activity metrics and missing outcome signals.
6. Recommend the smallest feedback-loop improvements.

## Decision rules
- A KPI without a linked decision or action threshold has limited governance value.
- More metrics are not automatically better.
- Feedback loops need cadence, owner and response mechanism.

## Output contract
Decision/outcome | evidence | owner | cadence | action threshold | observed response | gap | improvement.

## Model guidance
Default: **standard**.

## Quality checks
- [ ] Evidence linked to decisions.
- [ ] Activity vs outcome metrics distinguished.
- [ ] Action mechanism explicit.

