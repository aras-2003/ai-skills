# Report profiles

These are default structures, not rigid templates. Skip sections that add no decision value.

## Investment — portfolio review
Default to a concise executive report, not a portfolio dump.
1. Executive summary — 3–5 decision-relevant points
2. Portfolio risk
   - **required visual-floor slot:** at least one composition/concentration visual; run capability preflight; use `BLOCKED_NO_RENDERER` if no qualifying renderer exists and `PAYLOAD_RENDERED` when a valid chart payload is produced; client display remains `NOT_OBSERVABLE` to the model
   - prefer ranked horizontal bars for many positions;
   - a donut/pie is acceptable only for a small meaningful part-to-whole (for example top categories or top positions + Other), not for a crowded 14-slice portfolio;
   - overlap/look-through matrix only if supported and decision-relevant
3. Positions requiring attention
   - only material exceptions
4. Opportunity implications
   - 2–3 detailed candidates by default
   - compress the remaining queue into watch/defer notes
5. Cross-candidate comparison
   - one compact matrix/visual
6. Decision queue — 3–5 actions/gates
7. Evidence/limitations
   - distinguish CANONICAL / USER_PROVIDED / EXTERNAL_VERIFIED / DERIVED / UNKNOWN;
   - label unreproducible supplied aggregates as USER_PROVIDED;
   - do not attribute drift cause without sufficient history/transaction evidence;
   - keep missing-record limitations compact
8. Compact canonical receipt

If canonical storage lacks current market price history needed for price context, external market-data tools may be used. Label that data external and noncanonical.

## Investment — security review
1. Investment view / thesis state
2. WHY THIS / WHY NOW
   - explicit reason the security deserves attention now;
   - 2–3 measurable supporting signals
3. Historical business performance
   - 3–4 key KPIs;
   - default 12–20 quarters where available;
   - required historical KPI visual slot when verified series exist; use the best concrete renderer available and label static output accurately
4. Market/price context
   - prefer real historical time-series;
   - default 5Y price history plus 1Y current setup when available;
   - required historical price visual slot when verified series exist; use the best concrete renderer available and label static output accurately
5. Material-event timeline
   - align dated earnings/guidance/capex/M&A/regulatory/product events to major price/KPI moves;
   - separate OBSERVED / VERIFIED EVENT / INTERPRETATION / CONFIDENCE
6. What changed fundamentally
7. Valuation / priced-in expectations
   - historical valuation context where reliable;
   - scenario range only when evidence gates permit
8. Catalysts and risks
9. Portfolio fit / sizing constraints
10. Decision state / next trigger
11. Compact evidence/receipt block

Do not use price momentum as thesis validity. External market data may supplement canonical state but must be labeled external/noncanonical.

## Investment — opportunity hunter
1. Discovery logic
   - universe scanned;
   - why existing watchlist/opportunities did not dominate candidate generation
2. Broad radar
   - roughly 10–15 candidates by default;
   - WHY THIS / WHY NOW;
   - 2–3 measurable signals;
   - failure case;
   - PROMOTE / WATCH / DEFER / REJECT
3. Top 2–3 candidates in detail by default
   - exact reason each outranked alternatives;
   - 3–4 key KPIs with 12–20 quarter history where available;
   - 5Y price history + 1Y current setup;
   - valuation history where reliable;
   - dated material-event timeline;
   - observed moves vs likely causes + confidence;
   - catalyst/risk;
   - decision implication / next gate
4. In-chat visual dashboard and historical visuals
   - add a compact shortlist dashboard after the executive summary/radar: candidate, status, why-now signal, valuation/expectation risk, portfolio fit, and next gate;
   - when at least two verified price histories overlap on comparable dates and adjustment bases, use one shared line chart indexed to 100 at the first common date; label price basis, currency, period and sources;
   - otherwise keep price coverage separate and disclose incomparable or missing slots;
   - include one or two inline visuals for the thesis-driving KPIs in each detailed candidate section; retain each metric's units and never combine unlike KPIs;
   - use a chronological line for three or more observations; depict two observations as a period comparison, not a trend;
   - prefer a real documented interactive component when callable; otherwise embed the static renderer's returned image and label it static;
   - if neither renderer can produce an inline visual, mark the exact slot blocked/failed and show a compact diagnostic table; never imply completion from a tool attempt alone;
   - do not put image data URIs, base64, chart JSON, or encoded payloads in the answer text.
5. Cross-candidate comparison
6. Remaining names compressed into watch/defer/reject
7. Research queue / next actions
8. Compact receipts / limitations

Prefer one shared indexed price comparison when it answers the same decision question better than repeated candidate price charts. Keep candidate KPI charts separate. Do not compress unlike KPIs or business models into one misleading chart.

## Investment — attention review
1. What requires attention now
   - materiality x direction matrix
2. Holdings/themes with changed evidence
3. Noise suppressed
4. Next research questions
5. receipts / limitations

## Investment — theme discovery
1. Theme mechanism
   - value-chain / mechanism diagram
2. Leading indicators
3. Beneficiaries/losers
4. Candidate security sections
5. Invalidation
6. research queue / receipts

## OAF — health check
1. Executive diagnosis
2. Domain findings
   - heatmap only if dimensions are evidence-based
3. Causal/dependency interpretation
   - inline causal map
4. Highest-leverage gaps
5. Next diagnostic/design gate
6. evidence/unknowns

## OAF — operating-model redesign
1. Design objective
2. Current-state failure modes
3. Options
   - option comparison
4. Target model
   - editable operating-model map
5. Decision rights/interfaces
   - inline flow/diagram
6. Transition
   - roadmap
7. unresolved decisions/evidence

## OAF — governance redesign
1. Governance problem
2. Material decisions/bottlenecks
3. Proposed decision path
   - governance/decision flow
4. Rights and forums
5. Escalation/evidence loop
6. pilot/transition

## OAF — enterprise architecture
1. Architecture decision question
2. Current-state evidence
3. Capability/estate implications
   - map/heatmap
4. Options
   - comparison
5. Target direction
6. transition constraints/evidence gaps

## OAF — transformation
1. Transformation boundary
2. Workstreams
3. Sequence
   - roadmap/gantt inline
4. stage gates
5. transition risks
6. 30–90 day mobilisation
7. unresolved choices

## Commerce — opportunity review
1. Decision state
2. Shortlist
   - cards
3. Evidence gates
   - heatmap
4. Candidate sections
5. smallest next tests
6. unresolved evidence

## Commerce — product deep dive
1. Product thesis
2. Evidence map
3. Gate review
   - inline gate-status panel
4. Economics
   - bridge/waterfall when numeric evidence exists
5. Competition/differentiation
   - matrix
6. supply/regulation/acquisition
7. decision and smallest next test
