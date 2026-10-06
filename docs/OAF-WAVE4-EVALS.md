# OAF Wave 4 — Enterprise Architecture Runtime Evaluation

## Goal

Validate the enterprise-architecture layer without letting architecture become a technology-only redesign exercise.

Wave 4 tests whether the system can:
- keep business/capability outcomes primary;
- separate operating-model, funding, data/information and technology-estate issues;
- resist unsupported platform-retirement/consolidation recommendations;
- use capability analysis only when it materially improves the decision.

## Runtime fixture location

In Skills Factory Lab, canonical fixtures are packaged into each selected skill/workflow under `references/evals/`.

## Test order

### 1. Capability map review

Fixture:
`references/evals/case-capability-map-001.md`

Prompt:

> Use the `capability-map-review` skill on the exact lab fixture `references/evals/case-capability-map-001.md`. Review the map for the stated investment and architecture decisions. Detect capability/process/org/system contamination, but do not optimise taxonomy for its own sake. Do not invent maturity or owners. End with whether the map is fit now, fit with corrections, or not fit for the stated decisions.

Pass focus:
- decision use first;
- contamination detected;
- no invented maturity;
- targeted corrections, not full remap;
- fit-for-purpose judgment.

### 2. Capability gap analysis

Fixture:
`references/evals/case-capability-gap-001.md`

Prompt:

> Use the `capability-gap-analysis` skill on the exact lab fixture `references/evals/case-capability-gap-001.md`. Start from the 4-month time-to-market outcome. Identify only the material capabilities and separate capacity, maturity, integration, data, governance and ownership gaps. Treat workarounds as evidence, not automatic technology defects. Do not recommend platform replacement without evidence.

Pass focus:
- small material capability set;
- capacity vs maturity separated;
- no unsupported identity-platform defect;
- intervention hypotheses, not project list.

### 3. Enterprise architecture review

Fixture:
`references/evals/case-enterprise-architecture-review-001.md`

Prompt:

> Use the `oaf-enterprise-architecture-review` workflow on the exact lab fixture `references/evals/case-enterprise-architecture-review-001.md`. Reframe the platform-consolidation request as an evidence-backed architecture decision. Trace outcomes to capabilities, separate operating-model/funding/capacity issues from technology-estate issues, keep unproven technical defects unknown, compare bounded architecture options, and state the minimum evidence needed before final consolidation or retirement decisions.

Pass focus:
- consolidation not assumed;
- global standards != one implementation;
- architecture authority vs funding/capacity issue surfaced;
- data-team capacity included;
- bounded options;
- evidence gate before retirement/migration.

### 4. Enterprise architecture stop condition

Fixture:
`references/evals/case-enterprise-architecture-stop-001.md`

Prompt:

> Use the `oaf-enterprise-architecture-review` workflow on the exact stop-condition fixture `references/evals/case-enterprise-architecture-stop-001.md`. The user asks for the final target architecture and platform retirements. Apply the workflow preconditions and stop conditions strictly.

Pass focus:
- no target-state diagram;
- no invented estate defects;
- no retirement candidates;
- minimum evidence pack and decision framing instead.

## Model comparison

Run Luna first.

Use Sol only if Luna:
- makes a consequential target-architecture selection;
- recommends platform retirement/consolidation despite material ambiguity;
- must resolve highly coupled data/platform/operating-model trade-offs.

Compare decisions, evidence discipline and trade-offs—not prose polish.

## Promotion threshold

### Specialist skills
Require:
- representative positive case PASS;
- no invented maturity/technology defects;
- explicit decision use/outcome traceability;
- intended default model adequate.

### Workflow
Require:
- positive case PASS;
- stop-condition PASS;
- organisational/investment/technology problem classes separated;
- bounded options rather than default consolidation;
- explicit evidence gate before irreversible architecture decisions.
