# Investment Opportunity Hunter Workflow

## Purpose
Find a small number of XTB-investable research candidates by combining market change detection, structured equity research, primary-source verification, theme context, portfolio context and evidence quality without turning discovery into automatic trading.

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
1. Read current policy, portfolio, watchlist, prior opportunities and signal history through investment-record-store. Emit the canonical READ receipt.
2. If canonical history is unavailable, continue only as a fresh screen and state that no prior-state comparison was possible.
3. Use installed structured equity/ETF research plugins for breadth and candidate generation.
4. Run market-opportunity-scan; prefer changed signals over static rankings.
5. Verify decision-relevant claims with primary sources; use Firecrawl for live retrieval/parsing when useful.
6. Keep fundamental, valuation and market/trend evidence in separate fields and attach dated provenance/confidence.
7. Use investment-attention-triage when materiality is unclear.
8. If a theme drives the setup, use trend-theme-research before attributing benefit to a company.
9. Reduce to 3-10 research candidates.
10. For highest-materiality candidates only, run security-underwriting and valuation-scenario-review.
11. Run thesis-challenge before promoting a candidate to a conviction queue.
12. Persist sources, opportunities, research events and signals through investment-record-store only.
13. Emit canonical WRITE receipt. Data/analytics outputs and local files are NONCANONICAL.
14. Do not size or label BUY/SELL here; route portfolio action to investment-security-review or position-sizing-review.

## Evidence gates
- current claims require as-of/source dates;
- structured research is discovery evidence, not canonical state;
- critical figures require primary-source sanity checks;
- XTB availability must be confirmed before a candidate is called actionable;
- social/news attention alone cannot pass discovery.

## Output contract
Ticker | setup | fundamental change | valuation change | market/trend change | materiality | evidence/provenance | portfolio relevance | XTB status | next step | canonical persistence receipts.

## Stop conditions
Stop when 3-10 credible research candidates remain.
Stop deeper work when the evidence gap is larger than the apparent opportunity.
