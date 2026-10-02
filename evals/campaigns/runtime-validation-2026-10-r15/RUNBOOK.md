# Runtime Validation Campaign R15 — Visual Floor

## Identity
- campaign: `runtime-validation-2026-10-r15`
- behavior source: `c6467ab8a7f2cf6435ce613792615cc5e93769ad`
- production package source version: `arek-ai-skills 1.17.0`
- Lab package source version: `arek-ai-skills-lab 0.11.0`

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
5. If no suitable chat-native renderer exists, use a compact table/matrix fallback and make the renderer limitation explicit.
6. Do not generate HTML/PDF/Figma/deck/file output merely to satisfy the visual floor.
7. Existing report-quality defaults from R14 remain intact.

## Runtime focus
- portfolio review with short prompt: "Review my portfolio and opportunity queue."
- one opportunity/security review with supported time-series data.
- one OAF report with a chartable/structural relationship.

## Promotion rule
Require green static/package/isolation gates plus runtime evidence that at least one chartable report produces a real inline visual without prompt-level formatting instructions.
