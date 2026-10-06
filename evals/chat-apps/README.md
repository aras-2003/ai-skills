# Chat app end-to-end checks

These cases test the host's complete behavior, not only the MCP function in
isolation. Run each in a fresh chat with the exact app/runtime under test.

## Investment route-only case

Use `investment-route-only.input.md` in a fresh chat with Arek AI Skills Cloud.
Capture the app/version, visible tool trace, final answer and a screenshot or
saved page excerpt. A tool result saying `workflow_executed: false` is not a
PASS by itself: the final answer must also stop without substantive investment
content. If the host does not expose the trace or exact app identity, classify
the run as `NOT_RUN`/blocked, not PASS.

The rubric is evaluator-only and must not be sent to the chat being tested.

## Explicit line chart

Use `explicit-line-chart.input.md` in another fresh chat. Check the visible
chart and the accessible data table separately. A correct chart without a
trace linking it to the app renderer is `REVIEW_REQUIRED` for tool integration,
even when the display/data assertion passes.
