# Capability Map Review — Case 001

## Scenario

A retail/financial-services technology organisation maintains an L1/L2 business capability map for investment and architecture planning.

Extract:
- Customer Management
  - Customer Onboarding
  - CRM Team
  - Customer Service Process
  - Customer Data Platform
- Payments
  - Payment Processing
  - Fraud Management
  - Payment Operations
- Data & Analytics
  - Reporting
  - Data Governance
  - Power BI
  - Advanced Analytics

Leadership wants to use the map to:
1. identify where investment is duplicated;
2. link strategic priorities to capabilities;
3. map key applications and owners;
4. support portfolio prioritisation.

Known evidence:
- "CRM Team" is an organisation unit;
- "Customer Service Process" is a process label;
- "Customer Data Platform" and "Power BI" are technology/product labels;
- ownership is incomplete;
- some applications map to multiple capabilities;
- the map does not yet contain performance or maturity scores.

## Test objective

Evaluate whether `capability-map-review`:
- anchors the review to the stated investment/portfolio decision use;
- detects org/process/system contamination;
- does not infer capability maturity from labels;
- does not demand a perfect taxonomy before the map can be useful;
- prioritises corrections that materially improve investment/architecture decisions.

## Expected behavior

PASS if it:
- flags the contaminated entries;
- proposes capability-style replacements or reclassification without rebuilding the whole map;
- treats missing ownership as missing evidence/operating-model linkage;
- does not invent maturity scores;
- explains whether the current map is fit now, fit with corrections or not fit for the stated decisions.
