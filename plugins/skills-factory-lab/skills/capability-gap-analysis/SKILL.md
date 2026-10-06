---
name: capability-gap-analysis
description: 'Identify material gaps between required business capabilities and current
  organisational, process, information, technology, governance or capacity enablement.
  Use after strategic outcomes are sufficiently clear; do not translate every capability
  gap directly into a technology project.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.0.0
  maturity: production
  risk: medium
  last_reviewed: '2026-09-30'
---

# Capability Gap Analysis

## Purpose
Identify which capabilities are insufficient for the target outcome and what dimension of each capability is weak.

## Preconditions
Require:
- explicit business/strategic outcome;
- a bounded set of relevant capabilities or enough evidence to identify them;
- current-state evidence for at least some capability dimensions.

If these are missing, stop before prescribing interventions.

## Procedure
1. Start from the required outcome, not an application inventory.
2. Identify the smallest set of capabilities materially required for that outcome.
3. For each capability assess only evidenced dimensions:
   - ownership/accountability;
   - people/skills;
   - process/ways of working;
   - information/data;
   - technology;
   - governance/decision rights;
   - capacity/scalability.
4. Separate gap types:
   - capability absent;
   - insufficient maturity;
   - insufficient capacity;
   - poor integration/interface;
   - unclear ownership/decision rights;
   - missing or poor-quality information;
   - technology enablement issue.
5. Identify dependencies and shared bottlenecks.
6. Separate evidence, hypothesis and unknowns.
7. State intervention hypotheses at the capability dimension level.
8. Route to architecture, operating-model, governance or portfolio analysis only when the evidence supports that next step.

## Decision rules
- A capability is what the organisation must be able to do, not an org unit or system.
- Do not translate every gap into a new platform.
- Capability ownership and operating model may be the primary gap even when technology symptoms exist.
- Capacity shortage is different from maturity deficiency.
- Integration failure is different from capability absence.
- Do not assign target maturity scores without a decision need and evidence.
- Do not recommend a project portfolio until intervention hypotheses are comparable and dependencies understood.
- Shared queues or workarounds do not prove platform defects; test capacity, ownership, data and decision-system causes first.

## Output contract
Capability | required outcome | current evidence | gap type | affected dimension | dependency | consequence | confidence | intervention hypothesis | evidence needed.

Then:
- cross-capability bottlenecks;
- gaps that are organisational vs information vs technology;
- what can be acted on now;
- what remains unproven.

## Model guidance
Default: **standard**.
Escalate for complex cross-domain capability design or contested target-state capability boundaries.

## Quality checks
- [ ] Outcome-to-capability traceability.
- [ ] Capability vs process/org/system distinction preserved.
- [ ] Gap type explicit.
- [ ] Capacity vs maturity separated.
- [ ] Evidence/hypothesis/unknown separated.
- [ ] No automatic technology solution.

## Lab runtime eval inputs

When the user explicitly asks to run one of the exact lab eval cases below, load only the corresponding input file from `references/evals/`. The evaluator rubric is intentionally unavailable to the executor.

- `references/evals/case-capability-gap-001.input.md`
