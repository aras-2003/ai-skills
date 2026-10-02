# Investment OS Review Workflow

## Purpose
Act as the default orchestration front door for natural investment requests. Route the request into the smallest evidence-backed Investment OS workflow that can answer it, rather than answering with generic investment commentary.

This workflow does not replace the specialist workflows. It selects and invokes them.

## Natural activation
Use this workflow when the user asks about their investments in ordinary language and does not explicitly name a narrower Investment OS workflow.

Typical requests include:
- "review my portfolio" / "review this portfolio" / "what requires attention?";
- "review this stock/security";
- "find opportunities" / "what should I research next?";
- "what investment themes are worth researching?";
- "does this news/event matter for my holdings?";
- "help me define my investment policy/risk limits."

Do not require the user to know Investment OS terminology, canonical storage, specialist names or workflow names.

## Routing matrix
Choose exactly one primary route unless the request genuinely contains two separate decisions.

### Portfolio route
Use `investment-portfolio-review` when the request concerns:
- multiple holdings or portfolio weights;
- concentration, diversification, overlap, allocation or portfolio risk;
- current portfolio state, drift, policy fit or what requires attention;
- next portfolio-level decisions.

A prompt containing holdings/weights plus a request to review risk or next decisions MUST take this route.

### Security route
Use `investment-security-review` for one named security when the user wants end-to-end underwriting, valuation, thesis challenge, portfolio fit or sizing.

### Opportunity route
Use `investment-opportunity-hunter` when the user asks to scan for new securities/candidates or asks what to research next without a known security.

### Theme route
Use `investment-theme-discovery` for structural/cyclical investment themes, value chains or second-order beneficiaries.

### Attention route
Use `investment-attention-review` when the user brings new company/industry/market information and asks whether it changes prior theses or deserves deeper work.

### Policy route
Use `investment-policy-design` when the decision is about portfolio rules, risk limits, target bands, sizing constraints or investment governance rather than reviewing current holdings.

## Orchestration rules
1. Select the primary route before doing substantive analysis.
2. Invoke the selected child workflow/skill and follow its evidence/canonical rules.
3. Do not duplicate the child workflow with a generic answer before or after invocation.
4. If the portfolio route is selected:
   - canonical reads must be attempted by the child workflow;
   - user-supplied weights are evidence to reconcile, not a replacement for canonical state;
   - substantial chartable portfolio data must continue through integrated reporting and the visual-floor path.
5. If the request is ambiguous between routes, prefer the route that directly matches the user's decision object:
   - portfolio > multiple holdings/weights;
   - security > one named security;
   - attention > new event/news against existing holdings/theses;
   - opportunity > discovery of new securities;
   - theme > thematic research;
   - policy > rules/limits.
6. Do not fan out to every Investment OS workflow merely for completeness.
7. Missing evidence narrows the child workflow result; it does not justify bypassing the child workflow.

## Output contract
Return the selected child workflow's normal output. Do not add a separate router report.

When runtime diagnostics are explicitly requested, include:
- selected Investment OS route;
- selected child workflow;
- why that route matched the user's decision object.

## Stop conditions
Stop routing once one primary child workflow clearly owns the request.
Escalate to two routes only when the user explicitly asks two distinct investment decisions that cannot be answered by one child workflow.
