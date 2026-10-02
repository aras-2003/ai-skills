---
name: market-opportunity-scan
description: 'Screen the XTB-investable equity and ETF universe for research candidates
  using changes in fundamentals, valuation, expectations, price behavior and portfolio
  relevance. Use for broad opportunity hunting or change detection. Do not use to
  issue buy/sell instructions or to replace security underwriting.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.1.0
  maturity: production
  risk: medium
  last_reviewed: '2026-10-02'
---

# Market Opportunity Scan

## Purpose
Reduce a broad investable universe to a small research queue by looking for meaningful change, not merely popular tickers.

## Procedure
1. Constrain v1 to instruments confirmed or plausibly available in XTB; mark broker availability unverified until checked.
2. Compare current signals with prior observations when history exists.
3. Look for valuation dislocation, estimate revisions, margin/FCF inflection, cyclical normalization, quality temporarily mispriced and structural growth.
4. Separate fundamental, valuation and market/trend signals.
5. Evaluate signal materiality and decision relevance before promoting a name to the research queue.
6. Detect both positive candidates and portfolio-risk review candidates.
7. Remove ideas supported only by price momentum, social attention or narrative.
8. Route ambiguous-but-material changes through investment-attention-triage when the key question is whether the new information matters.
9. Return 3-10 research candidates with the evidence gap that must be closed next.

## Decision rules
- Discovery can be broad; conviction must be narrow.
- Price up + fundamentals up is not automatically attractive if valuation expanded more.
- Price down is not opportunity evidence without thesis integrity.
- XTB availability is a gate for the v1 actionable queue.

## Output contract
Ticker | setup | changed signal | materiality | evidence | valuation context | main risk | XTB status | next research step.

## Quality checks
- [ ] Change versus prior state is preferred over static score.
- [ ] Materiality is explicit before escalation.
- [ ] Fundamental, valuation and trend signals are distinct.
- [ ] No candidate is labeled a buy.
- [ ] Broker availability status is explicit.
