---
name: valuation-scenario-review
description: 'Build bear, base and bull valuation scenarios for one security using
  explicit operating assumptions, valuation methods and market-implied expectations.
  Use when valuation could change an investment decision or position size. Do not
  use as a standalone price-target generator.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.1.0
  maturity: candidate
  risk: high
  last_reviewed: '2026-10-02'
---

# Valuation Scenario Review

## Purpose
Make valuation assumptions visible and test sensitivity instead of producing false precision.

## Procedure
1. Select a method appropriate to the business and cycle.
2. Build bear/base/bull operating assumptions with an explicit horizon.
3. Separate earnings/cash-flow assumptions from terminal or exit multiple assumptions.
4. Compare with historical ranges and relevant peers where useful.
5. Estimate what current price appears to imply.
6. Identify which assumption drives most of the valuation dispersion.
7. Do not assign scenario probabilities unless there is an explicit evidence basis.

## Decision rules
- Peak-cycle earnings require normalized scenarios.
- A wide valuation range is information about uncertainty, not a reason to average mechanically.
- Analyst targets are secondary evidence.
- Precision beyond input quality is misleading.

## Output contract
Scenario table; key assumptions; implied expectations; sensitivity; major uncertainty; data gaps.

## Quality checks
- [ ] Bear/base/bull differ in operating logic, not only multiple.
- [ ] Current price implications are addressed.
- [ ] No unsupported probability weighting.
- [ ] Cyclicality is normalized where relevant.
