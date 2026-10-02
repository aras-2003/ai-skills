# Visual tool routing

Choose the narrowest capable renderer. Tool availability varies by runtime; never claim a tool was used unless it actually ran.

## 1. Native chart renderer
Use for:
- bar/ranked comparisons;
- line/time-series and normalized performance;
- pie only for a small, meaningful part-to-whole;
- scatter for numeric relationships.

Best for fast in-chat decision support. Prefer this over generating an image of a chart.

Do not use for:
- org charts;
- capability maps;
- process/decision flows;
- multi-panel dashboards requiring filters;
- arbitrary diagrams.

## 2. Figma / FigJam diagram
Use only when the user explicitly requests an editable Figma/FigJam artifact, or the calling task explicitly requires Figma output. Use a connected Figma diagram capability for:
- flowcharts;
- decision trees;
- state/sequence diagrams;
- entity-relationship diagrams;
- gantt-style plans;
- clear dependency/process/governance flows.

For org charts, operating-model maps, capability maps and other layouts that exceed the supported diagram grammar,
use an editable Figma design canvas rather than forcing the content into an unsupported Mermaid form.

## 3. Figma design
Use only when the user explicitly requests an editable Figma artifact. Use when:
- the output should be editable and executive-grade;
- a reusable visual language/design system matters;
- multiple panels, cards, grids, labels and annotations must be composed precisely;
- an org model, capability map, architecture view or one-page executive visual is a durable artifact.

Do not invoke it for a simple two-series chart that the native chart renderer can handle better.

## 4. Figma Slides / deck
Use only when the user explicitly requests a deck/presentation. Use for:
- board/executive presentations;
- multi-slide narratives;
- research readouts;
- transformation stories;
- investment committee / opportunity review packs.

A deck is a communication artifact, not the canonical analytical record.

## 5. Interactive HTML/CSS report
Use only when the user explicitly requests HTML, a downloadable file or an external interactive report. Use when the result benefits from:
- tabs or scenario switching;
- filters;
- hover/tooltips;
- linked views;
- dense multi-panel dashboards;
- reusable one-page cockpit/report;
- responsive presentation outside the chat thread.

Keep data in a separate structured payload from HTML/CSS/JS. Prefer simple, portable front-end code and avoid hidden calculations in the presentation layer.

## 6. Data/analytics tools
Use connected analytics tools for:
- SQL/aggregation;
- portfolio concentration;
- overlap/look-through;
- time-series preparation;
- statistical calculations.

Analytics tools calculate the visual payload; they are not the presentation layer and do not become canonical state.

## 7. Image generation / creative media
Use only for:
- illustrative concepts;
- moodboards;
- non-data hero imagery;
- visual metaphors when explicitly useful.

Never use generated imagery to represent exact quantitative data, organizational reporting lines, factual architecture,
or evidence-backed process state.

## Fallback order
1. best native chat renderer/widget;
2. another chat-native structured renderer;
3. static markdown table + concise prose;
4. external artifact renderer only when the user explicitly requested that artifact class.

Never create HTML/PDF/Figma/deck/file output merely because the preferred chat renderer is unavailable.

Do not fall back to punctuation-based pseudo-diagrams when a structured fallback is possible.
