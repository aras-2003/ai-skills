# Investment Attention Review Workflow

## Purpose
Answer one recurring question: **what changed since the last review, what actually matters, and where is deeper research worth the time?**

This is the default monitoring workflow for existing holdings, watchlist names and tracked themes. It is not a news digest.

## Required skills
- investment-attention-triage
- investment-record-store

## Optional skills
- thesis-monitor
- market-opportunity-scan
- trend-theme-research
- security-underwriting
- valuation-scenario-review
- thesis-challenge
- portfolio-state-review

## Sequence
1. Read Portfolio_Current, Watchlist, active Thesis_Register, Market_Themes and recent Signals_History.
2. Gather only new dated company, industry, earnings/guidance, contract/order, estimate, regulatory and relevant market evidence since the last review.
3. Run investment-attention-triage.
4. Suppress ordinary news and return a short attention queue.
5. For existing holdings:
   - use thesis-monitor when a material event maps to an existing assumption or kill criterion;
   - use valuation-scenario-review when price/expectations changed enough to alter attractiveness.
6. For new candidates:
   - use market-opportunity-scan when the signal suggests a broader opportunity;
   - use security-underwriting only for REVIEW/ESCALATE items where deeper work is justified.
7. Use thesis-challenge when positive evidence risks confirmation bias or the market may already price the thesis.
8. Persist material signals, source links, attention state and any updated thesis version.

## Materiality model
Evaluate at least:
- likely revenue/earnings/FCF significance;
- evidence about demand, pricing, margins or competitive position;
- strategic relevance;
- change versus prior expectation;
- valuation/expectations already embedded in price;
- portfolio relevance, including concentration.

## Output contract
### Worth attention now
Instrument/theme | what changed | thesis impact | materiality | priced-in context | why look deeper | exact next question | next skill/workflow.

### Monitor
Potentially useful changes that do not yet justify deep research.

### No material change
Suppress detail unless requested.

### Persistence receipt
What was recorded and the effective as-of date.

## Stop conditions
Stop when every escalated item has a concrete decision-relevant research question.
Do not expand into a full market report merely because more news exists.
