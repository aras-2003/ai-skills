# Governance Design — Case 001

## Scenario

A technology organisation has already completed decision-rights and bottleneck diagnosis for four material decisions:

1. portfolio intake/prioritisation;
2. funding reallocation across verticals;
3. architecture exceptions;
4. cross-domain dependency escalation.

Confirmed findings:
- final decision owners exist for all four classes;
- architecture and security are advisers for most investment decisions but often act as de facto gates;
- portfolio reprioritisation is discussed in two recurring forums with overlapping membership;
- funding reallocation requires CFO approval above an agreed threshold;
- architecture exceptions have no standard evidence pack or expiry/review rule;
- dependency escalations often enter a weekly steering forum even when the issue can be resolved directly by the responsible platform and domain leaders;
- leadership wants faster decisions and fewer meetings, not more governance.

## Test objective

Evaluate whether `governance-design`:
1. starts from the material decision set;
2. prefers direct rights / standing rules / asynchronous mechanisms when possible;
3. creates a forum only where a forum is genuinely needed;
4. separates advice from approval;
5. identifies existing mechanisms to remove, merge or narrow;
6. defines evidence inputs, outputs, escalation and effectiveness measures;
7. avoids inventing new decision owners.

## Expected behaviors

PASS if the design:
- does not create four new committees;
- merges or removes overlapping portfolio forums where evidence supports it;
- treats architecture/security advice as input unless explicit approval authority is intended;
- defines a bounded architecture-exception mechanism with required evidence and review/expiry;
- keeps low-level dependency resolution outside steering where possible;
- defines measures such as decision lead time, rework, escalation rate and decision reversals.

FAIL if it:
- equates governance with meeting cadence;
- creates committees without decision purpose;
- silently expands adviser authority into approval;
- leaves overlapping forums untouched while adding new ones.
