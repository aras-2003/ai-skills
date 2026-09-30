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

## Preconditions and inputs
Required for a non-provisional calculation:
- currency;
- quantity per order;
- sale price amount and whether it is gross or net;
- explicit VAT rate and whether input VAT is recoverable;
- each material variable cost with net/gross basis and unit/order scope;
- returns represented once, either as expected loss per order or return-rate × loss-per-return.

Optional:
- payment-fee fixed/rate basis;
- observed CAC;
- required contribution after CAC;
- MOQ for separate inventory cash exposure.

If a required convention is missing, return a provisional result and list the missing input instead of assuming a tax rate, target CAC or spend cap.

## Procedure
1. When exact inputs are available, run `scripts/calculator.py` using the contract in `references/input-schema.json`; otherwise state why deterministic calculation is unresolved.
2. Normalize sale price and costs using the supplied VAT/basis conventions. Calculate separately: COGS, inbound freight/duty, fulfilment, payment fees, returns/refunds, packaging and CAC.
3. Derive gross margin, pre-CAC contribution, break-even CAC and target CAC headroom.
4. Run sensitivity at minimum for CAC, COGS and returns.
5. Flag cash/MOQ/inventory exposure separately from per-order margin.
6. Mark assumptions explicitly.

## Decision rules
- Gross margin != contribution margin.
- High markup != healthy paid-acquisition economics.
- If break-even CAC leaves no realistic margin of safety, fail the gate.
- Do not hide unknown fulfilment or return costs inside COGS.
- If landed cost is incomplete, label break-even CAC as provisional and do not treat it as reliable test headroom.
- Break-even CAC is a ceiling, not a target CAC.
- Target CAC requires an explicit contribution or margin objective; do not invent a "safe" target as an arbitrary percentage below break-even.
- Use the deterministic calculator where exact inputs are available; LLM interpretation must not replace arithmetic.
- Never assume a jurisdictional VAT rate.
- Never count both a returns allowance and the same return loss again through a probability model.
- Keep per-order contribution separate from MOQ/inventory cash exposure.
- If the runtime cannot execute the calculator, disclose that limitation and show formulas/inputs as a provisional manual calculation; do not claim the script ran.

## Output contract
Currency | quantity/order | gross/net sale price | VAT convention | normalized costs | returns convention | pre-CAC contribution | break-even CAC | target CAC (only if required contribution was supplied) | observed CAC | sensitivity.
Then: economics gate = pass / conditional / fail / unresolved.
Always label provisional calculations and unresolved inputs.

## Model guidance
Default: standard; deterministic calculation preferred.
