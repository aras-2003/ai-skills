# Capability Gap Analysis — Case 001

## Scenario

Strategic outcome:
Reduce time-to-market for a cross-market digital service from 9 months to 4 months while preserving security, data and regulatory controls.

Evidence:
- Product teams can design local market journeys quickly.
- Shared identity and customer-data changes depend on two central teams with multi-month queues.
- Architecture standards are documented, but exception decisions are slow.
- Integration patterns differ across markets.
- Data definitions for customer status differ in three markets.
- No evidence shows that the core identity platform is technically unable to scale.
- Shared teams report capacity overload.
- Local teams sometimes build workarounds to meet deadlines.
- Funding for shared changes is negotiated separately by each market.

## Test objective

Evaluate whether `capability-gap-analysis`:
- starts from the time-to-market outcome;
- identifies only the material capabilities;
- separates capacity, integration, data, governance and ownership issues;
- does not call the identity platform obsolete or recommend replacement without evidence;
- distinguishes workarounds as symptoms/evidence rather than automatic architecture defects.

## Expected behavior

PASS if it identifies a small set of capabilities such as identity/customer-data enablement, integration, exception decisioning and shared funding/roadmap capacity; separates capacity from maturity; and proposes intervention hypotheses rather than technology projects.
