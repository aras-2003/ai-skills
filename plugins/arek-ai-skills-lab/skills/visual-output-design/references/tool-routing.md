# Visual tool routing

Choose the narrowest capable renderer. Tool availability varies by runtime; never claim a tool was used unless it actually ran.

## Capability preflight contract

Before satisfying a required visual slot, inspect the tools available in the current session and bind the slot to a concrete renderer capability.

A **qualifying deterministic data renderer** must:
- accept structured numeric/category/time-series data or an equivalent explicit chart specification;
- deterministically encode those supplied values into a rendered chart/visual;
- preserve labels, units and ordering without model-invented geometry;
- be invokable in the current runtime and embeddable in the intended response surface.

The following do **not** qualify as quantitative chart renderers:
- image generation or generic media generation;
- image viewing;
- Figma/FigJam diagram/design tools used as freeform drawing surfaces;
- text, markdown tables or ASCII/punctuation pseudo-charts.

Known bundled renderer:
- MCP server: `arek-chart-renderer`;
- qualifying quantitative tools: `render_bar_chart`, `render_line_chart`;
- these tools qualify only when they are actually exposed by the current runtime tool list. Package declaration alone is not proof of availability.
- a valid tool result proves renderer execution `PAYLOAD_RENDERED`; it does not prove client display. Client display is `NOT_OBSERVABLE` to the model.

Preflight status:
- `AVAILABLE`: a concrete qualifying renderer is present and invokable;
- `UNAVAILABLE`: inspected runtime capabilities contain no qualifying renderer;
- `UNKNOWN`: the runtime/tool contract is insufficient to prove a qualifying renderer exists.

For a required visual-floor slot, `UNAVAILABLE` or `UNKNOWN` means `BLOCKED_NO_RENDERER`. A table/text fallback may still be shown for usability, but it does not satisfy the visual requirement.

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
1. best qualifying native chat renderer/widget;
2. another qualifying chat-native structured renderer;
3. for **optional** visuals: static markdown table + concise prose;
4. for **required visual-floor** slots with no qualifying renderer: `BLOCKED_NO_RENDERER` plus an optional diagnostic table/prose fallback;
5. external artifact renderer only when the user explicitly requested that artifact class.

Never create HTML/PDF/Figma/deck/file output merely because the preferred chat renderer is unavailable.

Do not fall back to punctuation-based pseudo-diagrams when a structured fallback is possible.
