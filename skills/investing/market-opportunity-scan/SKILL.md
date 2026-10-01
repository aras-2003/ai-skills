---
name: market-opportunity-scan
description: >
  Screen the XTB-investable equity and ETF universe for research candidates using changes in fundamentals, valuation,
  expectations, price behavior and portfolio relevance. Use for broad opportunity hunting or change detection.
  Do not use to issue buy/sell instructions or to replace security underwriting.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-10-02
  execution:
    default_model_class: fast
---

# Market Opportunity Scan

## Purpose
Reduce a broad investable universe to a small research queue by looking for meaningful change, not merely popular tickers.

## Procedure
1. Constrain v1 to instruments confirmed or plausibly available in XTB; mark broker availability unverified until checked.
2. Compare current signals with prior observations when history exists.
3. Look for valuation dislocation, estimate revisions, margin/FCF inflection, cyclical normalization, quality temporarily mispriced and structural growth.
4. Separate fundamental, valuation and market/trend signals.
5. Detect both positive candidates and portfolio-risk review candidates.
6. Remove ideas supported only by price momentum, social attention or narrative.
7. Return 3-10 research candidates with the evidence gap that must be closed next.

## Decision rules
- Discovery can be broad; conviction must be narrow.
- Price up + fundamentals up is not automatically attractive if valuation expanded more.
- Price down is not opportunity evidence without thesis integrity.
- XTB availability is a gate for the v1 actionable queue.

## Output contract
Ticker | setup | changed signal | evidence | valuation context | main risk | XTB status | next research step.

## Quality checks
- [ ] Change versus prior state is preferred over static score.
- [ ] Fundamental, valuation and trend signals are distinct.
- [ ] No candidate is labeled a buy.
- [ ] Broker availability status is explicit.
