---
name: architecture-review
description: 'Review alignment across business direction, capabilities, organisational
  design, information and technology architecture. Use for enterprise or organisational
  architecture decisions; do not use as a low-level software design review.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.0.0
  maturity: production
  risk: medium
  last_reviewed: '2026-09-30'
---

# Architecture Review

## Purpose
Test whether organisational and technology architecture coherently supports strategic direction without assuming that organisational symptoms imply technology defects.

## Procedure
1. State the business outcomes, constraints and architectural decision problem.
2. Identify impacted capabilities, ownership and key dependencies.
3. Review business-to-architecture traceability.
4. Review organisational ownership and architecture governance.
5. Review how architecture enters portfolio, funding and delivery decisions.
6. Distinguish:
   - organisational/decision-system problems;
   - investment-system problems;
   - evidenced technology-estate problems.
7. Do not diagnose technology defects unless specific estate evidence supports them.
8. Identify current-state structural misfits and diagnostic options.
9. Recommend target-state architecture only when evidence is sufficient; otherwise state the minimum evidence needed.

## Decision rules
- Architecture decisions must trace to business/capability needs.
- Avoid technology-only recommendations when the problem is organisational.
- Architecture responsibility without investment/delivery authority is a governance issue before it is a technology issue.
- Local optimisation can create enterprise technology consequences without proving a technology defect.
- Explicitly surface trade-offs and reversibility.
- Unknown architecture debt must remain unknown.

## Output contract
- context and architectural decision problem;
- affected capabilities/ownership hypotheses;
- current-state diagnosis;
- organisational vs technology problem table;
- structural misfits;
- diagnostic options;
- minimum evidence before target-state design;
- recommendation on the next evidence-gathering step.

## Model guidance
Default: **standard**.
Validated on Luna for current-state diagnosis and architecture-governance review.
Escalate to strong for novel cross-domain target architecture, contested target-state trade-offs, or major transition design.

## Quality checks
- [ ] Business-to-architecture traceability explicit.
- [ ] Organisational and technology causes separated.
- [ ] No invented technology-estate defects.
- [ ] Architecture influence linked to investment/delivery timing and authority.
- [ ] Target-state design deferred when evidence is insufficient.
