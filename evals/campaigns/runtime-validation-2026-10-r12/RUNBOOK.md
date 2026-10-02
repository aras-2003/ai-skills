# Runtime Validation Campaign R12 — Integrated Decision Reports

## Identity
- campaign: `runtime-validation-2026-10-r12`
- behavior source: `63fd3fda0ab4931cc0652f0565aa29fc59b3b67d`
- production package source version: `arek-ai-skills 1.14.0`
- Lab package source version: `arek-ai-skills-lab 0.8.0`

R1–R11 remain historical evidence.

## Purpose
R12 validates the new report-composition layer above visual-output-design.

The system should produce one coherent decision report where narrative, evidence, decisions and visual components are interleaved by reading flow. It should no longer default to a complete text answer plus a separate duplicate dashboard.

## Runtime focus
Retest the Investment OS cases affected by integrated report composition:
- case-001-opportunity-hunter
- case-002-security-sizing
- case-003-portfolio-review
- case-004-theme-discovery
- case-006-attention-acn

Also run targeted clean-Lab checks from:
- `skills/meta/report-composer/tests/cases.yaml`
- `skills/meta/visual-output-design/tests/cases.yaml`

## Required behavioral checks
1. A security/company report places a verified price/performance visual inside the price-context section.
2. When comparable market data exist, a 3M / 6M / 12M interaction is offered only if the renderer supports it.
3. A portfolio report embeds concentration/overlap visuals in their analytical sections rather than emitting a second full dashboard.
4. An OAF operating-model report places its Figma/FigJam diagram inside the target-model section.
5. If inline embedding is unavailable, the runtime either:
   - uses an integrated text/table fallback, or
   - makes one rich HTML/Figma artifact the primary report and keeps chat summary short.
6. No renderer invents data, hierarchy, causal links or numeric precision.
7. Canonical receipts/provenance remain explicit.

## Promotion rule
Do not promote on attractive screenshots alone. Require:
- green static/package/isolation gates;
- no analytical/evidence regression;
- one successful Investment integrated-report run;
- one successful structural OAF/Figma-routing run;
- clean fallback when inline embedding is unavailable.
