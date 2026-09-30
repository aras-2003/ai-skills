---
name: portfolio-health-review
description: >
  Review whether an initiative portfolio is coherent, affordable, capacity-feasible, dependency-aware and aligned to strategic outcomes. Use for portfolio health diagnosis; do not force ranking when comparable evidence is missing.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Portfolio Health Review

## Purpose
Diagnose whether the portfolio as a system can realistically deliver its intended outcomes.

## Procedure
1. Establish portfolio objective, scope and strategic outcomes.
2. Review initiative inventory completeness and ownership.
3. Check value/outcome traceability.
4. Review mandatory/discretionary mix.
5. Review funding, capacity, critical skills and dependency load.
6. Identify duplication, orphan initiatives, overloaded capabilities and sequencing conflicts.
7. Review stop/pause/reprioritisation behaviour.
8. State what can and cannot be concluded from the available evidence.

## Decision rules
- Portfolio health is not the average health of individual projects.
- Too many green projects can still form an impossible portfolio.
- Capacity and dependencies are system constraints.
- Do not use ranking as a substitute for portfolio diagnosis.

## Output contract
Health dimension | evidence | issue | consequence | confidence | next validation/action.
Then: systemic portfolio risks, critical constraints, and whether prioritisation is ready.

## Model guidance
Default: **standard**. Fast may be adequate with structured portfolio data.

## Quality checks
- [ ] System constraints reviewed.
- [ ] Initiative success not confused with portfolio viability.
- [ ] Readiness for prioritisation explicit.

