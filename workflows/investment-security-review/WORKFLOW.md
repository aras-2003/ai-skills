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
1. Use investment-record-store to read prior research, thesis history, current portfolio and policy if they exist; emit the canonical READ receipt.
2. Underwrite the security with an explicit horizon; if both 6-18 month and 2-5 year cases matter, keep them separate.
3. Run the underwriting evidence-sanity gate. Resolve implausible, conflicting or extraction-uncertain decision-critical figures before valuation/sizing. If unresolved, classify the case VERIFY/RESEARCH and stop numeric sizing.
4. Build bear/base/bull valuation scenarios and what the current price implies.
5. Explicitly state business-thesis strength separately from security attractiveness and priced-in expectations.
6. Run thesis-challenge independently of the preferred case.
7. Classify the research state: REJECT / WATCH / RESEARCHED / THESIS SURVIVES / THESIS WEAKENED / INVALIDATED.
8. Only when a portfolio action is actually being considered and critical evidence is verified, run portfolio-state-review and position-sizing-review.
9. Persist Sources, Research_Log, Signals_History and a new Thesis_Register version through investment-record-store.
10. If the user makes an actual lifecycle decision, append Decision_Journal via decision-journal-update.
11. Emit canonical WRITE persistence receipt. A local file path is NONCANONICAL and cannot be presented as durable history.

## Decision rules
- company quality, security attractiveness and portfolio fit are three different questions;
- a surviving thesis does not imply a full position;
- a strong chart/earnings momentum signal does not override valuation or concentration;
- do not average bear/base/bull into false precision;
- no action state is acceptable when evidence does not justify change;
- unverified critical metrics block numeric sizing guidance.

## Output contract
Business thesis | evidence-sanity status | valuation scenarios | priced-in expectations | security attractiveness | strongest countercase | thesis state | portfolio constraints | drift source | lifecycle/sizing state if permitted | evidence gaps | next trigger | canonical READ/WRITE persistence receipts.

## Stop conditions
Stop before sizing if policy/portfolio context is missing.
Stop numeric sizing if decision-critical evidence is unverified/conflicted.
Escalate to fresh research if evidence is stale or the business/cycle regime changed.
