# OAF Governance Redesign Workflow

## Purpose
Redesign governance from real decision needs rather than from existing committees.

## Preconditions
Require:
- an evidenced decision problem;
- representative formal-vs-actual decision traces;
- enough evidence to distinguish authority ambiguity, evidence failure, queue/rework and true governance mechanism gaps.

If these are not met, stop and route back to `decision-rights-review` or `decision-bottleneck-analysis`.

## Stages
1. **Reuse diagnosis** — do not restart generic governance analysis if decision-rights/bottleneck findings already exist.
2. **Define the minimum material decision set** — identify only decisions whose failure materially affects outcomes.
3. **Clarify target decision rights** — separate proposer, adviser, decision owner, executor and escalation.
4. **Remove ambiguity first** — eliminate hidden vetoes, duplicate approvals and unclear advisory authority before adding forums.
5. **Choose the lightest mechanism** — use direct rights, standing rules, asynchronous approval, event-triggered escalation or a forum depending on the decision need.
6. **Use `governance-design`** — define only mechanisms needed for the selected decision architecture.
7. **Test the design** — latency, duplicate vetoes, evidence inputs, participant load, funding/execution authority and escalation.
8. **Define removals** — identify existing forums/approvals to remove, merge or narrow.
9. **Pilot** — where feasible, test the redesigned mechanism on a bounded decision set before enterprise rollout.
10. **Define evidence loop** — specify how decision speed, quality, accountability and rework will be measured and reviewed.

## Decision rules
- No new forum unless a specific material decision requires one.
- A named decision owner is preferable to shared committee accountability.
- Advice must not silently become approval.
- Governance redesign should remove at least as much ambiguity/ceremony as it adds.
- Do not redesign the whole committee landscape if a narrower decision-rights change resolves the problem.
- Retain/merge an existing forum only when its formal mandate and material decision need justify it.
- Risk control should be preserved through explicit evidence, ownership, thresholds, expiry/review and escalation—not extra approvals by default.
- Do not claim governance success from meeting cadence or attendance alone.

## Output contract
- diagnosis reused;
- material decision set;
- target decision-rights map;
- mechanism choices and rationale;
- governance mechanisms;
- mechanisms to remove/merge/narrow;
- latency/accountability trade-offs;
- pilot plan;
- effectiveness measures;
- unresolved design questions.

## Model guidance
Default: **standard** for bounded governance redesign.
Validated on Luna for diagnosis reuse, rights-vs-mechanism separation, forum minimisation, bounded pilot and effectiveness measures.
Escalate to strong for enterprise-wide executive authority redesign, politically contested mandates or high-impact final governance architecture selection.

## Stop conditions
Stop before design if the decision problem or owner is not sufficiently evidenced.
Stop before enterprise rollout if the mechanism has not been tested or the trade-offs remain material and unresolved.
