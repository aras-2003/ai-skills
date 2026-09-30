---
name: transformation-blueprint
description: >
  Convert an approved organisational diagnosis and target direction into a sequenced transformation blueprint with workstreams, dependencies, decision gates, capacity needs and evidence checkpoints. Use after diagnosis and target-state direction are sufficiently agreed; do not roadmap unresolved design choices as facts.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.2.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Transformation Blueprint

## Purpose
Turn validated diagnosis and target direction into a practical, evidence-gated change blueprint.

## Preconditions
Require:
- sufficiently evidenced diagnosis;
- explicit target direction or bounded target-state choice;
- known major constraints and dependencies;
- unresolved decisions clearly separated from settled design.

If target direction is not sufficiently decided, stop and return to the relevant design workflow.

## Procedure
1. Trace each transformation objective to a diagnosed structural problem and target-state principle.
2. Identify the minimum coherent workstreams needed to close those gaps.
3. For each workstream define:
   - intended outcome;
   - accountable owner or owner-to-confirm;
   - major deliverables/changes;
   - dependencies;
   - capability/capacity requirements;
   - decision gates;
   - evidence of progress/outcome.
4. Sequence foundational changes before dependent changes.
5. Separate:
   - reversible pilots/experiments;
   - enabling/foundation work;
   - scaled rollout;
   - decommission/retirement.
6. Identify critical path, bottleneck resources and cross-workstream dependencies.
7. Define 30–90 day mobilisation separately from longer transformation.
8. Define stage gates with explicit continue / adjust / stop criteria.
9. Surface transition costs, operational risks and temporary-state complexity.
10. Define feedback checkpoints that can change sequence, scope or target assumptions.

## Decision rules
- Do not roadmap unresolved design questions as if settled.
- Quick wins must support the target state, not create more fragmentation.
- Activity completion is not the same as transformation outcome.
- Capacity and dependency constraints can override desired sequencing.
- Do not assign named owners where ownership is not evidenced; use owner-to-confirm.
- Pilots should be used where reversibility materially reduces risk.
- Do not create a multi-year roadmap when evidence only supports the next mobilisation phase.

## Output contract
### Transformation logic
Problem | target principle | workstream | intended outcome.

### Workstream plan
Workstream | owner | outcome | key changes | dependencies | capacity | decision gates | evidence.

Then:
- sequence / critical path;
- 30–90 day mobilisation;
- pilots and reversible steps;
- stage gates and continue/adjust/stop criteria;
- transition risks;
- unresolved decisions;
- longer-horizon direction only where supported.

## Model guidance
Default: **standard** for bounded, evidence-backed blueprints.
Escalate to strong for enterprise-wide sequencing, large transition economics, contested target-state choices or major multi-country transformation.

## Quality checks
- [ ] Every workstream traces to diagnosis and target principle.
- [ ] Dependencies and critical path explicit.
- [ ] Capacity constraints explicit.
- [ ] Mobilisation separated from long-term rollout.
- [ ] Unresolved decisions remain unresolved.
- [ ] Stage gates can change the plan.
- [ ] Outcomes distinguished from activity.
