# Runtime Validation Campaign R11 — Visual Output Layer

## Identity
- campaign: `runtime-validation-2026-10-r11`
- behavior source: `0d2c5a892db96070000d551bc8f0d62bd0d1e63f`
- production package source version: `arek-ai-skills 1.13.0`
- Lab package source version: `arek-ai-skills-lab 0.7.0`

R1–R10 remain historical evidence.

## Purpose
R11 validates that the cross-domain visual presentation layer improves output quality without changing analytical conclusions or evidence discipline.

The visual layer must:
- select charts for quantitative comparisons and time series;
- select Figma/FigJam-style diagrams for structural/flow outputs;
- prefer interactive HTML only when multi-view interactivity adds value;
- preserve provenance, units, as-of dates, uncertainty and canonical receipts;
- never invent data, hierarchy or causal links for visual completeness;
- provide a concise text fallback when the preferred renderer is unavailable.

## Runtime focus
Retest the Investment OS focused cases because all five workflows now have visual-presentation behavior:
- case-001-opportunity-hunter
- case-002-security-sizing
- case-003-portfolio-review
- case-004-theme-discovery
- case-006-attention-acn

Also run targeted manual visual checks from `skills/meta/visual-output-design/tests/cases.yaml` in a clean Lab session.

## Promotion rule
Do not promote the visual layer on the basis of attractive screenshots alone. Require:
1. green static/package/isolation gates;
2. no regression in analytical/evidence behavior;
3. at least one successful quantitative chart case;
4. at least one successful structural diagram/Figma-routing case;
5. confirmation that missing renderer support falls back cleanly without fabricated output.
