from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
RENDERER = ROOT / "runtime" / "mcp" / "chart_renderer.py"


def load_renderer():
    spec = importlib.util.spec_from_file_location("arek_chart_renderer", RENDERER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load chart renderer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ChartRendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.renderer = load_renderer()

    def test_bar_chart_returns_png_image(self) -> None:
        image = self.renderer.render_bar_chart(
            labels=["ACN", "IUIT", "SMH"],
            values=[25.26, 22.16, 5.68],
            title="Portfolio concentration",
            unit="%",
        )
        self.assertIsNotNone(image.data)
        self.assertTrue(image.data.startswith(b"\x89PNG\r\n\x1a\n"))

    def test_line_chart_returns_png_image(self) -> None:
        image = self.renderer.render_line_chart(
            x_labels=["2026-01", "2026-02", "2026-03"],
            series_names=["Portfolio"],
            series_values=[[100.0, 103.5, 101.2]],
            title="Portfolio performance",
            unit="index",
        )
        self.assertIsNotNone(image.data)
        self.assertTrue(image.data.startswith(b"\x89PNG\r\n\x1a\n"))

    def test_invalid_parallel_data_fails_closed(self) -> None:
        with self.assertRaises(Exception):
            self.renderer.render_bar_chart(
                labels=["A", "B"],
                values=[1.0],
            )


if __name__ == "__main__":
    unittest.main()
