from __future__ import annotations

import argparse
import copy
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any

TWOPLACES = Decimal("0.01")


class InputError(ValueError):
    pass


def D(value: Any, field: str) -> Decimal:
    try:
        result = Decimal(str(value))
    except Exception as exc:
        raise InputError(f"{field} must be numeric") from exc
    if not result.is_finite():
        raise InputError(f"{field} must be finite")
    return result


def nonnegative(value: Any, field: str) -> Decimal:
    result = D(value, field)
    if result < 0:
        raise InputError(f"{field} must be >= 0")
    return result


def positive(value: Any, field: str) -> Decimal:
    result = D(value, field)
    if result <= 0:
        raise InputError(f"{field} must be > 0")
    return result


def money(value: Decimal) -> str:
    return str(value.quantize(TWOPLACES, rounding=ROUND_HALF_UP))


def normalize_price(data: dict[str, Any], vat_rate: Decimal) -> tuple[Decimal, Decimal]:
    price = data.get("sale_price") or {}
    amount = positive(price.get("amount"), "sale_price.amount")
    basis = price.get("basis")
    if basis == "gross":
        gross = amount
        net = gross / (Decimal("1") + vat_rate)
    elif basis == "net":
        net = amount
        gross = net * (Decimal("1") + vat_rate)
    else:
        raise InputError("sale_price.basis must be 'gross' or 'net'")
    return net, gross


def normalize_cost(
    item: dict[str, Any],
    *,
    vat_rate: Decimal,
    vat_recoverable: bool,
    quantity: Decimal,
    prefix: str,
) -> Decimal:
    amount = nonnegative(item.get("amount"), f"{prefix}.amount")
    basis = item.get("basis")
    scope = item.get("scope", "order")
    if basis not in {"gross", "net"}:
        raise InputError(f"{prefix}.basis must be 'gross' or 'net'")
    if scope not in {"unit", "order"}:
        raise InputError(f"{prefix}.scope must be 'unit' or 'order'")
    normalized = amount
    if basis == "gross" and vat_recoverable:
        normalized = amount / (Decimal("1") + vat_rate)
    if scope == "unit":
        normalized *= quantity
    return normalized


def apply_scenario(base: dict[str, Any], scenario: dict[str, Any]) -> dict[str, Any]:
    data = copy.deepcopy(base)
    if "cac" in scenario:
        data["cac"] = scenario["cac"]
    if "return_rate" in scenario:
        returns = data.setdefault("returns", {})
        if "expected_loss_per_order" in returns:
            raise InputError("return_rate sensitivity cannot be combined with returns.expected_loss_per_order")
        returns["rate"] = scenario["return_rate"]
    if "cogs_multiplier" in scenario:
        multiplier = nonnegative(scenario["cogs_multiplier"], "sensitivity.cogs_multiplier")
        cogs = data.get("costs", {}).get("cogs")
        if not isinstance(cogs, dict):
            raise InputError("cogs_multiplier sensitivity requires costs.cogs")
        cogs["amount"] = str(D(cogs.get("amount"), "costs.cogs.amount") * multiplier)
    return data


