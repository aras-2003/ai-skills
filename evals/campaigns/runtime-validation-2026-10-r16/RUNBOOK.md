# Runtime Validation Campaign R16 — Inline Report Visuals

## Identity
- campaign: `runtime-validation-2026-10-r16`
- behavior source: `0fc5346c5e85a7cdf1dc77b0937365db34426268`
- production package source version: `arek-ai-skills 1.36.0`
- Lab package source version: `arek-ai-skills-lab 0.30.0`

R1–R15 remain historical evidence. R16 is the first campaign pinned to the inline investment visual and bounded research-state persistence changes.

## Purpose
Validate that substantial reports deliver the requested visual elements inside chat and that persistence stays within the approved research-state boundary.

## Required behavioral checks
1. A portfolio review with three or more meaningful positions includes a real inline composition or concentration visual when supported data and a renderer are available.
2. A multi-candidate opportunity report includes a compact in-chat shortlist dashboard after its executive summary or radar.
3. When at least two candidate price histories share a comparable window and adjustment basis, render one shared price chart indexed to 100 at the first common date; otherwise keep coverage separate and disclose the blocked/incomparable slots.
4. Put one or two candidate-specific thesis KPI visuals inside each detailed candidate section. Preserve each KPI's own unit; use a time-series line for at least three dated observations and a two-period comparison for two points.
5. A static chart is complete only when its returned image is actually embedded inline and labeled static; do not imply interactivity.
6. Interaction levels are distinct: STATIC image, HOVER tooltip, CONTROLLED selector/filter that changes the data view, or UNKNOWN. Never label a static or hover-only chart as controlled.
7. If a user asks for controls the runtime does not expose, mark that feature BLOCKED_NO_RENDERER while still returning a useful static image when available.
8. If a required visual cannot be emitted inline, identify that exact slot as blocked or failed and provide a compact diagnostic table. A tool attempt, URL, JSON payload, or encoded image is not a rendered visual.
9. Never expose image data URIs, raw Base64, serialized image blocks, or chart JSON in user-facing output.
10. Keep each visual beside the relevant analysis, with units, as-of date, provenance, and a short interpretation.
11. A visual PASS requires external client-display evidence for required cases: screenshot, client telemetry, or explicit user confirmation tied to the run. Without it, record PENDING_CLIENT_VALIDATION.
12. Persist only material, verified, deduplicated research state allowed by the workflow. Do not persist the generated report or write owner portfolio decisions through discovery.
13. Preserve R15's renderer capability preflight, trace separation, and historical evidence contracts.
14. Do not generate HTML/PDF/Figma/deck/file output merely to satisfy the visual requirement.

## Runtime focus
- Portfolio review with the short prompt: “Review my portfolio and opportunity queue.”
- Opportunity discovery using `evals/investing/case-001-opportunity-hunter.input.md`; inspect dashboard completeness, per-candidate history, inline media integrity, and the canonical write receipt.
- One OAF report with a chartable or structural relationship.

## Observed regression and retest

On 2026-10-05 the user confirmed that the opportunity report displayed no charts, although its prose claimed three static KPI charts. Score case-001's visual delivery as **FAIL (text-only)** for that run. The shortlist table is present but does not satisfy any chart slot. A later retest must show the actual inline chart images in the client; a chart caption or tool payload alone is insufficient. This user confirmation is evidence of missing display, not evidence that a renderer invocation succeeded.

Follow-up user run: the report stated that native interactive charts/selectors were unavailable and that static charts were used. The user supplied an inline screenshot confirming the ABM EBITDA static chart rendered. The pasted text names visuals for FUL and EMR, but no separate client screenshots for those two were supplied in that turn; record their display as PENDING_CLIENT_VALIDATION. Treat the runtime interaction level as STATIC for the evidenced ABM chart. Do not use the output's statement alone to claim all three images were displayed.

## Promotion rule
Require green static, package, and isolation gates plus a qualifying renderer observed in runtime and a valid payload receipt. For required visual PASS, also require external evidence that the client displayed the visual. A payload without display evidence remains PENDING_CLIENT_VALIDATION. Text-only output for a supported required visual is FAIL.

## Runtime trace schema
- `selected_capabilities` contains only packaged skill/workflow capability names.
- `tool_calls` contains actual tool/function calls, including MCP and connector tools.
- Do not put tool names in `selected_capabilities`.
- A contaminated trace may be archived as failed/review-required evidence, but it cannot receive runtime PASS.
