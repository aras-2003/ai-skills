---
name: strategy-to-execution-diagnostic
description: >
  Diagnose whether strategic intent is translated into explicit priorities, accountable owners, funding, roadmaps and measurable outcomes. Use when strategy appears disconnected from execution; do not use for generic strategy creation.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Strategy to Execution Diagnostic

## Purpose
Find structural breaks between declared strategy and actual execution.

## Use when
- strategic priorities exist but delivery is inconsistent;
- initiatives proliferate without clear linkage to outcomes;
- ownership, funding or roadmaps are unclear.

## Procedure
1. Extract stated strategic outcomes and time horizon.
2. Map each outcome to accountable owner, decision forum, capability impact, portfolio initiatives, funding and measures.
3. Identify breaks in traceability: orphan initiatives, unfunded priorities, shared accountability, missing capabilities or absent outcomes.
4. Distinguish strategy-quality problems from execution-system problems.
5. Prioritize the few breaks that most impair delivery.
6. Recommend the next diagnostic/design action, not a full transformation plan.

## Decision rules
- Do not equate project activity with strategic execution.
- Shared ownership without a clear decision owner is a risk.
- Measures must test outcomes, not only activity/completion.

## Output contract
Strategic outcome | owner | execution mechanism | evidence | break/gap | consequence | priority.
Then: top 3 system breaks and next action.

## Model guidance
Default: **standard**. Escalate for conflicting executive interpretations or cross-enterprise strategy redesign.

## Quality checks
- [ ] Strategy and execution problems are separated.
- [ ] Traceability is explicit.
- [ ] Gaps have consequences, not just labels.

