from __future__ import annotations

import sys
from pathlib import Path

import yaml


REQUIRED_SKILLS = {
    "decision-journal-update",
    "investment-policy-design",
    "investment-record-store",
    "investor-pattern-research",
    "market-opportunity-scan",
    "portfolio-state-review",
    "position-sizing-review",
    "security-underwriting",
    "thesis-challenge",
    "thesis-monitor",
    "trend-theme-research",
    "valuation-scenario-review",
}

REQUIRED_WORKFLOWS = {
    "investment-opportunity-hunter",
    "investment-security-review",
    "investment-portfolio-review",
    "investment-theme-discovery",
}

REQUIRED_TABS = {
    "Portfolio_Current",
    "Transactions",
    "Portfolio_History",
    "Watchlist",
    "Opportunities",
    "Research_Log",
    "Signals_History",
    "Thesis_Register",
    "Decision_Journal",
    "Investment_Policy",
    "Market_Themes",
    "Sources",
}

LEAKAGE_MARKERS = ("expected_routing:", "failure_if:", "should_trigger:", "\nmust:", "\nmust_not:")


def fail(message: str) -> None:
    print(f"BLOCKER investing: {message}")


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    problems: list[str] = []

    skill_root = root / "skills" / "investing"
    found_skills = {p.parent.name for p in skill_root.rglob("SKILL.md")}
    missing_skills = REQUIRED_SKILLS - found_skills
    extra_skills = found_skills - REQUIRED_SKILLS
    if missing_skills:
        problems.append(f"missing required skills: {sorted(missing_skills)}")
    if extra_skills:
        problems.append(f"unexpected investing skills not covered by architecture test: {sorted(extra_skills)}")

    for name in REQUIRED_SKILLS:
        cases_path = skill_root / name / "tests" / "cases.yaml"
        if not cases_path.exists():
            problems.append(f"{name}: missing tests/cases.yaml")
            continue
        data = yaml.safe_load(cases_path.read_text(encoding="utf-8")) or {}
        cases = data.get("cases") or []
        positives = [c for c in cases if (c.get("expected") or {}).get("should_trigger") is True]
        negatives = [c for c in cases if (c.get("expected") or {}).get("should_trigger") is False]
        if not positives or not negatives:
            problems.append(f"{name}: requires positive and negative routing cases")

    workflow_root = root / "workflows"
    for name in REQUIRED_WORKFLOWS:
        p = workflow_root / name / "WORKFLOW.md"
        if not p.exists():
            problems.append(f"missing workflow: {name}")
            continue
        text = p.read_text(encoding="utf-8")
        if "investment-record-store" not in text:
            problems.append(f"{name}: durable storage dependency missing")
        if name != "investment-theme-discovery" and "XTB" not in text:
            problems.append(f"{name}: XTB v1 boundary missing")

    contract_path = skill_root / "investment-record-store" / "references" / "google-sheets-contract.md"
    if not contract_path.exists():
        problems.append("Google Sheets data contract missing")
    else:
        contract = contract_path.read_text(encoding="utf-8")
        for tab in REQUIRED_TABS:
            if f"### {tab}" not in contract:
                problems.append(f"data contract missing tab: {tab}")
        for required in ("append-only", "as_of_date", "source_date", "Personal data remains in Drive"):
            if required not in contract:
                problems.append(f"data contract missing integrity rule/token: {required}")

    sizing = (skill_root / "position-sizing-review" / "SKILL.md").read_text(encoding="utf-8")
    for required in ("investment policy", "portfolio state", "Without policy or portfolio state"):
        if required not in sizing:
            problems.append(f"position-sizing-review missing guardrail: {required}")

    monitor = (skill_root / "thesis-monitor" / "SKILL.md").read_text(encoding="utf-8")
    for required in ("Append a monitoring record", "never rewrite", "kill criteria"):
        if required.lower() not in monitor.lower():
            problems.append(f"thesis-monitor missing history guardrail: {required}")

    eval_root = root / "evals" / "investing"
    input_files = sorted(eval_root.glob("*.input.md"))
    rubric_files = sorted(eval_root.glob("*.rubric.yaml"))
    if len(input_files) < 5:
        problems.append("expected at least five investing workflow input evals")
    if len(input_files) != len(rubric_files):
        problems.append("every investing input eval must have exactly one rubric")

    for input_path in input_files:
        rubric_path = input_path.with_name(input_path.name.replace(".input.md", ".rubric.yaml"))
        if not rubric_path.exists():
            problems.append(f"missing rubric for {input_path.name}")
        text = input_path.read_text(encoding="utf-8")
        for marker in LEAKAGE_MARKERS:
            if marker in text:
                problems.append(f"{input_path.name}: evaluator leakage marker found: {marker!r}")

    registry = (workflow_root / "runtime-registry.yaml").read_text(encoding="utf-8")
    for name in REQUIRED_WORKFLOWS:
        if f"- name: {name}" not in registry:
            problems.append(f"runtime registry missing candidate workflow: {name}")
    if 'maturity: candidate' not in registry:
        problems.append("candidate maturity not represented in runtime registry")

    if problems:
        for problem in problems:
            fail(problem)
        return 1

    print(
        "Investing architecture validation passed: "
        f"{len(REQUIRED_SKILLS)} skills, {len(REQUIRED_WORKFLOWS)} workflows, "
        f"{len(input_files)} isolated workflow evals, {len(REQUIRED_TABS)} datastore tabs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
