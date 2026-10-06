---
name: investment-attention-triage
description: 'Triage new market, company, industry and portfolio information into
  a short attention queue based on materiality, thesis impact, valuation/expectations
  and decision relevance. Use structured research plugins for breadth, Firecrawl/primary
  sources for verification, and canonical Investment OS history for change detection.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.2.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-02'
---

# Investment Attention Triage

## Purpose
Convert noisy new information into a decision-focused queue: what changed, whether it matters, where to look deeper, and why.

## Procedure
1. Load relevant canonical portfolio, watchlist, thesis, signal history and prior attention state.
2. Use structured equity/ETF research tools for breadth, then retrieve primary evidence for material claims where practical; Firecrawl may be used for live retrieval/parsing.
3. For each item, identify the affected thesis assumption, KPI, catalyst, risk or valuation expectation.
4. Classify materiality: NOISE / MONITOR / REVIEW / ESCALATE.
5. Classify direction separately: STRENGTHENS / WEAKENS / MIXED / NEUTRAL.
6. Assess market reaction only as an interpretation, not proof.
7. State the specific next research question and smallest specialist path.
8. Persist only material items through investment-record-store.

## Decision rules
- Headline size != materiality.
- Research-provider ranking != thesis relevance.
- Price reaction != thesis validation.
- Company good news can coexist with worse valuation.
- Portfolio concentration can raise decision relevance.

## Output contract
Attention queue; noise suppressed; provenance; next research question; escalation path; canonical persistence receipt.

## Quality checks
- [ ] Every queued item says what changed versus prior state/expectation.
- [ ] Material claims have dated provenance.
- [ ] Materiality and direction are separate.
- [ ] Persistence routes through investment-record-store.
