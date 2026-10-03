# Investment Portfolio Observation Workflow

## Purpose
Observe what is changing in the user's portfolio over time and surface only changes that deserve attention.

This workflow is not a target-allocation optimiser and does not enforce a fixed portfolio structure. It answers:
- what changed;
- how large the change is;
- whether the change is structural, evidence-related or only observed state;
- which positions/exposures deserve attention now;
- what can safely be ignored.

## Natural activation
Use this workflow for ordinary requests such as:
- "what is happening with my portfolio?";
- "what changed in my portfolio?";
- "what should I watch?";
- "monitor my holdings";
- "show me portfolio drift";
- "co się dzieje z portfelem?";
- "co się zmieniło?";
- "co mam obserwować?";
- "obserwuj moje pozycje".

Do not require the user to ask for policy enforcement, rebalancing or a full portfolio review.

## Required skills
- portfolio-state-review
- investment-record-store

## Optional skills
- investment-attention-triage
- thesis-monitor
- report-composer
- visual-output-design

## Sequence
1. Resolve the canonical backend/project/schema through investment-record-store.
2. Read:
   - latest valid snapshot;
   - previous valid snapshot;
   - `portfolio_position_changes`;
   - current positions;
   - current portfolio exposures;
   - recent material signals/research;
   - ACTIVE theses when present;
   - DRAFT thesis presence as metadata only.
3. Establish observed change first. Do not infer causes from weight/value deltas.
4. For each position classify observation state:
   - `REQUIRES_ATTENTION`: material observed change, material new evidence, thesis issue, or a meaningful data-quality problem that could change a decision;
   - `MONITOR`: non-trivial change worth following but no decision is currently required;
   - `NO_MATERIAL_CHANGE`: no meaningful change since the comparison snapshot;
   - `DATA_GAP`: observation is blocked or materially incomplete.
5. Causal attribution is a separate evidence gate:
   - use transactions plus comparable state, or explicit canonical attribution metadata;
   - otherwise use `UNKNOWN`;
   - never infer market-driven/no-trade/trade-driven from an empty transaction table.
6. Review exposure drift only where look-through evidence exists.
   - distinguish measured exposure from partial/minimum exposure;
   - do not turn incomplete look-through into a precise total.
7. Use soft reference bands, if configured, only as attention signals. They are not policy breaches, target allocations or automatic rebalance instructions.
8. Run investment-attention-triage only for positions/exposures with material new evidence or meaningful observed change.
9. Run thesis-monitor only when an ACTIVE thesis exists. If only DRAFT exists, state that thesis monitoring is not yet active.
10. Suppress unchanged/noise items from the main attention queue; summarize them compactly under no material change.
11. Do not create buy/sell/rebalance instructions unless the user separately asks for a portfolio decision.
12. Persist only new canonical observations/signals that are materially useful and non-duplicative; do not write merely because the workflow ran.

## Observation dimensions
Use the minimum dimensions supported by evidence:
- position weight/value change;
- account-level duplication where relevant;
- single-name look-through;
- sector/theme exposure;
- cash change;
- thesis/evidence change;
- stale/missing data.

Do not invent unsupported dimensions merely for completeness.

## Soft reference semantics
Reference bands are optional observation heuristics.

Allowed use:
- "this exposure entered a review zone";
- "this position moved materially versus its own prior range";
- "overlap increased enough to deserve review".

Forbidden use unless an explicit canonical hard policy exists:
- "policy breach";
- "must rebalance";
- "must sell";
- "target allocation violated".

## Output contract
Return a compact observation report:

### Requires attention
Only material items. For each:
- position/exposure;
- observed change;
- evidence state;
- causal attribution or UNKNOWN;
- why it matters;
- smallest useful next step.

### Monitor
Only non-trivial items worth following.

### No material change
Compact summary; do not repeat every unchanged position unless explicitly requested.

### Data gaps
Only gaps that materially limit observation quality.

### Receipts
Canonical read/write status and relevant evidence limitations.

## Stop conditions
Stop when:
- every material observed change is classified;
- unsupported causality has been left UNKNOWN;
- unchanged/noise items are suppressed;
- no extra policy optimisation is required to answer the observation question.

## Integrated report presentation
Render directly in chat by default.

Use report-composer only when the observation set is substantial enough to benefit from an integrated report.
Use visual-output-design when a change/exposure chart materially improves understanding.

For an observation report, visuals are helpful but not mandatory unless the active report profile explicitly requires them. Do not fail the analytical observation merely because no renderer is available.
