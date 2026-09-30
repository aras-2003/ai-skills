# OAF Enterprise Architecture Review — Case 001

## Scenario

A multinational organisation wants to reduce duplicated customer, integration and data tooling across markets while improving local delivery speed.

Validated context:
- strategy requires faster cross-market product launches and reusable shared capabilities;
- local markets control most delivery budgets and are accountable for local outcomes;
- global architecture defines security, data and interoperability standards;
- shared platforms exist for customer identity, integration and data;
- some markets bypass shared platforms because lead times are too long;
- local CRM, integration and data solutions overlap in scope;
- architecture review happens in portfolio intake, but architecture does not control funding or delivery capacity;
- no reliable evidence yet quantifies duplication cost, technical debt, platform scalability or migration effort;
- three strategic initiatives depend on the same global data team, which is capacity constrained.

Leadership asks:
"Should we consolidate these platforms into one global target architecture?"

## Test objective

Evaluate whether `oaf-enterprise-architecture-review`:
1. reframes the consolidation request as an evidence-backed architecture decision;
2. traces business outcomes to capabilities;
3. separates operating-model/funding/capacity problems from evidenced technology-estate problems;
4. refuses to claim technical defects not in evidence;
5. treats duplication as a hypothesis to validate;
6. identifies architecture decision points and bounded options;
7. does not jump to one global implementation merely because standards are global;
8. makes the data-team capacity and funding model part of architecture feasibility;
9. states what evidence is required before final consolidation/retirement decisions.

## Expected behavior

PASS if:
- it says platform consolidation is not yet justified as a final decision;
- options include at least: improve shared-platform service/boundaries, federated shared core with bounded local extensions, and selective consolidation where evidence supports it;
- architecture influence without funding/capacity is treated as decision-system issue;
- technical scalability/debt remain unknown;
- next gate is evidence/pilot, not a final target-state migration roadmap.
