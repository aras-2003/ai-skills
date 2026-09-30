from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any

MONEY = Decimal("0.01")


def D(value: Any, field: str) -> Decimal:
    try:
        result = Decimal(str(value))
    except Exception as exc:
        raise ValueError(f"{field} must be numeric") from exc
    if not result.is_finite():
        raise ValueError(f"{field} must be finite")
    return result


def money(value: Decimal) -> str:
    return str(value.quantize(MONEY, rounding=ROUND_HALF_UP))


def _net_amount(amount: Decimal, basis: str, vat_rate: Decimal, input_vat_recoverable: bool) -> Decimal:
    if basis == "net":
        return amount
    if basis != "gross":
        raise ValueError("cost basis must be 'net' or 'gross'")
    if input_vat_recoverable:
        return amount / (Decimal("1") + vat_rate)
    return amount


def calculate(data: dict[str, Any]) -> dict[str, Any]:
    currency = str(data.get("currency") or "").strip()
    if not currency:
        raise ValueError("currency is required")

    quantity = D(data.get("quantity_per_order"), "quantity_per_order")
    if quantity <= 0:
        raise ValueError("quantity_per_order must be > 0")

    vat_rate = D(data.get("vat_rate"), "vat_rate")
    if vat_rate < 0 or vat_rate >= 1:
        raise ValueError("vat_rate must be in [0, 1)")
    input_vat_recoverable = data.get("input_vat_recoverable")
    if not isinstance(input_vat_recoverable, bool):
        raise ValueError("input_vat_recoverable must be boolean")

    sale = data.get("sale_price") or {}
    sale_amount = D(sale.get("amount"), "sale_price.amount")
    if sale_amount < 0:
        raise ValueError("sale_price.amount must be >= 0")
    sale_basis = sale.get("basis")
    if sale_basis == "gross":
        net_revenue = sale_amount / (Decimal("1") + vat_rate)
        gross_revenue = sale_amount
    elif sale_basis == "net":
        net_revenue = sale_amount
        gross_revenue = sale_amount * (Decimal("1") + vat_rate)
    else:
        raise ValueError("sale_price.basis must be 'gross' or 'net'")

    costs_total = Decimal("0")
    normalized_costs: list[dict[str, str]] = []
    for i, row in enumerate(data.get("costs") or []):
        if not isinstance(row, dict):
            raise ValueError(f"costs[{i}] must be an object")
        label = str(row.get("name") or f"cost-{i+1}")
        amount = D(row.get("amount"), f"costs[{i}].amount")
        if amount < 0:
            raise ValueError(f"costs[{i}].amount must be >= 0")
        scope = row.get("scope")
        if scope not in {"unit", "order"}:
            raise ValueError(f"costs[{i}].scope must be 'unit' or 'order'")
        normalized = _net_amount(amount, str(row.get("basis")), vat_rate, input_vat_recoverable)
        if scope == "unit":
            normalized *= quantity
        costs_total += normalized
        normalized_costs.append({"name": label, "normalized_order_cost": money(normalized)})

    fee = data.get("payment_fee")
    payment_fee = Decimal("0")
    if fee is not None:
        if not isinstance(fee, dict):
            raise ValueError("payment_fee must be an object")
        fixed = D(fee.get("fixed", 0), "payment_fee.fixed")
        rate = D(fee.get("rate", 0), "payment_fee.rate")
        if fixed < 0 or rate < 0:
            raise ValueError("payment fee values must be >= 0")
        base = fee.get("base", "gross")
        if base == "gross":
            fee_base = gross_revenue
        elif base == "net":
            fee_base = net_revenue
        else:
            raise ValueError("payment_fee.base must be 'gross' or 'net'")
        payment_fee = fixed + rate * fee_base

    returns = data.get("returns") or {"mode": "none"}
    if not isinstance(returns, dict):
        raise ValueError("returns must be an object")
    mode = returns.get("mode", "none")
    if mode == "none":
        return_loss = Decimal("0")
    elif mode == "expected_loss_per_order":
        return_loss = D(returns.get("amount"), "returns.amount")
    elif mode == "rate_x_loss":
        rate = D(returns.get("return_rate"), "returns.return_rate")
        loss = D(returns.get("loss_per_return"), "returns.loss_per_return")
        if rate < 0 or rate > 1 or loss < 0:
            raise ValueError("returns rate/loss values are invalid")
        return_loss = rate * loss
    else:
        raise ValueError("returns.mode must be none, expected_loss_per_order or rate_x_loss")
    if return_loss < 0:
        raise ValueError("return loss must be >= 0")

    pre_cac = net_revenue - costs_total - payment_fee - return_loss
    cac = data.get("cac")
    post_cac = None
    if cac is not None:
        cac_value = D(cac, "cac")
        if cac_value < 0:
            raise ValueError("cac must be >= 0")
        post_cac = pre_cac - cac_value

    required = data.get("required_contribution_after_cac")
    target_cac = None
    if required is not None:
        required_value = D(required, "required_contribution_after_cac")
        target_cac = pre_cac - required_value

    moq_units = data.get("moq_units")
    inventory_cash = None
    if moq_units is not None:
        moq = D(moq_units, "moq_units")
        if moq < 0:
            raise ValueError("moq_units must be >= 0")
        unit_cash_rows = [
            row for row in (data.get("costs") or [])
            if isinstance(row, dict) and row.get("scope") == "unit"
        ]
        unit_cash = sum(
            (_net_amount(D(row.get("amount"), "cost.amount"), str(row.get("basis")), vat_rate, input_vat_recoverable)
             for row in unit_cash_rows),
            Decimal("0"),
        )
        inventory_cash = moq * unit_cash

    return {
        "currency": currency,
        "quantity_per_order": str(quantity),
        "net_revenue_per_order": money(net_revenue),
        "gross_revenue_per_order": money(gross_revenue),
        "normalized_costs": normalized_costs,
        "payment_fee_per_order": money(payment_fee),
        "return_loss_per_order": money(return_loss),
        "pre_cac_contribution": money(pre_cac),
        "break_even_cac": money(pre_cac),
        "target_cac": money(target_cac) if target_cac is not None else None,
        "post_cac_contribution": money(post_cac) if post_cac is not None else None,
        "inventory_cash_exposure": money(inventory_cash) if inventory_cash is not None else None,
        "assumptions": {
            "vat_rate": str(vat_rate),
            "input_vat_recoverable": input_vat_recoverable,
            "sale_price_basis": sale_basis,
            "returns_mode": mode,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    print(json.dumps(calculate(data), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
