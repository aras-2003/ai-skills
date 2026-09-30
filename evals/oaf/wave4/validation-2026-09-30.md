# OAF Wave 4 Validation — 2026-09-30

## Runtime

Primary runtime: Arek AI Skills Lab.
Primary model: Luna.

Exact packaged fixtures under `references/evals/` were used.

## Results

| Component | Result | Disposition |
|---|---|---|
| capability-map-review | PASS+ on Luna | promote |
| capability-gap-analysis | PASS++ on Luna | promote |
| oaf-enterprise-architecture-review | PASS++ on Luna | promote |
| oaf-enterprise-architecture-review stop condition | PASS++ on Luna | promote |

## Capability map review

Validated:
- review anchored to the stated investment/architecture decision use;
- organisation/process/system contamination detected;
- ambiguous entries were validated rather than automatically rejected;
- no maturity/performance/owner invention;
- many-to-many application links were not treated as automatic duplication;
- targeted corrections preferred over rebuilding the map;
- result correctly classified as fit with corrections.

Guardrail:
- duplicate-investment analysis depends on relationship evidence, not taxonomy cleanliness alone.

## Capability gap analysis

Validated:
- started from the 9-to-4-month time-to-market outcome;
- isolated a small material capability set;
- separated capacity, maturity, integration, data, governance and ownership gaps;
- central queues/capacity overload were not treated as proof of low maturity or platform failure;
- workarounds were treated as diagnostic evidence;
- no unsupported identity-platform scalability or replacement conclusion;
- intervention hypotheses stayed at capability-dimension level rather than becoming a project list.

Regression:
- queue/overload != immature capability != broken platform;
- workaround != architecture defect without evidence.

## Enterprise architecture review

Validated:
- reframed consolidation into an outcome/capability/architecture decision;
- separated operating-model, funding, capacity and information issues from evidenced technology-estate issues;
- technical scalability, debt, obsolescence and migration feasibility remained unknown;
- duplication was treated as a hypothesis to validate;
- global standards were not equated with one global implementation;
- compared bounded options: improve shared service/boundaries, federated shared core, selective consolidation;
- funding and constrained data-team capacity were treated as architecture feasibility constraints;
- retirement required usage, dependency, migration and service-continuity evidence;
- next gate was a bounded pilot/evidence decision, not a final migration roadmap.

Guardrail:
- a working architecture direction is provisional, not a final target architecture.

## Stop condition

Validated:
- stopped before target-state design and retirement recommendations;
- "too many systems" was treated as perceived complexity, not proven duplication;
- no platform was labelled redundant, obsolete or safe to retire;
- minimum evidence pack and bounded decision framing were provided instead;
- no target-state diagram was generated without evidence.

Regression:
- "too many systems" != proven duplication != retirement candidate;
- architecture request + insufficient estate evidence -> stop -> evidence -> bounded decision -> review/pilot.

## Model routing

Luna is adequate for the tested:
- decision-use capability-map review;
- evidence-disciplined capability-gap analysis;
- bounded enterprise-architecture option review;
- strict enterprise-architecture stop conditions.

Strong/Sol remains escalation-only for final target-architecture selection, highly coupled platform/data redesign, irreversible consolidation/retirement, material transition economics or contested global/local trade-offs.

## Promotion

Promote:
- `capability-map-review`
- `capability-gap-analysis`
- `oaf-enterprise-architecture-review`
