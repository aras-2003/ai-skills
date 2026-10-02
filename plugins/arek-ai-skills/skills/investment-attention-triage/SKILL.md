---
name: investment-attention-triage
description: 'Triage new market, company, industry and portfolio information into
  a short attention queue based on materiality, thesis impact, valuation/expectations
  and decision relevance. Use when deciding what changed, what deserves deeper research
  now, and why. Do not use as a generic news summary or as a substitute for full underwriting.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.1.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-02'
---

# Investment Attention Triage

## Purpose
Convert noisy new information into a decision-focused queue: what changed, whether it matters, where to look deeper, and why.

## Procedure
1. Load relevant portfolio, watchlist, thesis, signal history and prior attention state when available.
2. Collect only dated new information from credible sources; distinguish company facts, industry data, market reaction and commentary.
3. For each item, identify the affected thesis assumption, KPI, catalyst, risk or valuation expectation.
4. Classify materiality:
   - NOISE — no meaningful thesis or valuation implication;
   - MONITOR — potentially relevant but not decision-changing yet;
   - REVIEW — material change worth focused follow-up;
   - ESCALATE — material enough to trigger fresh underwriting/valuation/challenge.
5. Classify direction separately:
   - STRENGTHENS;
   - WEAKENS;
   - MIXED;
   - NEUTRAL.
6. Assess whether the market reaction appears broadly consistent with, smaller than, or larger than the fundamental change. Mark this as an interpretation, not fact.
7. State the specific next research question and which specialist skill/workflow should run next.
8. Persist material items and their evidence links in Signals_History / Research_Log; do not persist ordinary noise unless it helps avoid repeated re-analysis.

## Decision rules
- Headline size != materiality.
- Price reaction != thesis validation.
- A new contract matters only through likely economic contribution, strategic signal or evidence about demand.
- A company can have good news while valuation attractiveness worsens.
- Portfolio concentration can raise the decision relevance of otherwise moderate news.
- Do not escalate every positive development into a buy/add decision.
- Prefer a short queue of the few items that can change a decision.

## Output contract
### Attention queue
Instrument/theme | what changed | materiality | thesis impact | valuation/expectations implication | market reaction context | why it matters | next research question | escalation path.

### Noise suppressed
Only categories/counts unless a discarded item is counterintuitive.

### Persistence receipt
Material records written or explicit storage failure.

## Quality checks
- [ ] Every queued item says what changed versus a prior state or expectation.
- [ ] Materiality and direction are separate.
- [ ] Market reaction is not treated as proof.
- [ ] Next research question is concrete.
- [ ] Escalation routes to the smallest specialist path that can answer it.
