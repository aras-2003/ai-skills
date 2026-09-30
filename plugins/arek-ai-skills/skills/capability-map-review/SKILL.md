---
name: capability-map-review
description: >
  Assess whether a business capability map is coherent and decision-useful, including level consistency, overlap, gaps, ownership and linkage to strategy, investments, applications, risks or performance. Use to improve a map for a defined decision; do not infer detailed processes or technology defects from capability names alone.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.0.0"
  maturity: production
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: fast
    validated_models:
      luna:
        status: pass
        validated_on: 2026-09-30
        validated_use:
          - decision-use capability map review
          - taxonomy contamination detection
          - fit-for-purpose assessment
---

# Capability Map Review

## Purpose
Make a capability map useful for decisions rather than decorative taxonomy.

## Preconditions
Require:
- a stated decision/use case for the map;
- the relevant capability map or representative extract;
- enough context to distinguish capability names from org units, processes and systems.

If the decision use is unknown, first clarify or infer the narrowest plausible decision context.

## Procedure
1. State the decision the map must support.
2. Check level consistency and whether entries represent stable business abilities.
3. Detect:
   - process/activity wording;
   - organisation-unit labels;
   - application/system labels;
   - duplicate or overlapping capabilities;
   - material gaps;
   - inconsistent granularity.
4. Review ownership only where evidence exists; do not invent owners.
5. Test links to strategy, outcomes, investments, applications, risks and performance where available.
6. Distinguish taxonomy defects from missing evidence/linkage.
7. Prioritise only defects that materially reduce usefulness for the stated decision.
8. State whether the map is fit for the decision now, fit with corrections, or not yet fit.

## Decision rules
- Capabilities describe what the organisation can do, not who does it, the process flow or the system name.
- Do not demand perfect taxonomy if the map already supports the target decision.
- A missing owner is an evidence/operating-model issue, not proof the capability itself is invalid.
- Do not infer maturity, performance or technology quality from capability labels alone.
- Avoid re-leveling the entire map when a local correction is sufficient.
- Prefer decision usefulness over taxonomy purity.
- Treat many-to-many application mappings as relationships to understand, not automatic duplication.
- If duplicate-investment analysis depends on missing application/investment relationships, state that limitation explicitly.

## Output contract
Finding | affected capability | defect type | severity for stated decision | evidence | recommended correction.

Then:
- fit-for-purpose assessment;
- highest-value corrections;
- missing evidence/linkages;
- optional next skill if a true capability gap or architecture issue is discovered.

## Model guidance
Default: **fast** for structured map review.
Escalate to standard when capability boundaries require complex domain interpretation or materially affect operating-model/investment choices.

## Quality checks
- [ ] Decision use explicit.
- [ ] Level consistency checked.
- [ ] Process/org/system contamination checked.
- [ ] No invented maturity or owners.
- [ ] Corrections prioritised by decision impact.
