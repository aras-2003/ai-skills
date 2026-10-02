# OAF Enterprise Architecture Review Workflow

## Purpose
Review whether enterprise architecture supports business outcomes, capability needs, operating-model boundaries and investment decisions without assuming that organisational symptoms imply technology defects.

## Preconditions
Require:
- a defined business outcome or architectural decision problem;
- enough current-state evidence to separate organisational, investment and technology issues;
- known constraints and major dependencies.

If the evidence cannot support technology conclusions, keep those conclusions unknown.

## Stages
1. **Frame the decision** — state the business outcome, architecture decision boundary, constraints and what is explicitly out of scope.
2. **Trace outcome to capabilities** — use `capability-map-review` only if map quality/structure materially affects the decision; use `capability-gap-analysis` only if the required capability set is sufficiently clear.
3. **Run/reuse `architecture-review`** — test business-to-architecture traceability, ownership, governance and architecture influence on funding/delivery.
4. **Separate problem classes**:
   - operating-model / decision-rights issue;
   - portfolio / funding / investment issue;
   - information/data issue;
   - evidenced technology-estate issue;
   - unknown / evidence gap.
5. **Identify architecture decision points** — standards, platform boundaries, data/integration contracts, exception rules, reuse/local variation, lifecycle/retirement decisions where evidence supports them.
6. **Generate bounded options** only when evidence is sufficient. Compare 2–3 options by:
   - business outcome support;
   - capability fit;
   - interoperability/data implications;
   - local/global boundaries;
   - cost/capacity;
   - transition complexity;
   - reversibility;
   - investment/decision-right implications.
7. **Avoid premature target architecture** — if current-state evidence is weak, define the minimum evidence collection instead.
8. **Connect to portfolio** — state which investment/roadmap decisions can be made now and which depend on further evidence.
9. **Define next gate** — diagnostic evidence, architecture decision, pilot, or transformation-design handoff.

## Decision rules
- Architecture must trace to business/capability outcomes.
- Architecture governance failure is not automatically a technology-estate failure.
- Duplication is not automatically waste; validate purpose, divergence, integration cost and local constraints.
- A global standard does not automatically require one implementation.
- Do not invent platform/data/integration defects without evidence.
- Do not create a target-state diagram merely because the user asked for “architecture”.
- Prefer reversible architecture decisions where uncertainty is material.
- Technology recommendations must identify the business/capability problem they solve.
- A working architecture direction must remain provisional until evidence supports final target-state selection.

## Output contract
- architecture decision framing;
- outcome-to-capability traceability;
- current-state diagnosis;
- problem-class separation;
- material architecture decision points;
- bounded options and trade-offs, if evidence permits;
- evidence gaps / unknowns;
- investment/portfolio implications;
- recommendation for next gate.

## Model guidance
Default: **standard** for evidence-backed enterprise architecture review.
Validated on Luna for evidence-disciplined architecture review, bounded option comparison and strict stop-condition enforcement.
Escalate to strong for novel target architecture, major platform/data boundary redesign, highly coupled global architectures, contested target-state trade-offs or material transition economics.

## Stop conditions
Stop before target-state design if current-state evidence cannot distinguish organisational/investment issues from technology-estate issues.
Stop before recommending platform consolidation/retirement when duplication purpose, dependency and transition evidence are insufficient.

## Integrated report presentation
After architectural synthesis, call `report-composer`.

Default profile:
- architecture decision question;
- current-state evidence;
- capability/estate implications with inline map/heatmap;
- options with comparison visual when supported;
- target direction;
- transition constraints/evidence gaps.

Use `visual-output-design` for capability maps, dependency diagrams and option visuals. Never invent application/interface/dependency detail to complete a diagram.
