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
- trend-theme-research
- portfolio-state-review
- security-underwriting
- valuation-scenario-review
- thesis-challenge

## Sequence
1. Read current policy, portfolio, watchlist, prior opportunities and signal history when available.
2. Run market-opportunity-scan; prefer changed signals over static rankings.
3. If a theme drives the setup, use trend-theme-research before attributing benefit to a company.
4. Reduce to 3-10 research candidates.
5. For the highest-value candidates only, run security-underwriting and valuation-scenario-review.
6. Run thesis-challenge before promoting a candidate to a conviction queue.
7. Persist Sources, Opportunities, Research_Log and Signals_History.
8. Do not size or label BUY/SELL here; route portfolio action to investment-security-review or position-sizing-review.

## Evidence gates
- current claims require as-of/source dates;
- XTB availability must be confirmed before a candidate is called actionable in v1;
- social/news attention alone cannot pass discovery;
- improving fundamentals with stretched valuation may remain WATCH rather than advance.

## Output contract
### Attention queue
Ticker | setup | what changed | evidence | valuation state | portfolio relevance | XTB status | next step.

### Rejected/deferred signals
Only material false positives and why they failed.

### Persistence receipt
Records appended/updated or explicit storage failure.

## Stop conditions
Stop when 3-10 credible research candidates remain.
Stop deeper work when the evidence gap is larger than the apparent opportunity.
