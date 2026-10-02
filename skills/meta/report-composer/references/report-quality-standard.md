# Decision report quality standard

Apply this standard by default to substantial decision reports unless the user asks for a different style.

## 1. Executive hierarchy
- Start with an executive summary of 3–5 decision-relevant points.
- Lead with the decision state, not background.
- Show only numbers that change the interpretation or next action.
- Keep long evidence detail out of the opening screen.

## 2. Section economy
- Use a small number of meaningful sections.
- Prefer one strong visual per analytical question over several weak visuals.
- Do not repeat the same facts in prose, a table and a chart.
- Keep post-visual interpretation to roughly 2–3 sentences unless the issue genuinely needs more.
- Use detailed tables only where exact comparison matters.

## 3. Entity depth
For opportunity/security comparisons:
- default to 2–3 detailed candidates when the workflow has a larger queue;
- compress the remaining names into a short watch/defer block;
- for each detailed candidate, prefer:
  1. thesis/setup;
  2. 3–4 decision-relevant KPIs;
  3. price/valuation context;
  4. catalyst/risk;
  5. decision implication / next gate.
- Do not create a long mini-report for every candidate in a broad queue unless the user asks for it.

## 4. Visual placement
- Put the visual immediately after the short context it helps explain.
- Put interpretation immediately after the visual.
- Do not collect all charts into a separate dashboard or visual appendix by default.
- Do not add a visual just to make a section look richer.
- **Visual floor:** when a substantial decision report contains a clear quantitative composition, ranking, time-series, matrix or structural relationship, create at least one required visual slot and run renderer `capability_preflight`.
- If no qualifying renderer exists, renderer execution is `BLOCKED_NO_RENDERER`.
- If invocation succeeds and a valid image/chart payload is returned, renderer execution is `PAYLOAD_RENDERED`.
- Client display is not observable by the language model and must remain `NOT_OBSERVABLE`; never infer inline visibility from payload success.
- For portfolio reviews with 3+ meaningful positions/categories, attempt at least one portfolio-composition/concentration visual when a qualifying renderer exists.
- A compact table/matrix may accompany unavailable/failed rendering as a diagnostic fallback, but it does not change renderer execution state.

## 5. Visual quality
Prefer:
- horizontal bars for ranked concentration/allocation;
- normalized line charts for actual time-series / relative performance;
- overlap or exposure matrices for portfolio overlap;
- range/scenario visuals for valuation;
- compact KPI cards/strips for a handful of key metrics;
- timelines for catalysts/risks or sequencing;
- option matrices for trade-offs.

Avoid:
- text-only reporting when material chartable data and a suitable chat-native renderer are available;
- ASCII bars;
- punctuation-based pseudo-charts;
- raw Mermaid code fences shown to the user;
- Mermaid xychart for polished executive reporting when a better native chart/widget exists;
- decorative gauges;
- pie charts with many slices;
- repeated bar charts for every candidate;
- a separate 3M/6M/12M bar chart per security when one cross-candidate or real time-series visual would communicate the decision better.

If no suitable chat-native visual renderer is available, use a compact table/matrix only as a diagnostic aid and keep renderer execution at `BLOCKED_NO_RENDERER`; do not imply renderer success or client-visible completion.

## 6. Price and market context
- Canonical portfolio/research state remains canonical.
- Market price history may come from current external market-data/research tools when canonical storage does not contain it.
- Label such data as **external market data**, including as-of context/source.
- Do not treat external price history as canonical state.
- Prefer real historical series over three isolated trailing-return numbers when the series is available.
- For security reports, 3M / 6M / 12M switching is useful only when the renderer and verified data support it.
- Price momentum is context, not thesis validity.

## 7. Canonical vs derived vs external
Keep these visibly distinct:
- **Canonical data** — system of record.
- **Derived analytics** — calculations from canonical or sourced data.
- **External market/research data** — current context from external tools/sources.

Do not blend these categories in one unlabeled table/chart if the distinction affects trust.

## 8. Decision close
End with a compact decision queue:
- ideally 3–5 items;
- what to verify;
- what not to do;
- next decision gate.

Do not end with a generic summary that repeats the opening.

## 9. Receipts
- Keep canonical READ/WRITE receipts explicit but compact.
- Prefer a short receipt block over a wide table unless field-by-field audit detail is requested.
- Surface warnings that materially limit the conclusion.

## 10. Chat-native default
- The substantive report belongs in chat by default.
- External HTML/PDF/Figma/deck/file output requires explicit user request.
- Missing visual capability must remain inside chat as an explicit blocked state, not disappear behind a successful text-only fallback and not escape into an unsolicited file.


## Evidence discipline
- Classify decision-relevant facts as CANONICAL, USER_PROVIDED, EXTERNAL_VERIFIED, DERIVED or UNKNOWN.
- A DERIVED metric must be reproducible from identified inputs.
- A user-provided aggregate that cannot be recomputed from visible inputs stays USER_PROVIDED.
- Do not turn missing transaction history into evidence that no trade occurred.
- Historical or causal attribution requires evidence that distinguishes competing causes.
- Run a contradiction check before final output: no missing-history limitation may coexist with a confident historical attribution; no missing-policy limitation may coexist with a policy-breach claim.
- Keep limitations compact: state each material evidence gap once unless it changes a separate decision.
