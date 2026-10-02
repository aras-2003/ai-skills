---
name: market-opportunity-scan
description: 'Screen the XTB-investable equity and ETF universe for research candidates
  using changes in fundamentals, valuation, expectations, price behavior and portfolio
  relevance. Use for broad opportunity hunting or change detection. Prefer installed
  structured equity-research plugins for breadth, Firecrawl/primary sources for verification,
  and canonical portfolio context from investment-record-store. Do not issue buy/sell
  instructions.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.2.0
  maturity: production
  risk: medium
  last_reviewed: '2026-10-02'
---

# Market Opportunity Scan

## Purpose
Reduce a broad investable universe to a small research queue by looking for meaningful change, not merely popular tickers.

## Tool routing
Use the narrowest available source for each job:
1. **Canonical state**: investment-record-store -> Supabase (or explicit legacy mode before cutover).
2. **Breadth / candidate discovery**: installed structured equity/ETF research plugins such as Public Equity Investing or Stock & ETF Research Panel.
3. **Primary-source verification**: company IR, filings, official ETF pages; use Firecrawl when live retrieval/extraction is useful.
4. **Derived portfolio analytics**: Data plugin or equivalent analytics layer may query canonical data; its output is derived, not canonical.
5. **Google Drive**: raw files/exports only.

Do not treat any research plugin as the canonical portfolio store.

## Procedure
1. Constrain actionable v1 candidates to instruments confirmed or plausibly available in XTB; mark broker availability unverified until checked.
2. Load portfolio/watchlist/opportunity/signal history from canonical state.
3. Use structured research tools to generate a broad candidate set and current signals.
4. Compare current signals with prior observations when history exists.
5. Look for valuation dislocation, estimate revisions, margin/FCF inflection, cyclical normalization, quality temporarily mispriced and structural growth.
6. Separate fundamental, valuation and market/trend signals.
7. Verify decision-relevant changed claims in primary sources before promotion to the research queue.
8. Evaluate signal materiality and portfolio relevance.
9. Remove ideas supported only by price momentum, social attention or narrative.
10. Return 3-10 research candidates with the exact evidence gap to close next.

## Decision rules
- Discovery can be broad; conviction must be narrow.
- Structured research accelerates discovery; primary sources anchor conviction.
- Price up + fundamentals up is not automatically attractive if valuation expanded more.
- XTB availability is a gate for the actionable queue.
- Analytics output cannot overwrite canonical records except through investment-record-store.

## Output contract
Ticker | setup | changed signal | materiality | evidence/provenance | valuation context | portfolio relevance | main risk | XTB status | next research step.

## Quality checks
- [ ] Canonical portfolio/watchlist context was attempted.
- [ ] Change versus prior state is preferred over static score.
- [ ] Fundamental, valuation and trend signals are distinct.
- [ ] Decision-relevant claims were verified or marked unverified.
- [ ] No candidate is labeled a buy.
- [ ] Broker availability status is explicit.
