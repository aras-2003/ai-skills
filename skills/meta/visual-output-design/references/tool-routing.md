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

Known bundled static renderer:
- MCP server: `arek-chart-renderer`;
- tools: `render_bar_chart`, `render_line_chart`;
- these tools qualify for ordinary static quantitative visual slots only when exposed by the current runtime.
- they **do not qualify** for a slot that explicitly requires chat-native interactivity.
- a valid tool result proves renderer execution `PAYLOAD_RENDERED`; it does not prove client display. Client display is `NOT_OBSERVABLE` to the model.

Interactive investment-history requirement:
- when a workflow/profile marks a price/KPI history slot as interactive, preflight should locate a chat-native interactive quantitative chart/widget capability when observable; if host-native capability visibility is incomplete, follow the attempt-first rule instead of blocking early;
- **preferred ChatGPT capability: native `chart` widget** (JSON-backed interactive bar/line/pie/scatter chart) when exposed by the runtime;
- for price/KPI history use `chart` with `chartType: "line"` and explicit time-series rows;
- the native `chart` widget qualifies as interactive because the client renderer provides hover/tooltips and native chart interaction over deterministic supplied data;
- do not require the skill package itself to own an MCP tool named `chart`; runtime-native widgets exposed by the host count during capability preflight;
- if `chart` is available, use it before `arek-chart-renderer`;
- other interactive quantitative chart/widget capabilities may also qualify if they accept explicit numeric/time-series data and are chat-native;
- static PNG/SVG/image payloads, markdown tables and generated images do not satisfy the interactive slot;
- if a host-native attempt proves no such capability exists, return `BLOCKED_NO_RENDERER` for that slot.

Preflight status:
- `AVAILABLE`: a concrete qualifying renderer is present and invokable;
- `UNAVAILABLE`: the host/runtime explicitly proves that no qualifying renderer can be invoked;
- `UNKNOWN`: tool enumeration is insufficient to determine whether a host-native renderer exists.

### Attempt-first rule for required interactive investment charts
For required price/KPI history slots, `UNKNOWN` is **not** a terminal blocked state.

If the host surface may support a native chart component that is not exposed through MCP/tool enumeration:
1. prepare the factual chart payload;
2. attempt the host-native interactive chart using the host's response/widget contract;
3. if the host accepts/renders the chart payload, record `AVAILABLE` + `PAYLOAD_RENDERED`;
4. if the host explicitly rejects or lacks the capability, use `BLOCKED_NO_RENDERER` (or `FAIL_RENDERER_INVOCATION` when invocation was available but failed).

Do not convert `UNKNOWN` directly into `BLOCKED_NO_RENDERER` without a host-native chart attempt for required investment-history visuals.

A table/text fallback may accompany a blocked state for usability, but it does not satisfy the visual requirement.

## 1. Native interactive chart widget
Preferred for investment price/KPI history when the host runtime exposes the native `chart` widget.

Use:
- `chartType: "line"` for price and KPI time series;
- one chart per analytical question;
- multiple series only when units and comparison are genuinely compatible;
- inline data rows with source-backed values;
- user-friendly time labels;
- tooltips/hover supplied by the host renderer.

This is the default renderer for required interactive investment-history slots.

## 2. Static native/MCP chart renderer
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

## 3. Figma / FigJam diagram
Use only when the user explicitly requests an editable Figma/FigJam artifact, or the calling task explicitly requires Figma output. Use a connected Figma diagram capability for:
- flowcharts;
- decision trees;
- state/sequence diagrams;
- entity-relationship diagrams;
- gantt-style plans;
- clear dependency/process/governance flows.

For org charts, operating-model maps, capability maps and other layouts that exceed the supported diagram grammar,
use an editable Figma design canvas rather than forcing the content into an unsupported Mermaid form.

## 4. Figma design
Use only when the user explicitly requests an editable Figma artifact. Use when:
- the output should be editable and executive-grade;
- a reusable visual language/design system matters;
- multiple panels, cards, grids, labels and annotations must be composed precisely;
- an org model, capability map, architecture view or one-page executive visual is a durable artifact.

Do not invoke it for a simple two-series chart that the native chart renderer can handle better.

## 5. Figma Slides / deck
Use only when the user explicitly requests a deck/presentation. Use for:
- board/executive presentations;
- multi-slide narratives;
- research readouts;
- transformation stories;
- investment committee / opportunity review packs.

A deck is a communication artifact, not the canonical analytical record.

## 6. Interactive HTML/CSS report
Use only when the user explicitly requests HTML, a downloadable file or an external interactive report. Use when the result benefits from:
- tabs or scenario switching;
- filters;
- hover/tooltips;
- linked views;
- dense multi-panel dashboards;
- reusable one-page cockpit/report;
- responsive presentation outside the chat thread.

Keep data in a separate structured payload from HTML/CSS/JS. Prefer simple, portable front-end code and avoid hidden calculations in the presentation layer.

## 7. Data/analytics tools
Use connected analytics tools for:
- SQL/aggregation;
- portfolio concentration;
- overlap/look-through;
- time-series preparation;
- statistical calculations.

Analytics tools calculate the visual payload; they are not the presentation layer and do not become canonical state.

## 8. Image generation / creative media
Use only for:
- illustrative concepts;
- moodboards;
- non-data hero imagery;
- visual metaphors when explicitly useful.

Never use generated imagery to represent exact quantitative data, organizational reporting lines, factual architecture,
or evidence-backed process state.

## Fallback order
1. native host `chart` widget for quantitative interactive charts when available;
2. another qualifying chat-native interactive structured renderer;
3. static `arek-chart-renderer` only for non-interactive slots or as diagnostic fallback;
4. for **optional** visuals: static markdown table + concise prose;
5. for **required visual-floor** slots with no qualifying renderer: `BLOCKED_NO_RENDERER` plus an optional diagnostic table/prose fallback;
6. external artifact renderer only when the user explicitly requested that artifact class.

Never create HTML/PDF/Figma/deck/file output merely because the preferred chat renderer is unavailable.

Do not fall back to punctuation-based pseudo-diagrams when a structured fallback is possible.
