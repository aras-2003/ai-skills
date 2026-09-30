# OAF / Organisational Architecture Framework

OAF is a practical synthesis for connecting strategy, operating model, governance, enterprise architecture, portfolio/execution and evidence feedback.

It is treated here as a **thinking and decision framework**, not as a new theory or a monolithic product.

Core loop:

```
Direction -> Architecture -> Priorities -> Execution -> Evidence -> next decision
```

The skill library decomposes OAF into reusable decision procedures rather than one giant "OAF skill".

## Subdomains

### 1. Direction & strategy execution
- `strategy-to-execution-diagnostic` — test whether strategic intent is translated into accountable execution.

### 2. Operating model
- `operating-model-review` — review global/local split, role clarity, interfaces, autonomy and coordination.

### 3. Decision architecture & governance
- `decision-rights-review` — map who decides, recommends, executes and escalates.
- `governance-design` — design governance forums, decision cadence, escalation and information flows.

### 4. Enterprise & organisational architecture
- `architecture-review` — review alignment between business direction, capabilities, organisation and technology.
- `capability-map-review` — assess capability-map quality, ownership, gaps and decision usefulness.

### 5. Portfolio & execution
- `portfolio-prioritization` — structure evidence-based prioritisation across initiatives.
- `transformation-blueprint` — convert diagnosis into sequenced target-state changes and mobilisation plan.

### 6. Evidence & adaptation
- `evidence-loop-review` — test whether KPIs, outcomes and feedback actually influence decisions.

## OAF diagnostic workflow

Use `workflows/oaf-health-check/WORKFLOW.md` for a multi-stage diagnostic.

The workflow must not blindly execute every skill. It should route only to the subdomains where evidence indicates a meaningful problem.

## Model-class defaults

- **fast:** capability-map-review, portfolio-prioritization
- **standard:** strategy-to-execution-diagnostic, operating-model-review, decision-rights-review, governance-design, architecture-review, evidence-loop-review, transformation-blueprint
- **strong:** escalation only for novel cross-domain redesign, conflicting executive evidence, or high-impact structural choices

See `docs/MODEL-ROUTING.md`.

## Boundary principle

OAF skills diagnose and design organisational decision systems. They should not become generic strategy, HR, software architecture, PMO or transformation prompts without an explicit OAF-relevant decision problem.
