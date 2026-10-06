---
name: company-context-research
description: 'Research factual company context relevant to executive technology opportunities,
  including scale, revenue, headcount, ownership, leadership, transactions, strategy
  and technology organization. Use when the user asks for company facts or organizational
  context. Do not evaluate role attractiveness, candidate fit, career value, mandate
  quality or recommended recruitment actions unless the user explicitly asks what
  the company context means for a specific role; in that case hand off to executive-role-evaluator.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.0.0
  maturity: production
  risk: low
  last_reviewed: '2026-09-30'
---

# Company Context Research

## Purpose

Build an evidence-based factual picture of a company without silently turning research into career advice.

## Use when

- The user asks for revenue, employee count, ownership, legal entities or acquisitions.
- The user asks about management, technology leadership, strategy or organizational context.
- The user wants company background before deciding whether deeper role evaluation is needed.

## Do not use when

- The user asks whether a role is worth pursuing.
- The user asks about candidate fit, career value, mandate quality or recruitment strategy.
- The user asks for CV tailoring or interview preparation.

When those questions are explicit, route to the relevant specialist skill.

## Procedure

1. **Clarify entity scope from evidence**
   - Distinguish group, country organization, subsidiary, business unit and legal entity.
   - Do not merge metrics from different entities without saying so.

2. **Collect decision-relevant facts**
   - Company scale and geography.
   - Revenue/profitability when available.
   - Employee count.
   - Ownership and major transactions.
   - Leadership and relevant technology/digital functions.
   - Strategy, transformation and organizational changes when relevant.

3. **Prefer strong sources**
   - Official company materials, annual reports, investor relations, regulatory filings.
   - Reputable business media for transactions/context.
   - Aggregators only when primary data is unavailable; label them accordingly.

4. **Separate fact from uncertainty**
   - State the period, entity and source basis.
   - Mark conflicting or approximate values.
   - Do not infer unsupported organizational authority.

5. **Stop at the research boundary**
   - Summarize what the facts establish.
   - Do not append unsolicited judgments about whether a role is good, whether the candidate fits, or what recruitment action to take.
   - If the user explicitly asks what these facts mean for a specific role, invoke/handoff to `executive-role-evaluator`.

## Output contract

Return a concise factual brief with:
- entity/scope;
- key facts and dates;
- material organizational/technology context;
- source quality/uncertainty;
- optional factual follow-up questions if the entity scope is ambiguous.

Do not include:
- PURSUE / INVESTIGATE / SKIP;
- candidate-fit judgments;
- career-value judgments;
- recruitment recommendations;
- mandate-quality conclusions.

## Quality checks

- [ ] Group and legal-entity data are not conflated.
- [ ] Every time-sensitive claim has a clear period/date.
- [ ] Primary/official sources are preferred.
- [ ] Fact and inference are distinguished.
- [ ] No unsolicited role evaluation or career advice is added.
- [ ] Explicit role-impact questions are routed to `executive-role-evaluator`.
