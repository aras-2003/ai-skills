"""Single Skills Factory MCP runtime for local stdio and remote HTTP profiles."""

from __future__ import annotations

from chart_renderer import render_bar_chart as _render_bar_chart
from chart_renderer import render_line_chart as _render_line_chart
from investment_runtime import route_investment_request as _route_investment_request
from mcp.server import MCPServer

SERVER_INSTRUCTIONS = """
Skills Factory runtime contract.

For every request about investments, securities, ETFs, a portfolio, investment
themes, opportunities, policy or risk limits, call route_investment_request
before composing substantive output. This runtime only routes the request; it
does not execute a selected workflow, read holdings, fetch market data or
make investment recommendations. If execution_state is "routed_only" or
workflow_executed is false, stop without substantive investment output.
Do not draft policy, thresholds, allocations, valuations or buy/sell opinions
from a routing result alone.

Use chart tools only with explicit numeric inputs from the user or a completed,
source-backed workflow. Preserve supplied labels, values and units. Do not
invent missing observations.
""".strip()
CLOUD_SERVER_INSTRUCTIONS = SERVER_INSTRUCTIONS

mcp = MCPServer(
    "Skills Factory runtime",
    description="Unified Skills Factory runtime for investment routing and factual chart rendering.",
    instructions=SERVER_INSTRUCTIONS,
)


@mcp.tool()
def route_investment_request(user_request: str) -> dict[str, str | bool]:
    """MANDATORY first step for every investment request, before analysis."""
    result = _route_investment_request(user_request)
    if result.get("is_investment_request"):
        result.update(
            {
                "workflow_executed": False,
                "execution_state": "routed_only",
                "response_policy": "stop_without_substantive_investment_output",
            }
        )
    return result


@mcp.tool()
def render_bar_chart(
    labels: list[str],
    values: list[float],
    title: str = "",
    unit: str = "",
    horizontal: bool = True,
):
    """Render a deterministic factual bar chart from explicit values."""
    return _render_bar_chart(labels, values, title, unit, horizontal)


@mcp.tool()
def render_line_chart(
    x_labels: list[str],
    series_names: list[str],
    series_values: list[list[float]],
    title: str = "",
    unit: str = "",
):
    """Render a deterministic factual line chart from explicit values."""
    return _render_line_chart(x_labels, series_names, series_values, title, unit)


app = mcp.streamable_http_app()


if __name__ == "__main__":
    mcp.run()
