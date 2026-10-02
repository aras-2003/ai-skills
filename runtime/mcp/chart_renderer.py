# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "mcp>=2,<3",
#   "matplotlib>=3.9,<4",
# ]
# ///

from __future__ import annotations

from io import BytesIO
from typing import Sequence

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mcp.server import MCPServer
from mcp.server.mcpserver import Image
from mcp.server.mcpserver.exceptions import ToolError

mcp = MCPServer(
    "Arek deterministic chart renderer",
    instructions=(
        "Render factual quantitative charts from explicit numeric inputs. "
        "Never infer missing values. Preserve labels, order and units."
    ),
)


def _validate_parallel(labels: Sequence[str], values: Sequence[float]) -> None:
    if not labels or not values:
        raise ToolError("labels and values must be non-empty")
    if len(labels) != len(values):
        raise ToolError("labels and values must have equal length")
    if len(labels) > 80:
        raise ToolError("maximum 80 data points per chart")


def _png(fig) -> Image:
    buffer = BytesIO()
    fig.savefig(buffer, format="png", dpi=160, bbox_inches="tight")
    plt.close(fig)
    return Image(data=buffer.getvalue(), format="png")


@mcp.tool()
def render_bar_chart(
    labels: list[str],
    values: list[float],
    title: str = "",
    unit: str = "",
    horizontal: bool = True,
) -> Image:
    """Render a deterministic factual bar chart from explicit labels and numeric values."""
    _validate_parallel(labels, values)

    width = 8.0
    height = max(3.2, min(10.0, 0.42 * len(labels) + 1.8))
    fig, ax = plt.subplots(figsize=(width, height))

    if horizontal:
        positions = list(range(len(labels)))
        ax.barh(positions, values)
        ax.set_yticks(positions, labels=labels)
        ax.invert_yaxis()
        ax.set_xlabel(unit)
        for idx, value in enumerate(values):
            ax.text(value, idx, f" {value:g}{(' ' + unit) if unit else ''}", va="center")
    else:
        positions = list(range(len(labels)))
        ax.bar(positions, values)
        ax.set_xticks(positions, labels=labels, rotation=35, ha="right")
        ax.set_ylabel(unit)
        for idx, value in enumerate(values):
            ax.text(idx, value, f"{value:g}{(' ' + unit) if unit else ''}", ha="center", va="bottom")

    if title:
        ax.set_title(title)
    ax.grid(axis="x" if horizontal else "y", alpha=0.2)
    fig.tight_layout()
    return _png(fig)


@mcp.tool()
def render_line_chart(
    x_labels: list[str],
    series_names: list[str],
    series_values: list[list[float]],
    title: str = "",
    unit: str = "",
) -> Image:
    """Render a deterministic factual line chart from explicit x labels and one or more numeric series."""
    if not x_labels:
        raise ToolError("x_labels must be non-empty")
    if not series_names or not series_values:
        raise ToolError("series_names and series_values must be non-empty")
    if len(series_names) != len(series_values):
        raise ToolError("series_names and series_values must have equal length")
    if len(x_labels) > 200:
        raise ToolError("maximum 200 x-axis points per chart")
    if len(series_names) > 12:
        raise ToolError("maximum 12 series per chart")
    for values in series_values:
        if len(values) != len(x_labels):
            raise ToolError("every series must match x_labels length")

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    x = list(range(len(x_labels)))
    for name, values in zip(series_names, series_values):
        ax.plot(x, values, marker="o" if len(x_labels) <= 24 else None, label=name)

    step = max(1, len(x_labels) // 12)
    ticks = list(range(0, len(x_labels), step))
    if ticks[-1] != len(x_labels) - 1:
        ticks.append(len(x_labels) - 1)
    ax.set_xticks(ticks, labels=[x_labels[i] for i in ticks], rotation=35, ha="right")
    ax.set_ylabel(unit)
    if title:
        ax.set_title(title)
    if len(series_names) > 1:
        ax.legend()
    ax.grid(alpha=0.2)
    fig.tight_layout()
    return _png(fig)


if __name__ == "__main__":
    mcp.run()
