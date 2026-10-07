"""Single Skills Factory MCP runtime for local stdio and remote HTTP profiles."""

from __future__ import annotations

import os

from chart_renderer import render_bar_chart as _render_bar_chart
from chart_renderer import render_line_chart as _render_line_chart
from investment_runtime import route_investment_request as _route_investment_request
from skill_catalog import list_skills as _list_skills
from skill_catalog import load_skill as _load_skill
from mcp.server import MCPServer

SERVER_INSTRUCTIONS = """
Skills Factory runtime contract.

Call runtime_info first when a test, receipt or compatibility decision depends
on the exact runtime identity. A result with attestation_status "unattested"
must not be treated as evidence of exact-version compatibility.

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

The packaged Lab catalog is the source of truth for skill parity. Use
list_skills when selecting a packaged capability and load_skill before
executing that capability. The MCP server loads the same packaged SKILL.md
instructions as the Lab; the host model executes those instructions. Do not
claim that the MCP server itself completed model reasoning or external actions.
""".strip()
CLOUD_SERVER_INSTRUCTIONS = SERVER_INSTRUCTIONS

RUNTIME_FIELDS = (
    "release_id",
    "source_revision",
    "channel",
    "capability_contract_version",
    "tool_schema_digest",
    "deployed_at",
)


def _runtime_value(name: str, default: str = "unattested") -> str:
    value = os.environ.get(name, "").strip()
    return value or default

mcp = MCPServer(
    "Skills Factory runtime",
    description="Unified Skills Factory runtime for investment routing and factual chart rendering.",
    instructions=SERVER_INSTRUCTIONS,
)


@mcp.tool()
def runtime_info() -> dict[str, str]:
    """Return deployment identity without performing any external action."""
    values = {
        "runtime_name": "Skills Factory runtime",
        "release_id": _runtime_value("SKILLS_FACTORY_RELEASE_ID"),
        "source_revision": _runtime_value("SKILLS_FACTORY_SOURCE_REVISION"),
        "channel": _runtime_value("SKILLS_FACTORY_CHANNEL", "unknown"),
        "capability_contract_version": _runtime_value(
            "SKILLS_FACTORY_CAPABILITY_CONTRACT_VERSION", "repository-side-v1"
        ),
        "tool_schema_digest": _runtime_value("SKILLS_FACTORY_TOOL_SCHEMA_DIGEST"),
        "deployed_at": _runtime_value("SKILLS_FACTORY_DEPLOYED_AT"),
    }
    values["attestation_status"] = (
        "verified"
        if all(values[field] not in {"unattested", "unknown"} for field in RUNTIME_FIELDS)
        else "unattested"
    )
    return values


@mcp.tool()
def list_skills() -> dict:
    """List the skills packaged in the same catalog as the active Lab profile."""
    return _list_skills()


@mcp.tool()
def load_skill(skill_name: str) -> dict:
    """Load packaged skill instructions and safe textual references for host-model execution."""
    return _load_skill(skill_name)


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
