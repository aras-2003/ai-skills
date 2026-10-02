# Integrated Decision Report Architecture

## Goal
Produce one coherent decision report in which narrative, evidence, visuals, interactive controls and sources are composed
together according to reading flow.

This replaces the weaker pattern of:
- full text answer;
- plus a parallel dashboard/HTML artifact containing the same content again.

## Architecture

Evidence / canonical state
-> Domain skills
-> Workflow synthesis
-> **Report Composer**
   -> ordered sections
   -> narrative/evidence/decision blocks
   -> inline visual slots
-> **Visual Output Design**
   -> renderer selection per slot
-> Chat-native report or one rich integrated artifact

`report-composer` owns document structure and placement.
`visual-output-design` owns visual encoding and rendering.

## Semantic report model
A report contains:
- title;
- decision headline;
- target;
- sections;
- receipts;
- limitations.

A section contains:
- narrative;
- evidence;
- zero or more visual slots;
- interpretation;
- decision/next step;
- provenance;
- uncertainty.

## Targets

### Chat-native report
Use when the runtime can render suitable charts/widgets inline.
The narrative remains in chat and visuals appear next to the relevant sections.

### Rich integrated report
Use when HTML/React/Figma/deck is required for interactivity, high-fidelity layout or complex structural visuals.
The rich artifact is the report itself. Avoid producing a second complete report in chat.

### Text fallback
Use when richer renderers are unavailable. Preserve section structure and decision logic.

## Interaction
Interactive controls must answer a real decision question.
Examples:
- security price chart: 3M / 6M / 12M;
- valuation: bear/base/bull toggle;
- portfolio: nominal vs look-through exposure;
- OAF: current vs target model toggle.

Do not add filters/tabs solely because HTML supports them.

## Cross-domain adoption
Investment OS, OAF and Commerce workflows should call Report Composer after analytical synthesis.
Visual Output Design remains a shared renderer utility.
New skills/workflows should specify report/visual affordances during specification and authoring.

## Integrity
- presentation cannot introduce facts;
- visuals inherit workflow evidence standards;
- canonical receipts remain explicit;
- unknown relationships remain unknown;
- rich artifacts are derivative and noncanonical unless a separate storage contract says otherwise.
