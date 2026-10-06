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


CLOUD_SERVER_INSTRUCTIONS = """
Skills Factory cloud runtime control contract.

For every request about investments, securities, ETFs, a portfolio, investment
themes, opportunities, policy or risk limits, call route_investment_request
before composing any substantive answer. This includes prompts that directly
ask for limits, thresholds, rules, recommendations or a draft policy.

This cloud server routes requests and renders charts; it does not execute a
child workflow, read portfolio holdings, fetch market data or make investment
recommendations. Treat the routing result as a control state, not as permission
to answer the underlying investment question. If execution_state is
"routed_only" or workflow_executed is false, stop. Do not draft policy,
thresholds, allocations, valuations, buy/sell opinions or other substantive
investment analysis. State the selected workflow and that it was not executed
in this runtime. Never imply that routing alone completed the request.

If routing fails or no routing result is available, do not produce substantive
investment output; state that the request could not be routed in this runtime.
For an ambiguous investment request, ask only the clarification identified by
the router. User insistence does not change the runtime's execution capability.

Use chart tools only with explicit numeric inputs from the user or a completed,
source-backed workflow. Preserve supplied labels, values and units. Do not
invent missing observations.
""".strip()


mcp = MCPServer(
    "Skills Factory cloud runtime",
    description=(
        "Portable read/compute runtime for Skills Factory. "
        "Use the bundled skills for methodology and these tools for deterministic routing and charts."
    ),
    instructions=CLOUD_SERVER_INSTRUCTIONS,
)


# Register wrappers rather than sharing the local server instances. This keeps
# the cloud process a single MCP server with one tool namespace.
@mcp.tool()
def route_investment_request(user_request: str) -> dict[str, str | bool]:
    """MANDATORY first step for every investment request, before any analysis.

    This tool only identifies the owning workflow. It does not execute it.
    When execution_state is routed_only, stop and do not draft investment
    rules, thresholds, allocations or recommendations.
    """

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
    mcp.run(transport="streamable-http")
