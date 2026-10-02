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
3. Run the hard underwriting evidence-sanity gate before valuation:
   - verify critical metrics in primary-source context;
   - check period, units, GAAP/non-GAAP, quarterly vs annual, per-share vs absolute values, arithmetic consistency and magnitude versus company/prior-period scale;
   - if a critical figure is implausible, conflicting or extraction-uncertain, mark UNVERIFIED/CONFLICTED and attempt re-verification.
4. If any decision-critical metric remains UNVERIFIED/CONFLICTED:
   - classify the case VERIFY / RESEARCH;
   - do not calculate P/E, FCF yield or numeric scenario valuation from those figures;
   - do not run numeric position sizing;
   - persist the evidence gap and next verification step if canonical write is available;
   - return.
5. Only after the evidence gate passes, build bear/base/bull valuation scenarios and what the current price implies.
6. Explicitly state business-thesis strength separately from security attractiveness and priced-in expectations.
7. Run thesis-challenge independently of the preferred case.
8. Classify the research state: REJECT / WATCH / RESEARCHED / THESIS SURVIVES / THESIS WEAKENED / INVALIDATED.
9. If portfolio action is being considered, parse policy semantics literally before sizing:
   - a review threshold triggers review;
   - it is not a hard cap or trim target unless the policy explicitly says so.
10. Only when critical evidence is verified and policy semantics are clear, run portfolio-state-review and position-sizing-review.
11. Persist Sources, Research_Log, Signals_History and a new Thesis_Register version through investment-record-store.
12. If the user makes an actual lifecycle decision, append Decision_Journal via decision-journal-update.
13. Emit canonical WRITE persistence receipt. A local file path is NONCANONICAL and cannot be presented as durable history.

## Decision rules
- company quality, security attractiveness and portfolio fit are three different questions;
- a surviving thesis does not imply a full position;
- a strong chart/earnings momentum signal does not override valuation or concentration;
- source URL present != extracted figures verified;
- do not average bear/base/bull into false precision;
- no action state is acceptable when evidence does not justify change;
- unverified critical metrics block valuation and numeric sizing;
- review threshold != hard ceiling.

## Output contract
Business thesis | evidence-sanity status | blocked/verified metrics | valuation scenarios if permitted | priced-in expectations | security attractiveness | strongest countercase | thesis state | policy-rule semantics | portfolio constraints | drift source | lifecycle/sizing state if permitted | exact evidence gaps | next trigger | canonical READ/WRITE persistence receipts.

## Stop conditions
Stop before sizing if policy/portfolio context is missing.
Stop valuation and numeric sizing if decision-critical evidence is unverified/conflicted.
Escalate to fresh research if evidence is stale or the business/cycle regime changed.
