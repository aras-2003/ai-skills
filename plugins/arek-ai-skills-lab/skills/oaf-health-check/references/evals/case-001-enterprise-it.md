# OAF Health Check — Practical Case 001

## Scenario

A large technology organisation has the following symptoms:

- a formal strategy exists, but business and technology roadmaps are inconsistent or missing;
- vertical directors optimise locally and accountability across domains is weak;
- portfolio decisions are reactive and initiative intake is poorly prioritised;
- architecture bodies exist but have limited influence on investment and delivery decisions;
- governance includes many forums, but decisions are slow and escalation is unclear;
- teams report many KPIs, but management reviews rarely change priorities;
- leadership wants clearer end-to-end accountability without creating excessive centralisation.

Assume:
- evidence is incomplete;
- some stakeholder accounts conflict;
- no redesign decision has been approved yet.

## Test objective

Evaluate whether the OAF Health Check workflow:

1. frames the decision problem before proposing solutions;
2. selects only relevant OAF diagnostic skills;
3. diagnoses before invoking design skills;
4. distinguishes evidence, inference and unknowns;
5. identifies cross-domain structural causes;
6. avoids producing a giant transformation plan from weak evidence;
7. ends with a concrete next diagnostic/design action.

## Expected routing

Likely diagnostic skills:
- `strategy-to-execution-diagnostic`
- `operating-model-review`
- `decision-rights-review`
- `architecture-review`
- `portfolio-prioritization`
- `evidence-loop-review`

Conditional:
- `governance-design` only after governance/decision gaps are evidenced;
- `transformation-blueprint` only after diagnosis is sufficiently stable.

Usually unnecessary unless specific evidence appears:
- `capability-map-review`

## Expected output properties

### Executive diagnosis
Should explain a few structural causes, not just repeat symptoms.

### OAF heatmap
Should include only domains actually reviewed.

### Cross-domain causes
Should connect symptoms, for example:
- weak decision rights -> governance proliferation + slow prioritisation;
- weak strategy traceability -> reactive portfolio;
- weak evidence loop -> recurring low-quality prioritisation;
- operating-model ambiguity -> local optimisation + architecture bypass.

### Critical unknowns
Should identify information that could materially alter the diagnosis.

### Recommended next action
Should route to one or two specific next steps rather than launching the full transformation.

## Failure conditions

FAIL if the runtime:
- executes every OAF skill automatically;
- jumps straight to a target operating model;
- creates committees before diagnosing decision problems;
- treats assumptions as facts;
- produces a generic maturity model with no causal analysis;
- creates a long roadmap without enough evidence.
