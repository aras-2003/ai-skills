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
2. Business performance
   - 3–4 key KPIs
3. Market/price context
   - prefer real historical time-series;
   - support 3M / 6M / 12M switching when the renderer and verified data support it
4. What changed fundamentally
5. Valuation / priced-in expectations
   - scenario range only when evidence gates permit
6. Catalysts and risks
   - compact timeline or matrix
7. Portfolio fit / sizing constraints
8. Decision state / next trigger
9. Compact evidence/receipt block

Do not use price momentum as thesis validity. External market data may supplement canonical state but must be labeled external/noncanonical.

## Investment — opportunity hunter
1. Executive shortlist context
2. Top 2–3 candidates in detail by default
   - thesis/setup
   - 3–4 key KPIs
   - price/valuation context
   - catalyst/risk
   - decision implication / next gate
3. One cross-candidate visual/matrix
4. Remaining names compressed into watch/defer
5. Research queue / next actions
6. Compact receipts / limitations

Prefer one shared comparison/time-series visual over repetitive per-candidate charts when it communicates the decision better.

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
