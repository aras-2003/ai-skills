# OAF End-to-End Validation — 2026-09-30

## Runtime

Primary model: Luna.

Fixture:
- `evals/oaf/e2e/case-001-enterprise-change.md`

## Result

`oaf-enterprise-change-review`: PASS++ on Luna.

## Validated routing

Selected:
- strategy-to-execution-diagnostic
- operating-model-review
- global-local-model-review
- decision-rights-review
- decision-bottleneck-analysis
- portfolio-health-review
- oaf-enterprise-architecture-review
- evidence-loop-review
- oaf-operating-model-redesign
- oaf-governance-redesign
- oaf-transformation-design

Correctly omitted:
- capability-map-review
- capability-gap-analysis
- portfolio-prioritization
- kpi-quality-review

The run demonstrated minimum-sufficient routing rather than full-catalog execution.

## Validated synthesis

The runtime built one cross-domain causal model rather than independent domain summaries.

Key reinforcing loop:
- local funding/accountability -> fragmented shared-capability demand;
- constrained shared teams -> queues;
- slow decision/exception paths -> bypasses/workarounds;
- workarounds -> more duplication/integration complexity;
- weak evidence-to-decision feedback -> overloaded demand persists.

Technology defects remained unproven.

## Validated design discipline

The run:
- separated design readiness by domain;
- treated the federated shared-capability direction as provisional;
- preserved unresolved platform consolidation, retirement, scalability, technical-debt and migration questions;
- avoided initiative ranking because comparable evidence was missing;
- avoided default centralisation;
- avoided new governance forums as the default answer;
- reused prior diagnosis in downstream design;
- produced a bounded 30–90 day mobilisation.

## Validated stop discipline

The run did not:
- create a fixed multi-year roadmap;
- recommend platform retirement;
- claim a final target architecture;
- invent named owners;
- treat reporting volume as evidence of an effective evidence loop.

## Regression guardrails

- successful shared-capability or operating-model pilot != evidence for platform consolidation;
- pilot capability owner / owner-to-confirm != permanent enterprise capability owner;
- portfolio overload without comparable initiative evidence -> health/capacity diagnosis before ranking;
- architecture duplication != consolidation;
- global standards != central delivery or single implementation;
- governance redesign != new forums;
- transformation design != multi-year commitment.

## Model routing

Luna is adequate for the tested end-to-end orchestration case.

Use strong/Sol only when:
- final irreversible cross-enterprise target-state selection is required;
- material executive evidence conflicts across domains;
- operating-model and architecture choices are tightly coupled and hard to reverse;
- transition economics materially determine the choice;
- the decision commits major authority, funding or platform-retirement changes.

## Promotion

Promote `oaf-enterprise-change-review` to production 1.0.0.

This validates the tested orchestration pattern, not all enterprise transformation cases.
