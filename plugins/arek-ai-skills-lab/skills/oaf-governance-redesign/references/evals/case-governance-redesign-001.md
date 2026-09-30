# OAF Governance Redesign — Workflow Case 001

## Scenario

A technology organisation has completed representative decision traces.

Confirmed diagnosis:
- two portfolio forums discuss the same prioritisation decisions with overlapping membership;
- architecture/security advice is often treated as implicit approval even though policy says advisory;
- funding reallocations have a clear CFO threshold but teams escalate below the threshold because local managers fear accountability;
- architecture exceptions lack a standard evidence pack, expiry condition and risk owner;
- weekly steering spends significant time on operational dependencies that platform/domain leaders could resolve directly;
- leadership wants to reduce decision lead time by at least 30% without weakening risk controls.

Formal decision owners are known.

## Test objective

Evaluate whether `oaf-governance-redesign`:
1. reuses the diagnosis;
2. distinguishes decision-rights fixes from governance mechanisms;
3. removes/merges before adding;
4. uses `governance-design` selectively;
5. proposes a bounded pilot;
6. defines evidence of effectiveness;
7. does not equate risk control with more approvals.

## Expected behaviors

PASS if:
- overlapping portfolio forums are candidates for merge/removal;
- low-threshold funding escalation is treated partly as accountability/risk behavior, not a missing committee;
- architecture exception governance is made explicit and bounded;
- operational dependencies are delegated where possible;
- pilot measures include lead time, rework, escalation and control exceptions.

FAIL if:
- it creates a new enterprise governance board;
- leaves all existing forums and adds new ones;
- increases approval layers to improve risk control;
- ignores formal vs actual decision behavior.
