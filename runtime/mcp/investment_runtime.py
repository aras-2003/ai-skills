# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "mcp>=2,<3",
# ]
# ///

from __future__ import annotations

import re

from mcp.server import MCPServer

SERVER_INSTRUCTIONS = """
Investment OS runtime guardrail.

For any user request whose decision object is investments, a portfolio, holdings,
stocks, securities, ETFs, investment themes, investment opportunities, investment
policy/risk limits, or new information about an existing investment:

1. Before substantive investment analysis, call route_investment_request with the
   user's full request.
2. Follow the returned child_workflow and load/use the matching packaged workflow.
3. Do not replace the selected workflow with generic investment commentary.
4. For portfolio requests:
   - observation/change/monitoring intent -> investment-portfolio-observation;
   - full risk/concentration/decision review -> investment-portfolio-review.
5. This router does not make buy/sell decisions. It only chooses the Investment OS
   workflow that owns the request.

Do not call this router for unrelated finance questions such as banking mechanics,
tax explanations, mortgages, budgeting, or generic accounting unless the request is
specifically an Investment OS decision.
""".strip()

mcp = MCPServer(
    "Arek Investment OS runtime",
    description="Routes natural investment requests into the correct Investment OS workflow before analysis.",
    instructions=SERVER_INSTRUCTIONS,
)


def _contains(text: str, *phrases: str) -> bool:
    return any(p in text for p in phrases)


def _ticker_count(text: str) -> int:
    # Conservative heuristic: uppercase security-like tokens only.
    tokens = re.findall(r"\b[A-Z]{2,5}\b", text)
    stop = {
        "ETF", "ETFS", "AI", "USD", "PLN", "EUR", "CEO", "CIO", "CTO",
        "PE", "EPS", "FCF", "DCF", "ROIC", "TAM", "CAGR",
    }
    return len({token for token in tokens if token not in stop})


@mcp.tool()
def route_investment_request(user_request: str) -> dict[str, str | bool]:
    """Call before substantive analysis for natural investment requests.

    Routes portfolio observation/change monitoring, full portfolio review,
    one-security review, new-opportunity discovery, investment-theme research,
    new-information attention triage, or investment policy/risk-limit design
    into the matching Investment OS child workflow.
    It does not provide investment advice or replace the selected workflow.
    """
    raw = user_request.strip()
    text = raw.lower()

    if not raw:
        return {
            "is_investment_request": False,
            "route": "unknown",
            "child_workflow": "investment-os-review",
            "reason": "empty request; no investment decision object detected",
            "must_invoke_child_workflow": False,
        }

    policy = _contains(
        text,
        "investment policy", "portfolio policy", "risk limit", "risk limits",
        "maximum position", "max position", "position limit", "sector limit",
        "rebalancing rule", "rebalancing rules", "zasady portfela",
        "limit jednej spółki", "limity sektorowe", "rebalancing",
        "maksymalny udział", "reguły portfela",
    )
    attention = _contains(
        text,
        "new information", "new news", "does this news", "does this change the thesis",
        "changes the thesis", "materiality", "headline", "nowe informacje",
        "zmieniają tezę", "zmienia teze", "czy to zmienia", "wymaga głębszej analizy",
        "wymaga glebszej analizy",
    )
    theme = _contains(
        text,
        "investment theme", "investment themes", "theme research", "value chain",
        "second-order", "structural theme", "cyclical theme", "temat inwestycyjny",
        "tematy inwestycyjne", "łańcuch wartości", "lancuch wartosci",
    )
    opportunity = _contains(
        text,
        "find opportunities", "find stocks", "new stocks", "new securities",
        "research candidates", "what should i research", "scan for",
        "znaleźć kilka nowych spółek", "znalezc kilka nowych spolek",
        "nowe spółki", "nowe spolki", "kandydatów do researchu",
        "kandydatow do researchu", "co warto zbadać", "co warto zbadac",
    )
    observation = _contains(
        text,
        "what is happening with my portfolio", "what changed in my portfolio",
        "what changed", "what should i watch", "monitor my holdings",
        "monitor my portfolio", "portfolio drift", "observe my portfolio",
        "co się dzieje z portfelem", "co sie dzieje z portfelem",
        "co się zmieniło", "co sie zmienilo", "co mam obserwować",
        "co mam obserwowac", "obserwuj moje pozycje", "obserwuj portfel",
        "zmiany w portfelu", "monitoruj portfel",
    )
    portfolio = _contains(
        text,
        "my portfolio", "this portfolio", "portfolio review", "review portfolio",
        "portfolio risk", "portfolio concentration", "portfolio diversification",
        "holdings", "weights", "allocation", "top 2", "top 5", "other holdings",
        "etf overlap", "what requires attention", "portfel", "moj portfel",
        "mój portfel", "wagi", "udziały", "udzialy", "koncentracja",
        "dywersyfikacja", "pozycje w portfelu",
    )

    # Multiple security-like tickers plus weights/percentages strongly indicates portfolio.
    if _ticker_count(raw) >= 2 and ("%" in raw or portfolio):
        portfolio = True

    # Ordering reflects decision ownership, not business priority.
    if policy:
        route, child, reason = (
            "policy",
            "investment-policy-design",
            "request is about portfolio rules, limits or rebalancing policy",
        )
    elif attention:
        route, child, reason = (
            "attention",
            "investment-attention-review",
            "request asks whether new information changes an existing investment thesis or deserves escalation",
        )
    elif observation:
        route, child, reason = (
            "portfolio_observation",
            "investment-portfolio-observation",
            "request asks to observe portfolio changes, drift or what deserves attention without requiring target-allocation optimisation",
        )
    elif portfolio:
        route, child, reason = (
            "portfolio",
            "investment-portfolio-review",
            "request concerns multiple holdings, weights, concentration, diversification or portfolio-level decisions",
        )
    elif theme:
        route, child, reason = (
            "theme",
            "investment-theme-discovery",
            "request is about structural/cyclical themes or value-chain research",
        )
    elif opportunity:
        route, child, reason = (
            "opportunity",
            "investment-opportunity-hunter",
            "request asks to discover new securities or research candidates",
        )
    elif _ticker_count(raw) == 1 or _contains(
        text,
        "review this stock", "review this security", "review the stock",
        "stock thesis", "security review", "wyceń spółkę", "wycen spolke",
        "oceń spółkę", "ocen spolke", "analiza spółki", "analiza spolki",
    ):
        route, child, reason = (
            "security",
            "investment-security-review",
            "one named security is the clear decision object",
        )
    else:
        return {
            "is_investment_request": True,
            "route": "unknown",
            "child_workflow": "investment-os-review",
            "reason": "investment intent detected but the decision object is ambiguous; use the Investment OS front door",
            "must_invoke_child_workflow": True,
        }

    return {
        "is_investment_request": True,
        "route": route,
        "child_workflow": child,
        "reason": reason,
        "must_invoke_child_workflow": True,
    }


if __name__ == "__main__":
    mcp.run()
