"""Unified remote MCP entrypoint for the portable cloud profile.

The local chart and Investment OS servers remain separate for backwards
compatibility. This module is the cloud deployment boundary: one HTTPS MCP
endpoint exposes the same read/compute tools without starting a local stdio
process in the ChatGPT package.

Run locally for a transport smoke test with:

    python runtime/mcp/cloud_server.py

For a hosted deployment, expose ``app`` through an ASGI server and configure
the host to use the streamable HTTP transport. Authentication and TLS belong
at the deployment edge; this process does not contain credentials.
"""

from __future__ import annotations

from chart_renderer import render_bar_chart as _render_bar_chart
from chart_renderer import render_line_chart as _render_line_chart
from investment_runtime import route_investment_request as _route_investment_request
from mcp.server import MCPServer


mcp = MCPServer(
    "Arek AI Skills cloud runtime",
    description=(
        "Portable read/compute runtime for Arek AI Skills. "
        "Use the bundled skills for methodology and these tools for deterministic routing and charts."
    ),
    instructions=(
        "Use route_investment_request before substantive Investment OS analysis. "
        "Use chart tools only with explicit numeric inputs."
    ),
)


# Register wrappers rather than sharing the local server instances. This keeps
# the cloud process a single MCP server with one tool namespace.
@mcp.tool()
def route_investment_request(user_request: str) -> dict[str, str | bool]:
    """Route an investment request to the owning Investment OS workflow."""

    return _route_investment_request(user_request)


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
    mcp.run(transport="streamable-http")
