from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CALC_PATH = ROOT / "skills/commerce/economics/unit-economics-review/scripts/calculator.py"
spec = importlib.util.spec_from_file_location("unit_economics_calculator", CALC_PATH)
calc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(calc)


class UnitEconomicsCalculatorTests(unittest.TestCase):
    def base(self) -> dict:
        return {
            "currency": "PLN",
            "quantity_per_order": 1,
            "sale_price": {"amount": 123, "basis": "gross"},
            "vat_rate": 0.23,
            "input_vat_recoverable": True,
            "costs": [
                {"name": "cogs", "amount": 12.3, "basis": "gross", "scope": "unit"},
                {"name": "fulfilment", "amount": 10, "basis": "net", "scope": "order"},
            ],
            "returns": {"mode": "none"},
        }

    def test_gross_sale_and_recoverable_input_vat(self) -> None:
        out = calc.calculate(self.base())
        self.assertEqual(out["net_revenue_per_order"], "100.00")
        self.assertEqual(out["pre_cac_contribution"], "80.00")
        self.assertEqual(out["break_even_cac"], "80.00")
        self.assertIsNone(out["target_cac"])

    def test_nonrecoverable_input_vat_keeps_gross_cost(self) -> None:
        data = self.base()
        data["input_vat_recoverable"] = False
        out = calc.calculate(data)
        self.assertEqual(out["pre_cac_contribution"], "77.70")

    def test_quantity_scales_unit_cost_not_order_cost(self) -> None:
        data = self.base()
        data["quantity_per_order"] = 2
        out = calc.calculate(data)
        self.assertEqual(out["pre_cac_contribution"], "70.00")

    def test_returns_modes_are_exclusive_and_not_double_counted(self) -> None:
        data = self.base()
        data["returns"] = {"mode": "rate_x_loss", "return_rate": 0.2, "loss_per_return": 25}
        out = calc.calculate(data)
        self.assertEqual(out["return_loss_per_order"], "5.00")
        self.assertEqual(out["pre_cac_contribution"], "75.00")

    def test_target_cac_requires_explicit_required_contribution(self) -> None:
        data = self.base()
        data["required_contribution_after_cac"] = 25
        out = calc.calculate(data)
        self.assertEqual(out["target_cac"], "55.00")

    def test_weighted_blanket_baseline(self) -> None:
        data = {
            "currency": "PLN",
            "quantity_per_order": 1,
            "sale_price": {"amount": 299, "basis": "gross"},
            "vat_rate": 0.23,
            "input_vat_recoverable": True,
            "costs": [
                {"name": "cogs", "amount": 95, "basis": "net", "scope": "order"},
                {"name": "freight-duty", "amount": 42, "basis": "net", "scope": "order"},
                {"name": "fulfilment-packaging", "amount": 32, "basis": "net", "scope": "order"},
                {"name": "payment-fees", "amount": 7, "basis": "net", "scope": "order"},
            ],
            "returns": {"mode": "expected_loss_per_order", "amount": 45},
        }
        out = calc.calculate(data)
        self.assertEqual(out["net_revenue_per_order"], "243.09")
        self.assertEqual(out["break_even_cac"], "22.09")

    def test_invalid_quantity_and_vat_are_rejected(self) -> None:
        data = self.base()
        data["quantity_per_order"] = 0
        with self.assertRaises(ValueError):
            calc.calculate(data)
        data = self.base()
        data["vat_rate"] = None
        with self.assertRaises(ValueError):
            calc.calculate(data)


if __name__ == "__main__":
    unittest.main()
