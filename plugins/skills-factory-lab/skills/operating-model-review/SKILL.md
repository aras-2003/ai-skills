---
name: operating-model-review
description: 'Review an operating model for role clarity, interfaces, accountability,
  autonomy, coordination and authority/resource alignment. Use as the lead diagnosis
  when symptoms span cross-unit handoffs plus unclear accountability or capacity/funding
  authority and the failure has not yet been isolated to one decision class. Do not
  reduce the review to an org chart.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.1.0
  maturity: production
  risk: medium
  last_reviewed: '2026-09-30'
---

# Operating Model Review

## Purpose
Assess whether the organisation's division of responsibility, cross-unit interfaces and authority/resource model support its strategic goals.

When a problem mixes handoffs, accountability and effective authority/capacity across units, lead with this skill to classify the operating-model failure before routing into a decision-specific specialist.

## Procedure
1. Identify major value streams/functions/business units and their mandates.
2. Map global/central/local ownership and decision boundaries.
3. Review interfaces where work, resources or decisions cross units.
4. Identify duplication, gaps, excessive handoffs, unclear accountability and over-centralisation/fragmentation.
5. Test whether accountability matches authority, funding, capacity and dependency control.
6. Test whether governance mechanisms are solving decisions or compensating for unclear interfaces.
7. Separate evidence from structural inference.
8. State design implications, but do not select a target operating model until the critical interfaces and authority/resource patterns are evidenced.

## Decision rules
- Structure alone is not the operating model.
- Local optimisation can be rational while enterprise outcomes remain weak.
- Centralise where scale, consistency, interoperability or risk materially matter.
- Localise where context, speed and domain expertise create value.
- Accountability must match authority and resources.
- Mixed interface/accountability/capacity symptoms are an operating-model diagnosis until evidence isolates a specific decision-rights or decision-latency problem.
- Once a specific material decision class is identified, route the relevant slice to `decision-rights-review` or `decision-bottleneck-analysis` rather than duplicating their detailed procedure.
- Forums should not compensate for unclear ownership.
- Centralisation versus autonomy is a trade-off to diagnose, not a default answer.

## Output contract
- current operating-model summary;
- evidence vs inference;
- key interfaces;
- top structural misfits;
- authority-accountability-resource alignment;
- design implications, clearly labelled as implications rather than recommendations;
- what must be validated before target operating-model design;
- next diagnostic action.

## Model guidance
Default: **standard**.
Validated on Luna for structured operating-model diagnosis.
Escalate for multi-country/global-local redesign, politically contested autonomy choices, or target operating-model design.

## Quality checks
- [ ] Global/local split explicit.
- [ ] Interfaces reviewed.
- [ ] Authority/accountability/resources checked together.
- [ ] Centralisation/autonomy treated as a trade-off.
- [ ] Diagnosis does not jump to an org-chart redesign.
