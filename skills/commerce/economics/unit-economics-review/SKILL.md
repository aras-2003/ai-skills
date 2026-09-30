---
name: unit-economics-review
description: >
  Evaluate e-commerce unit economics including VAT, COGS, freight, fulfilment, fees, returns and CAC headroom. Use before recommending a product test or scale decision.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Unit Economics Review

## Purpose
Determine whether the product can support acquisition and operational costs with acceptable downside.


## Preconditions
Use the deterministic calculator when exact arithmetic is requested and the required conventions in `references/input-contract.md` are supplied. Currency, quantity/order, sale-price basis, VAT rate and recoverability must be explicit; never assume a jurisdictional VAT rate.

## Inputs and evidence
Keep net/gross cost basis, unit/order scope, fees, return-loss model, CAC and required contribution explicit. Treat MOQ/cash exposure separately from per-order economics.

## Uncertainty and tool failure
Missing conventions make the result unresolved/provisional. If the calculator cannot be executed, state that arithmetic was not tool-verified and do not claim it ran. Never invent target CAC or spend caps.

## Procedure
1. Verify the explicit input conventions in `references/input-contract.md`; do not fill missing VAT, recoverability, cost basis or quantity assumptions.
2. For exact inputs, run `scripts/calculator.py` and preserve its normalized net/gross basis in the analysis.
3. Keep COGS, inbound freight/duty, fulfilment, payment fees, returns/refunds and packaging separate.
4. Derive pre-CAC contribution and break-even CAC. Derive target CAC only when a required contribution after CAC is supplied.
5. Run only user/evidence-supplied sensitivity scenarios; do not invent scenario ranges.
6. Flag cash/MOQ/inventory exposure separately from per-order margin.
7. Mark assumptions, unresolved inputs and whether calculator execution succeeded explicitly.

## Decision rules
- Gross margin != contribution margin.
- High markup != healthy paid-acquisition economics.
- If break-even CAC leaves no realistic margin of safety, fail the gate.
- Do not hide unknown fulfilment or return costs inside COGS.
- If landed cost is incomplete, label break-even CAC as provisional and do not treat it as reliable test headroom.
- Break-even CAC is a ceiling, not a target CAC.
- Target CAC requires an explicit contribution or margin objective; do not invent a "safe" target as an arbitrary percentage below break-even.
- Use code/calculation where exact inputs are available; LLM interpretation should not replace arithmetic.

## Output contract
State calculator status: executed / not executed / unresolved inputs.
Then report: currency | quantity/order | gross/net price | VAT convention | COGS | freight/duty | fulfilment | fees | returns | pre-CAC contribution | break-even CAC | target CAC (only if derived from required contribution) | supplied sensitivity.
Keep MOQ/cash exposure in a separate block.
Then: economics gate = pass / conditional / fail / unresolved.

## Model guidance
Default: standard; deterministic calculation preferred.
