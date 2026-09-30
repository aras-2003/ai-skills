# OAF / Organisational Architecture Framework

OAF is a practical synthesis for connecting strategy, operating model, decision architecture, enterprise architecture, portfolio/execution and evidence feedback.

It is treated as a **thinking and decision framework**, not a monolithic prompt or a new theory.

Core loop:

```
Direction -> Operating Model -> Decisions -> Architecture -> Portfolio/Execution -> Evidence -> next decision
```

The library decomposes OAF into specialist skills and evidence-gated workflows.

## Domain architecture

### 1. Direction & strategy execution
Core:
- `strategy-to-execution-diagnostic`

Planned/deferred:
- `strategy-traceability-review`
- `strategic-priority-review`
- `outcome-ownership-review`

### 2. Operating model
Production:
- `operating-model-review`
- `global-local-model-review`

Candidate:
- `organizational-interface-review`

Future:
- `organizational-layering-review`
- `span-of-control-review`
- `shared-services-model-review`

### 3. Decision architecture & governance
Production:
- `decision-rights-review`
- `decision-bottleneck-analysis`
- `governance-design`

Future:
- `governance-forum-review`
- `governance-overlap-review`
- `decision-quality-review`

### 4. Enterprise & organisational architecture
Production:
- `architecture-review`
- `capability-map-review`
- `capability-gap-analysis`

Future:
- `architecture-alignment-review`
- `architecture-debt-review`
- `technology-enablement-review`
- `data-capability-review`

### 5. Portfolio & execution
Production:
- `portfolio-prioritization`
- `portfolio-health-review`
- `transformation-blueprint`

Future:
- `investment-prioritization`
- `capacity-funding-review`
- `execution-model-review`
- `delivery-bottleneck-analysis`

### 6. Evidence & adaptation
Production:
- `evidence-loop-review`

Candidate:
- `kpi-quality-review`

Future:
- `performance-review-design`
- `learning-loop-review`
- `adaptive-governance-review`

### 7. Leadership & change enablement
Future — intentionally deferred until core OAF is stable:
- `leadership-model-review`
- `leadership-accountability-review`
- `change-readiness-review`
- `stakeholder-alignment-review`

## Workflows

Production:
- `oaf-health-check` — selective cross-domain diagnosis.
- `oaf-operating-model-redesign` — evidence-gated bounded redesign with option/trade-off testing.
- `oaf-governance-redesign` — decision-led governance redesign with mechanism minimisation.
- `oaf-enterprise-architecture-review` — evidence-gated enterprise architecture review.
- `oaf-transformation-design` — bounded, evidence-gated transformation mobilisation and sequencing.
- `oaf-enterprise-change-review` — selective end-to-end orchestration across OAF domains.

Candidate:
- `oaf-strategy-execution-reset`

## Routing principle

Do not run every OAF skill.

```
symptom/problem
   -> narrow diagnostic skill if possible
   -> specialist evidence
   -> cross-domain synthesis only when needed
   -> design skill/workflow only after diagnosis gate
```

Examples:
- slow/unclear decisions -> `decision-rights-review`
- repeated escalations -> `decision-bottleneck-analysis`
- global/local tension -> `global-local-model-review`
- cross-unit handoff failure -> `organizational-interface-review`
- initiative overload -> `portfolio-health-review` then `portfolio-prioritization` when ready
- reporting without action -> `evidence-loop-review`
- KPI set quality -> `kpi-quality-review`

## Model-class defaults

Validated on Luna:
- `decision-rights-review`
- `portfolio-prioritization`
- `operating-model-review`
- `architecture-review`
- `evidence-loop-review`
- `global-local-model-review`
- `decision-bottleneck-analysis`
- `portfolio-health-review`
- `oaf-health-check`
- `oaf-operating-model-redesign` for bounded redesign
- `governance-design`
- `transformation-blueprint`
- `oaf-governance-redesign`
- `oaf-transformation-design`
- `capability-map-review`
- `capability-gap-analysis`
- `oaf-enterprise-architecture-review`
- `oaf-enterprise-change-review`

Sol comparisons on `oaf-operating-model-redesign` and `oaf-transformation-design` improved framing but did not materially change the decision/plan, so strong remains escalation-only for the validated bounded uses.

Candidate defaults:
- **fast:** `kpi-quality-review`
- **standard:** remaining diagnostic/design candidates
- **strong escalation:** final high-impact target-state selection, contested executive evidence, major multi-country/global-local redesign, transition economics

Wave 3 validated that design skills can remain on the standard model class when they preserve evidence gates, reversibility and stop conditions.

See `docs/MODEL-ROUTING.md`, `evals/oaf/core-validation-2026-09-30.md`, `evals/oaf/wave2/validation-2026-09-30.md`, `evals/oaf/wave3/validation-2026-09-30.md`, `evals/oaf/wave4/validation-2026-09-30.md`, and `evals/oaf/e2e/validation-2026-09-30.md`.

## Boundary principle

OAF skills diagnose and design organisational decision systems. They should not silently become generic strategy, HR, software architecture, PMO or transformation prompts.

The preferred sequence is:

```
evidence -> diagnosis -> design implication -> design choice -> pilot -> evidence loop
```

Not:

```
symptom -> best-practice redesign
```
