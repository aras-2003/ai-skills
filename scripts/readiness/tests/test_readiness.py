from __future__ import annotations

import datetime as dt
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
READINESS_DIR = HERE.parents[1]
if str(READINESS_DIR) not in sys.path:
    sys.path.insert(0, str(READINESS_DIR))

import validate_readiness


class ReadinessPolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.today = dt.date(2026, 10, 1)
        self.review_by = dt.date(2026, 10, 14)

    def _pending(self) -> dict:
        return {
            "current_runtime_receipt": "pending",
            "maturity_disposition": "retain-existing-pending-evidence-review",
            "evidence_gap": "runtime receipt missing",
            "limitation": "no current runtime proof",
            "exception_owner": "owner",
            "exception_expires": "2026-10-14",
        }

    def test_verified_without_receipt_is_blocked(self) -> None:
        rec = {
            "current_runtime_receipt": "verified",
            "maturity_disposition": "verified-current-version",
        }
        with tempfile.TemporaryDirectory() as td:
            errors = validate_readiness.validate_record(
                Path(td), "demo", "1.0.0", rec,
                review_by=self.review_by, today=self.today,
            )
        self.assertTrue(any("verified requires receipt" in e for e in errors))

    def test_historical_receipt_cannot_satisfy_verified(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            receipt_path = root / "receipt.json"
            receipt_path.write_text(json.dumps({
                "evidence_scope": "historical",
                "evaluation": {"status": "PASS"},
                "component": {"name": "demo", "version": "1.0.0"},
                "source_revision": "abcdef1",
            }), encoding="utf-8")
            rec = {
                "current_runtime_receipt": "verified",
                "maturity_disposition": "verified-current-version",
                "receipt": "receipt.json",
            }
            with patch.object(validate_readiness.eval_receipt, "validate_receipt_data", return_value=[]):
                errors = validate_readiness.validate_record(
                    root, "demo", "1.0.0", rec,
                    review_by=self.review_by, today=self.today,
                )
        self.assertTrue(any("evidence_scope=current-version" in e for e in errors))

    def test_expired_pending_exception_is_blocked(self) -> None:
        rec = self._pending()
        rec["exception_expires"] = "2000-01-01"
        with tempfile.TemporaryDirectory() as td:
            errors = validate_readiness.validate_record(
                Path(td), "demo", "1.0.0", rec,
                review_by=self.review_by, today=self.today,
            )
        self.assertTrue(any("exception expired" in e for e in errors))

    def test_pending_exception_cannot_cover_known_high_severity_failure(self) -> None:
        rec = self._pending()
        rec["known_high_severity_failure"] = True
        with tempfile.TemporaryDirectory() as td:
            errors = validate_readiness.validate_record(
                Path(td), "demo", "1.0.0", rec,
                review_by=self.review_by, today=self.today,
            )
        self.assertTrue(any("high-severity" in e for e in errors))

    def test_not_required_needs_justification(self) -> None:
        rec = {
            "current_runtime_receipt": "not-required",
            "maturity_disposition": "not-required",
        }
        with tempfile.TemporaryDirectory() as td:
            errors = validate_readiness.validate_record(
                Path(td), "demo", "1.0.0", rec,
                review_by=self.review_by, today=self.today,
            )
        self.assertTrue(any("not_required_reason" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
