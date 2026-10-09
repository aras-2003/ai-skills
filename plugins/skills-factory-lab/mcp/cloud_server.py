"""Backward-compatible remote entrypoint for the unified Skills Factory MCP."""

from server import (
    SERVER_INSTRUCTIONS as CLOUD_SERVER_INSTRUCTIONS,
    app,
    mcp,
    runtime_info,
    render_bar_chart,
    render_line_chart,
    route_investment_request,
)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
