---
name: unit-economics-review
description: 'Evaluate e-commerce unit economics including VAT, COGS, freight, fulfilment,
  fees, returns and CAC headroom. Use before recommending a product test or scale
  decision.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.1.0
  maturity: production
  risk: medium
  last_reviewed: '2026-09-30'
---

# Unit Economics Review

## Purpose
Determine whether an e-commerce offer can support its variable costs and acquisition while keeping inventory/cash exposure visible.

## Preconditions
Require explicit commercial conventions for any exact calculation. Missing conventions produce a provisional/unresolved result, not guessed defaults.

## Inputs
For deterministic calculation provide:
- currency;
- quantity per order;
- sale price amount and basis: gross or net;
- VAT rate as an explicit fraction and whether input VAT on costs is recoverable;
- variable costs with amount, net/gross basis and unit/order scope: COGS, inbound logistics, fulfilment, packaging and other variable cost;
- payment fee: fixed amount and/or percentage plus gross/net fee basis;
- returns as either expected loss per order **or** return rate + loss per return, never both;
- CAC when known;
- required contribution after CAC only when a target CAC is requested;
- MOQ and landed cash cost per unit separately for inventory exposure;
- sensitivity scenarios only for values/ranges supplied by the user/evidence.

## Procedure
1. Normalize gross/net sale price using the supplied VAT rate.
2. Normalize variable costs using their declared basis/scope and VAT recoverability.
3. Calculate fees and expected return loss once; reject double-counted return models.
4. Calculate pre-CAC contribution and break-even CAC.
5. If CAC is supplied, calculate contribution after CAC.
6. Calculate target CAC only from an explicit required contribution after CAC.
7. Keep MOQ/cash exposure separate from per-order contribution.
8. Run only user/evidence-supplied sensitivity scenarios.
9. Interpret the arithmetic and state unresolved assumptions.

When tool execution is available, use `scripts/calculator.py` for exact arithmetic. The model interprets; code calculates.

## Decision rules
- Gross margin != contribution margin.
- Break-even CAC is a ceiling, not a target.
- Do not invent a VAT rate, target CAC, spend cap, return rate or fee basis.
- Unknown landed/return/fulfilment inputs make economics provisional.
- Inventory cash exposure is not a per-order variable-cost deduction unless the input explicitly says so.
- If expected CAC exceeds break-even even under supplied favorable sensitivity, the current price/cost/channel thesis fails.
- A failed thesis does not automatically reject the category.

## Tool failure / no-execution fallback
If `scripts/calculator.py` cannot be executed, do not claim it ran. Either:
- perform clearly shown arithmetic from complete explicit inputs and label it manual; or
- return `UNRESOLVED` with the missing conventions needed for a calculation.

## Output contract
Currency and order quantity; gross/net revenue; normalized variable costs; expected return loss; pre-CAC contribution; break-even CAC; supplied CAC and after-CAC contribution; target CAC only when derived from an explicit required contribution; inventory cash exposure; supplied sensitivity; assumptions/unknowns.

Economics gate: `pass / conditional / fail / unresolved`.

## Quality checks
- [ ] VAT rate and recoverability came from input, not a jurisdictional assumption.
- [ ] Gross/net and unit/order bases are explicit.
- [ ] Returns are counted once.
- [ ] Break-even CAC is not presented as target CAC.
- [ ] Target CAC has an explicit contribution objective.
- [ ] MOQ cash exposure is separated from unit economics.
- [ ] Tool execution is not claimed if unavailable.
