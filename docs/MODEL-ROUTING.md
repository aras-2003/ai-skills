# Model-class routing

## Goal

Use the cheapest model class that can execute a skill reliably, and escalate only when task complexity or risk justifies it.

Model guidance is advisory. It describes reasoning demand, not a hard dependency on a specific vendor/model name.

## Classes

### fast
Use for:
- retrieval and filtering;
- freshness/validity checks;
- structured extraction;
- tracker/status updates;
- deterministic or narrowly bounded tasks.

Escalate when evidence conflicts materially or interpretation changes a high-impact decision.

### standard
Use for:
- evidence-backed synthesis;
- CV gap analysis/tailoring;
- interview preparation;
- decision briefs with moderate ambiguity;
- most repeatable executive reasoning tasks.

Escalate when the task is novel, cross-domain, politically/organizationally complex, or has conflicting evidence and high impact.

### strong
Use selectively for:
- genuinely novel strategy/design problems;
- high-ambiguity cross-domain decisions;
- complex architecture/operating-model trade-offs;
- adversarial review where subtle reasoning matters.

Do not default to strong merely because the output is important.

## Skill metadata

Skills may include:

```yaml
metadata:
  execution:
    default_model_class: fast
```

A skill can also describe escalation conditions in its `Model guidance` section.

## Principle

**Procedure first, model second.**

A mature skill should reduce the amount of method invention required from the model. If the procedure, evidence contract and quality gates are explicit, many tasks can run reliably on a cheaper model class.

## Current Career defaults

| Skill | Default class |
|---|---|
| job-discovery | fast |
| job-validity-check | fast |
| company-context-research | standard |
| executive-role-evaluator | standard |
| cv-gap-analysis | standard |
| cv-tailoring | standard |
| interview-brief | standard |
| process-update | fast |

These defaults should be validated empirically with behavioral evals before they are treated as cost/quality commitments.


## OAF defaults

Validated on Luna for structured diagnosis:
- `decision-rights-review` — standard
- `portfolio-prioritization` — fast/standard boundary; Luna passed the tested evidence-readiness case
- `operating-model-review` — standard
- `architecture-review` — standard
- `evidence-loop-review` — standard
- `oaf-health-check` — standard workflow synthesis

Validated on Luna in Wave 2:
- `global-local-model-review` — standard
- `decision-bottleneck-analysis` — standard
- `portfolio-health-review` — standard
- `oaf-operating-model-redesign` — standard for bounded redesign, option generation, trade-off analysis and pilot design

Sol comparison for `oaf-operating-model-redesign`:
- improved alternative framing and selection discipline;
- did not materially change the recommended direction;
- keep as escalation, not default.

Validated on Luna in Wave 3:
- `governance-design` — standard for bounded decision-led governance design
- `transformation-blueprint` — standard for bounded blueprints and strict stop-condition enforcement
- `oaf-governance-redesign` — standard for bounded governance redesign
- `oaf-transformation-design` — standard for bounded 90-day transformation design

Sol comparison for `oaf-transformation-design`:
- slightly stronger narrative/selection framing;
- no material change in sequence, risk posture or recommended plan;
- strong remains escalation-only.

Validated on Luna in Wave 4:
- `capability-map-review` — fast for decision-use map review and contamination detection
- `capability-gap-analysis` — standard for outcome-led gap analysis and capacity-vs-maturity separation
- `oaf-enterprise-architecture-review` — standard for bounded evidence-disciplined EA review and stop-condition enforcement

Candidate defaults:
- `kpi-quality-review` — fast
- `organizational-interface-review` — standard
- `strategy-to-execution-diagnostic` — standard

Use strong for final high-impact target-state selection, materially conflicting executive evidence, major multi-country/global-local redesign, material transition economics, politically contested authority/funding choices, or novel enterprise transformation design.

A successful Luna result validates the tested use case, not every possible use of the skill. See `evals/oaf/core-validation-2026-09-30.md` and `evals/oaf/wave2/validation-2026-09-30.md`.

## Wave 3 design-layer rule

Governance and transformation design have a higher evidence bar than diagnosis.

Default to standard/Luna only when:
- diagnosis and target direction are already sufficiently evidenced;
- the task is bounded;
- ownership/authority are known or explicitly marked unresolved;
- the output remains reversible or evidence-gated.

Escalate to strong/Sol for:
- final high-impact authority/governance selection;
- enterprise-wide multi-year sequencing;
- material transition economics;
- politically contested mandates;
- unresolved target-state choices that could change the plan.

See `docs/OAF-WAVE3-EVALS.md` and `evals/oaf/wave3/validation-2026-09-30.md`.


## Wave 4 enterprise-architecture rule

Use fast/standard models only when architecture conclusions remain evidence-backed and reversible.

Escalate to strong when the task requires:
- final target-architecture selection across tightly coupled domains;
- major platform/data boundary redesign;
- irreversible consolidation/retirement decisions;
- material transition economics or contested global/local architecture trade-offs.

Do not escalate merely because the user asks for an architecture diagram. See `docs/OAF-WAVE4-EVALS.md` and `evals/oaf/wave4/validation-2026-09-30.md`.


## End-to-end OAF orchestration

Candidate:
- `oaf-enterprise-change-review` — standard; runtime validation pending.

Use standard only when specialist evidence can be reused and the resulting design remains bounded and reversible.

Escalate to strong for final irreversible cross-enterprise target-state selection, materially conflicting executive evidence, tightly coupled operating-model/architecture trade-offs, or material transition economics.

See `docs/OAF-END-TO-END-EVAL.md`.
