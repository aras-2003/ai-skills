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

| Skill | Default class |
|---|---|
| strategy-to-execution-diagnostic | standard |
| operating-model-review | standard |
| decision-rights-review | standard |
| governance-design | standard |
| architecture-review | standard |
| capability-map-review | fast |
| portfolio-prioritization | fast + deterministic calculation |
| transformation-blueprint | standard |
| evidence-loop-review | standard |

The OAF Health Check workflow should prefer selective routing over escalating model class. Use strong only when the cross-domain design problem is genuinely novel, contested or high-impact.
