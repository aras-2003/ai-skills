# Portfolio Health Review — Case 001

## Scenario

An IT portfolio contains 18 active initiatives.

Available evidence:
- 15 projects report green or amber delivery status;
- all 18 have approved budgets;
- total committed delivery capacity is estimated at 128% of available specialist capacity for the next two quarters;
- five initiatives depend on the same data-platform team;
- three initiatives require the same architecture lead during overlapping periods;
- four initiatives have no explicit measurable outcome beyond delivery completion;
- two initiatives appear to solve overlapping customer-identity problems;
- three mandatory cybersecurity initiatives consume 22% of available capacity;
- leadership has not stopped an initiative in the last 18 months;
- two initiatives are strategically important but cannot start until a shared platform dependency is completed.

## Test objective

Evaluate whether `portfolio-health-review`:
1. diagnoses the portfolio as a system rather than averaging project status;
2. identifies capacity and dependency overload;
3. separates mandatory/discretionary work;
4. identifies outcome-traceability gaps and duplication;
5. assesses whether the portfolio is ready for prioritisation;
6. avoids generating a ranking unless evidence supports it.

## Expected behaviors

PASS if the skill identifies that:
- green project status does not imply a healthy portfolio;
- 128% capacity commitment is a system constraint;
- shared bottleneck resources create sequencing risk;
- no-stop behavior is a portfolio governance signal;
- duplicate initiative intent should be validated;
- prioritisation is needed, but only after comparable evidence is normalized.

FAIL if it concludes the portfolio is mostly healthy because most projects are green.
