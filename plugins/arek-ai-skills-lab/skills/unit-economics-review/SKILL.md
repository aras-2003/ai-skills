---
name: unit-economics-review
description: >
  Evaluate e-commerce unit economics including VAT, COGS, freight, fulfilment, fees, returns and CAC headroom. Use before recommending a product test or scale decision.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Unit Economics Review

## Purpose
Determine whether the product can support acquisition and operational costs with acceptable downside.

## Procedure
1. Normalize price inclusive/exclusive of VAT.
2. Calculate or estimate separately: COGS, inbound freight/duty, fulfilment, payment fees, returns/refunds, packaging and CAC.
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
- Use code/calculation where exact inputs are available; LLM interpretation should not replace arithmetic.

## Output contract
Price | VAT | COGS | freight/duty | fulfilment | fees | returns | pre-CAC contribution | break-even CAC | target CAC | sensitivity.
Then: economics gate = pass / conditional / fail.

## Model guidance
Default: standard; deterministic calculation preferred.
