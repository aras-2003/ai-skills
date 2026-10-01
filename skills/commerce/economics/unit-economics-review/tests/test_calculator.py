from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "calculator.py"
spec = importlib.util.spec_from_file_location("unit_economics_calculator", MODULE_PATH)
calculator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(calculator)


def base() -> dict:
    return {
        "currency": "PLN",
        "quantity_per_order": 1,
        "sale_price": {"amount": 123, "basis": "gross"},
        "vat": {"rate": 0.23, "recoverable": True},
        "costs": {
            "cogs": {"amount": 24.6, "basis": "gross", "scope": "unit"},
            "fulfilment": {"amount": 10, "basis": "net", "scope": "order"},
        },
        "fees": {"fixed_per_order": 0, "percent_rate": 0, "percent_basis": "gross"},
        "returns": {"expected_loss_per_order": 5},
        "cac": 20,
        "required_contribution_after_cac": 15,
    }


class CalculatorTests(unittest.TestCase):
    def test_gross_price_and_recoverable_cost_vat(self) -> None:
        result = calculator.calculate(base())
        self.assertEqual("100.00", result["revenue"]["net"])
        self.assertEqual("20.00", result["variable_costs_net_economic_basis"]["cogs"])
        self.assertEqual("65.00", result["contribution"]["pre_cac"])
        self.assertEqual("45.00", result["contribution"]["after_cac"])
        self.assertEqual("50.00", result["contribution"]["target_cac_from_required_contribution"])

    def test_nonrecoverable_gross_cost_stays_gross(self) -> None:
        data = base()
        data["vat"]["recoverable"] = False
        result = calculator.calculate(data)
        self.assertEqual("24.60", result["variable_costs_net_economic_basis"]["cogs"])

    def test_net_sale_price_is_grossed_up(self) -> None:
        data = base()
        data["sale_price"] = {"amount": 100, "basis": "net"}
        result = calculator.calculate(data)
        self.assertEqual("100.00", result["revenue"]["net"])
        self.assertEqual("123.00", result["revenue"]["gross"])

    def test_explicit_different_vat_rate(self) -> None:
        data = base()
        data["sale_price"] = {"amount": 120, "basis": "gross"}
        data["vat"]["rate"] = 0.20
        result = calculator.calculate(data)
        self.assertEqual("100.00", result["revenue"]["net"])

    def test_quantity_multiplies_unit_cost(self) -> None:
        data = base()
        data["quantity_per_order"] = 3
        result = calculator.calculate(data)
        self.assertEqual("60.00", result["variable_costs_net_economic_basis"]["cogs"])

    def test_returns_rate_model(self) -> None:
        data = base()
        data["returns"] = {"rate": 0.1, "loss_per_return": 50}
        result = calculator.calculate(data)
        self.assertEqual("5.00", result["variable_costs_net_economic_basis"]["expected_return_loss"])

    def test_returns_models_cannot_be_double_counted(self) -> None:
        data = base()
        data["returns"] = {"expected_loss_per_order": 5, "rate": 0.1, "loss_per_return": 50}
        with self.assertRaises(calculator.InputError):
            calculator.calculate(data)

    def test_missing_vat_is_unresolved_not_defaulted(self) -> None:
        data = base()
        del data["vat"]["rate"]
        with self.assertRaisesRegex(calculator.InputError, "vat.rate is required"):
            calculator.calculate(data)

    def test_zero_quantity_is_invalid(self) -> None:
        data = base()
        data["quantity_per_order"] = 0
        with self.assertRaises(calculator.InputError):
            calculator.calculate(data)

    def test_moq_cash_is_separate(self) -> None:
        data = base()
        data["inventory"] = {"moq_units": 200, "landed_cash_cost_per_unit": 12.5}
        result = calculator.calculate(data)
        self.assertEqual("2500.00", result["inventory_cash_exposure"]["moq_cash"])
        self.assertEqual("65.00", result["contribution"]["pre_cac"])

    def test_user_supplied_sensitivity(self) -> None:
        data = base()
        data["returns"] = {"rate": 0.1, "loss_per_return": 50}
        data["sensitivity"] = [
            {"cac": 30},
            {"return_rate": 0.2},
            {"cogs_multiplier": 1.5},
        ]
        result = calculator.calculate(data)
        self.assertEqual(3, len(result["sensitivity"]))


if __name__ == "__main__":
    unittest.main()
