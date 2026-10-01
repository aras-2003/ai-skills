# Investment Security Review Workflow

## Purpose
Evaluate one XTB security from thesis creation through falsification, valuation, portfolio fit and a policy-consistent lifecycle/sizing state.

## Required skills
- security-underwriting
- valuation-scenario-review
- thesis-challenge
- investment-record-store

## Optional skills
- trend-theme-research
- portfolio-state-review
- position-sizing-review
- decision-journal-update

## Sequence
1. Read prior research, thesis history, current portfolio and policy if they exist.
2. Underwrite the security with an explicit horizon; if both 6-18 month and 2-5 year cases matter, keep them separate.
3. Build bear/base/bull valuation scenarios and what the current price implies.
4. Run thesis-challenge independently of the preferred case.
5. Classify the research state: REJECT / WATCH / RESEARCHED / THESIS SURVIVES / THESIS WEAKENED / INVALIDATED.
6. Only when a portfolio action is actually being considered, run portfolio-state-review and position-sizing-review.
7. Persist Sources, Research_Log, Signals_History and a new Thesis_Register version.
8. If the user makes an actual lifecycle decision, append Decision_Journal via decision-journal-update.

## Decision rules
- company quality, security attractiveness and portfolio fit are three different questions;
- a surviving thesis does not imply a full position;
- do not average bear/base/bull into false precision;
- no action state is acceptable when evidence does not justify change.

## Output contract
Thesis | valuation scenarios | strongest countercase | thesis state | portfolio constraints | lifecycle/sizing state if requested | evidence gaps | next trigger | persistence receipt.

## Stop conditions
Stop before sizing if policy/portfolio context is missing.
Escalate to fresh research if evidence is stale or the business/cycle regime changed.
