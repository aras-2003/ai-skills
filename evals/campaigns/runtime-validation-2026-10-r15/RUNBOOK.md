# Runtime Validation Campaign R15 — Visual Floor

## Identity
- campaign: `runtime-validation-2026-10-r15`
- behavior source: `9c83b569b8ad6467ee2a43cb7b7c8be5faa83b1d`
- production package source version: `arek-ai-skills 1.26.0`
- Lab package source version: `arek-ai-skills-lab 0.20.0`

R1–R14 remain historical evidence.

## Purpose
Validate that substantial reports with material chartable data no longer silently degrade to text-only output.

The system should include at least one real chat-native visual when:
- the report contains a clear composition, ranking, time-series, matrix or structural relationship;
- the relevant data are supported;
- a suitable chat-native renderer is available.

## Required behavioral checks
1. A portfolio review with 3+ meaningful positions/categories includes at least one real composition/concentration visual when renderable.
2. The visual is embedded next to the portfolio-risk argument it supports.
3. For many positions, prefer ranked horizontal bars; a donut/pie is acceptable only for a small meaningful part-to-whole such as top categories or top positions + Other.
4. The report must not substitute ASCII bars or raw Mermaid code.
5. Run `capability_preflight`. If no qualifying deterministic chat-native data renderer exists, renderer execution is `BLOCKED_NO_RENDERER` and the runtime evaluation is FAIL.
6. If the renderer returns a valid image/chart payload, record `PAYLOAD_RENDERED`. The model must record client display as `NOT_OBSERVABLE`; it must not claim `UI_CONFIRMED`, visible rendering, or visual-floor PASS.
7. R15 visual-floor PASS requires external client-display evidence: screenshot, client telemetry, or explicit user confirmation tied to the run. Without that evidence, a valid payload remains `PENDING_CLIENT_VALIDATION`.
8. A compact table/matrix may be included only as diagnostic fallback; it does not substitute for renderer execution.
9. Do not generate HTML/PDF/Figma/deck/file output merely to satisfy the visual floor.
10. Existing report-quality defaults from R14 remain intact.

## Runtime focus
- portfolio review with short prompt: "Review my portfolio and opportunity queue."
- one opportunity/security review with supported time-series data.
- one OAF report with a chartable/structural relationship.

## Promotion rule
Require green static/package/isolation gates plus:
- a qualifying renderer observed in runtime;
- a valid chart payload receipt;
- external evidence that the client actually displayed the required visual.

A payload without external display evidence is PENDING_CLIENT_VALIDATION, not PASS. Any text-only fallback for a required chartable case is FAIL. Model-authored claims such as "rendered above" or `UI_CONFIRMED` are not client evidence.


## Runtime trace schema

Runtime traces keep capability selection separate from tool execution.

- `selected_capabilities` contains only packaged skill/workflow capability names.
- `tool_calls` contains actual tool/function calls, including MCP and connector tools.
- Do not place MCP/tool names such as `mcp__arek_investment_os__route_investment_request` in `selected_capabilities`.
- A contaminated trace may be archived as evidence of a failed/review-required run, but it cannot receive runtime PASS.