def calculate(data: dict[str, Any], include_sensitivity: bool = True) -> dict[str, Any]:
    currency = data.get("currency")
    if not isinstance(currency, str) or not currency.strip():
        raise InputError("currency is required")

    quantity = positive(data.get("quantity_per_order"), "quantity_per_order")
    vat = data.get("vat") or {}
    if "rate" not in vat:
        raise InputError("vat.rate is required; do not assume a jurisdictional default")
    vat_rate = nonnegative(vat.get("rate"), "vat.rate")
    if vat_rate >= 1:
        raise InputError("vat.rate must be expressed as a fraction below 1, e.g. 0.23")
    if not isinstance(vat.get("recoverable"), bool):
        raise InputError("vat.recoverable must be true or false")
    recoverable = vat["recoverable"]

    net_revenue, gross_revenue = normalize_price(data, vat_rate)

    costs_data = data.get("costs") or {}
    if not isinstance(costs_data, dict):
        raise InputError("costs must be a mapping")
    normalized_costs: dict[str, Decimal] = {}
    for name in ("cogs", "inbound_logistics", "fulfilment", "packaging", "other_variable"):
        item = costs_data.get(name)
        if item is None:
            continue
        if not isinstance(item, dict):
            raise InputError(f"costs.{name} must be a mapping")
        normalized_costs[name] = normalize_cost(
            item,
            vat_rate=vat_rate,
            vat_recoverable=recoverable,
            quantity=quantity,
            prefix=f"costs.{name}",
        )

    fees = data.get("fees") or {}
    fixed_fee = nonnegative(fees.get("fixed_per_order", 0), "fees.fixed_per_order")
    pct = nonnegative(fees.get("percent_rate", 0), "fees.percent_rate")
    fee_basis = fees.get("percent_basis", "gross")
    if fee_basis not in {"gross", "net"}:
        raise InputError("fees.percent_basis must be 'gross' or 'net'")
    if pct > 1:
        raise InputError("fees.percent_rate must be a fraction, e.g. 0.029")
    fee_amount = fixed_fee + pct * (gross_revenue if fee_basis == "gross" else net_revenue)

    returns = data.get("returns") or {}
    has_expected = returns.get("expected_loss_per_order") is not None
    has_rate = returns.get("rate") is not None or returns.get("loss_per_return") is not None
    if has_expected and has_rate:
        raise InputError("use either returns.expected_loss_per_order or rate/loss_per_return, not both")
    if has_expected:
        return_loss = nonnegative(returns["expected_loss_per_order"], "returns.expected_loss_per_order")
    elif has_rate:
        if returns.get("rate") is None or returns.get("loss_per_return") is None:
            raise InputError("returns.rate and returns.loss_per_return must be provided together")
        return_rate = nonnegative(returns["rate"], "returns.rate")
        if return_rate > 1:
            raise InputError("returns.rate must be <= 1")
        loss_per_return = nonnegative(returns["loss_per_return"], "returns.loss_per_return")
        return_loss = return_rate * loss_per_return
    else:
        return_loss = Decimal("0")

    total_variable = sum(normalized_costs.values(), Decimal("0")) + fee_amount + return_loss
    pre_cac = net_revenue - total_variable
    break_even_cac = pre_cac

    cac_value = data.get("cac")
    cac = None if cac_value is None else nonnegative(cac_value, "cac")
    after_cac = None if cac is None else pre_cac - cac

    required_value = data.get("required_contribution_after_cac")
    required = None if required_value is None else D(required_value, "required_contribution_after_cac")
    target_cac = None if required is None else pre_cac - required

    cash = data.get("inventory") or {}
    moq = cash.get("moq_units")
    landed = cash.get("landed_cash_cost_per_unit")
    moq_cash = None
    if moq is not None or landed is not None:
        if moq is None or landed is None:
            raise InputError("inventory.moq_units and inventory.landed_cash_cost_per_unit must be provided together")
        moq_cash = positive(moq, "inventory.moq_units") * nonnegative(
            landed, "inventory.landed_cash_cost_per_unit"
        )

    result: dict[str, Any] = {
        "currency": currency,
        "quantity_per_order": str(quantity),
        "revenue": {
            "gross": money(gross_revenue),
            "net": money(net_revenue),
            "vat_rate": str(vat_rate),
            "vat_recoverable_for_costs": recoverable,
        },
        "variable_costs_net_economic_basis": {
            **{key: money(value) for key, value in normalized_costs.items()},
            "fees": money(fee_amount),
            "expected_return_loss": money(return_loss),
            "total": money(total_variable),
        },
        "contribution": {
            "pre_cac": money(pre_cac),
            "break_even_cac": money(break_even_cac),
            "cac": None if cac is None else money(cac),
            "after_cac": None if after_cac is None else money(after_cac),
            "required_after_cac": None if required is None else money(required),
            "target_cac_from_required_contribution": None if target_cac is None else money(target_cac),
        },
        "inventory_cash_exposure": {
            "moq_cash": None if moq_cash is None else money(moq_cash)
        },
    }

    scenarios = data.get("sensitivity") or []
    if include_sensitivity:
        if not isinstance(scenarios, list):
            raise InputError("sensitivity must be a list of scenario patches")
        sensitivity_results = []
        base_without = copy.deepcopy(data)
        base_without.pop("sensitivity", None)
        for index, scenario in enumerate(scenarios, start=1):
            if not isinstance(scenario, dict):
                raise InputError(f"sensitivity[{index}] must be a mapping")
            scenario_data = apply_scenario(base_without, scenario)
            sensitivity_results.append(
                {
                    "scenario": scenario,
                    "result": calculate(scenario_data, include_sensitivity=False)["contribution"],
                }
            )
        result["sensitivity"] = sensitivity_results

    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    try:
        result = calculate(data)
    except InputError as exc:
        raise SystemExit(f"INPUT_ERROR: {exc}")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
