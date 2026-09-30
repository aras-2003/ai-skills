# Decision Bottleneck Analysis — Case 001

## Scenario

An enterprise technology investment decision took 47 calendar days.

Observed path:
- business sponsor submitted the proposal on day 0;
- portfolio office reviewed completeness on day 2;
- architecture review occurred on day 8;
- security requested additional evidence on day 11;
- finance requested a revised business case on day 14;
- proposal returned to the sponsor on day 17;
- revised materials were submitted on day 28;
- architecture re-reviewed on day 31 even though no architecture scope changed;
- finance approved on day 35;
- a steering committee discussed the item on day 39 but did not have formal decision authority;
- COO approved on day 47.

Formal process documentation says:
- portfolio office checks intake quality;
- architecture and security are advisers;
- finance confirms affordability;
- COO is final decision owner.

Stakeholders disagree on whether the steering committee is mandatory.

## Test objective

Evaluate whether `decision-bottleneck-analysis`:
1. reconstructs formal and actual paths;
2. separates active decision work from waiting/rework;
3. identifies duplicate reviews, hidden vetoes, missing evidence and authority ambiguity;
4. does not assume “too many committees” is the only problem;
5. proposes the smallest validation/removal experiment.

## Expected behaviors

The analysis should notice at least:
- large delay caused by evidence rework between day 17 and 28;
- architecture re-review may be duplicate work;
- steering committee may be a shadow veto / unclear step;
- advisers may function as de facto approvers;
- the process has a clear formal owner but still suffers actual-path ambiguity.

FAIL if it simply recommends eliminating governance layers without tracing the delay.
