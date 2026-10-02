---
name: security-underwriting
description: 'Underwrite one equity or ETF as an investment using structured equity
  research for breadth and primary filings/IR for decision-critical verification,
  then analyze economics, financial quality, growth drivers, valuation, catalysts,
  risks, variant perception and thesis invalidation. Do not use for broad market scanning.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.4.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-02'
---

# Security Underwriting

## Purpose
Produce an evidence-backed investment case that can later be challenged, valued, sized and monitored.

## Research routing
- Use structured equity/ETF research plugins for fast context, estimates, peer framing and screening.
- For decision-critical financial metrics, prefer company filings, IR releases, official ETF/provider data and regulators.
- Use Firecrawl to retrieve/parse primary pages or filings when helpful.
- Use canonical prior thesis/portfolio context from investment-record-store.
- Research-provider outputs are evidence inputs, never canonical portfolio state.

## Procedure
1. Define instrument, thesis horizon and current as-of date.
2. Load prior thesis/research/portfolio context when available.
3. Explain business model, segment economics, competitive position and capital intensity.
4. Review revenue, margins, cash flow, ROIC/returns, balance sheet, dilution and capex using dated sources.
5. Run a hard evidence-sanity gate on every decision-critical reported metric before any valuation or sizing:
   - verify the exact metric in primary-source context where possible;
   - confirm period, units, currency, GAAP/non-GAAP basis, quarterly vs annual basis, per-share vs absolute values and arithmetic consistency;
   - compare magnitude against adjacent disclosures and prior-period/company scale;
   - extraordinary values trigger re-verification, not automatic rejection;
   - mark unresolved conflicting/extraction-uncertain figures UNVERIFIED or CONFLICTED.
6. If any decision-critical metric remains UNVERIFIED/CONFLICTED:
   - classify research state as VERIFY / RESEARCH;
   - do not compute P/E, FCF yield, numeric valuation scenarios or numeric sizing from those figures;
   - state exactly what must be verified next.
7. Only after the evidence gate passes, identify growth/cycle drivers and consensus expectations.
8. Evaluate valuation relative to history, peers and scenario economics.
9. Explicitly separate business-thesis strength, security attractiveness at the current price and priced-in expectations.
10. State catalysts, risks, dependencies and variant perception.
11. Form a compact thesis with explicit assumptions and kill criteria.
12. Hand off conviction challenge to thesis-challenge before portfolio action.

## Decision rules
- Source existence is not evidence that an extracted metric is correct.
- Structured research is a speed layer, not a substitute for primary-source verification of critical figures.
- Extreme numbers may be real; verify before accepting or rejecting them.
- Good business != good security at any price.
- A cheap multiple can reflect peak earnings.
- Never pass UNVERIFIED/CONFLICTED critical metrics into valuation or sizing.

## Output contract
Business; financial quality; evidence-sanity status; verified/blocked metrics; drivers; business-thesis strength; valuation context if permitted; priced-in expectations; security attractiveness; catalysts; risks; variant perception; thesis; assumptions; kill criteria; exact verification requirements; confidence; provenance.

## Quality checks
- [ ] Prior canonical context was attempted when relevant.
- [ ] Current and historical evidence are dated.
- [ ] Critical metrics were independently verified in primary-source context.
- [ ] Extreme values were verified rather than rejected merely for magnitude.
- [ ] No valuation or sizing was computed from blocked metrics.
- [ ] Business thesis and security attractiveness are separate.
- [ ] Kill criteria are falsifiable.
