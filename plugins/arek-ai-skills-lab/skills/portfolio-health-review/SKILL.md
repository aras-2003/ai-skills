---
name: portfolio-health-review
description: 'Review whether an initiative portfolio is coherent, affordable, capacity-feasible,
  dependency-aware and aligned to strategic outcomes. Use for portfolio health diagnosis;
  do not force ranking when comparable evidence is missing.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.0.0
  maturity: production
  risk: medium
  last_reviewed: '2026-09-30'
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
8. State whether the portfolio is ready for defensible prioritisation.
9. State what can and cannot be concluded from the available evidence.

## Decision rules
- Portfolio health is not the average health of individual projects.
- Many green projects can still form an impossible portfolio.
- Approved budgets do not prove operational deliverability.
- Capacity and dependencies are system constraints.
- Mandatory work reduces discretionary capacity and should be visible separately.
- Shared bottleneck resources can override local project status.
- No-stop behavior is a portfolio adaptation signal, not automatic proof that all initiatives are weak.
- Possible duplication must be validated before being treated as waste.
- Do not use ranking as a substitute for portfolio diagnosis.
- Do not assign a new portfolio-level owner merely because current ownership is unknown; first verify whether effective ownership already exists.

## Output contract
Health dimension | evidence | issue | consequence | confidence | next validation/action.

Then:
- systemic portfolio risks;
- critical constraints;
- readiness for prioritisation;
- minimum normalization needed before ranking/scenario comparison.

## Model guidance
Default: **standard**.
Validated on Luna for portfolio-system diagnosis and prioritisation readiness.
Fast may be adequate with structured portfolio data. Escalate for contested strategic value or coupled portfolio scenario design.

## Quality checks
- [ ] System constraints reviewed.
- [ ] Initiative success not confused with portfolio viability.
- [ ] Funding separated from capacity feasibility.
- [ ] Mandatory work explicit.
- [ ] Dependency/shared-resource bottlenecks explicit.
- [ ] Readiness for prioritisation explicit.

## Lab runtime eval inputs

When the user explicitly asks to run one of the exact lab eval cases below, load only the corresponding input file from `references/evals/`. The evaluator rubric is intentionally unavailable to the executor.

- `references/evals/case-portfolio-health-001.input.md`
