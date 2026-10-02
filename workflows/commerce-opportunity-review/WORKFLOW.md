# Commerce Opportunity Review Workflow

## Purpose
Orchestrate the minimum evidence-backed commerce path for discovering, screening or selecting e-commerce opportunities without running every skill by default.

## Entry modes

### Discovery mode
Use `product-opportunity-discovery` to reduce noisy market signals to 3–5 evidence-linked hypotheses before deeper validation. Do not rank numerically or treat interview intent as purchase evidence.

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
- Prefer one real-world experiment over another research cycle once desk-research uncertainty is low.
- Market test != first test: use the cheapest experiment that can falsify a decision-critical assumption before paid acquisition or inventory commitment.
- For cross-market transfer, validate target-market context prevalence, substitutes and price/logistics constraints before testing the copied source-market offer.
- Do not bundle several validation steps into one sprint when an earlier cheap screen could kill the thesis; stage evidence so each step earns the next.
- Do not invent spend caps without a user-supplied budget or an explicit sample-size/evidence basis.

## Output contract
### Selected path
Skill/workflow | why selected | evidence needed.

### Opportunity table
Opportunity | problem | differentiation | economics | acquisition | supply/regulation | transferability | biggest unknown.

### Decision state
BADAĆ TERAZ / TESTOWAĆ / ODŁOŻYĆ / ODRZUCIĆ.

### Next action
The smallest staged action that can change the decision. For cross-market transfer, show the sequence from cheapest context screen to any later offer/paid test.

## Model guidance
Default: standard for synthesis; fast for broad discovery and extraction. Broad discovery is validated on Luna for shortlist reduction from mixed signals. Escalate to strong only when a high-capital or highly regulated decision genuinely requires it.

## Stop conditions
Stop discovery when 3–5 credible hypotheses remain.
Stop analysis when a fatal gate fails.
Stop research and test when the remaining uncertainty is conversion/CAC/offer response and cheaper pre-market blockers have already been cleared.

## Visual presentation
Call `visual-output-design` when comparing multiple opportunities or evidence gates.
Prefer shortlist cards, evidence heatmaps and simple category/market comparisons. Use charts only for measured quantitative data and keep Evidence / Hypothesis / Unknown visually distinct.
