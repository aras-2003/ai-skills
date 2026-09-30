# Unit economics calculator input contract

Use the calculator only when the required conventions are explicitly known.

Required:
- `currency`;
- `quantity_per_order`;
- `sale_price.amount` and `sale_price.basis` = `gross` or `net`;
- `vat.rate` as an explicit fraction (for example `0.23`);
- `vat.recoverable` as an explicit boolean;
- each supplied variable cost states `amount`, `basis` (`gross`/`net`) and `scope` (`unit`/`order`).

Optional:
- fee fixed amount and percentage basis;
- returns either as an explicit expected loss per order **or** return rate × loss per return, never both;
- CAC;
- required contribution after CAC;
- MOQ and landed cash cost per unit, provided together;
- sensitivity scenario patches for CAC, return rate or COGS multiplier.

The calculator never assumes VAT, recoverability, target CAC or test budget. Missing required conventions remain unresolved rather than being filled with jurisdiction defaults.
