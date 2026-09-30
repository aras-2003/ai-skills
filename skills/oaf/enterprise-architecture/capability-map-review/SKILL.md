---
name: capability-map-review
description: >
  Assess whether a business capability map is coherent, decision-useful and properly owned, including level consistency, overlap, gaps and linkage to strategy. Use to review capability maps, not to infer detailed processes from names alone.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: fast
---

# Capability Map Review

## Purpose
Make a capability map useful for decisions rather than decorative taxonomy.

## Procedure
1. Check level consistency and naming as stable business abilities.
2. Detect overlap, process-like entries, organisation-unit labels and missing capabilities.
3. Review ownership and evidence of strategic importance.
4. Test links to strategy, applications, investments, risks or performance where available.
5. Identify which defects materially reduce decision usefulness.
6. Return prioritized corrections.

## Decision rules
- Capabilities describe what the organisation can do, not who does it or how the process flows.
- Do not demand perfect taxonomy if the map already supports the target decision.

## Output contract
Finding | affected capability | severity | reason | recommended correction.
Then: overall usability for the stated decision.

## Model guidance
Default: **fast**. Escalate if capability boundaries require complex domain interpretation.

## Quality checks
- [ ] Levels consistent.
- [ ] Process/org-unit contamination checked.
- [ ] Review tied to decision use.

