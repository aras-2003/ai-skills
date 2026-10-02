---
name: security-underwriting
description: >
  Underwrite one equity or ETF as an investment by analyzing business economics, financial quality, growth drivers,
  valuation context, catalysts, risks, variant perception and thesis invalidation. Use after a security enters the
  research queue or when the user asks for a full investment case. Do not use for broad market scanning.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.2.0"
  maturity: production
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
4. Run an evidence sanity gate on decision-critical figures:
   - prefer the primary filing/earnings release for exact reported metrics;
   - check units, period, GAAP/non-GAAP basis and simple arithmetic consistency;
   - compare scale against adjacent company disclosures or prior-period ranges;
   - when a figure is implausible, internally inconsistent or source extraction is uncertain, mark it UNVERIFIED/CONFLICTED and resolve before using it in valuation or sizing.
5. Identify growth/cycle drivers and consensus expectations where available.
6. Evaluate valuation relative to history, peers and scenario economics; do not rely on a single target price.
7. Explicitly separate:
   - business-thesis strength;
   - security attractiveness at the current price;
   - what expectations appear already priced in.
8. State catalysts, risks, dependencies and variant perception.
9. Form a compact thesis with explicit assumptions and kill criteria.
10. Hand off conviction challenge to thesis-challenge before portfolio action.

## Decision rules
- Good business != good security at any price.
- A cheap multiple can reflect peak earnings.
- Consensus is context, not truth.
- Every material current claim needs source date and as-of relevance.
- Do not pass an unverified decision-critical metric into valuation or sizing.
- When evidence quality is insufficient, the correct state is VERIFY / RESEARCH, not false precision.

## Output contract
Business; financial quality; evidence-sanity status; drivers; business-thesis strength; valuation context; priced-in expectations; security attractiveness; catalysts; risks; variant perception; thesis; assumptions; kill criteria; evidence gaps; confidence.

## Quality checks
- [ ] Thesis horizon is explicit.
- [ ] Current and historical evidence are dated.
- [ ] Decision-critical metrics passed sanity/provenance checks or are blocked as unverified.
- [ ] Business thesis and security attractiveness are separate.
- [ ] Priced-in expectations are explicit.
- [ ] Kill criteria are falsifiable.
- [ ] Portfolio sizing is deferred.
