# Commerce Opportunity Review Workflow

## Purpose
Orchestrate the minimum evidence-backed commerce path for discovering, screening or selecting e-commerce opportunities without running every skill by default.

## Entry modes

### Discovery mode
Use when the user asks for new product ideas or categories.
Start with `product-opportunity-discovery`, then apply only fast kill screens needed to reduce to 3–5 hypotheses.

### Known-product mode
Use when the user provides a concrete product or benchmark.
Route directly to the relevant specialists or `commerce-product-deep-dive`.

### Comparison mode
Use when multiple opportunities already have comparable evidence packs.
Compare only after missing evidence is normalized. Do not score unlike evidence as if precise.

## Routing
Select only what changes the decision:
- foreign-market thesis -> `market-transferability-review`
- unclear problem strength -> `problem-demand-validation`
- unclear market gap -> `competition-landscape-review`
- premium/commodity question -> `differentiation-review`
- price/CAC feasibility -> `unit-economics-review`
- MOQ/quality/lead-time risk -> `supplier-viability-review`
- paid-social/channel suitability -> `acquisition-fit-review`
- safety/claims/compliance complexity -> `commerce-regulatory-risk-review`

## Gate sequence
1. Problem gate.
2. Product/differentiation gate.
3. Economics gate.
4. Acquisition gate.
5. Supply/regulation gate.
6. Only after the gates: optional relative prioritisation.

## Decision rules
- Gate before score.
- Missing evidence is not a zero score and not a pass.
- Popularity, TAM or US success cannot compensate for a failed economics or compliance gate.
- A boring product can outperform a trendy one when economics, logistics and acquisition are stronger.
- If evidence packs are not comparable, state which candidate needs validation rather than ranking.
- Prefer one real market test over another research cycle once desk-research uncertainty is low.

## Output contract
### Selected path
Skill/workflow | why selected | evidence needed.

### Opportunity table
Opportunity | problem | differentiation | economics | acquisition | supply/regulation | transferability | biggest unknown.

### Decision state
BADAĆ TERAZ / TESTOWAĆ / ODŁOŻYĆ / ODRZUCIĆ.

### Next action
The smallest action that can change the decision.

## Model guidance
Default: standard for synthesis; fast for broad discovery and extraction. Escalate to strong only when a high-capital or highly regulated decision genuinely requires it.

## Stop conditions
Stop discovery when 3–5 credible hypotheses remain.
Stop analysis when a fatal gate fails.
Stop research and test when the remaining uncertainty is conversion/CAC/offer response.
