---
name: security-underwriting
description: >
  Underwrite one equity or ETF as an investment by analyzing business economics, financial quality, growth drivers,
  valuation context, catalysts, risks, variant perception and thesis invalidation. Use after a security enters the
  research queue or when the user asks for a full investment case. Do not use for broad market scanning.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: high
  last_reviewed: 2026-10-02
  execution:
    default_model_class: strong
---

# Security Underwriting

## Purpose
Produce an evidence-backed investment case that can later be challenged, sized and monitored.

## Procedure
1. Define instrument, thesis horizon and current as-of date.
2. Explain business model, segment economics, competitive position and capital intensity.
3. Review revenue, margins, cash flow, ROIC/returns, balance sheet, dilution and capex using dated sources.
4. Identify growth/cycle drivers and consensus expectations where available.
5. Evaluate valuation relative to history, peers and scenario economics; do not rely on a single target price.
6. State catalysts, risks, dependencies and what the market appears to already price.
7. Form a compact thesis with explicit assumptions and kill criteria.
8. Hand off conviction challenge to thesis-challenge before portfolio action.

## Decision rules
- Good business != good security at any price.
- A cheap multiple can reflect peak earnings.
- Consensus is context, not truth.
- Every material current claim needs source date and as-of relevance.

## Output contract
Business; financial quality; drivers; valuation context; catalysts; risks; variant perception; thesis; assumptions; kill criteria; evidence gaps; confidence.

## Quality checks
- [ ] Thesis horizon is explicit.
- [ ] Current and historical evidence are dated.
- [ ] Valuation and quality are separate.
- [ ] Kill criteria are falsifiable.
- [ ] Portfolio sizing is deferred.
