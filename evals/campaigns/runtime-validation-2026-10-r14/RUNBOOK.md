# Runtime Validation Campaign R14 — Report Quality Defaults

## Identity
- campaign: `runtime-validation-2026-10-r14`
- behavior source: `efe703e9d14f5bbe1b5fbeef7346539d3bd0c978`
- production package source version: `arek-ai-skills 1.16.0`
- Lab package source version: `arek-ai-skills-lab 0.10.0`

R1–R13 remain historical evidence.

## Purpose
Validate that professional report composition no longer depends on a long formatting prompt.

A short request such as "review my portfolio and opportunity queue" should automatically produce the quality baseline encoded in `report-composer` and `visual-output-design`.

## Required behavioral checks
1. Executive summary contains 3–5 decision-relevant points.
2. The report stays chat-native unless an external artifact is explicitly requested.
3. Visuals are selective and placed next to the argument they support.
4. No ASCII bars or raw Mermaid code are shown.
5. Mermaid xychart is not used when a better chat-native renderer/widget exists.
6. Investment opportunity reports default to 2–3 detailed candidates and compress the rest.
7. Candidate sections use thesis/setup, a small KPI set, price/valuation context, catalyst/risk and decision implication.
8. Canonical, derived analytics and external market data are clearly distinguished.
9. External market data may fill price-history context when canonical storage lacks it, but remains explicitly noncanonical.
10. Receipts are compact and decision queue is normally 3–5 items.
11. No repeated prose + table + chart containing the same information.

## Runtime focus
- portfolio review with a short natural-language prompt and no formatting instructions;
- opportunity hunter with a broad queue;
- single-security review;
- one OAF report to verify the standard generalizes without forcing investment-specific structure.

## Promotion rule
Require green static/package/isolation gates and clean runtime evidence showing that the quality behavior is intrinsic to the skill, not copied from a detailed user prompt.
