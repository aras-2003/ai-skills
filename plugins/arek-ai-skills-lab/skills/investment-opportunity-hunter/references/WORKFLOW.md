# Investment Opportunity Hunter Workflow

## Purpose
Find a small number of XTB-investable research candidates by combining market change detection, theme context, portfolio context and evidence quality without turning discovery into automatic trading.

## Entry modes
- broad scan: search the XTB-investable universe;
- watchlist change scan: detect names that became materially more or less interesting;
- theme-led scan: start from a validated theme and find candidate beneficiaries.

## Required skills
- market-opportunity-scan
- investment-record-store

## Optional skills
- investment-attention-triage
- trend-theme-research
- portfolio-state-review
- security-underwriting
- valuation-scenario-review
- thesis-challenge

## Sequence
1. Use investment-record-store to read current policy, portfolio, watchlist, prior opportunities and signal history. Emit the canonical READ persistence receipt before proceeding.
2. If canonical history is unavailable, continue only as a fresh screen and state that no prior-state comparison was possible; never invent historical change.
3. Run market-opportunity-scan; prefer changed signals over static rankings.
4. Keep fundamental, valuation and market/trend evidence in separate fields and attach dated provenance/confidence to every decision-relevant changed signal.
5. Use investment-attention-triage when a new event/signal must first be judged for materiality before spending deep-research effort.
6. If a theme drives the setup, use trend-theme-research before attributing benefit to a company.
7. Reduce to 3-10 research candidates.
8. For the highest-materiality candidates only, run security-underwriting and valuation-scenario-review.
9. Run thesis-challenge before promoting a candidate to a conviction queue.
10. Persist Sources, Opportunities, Research_Log and Signals_History through investment-record-store.
11. Emit the canonical WRITE persistence receipt. A local markdown/JSON artifact may be linked only as NONCANONICAL and must not be described as preserved Investment OS state.
12. Do not size or label BUY/SELL here; route portfolio action to investment-security-review or position-sizing-review.

## Evidence gates
- current claims require as-of/source dates;
- decision-relevant figures must pass evidence sanity checks before promotion;
- XTB availability must be confirmed before a candidate is called actionable in v1;
- social/news attention alone cannot pass discovery;
- improving fundamentals with stretched valuation may remain WATCH rather than advance.

## Output contract
### Attention queue
Ticker | setup | fundamental change | valuation change | market/trend change | materiality | evidence/provenance | portfolio relevance | XTB status | next step.

### Rejected/deferred signals
Only material false positives and why they failed.

### Persistence receipts
Canonical READ receipt and canonical WRITE receipt, each with SUCCESS / UNAVAILABLE / FAILED. Local artifacts do not count as canonical persistence.

## Stop conditions
Stop when 3-10 credible research candidates remain.
Stop deeper work when the evidence gap is larger than the apparent opportunity.
