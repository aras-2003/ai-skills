# Runtime Validation Campaign R13 — Chat-native Integrated Reports

## Identity
- campaign: `runtime-validation-2026-10-r13`
- behavior source: `32fd24fbf12d924949e1af40829481bd95d68ec4`
- production package source version: `arek-ai-skills 1.15.0`
- Lab package source version: `arek-ai-skills-lab 0.9.0`

R1–R12 remain historical evidence.

## Purpose
Validate the corrected delivery contract: the integrated decision report is rendered in the chat response by default.

HTML, PDF, Figma, deck or other files are opt-in outputs. Missing inline renderer capability must fall back to another chat-native renderer, table or structured prose, not to an unsolicited external artifact.

## Runtime focus
Retest:
- case-001-opportunity-hunter
- case-002-security-sizing
- case-003-portfolio-review
- case-004-theme-discovery
- case-006-attention-acn

Also run the targeted cases in:
- `skills/meta/report-composer/tests/cases.yaml`
- `skills/meta/visual-output-design/tests/cases.yaml`

## Required behavioral checks
1. Normal report requests return the substantive report directly in chat.
2. Visuals are embedded next to the claims/sections they support.
3. Company/security reports use 3M / 6M / 12M switching only when a chat-native renderer supports it and verified data exist.
4. Portfolio concentration/overlap visuals remain inside their report sections.
5. If an ideal embedded visual is unavailable, use a chat-native fallback; do not create HTML/PDF/Figma/deck/file output.
6. External artifacts are created only when the user explicitly requests that artifact or file format.
7. An explicit request such as "export to HTML/PDF/Figma" may produce that artifact.
8. No renderer invents data, hierarchy, relationships or numeric precision.
9. Canonical receipts/provenance remain explicit.

## Promotion rule
Do not promote on static tests alone. Require:
- green static/package/isolation gates;
- one successful Investment report delivered fully in chat;
- one successful structural/OAF report with a chat-native visual/fallback;
- one explicit artifact-request case that correctly produces an artifact;
- one negative case proving that a normal report request does not produce an unsolicited file.
