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
1. Read prior research, thesis history, current portfolio and policy through investment-record-store; emit canonical READ receipt.
2. Use structured equity/ETF research plugins for context and consensus framing, then underwrite the security with an explicit horizon.
3. Verify decision-critical metrics in primary-source context; use Firecrawl to retrieve/parse filings or IR pages when useful.
4. Run the hard evidence-sanity gate: period, units, GAAP/non-GAAP, quarterly/annual, per-share/absolute, arithmetic and scale.
5. If any critical metric remains UNVERIFIED/CONFLICTED, classify VERIFY/RESEARCH; block numeric valuation and sizing; persist the gap if possible and return.
6. Only after the gate passes, build bear/base/bull valuation scenarios and current-price implications.
7. Separate business-thesis strength, security attractiveness and priced-in expectations.
8. Run thesis-challenge independently.
9. Classify research state: REJECT / WATCH / RESEARCHED / THESIS SURVIVES / THESIS WEAKENED / INVALIDATED.
10. If portfolio action is considered, parse policy semantics literally and run portfolio-state-review/position-sizing-review as needed.
11. Persist sources, research events, signals and a new thesis version through investment-record-store.
12. If the user makes a lifecycle decision, append it via decision-journal-update.
13. Emit canonical WRITE receipt. Research plugins, Data analytics and local files never count as canonical persistence.

## Decision rules
- company quality, security attractiveness and portfolio fit are different questions;
- structured research speeds discovery but does not replace primary verification;
- extreme figures must be verified, not rejected by magnitude;
- source URL present != extracted figure verified;
- unverified critical metrics block valuation and numeric sizing;
- review threshold != hard ceiling.

## Output contract
Business thesis | evidence-sanity status | verified/blocked metrics | valuation if permitted | priced-in expectations | security attractiveness | strongest countercase | thesis state | portfolio constraints | lifecycle/sizing state if permitted | exact evidence gaps | next trigger | canonical READ/WRITE receipts.

## Stop conditions
Stop before sizing if policy/portfolio context is missing.
Stop valuation and numeric sizing if critical evidence is unresolved.
