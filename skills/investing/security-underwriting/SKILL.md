---
name: security-underwriting
description: >
  Underwrite one equity or ETF as an investment by analyzing business economics, financial quality, growth drivers,
  valuation context, catalysts, risks, variant perception and thesis invalidation. Use after a security enters the
  research queue or when the user asks for a full investment case. Do not use for broad market scanning.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.3.0"
  maturity: production
  risk: high
  last_reviewed: 2026-10-02
  execution:
    default_model_class: strong
---

# Security Underwriting

## Purpose
Produce an evidence-backed investment case that can later be challenged, valued, sized and monitored.

## Procedure
1. Define instrument, thesis horizon and current as-of date.
2. Explain business model, segment economics, competitive position and capital intensity.
3. Review revenue, margins, cash flow, ROIC/returns, balance sheet, dilution and capex using dated sources.
4. Run a hard evidence-sanity gate on every decision-critical reported metric before any valuation or sizing:
   - verify the exact metric in primary-source context where possible;
   - confirm period, units, currency, GAAP/non-GAAP basis, quarterly vs annual basis, per-share vs absolute values and simple arithmetic consistency;
   - compare magnitude against adjacent disclosures and prior-period/company scale;
   - treat extraordinary jumps, implausible margins/EPS/cash-flow levels, or ambiguous extraction as a trigger for re-verification, even when a source URL exists;
   - when a critical figure is implausible, internally inconsistent, extraction-uncertain or conflicts with another source, mark it UNVERIFIED or CONFLICTED and re-read the primary filing/release.
5. If any decision-critical metric remains UNVERIFIED/CONFLICTED after re-verification:
   - classify research state as VERIFY / RESEARCH;
   - do not compute or quote P/E, FCF yield or other valuation multiples from those figures;
   - do not build numeric bear/base/bull valuation scenarios from those figures;
   - do not hand those figures to position-sizing-review;
   - state exactly what must be verified next.
6. Only after the hard gate passes, identify growth/cycle drivers and consensus expectations where available.
7. Evaluate valuation relative to history, peers and scenario economics; do not rely on a single target price.
8. Explicitly separate:
   - business-thesis strength;
   - security attractiveness at the current price;
   - what expectations appear already priced in.
9. State catalysts, risks, dependencies and variant perception.
10. Form a compact thesis with explicit assumptions and kill criteria.
11. Hand off conviction challenge to thesis-challenge before portfolio action.

## Decision rules
- Source existence is not evidence that an extracted metric is correct.
- Good business != good security at any price.
- A cheap multiple can reflect peak earnings.
- Consensus is context, not truth.
- Every material current claim needs source date and as-of relevance.
- Never pass an UNVERIFIED/CONFLICTED decision-critical metric into valuation or sizing.
- When evidence quality is insufficient, the correct state is VERIFY / RESEARCH, not false precision.

## Output contract
Business; financial quality; evidence-sanity status; verified/blocked metrics; drivers; business-thesis strength; valuation context if permitted; priced-in expectations; security attractiveness; catalysts; risks; variant perception; thesis; assumptions; kill criteria; exact verification requirements; confidence.

## Quality checks
- [ ] Thesis horizon is explicit.
- [ ] Current and historical evidence are dated.
- [ ] Critical metrics were independently sanity-checked in primary-source context.
- [ ] Implausible/extraction-uncertain metrics are blocked as UNVERIFIED/CONFLICTED.
- [ ] No valuation or sizing was computed from blocked metrics.
- [ ] Business thesis and security attractiveness are separate.
- [ ] Priced-in expectations are explicit only when evidence permits.
- [ ] Kill criteria are falsifiable.
