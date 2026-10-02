from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import sys

HERE = Path(__file__).resolve()
EVAL_DIR = HERE.parents[1]
ROOT = HERE.parents[3]
if str(EVAL_DIR) not in sys.path:
    sys.path.insert(0, str(EVAL_DIR))

import campaign
import receipt
from common import load_campaign_cases, load_supplemental_cases


class RuntimeCampaignTests(unittest.TestCase):
    def setUp(self) -> None:
        (ROOT / ".tmp").mkdir(exist_ok=True)

    def test_campaign_resolves_exact_scope_and_isolation(self) -> None:
        self.assertEqual([], campaign.validate_campaign())
        cases = load_campaign_cases(ROOT, campaign.config()["campaign"])
        self.assertEqual(39, len(cases))
        counts = {}
        for case in cases.values():
            counts[case["suite"]] = counts.get(case["suite"], 0) + 1
        self.assertEqual(
            {"commerce": 6, "routing": 17, "executive-role": 14, "production-fallback": 2},
            counts,
        )
        supplemental = load_supplemental_cases(ROOT, campaign.config()["campaign"])
        self.assertEqual(
            [
                "oaf-decision-bottleneck-natural-pl",
                "oaf-decision-rights-natural-pl",
                "oaf-interface-natural-pl",
            ],
            sorted(supplemental),
        )
        self.assertEqual("operating-model-review", supplemental["oaf-interface-natural-pl"]["target"])
        self.assertEqual("decision-bottleneck-analysis", supplemental["oaf-decision-bottleneck-natural-pl"]["target"])
        self.assertEqual("decision-rights-review", supplemental["oaf-decision-rights-natural-pl"]["target"])
        self.assertEqual(
            ["case-001-opportunity-hunter", "case-002-security-sizing", "case-003-portfolio-review", "case-004-theme-discovery", "case-006-attention-acn"],
            campaign.config().get("retest_focus_case_ids"),
        )


    def test_explicit_fallback_requires_target_name_in_executor_input(self) -> None:
        case = {
            "id": "synthetic-explicit",
            "suite": "production-fallback",
            "mode": "explicit",
            "target": "oaf-health-check",
        }
        errors = campaign.explicit_fallback_input_errors(
            case,
            "Zrób przekrojową diagnozę problemu bez wskazywania workflow.",
        )
        self.assertTrue(any("must name target workflow oaf-health-check" in e for e in errors))

        self.assertEqual(
            [],
            campaign.explicit_fallback_input_errors(
                case,
                "Uruchom workflow oaf-health-check dla tej sytuacji.",
            ),
        )


    def test_generated_queue_uses_current_explicit_strategy_input(self) -> None:
        queue = campaign.queue_text(include_supplemental=True)
        self.assertIn(
            "Uruchom workflow oaf-health-check dla tej sytuacji.",
            queue,
        )

    def test_prepare_locks_package_catalog_components_and_fallback_absence(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            out = Path(td) / "campaign"
            campaign.prepare(out, require_pinned_commit=False)
            lock = json.loads((out / "lock.json").read_text(encoding="utf-8"))
            self.assertEqual("c7d64fcf6a89430524a805251180a71aa7e2ab38", lock["behavior_source_revision"])
            self.assertEqual("arek-ai-skills", lock["packages"]["production"]["name"])
            self.assertEqual("1.20.0", lock["packages"]["production"]["version"])
            self.assertEqual("arek-ai-skills-lab", lock["packages"]["lab"]["name"])
            self.assertEqual("0.14.0", lock["packages"]["lab"]["version"])
            self.assertNotIn("strategy-to-execution-diagnostic", lock["expected_catalogs"]["production"])
            self.assertNotIn("organizational-interface-review", lock["expected_catalogs"]["production"])
            self.assertIn("organizational-interface-review", lock["expected_catalogs"]["lab"])
            self.assertTrue(lock["components"])
            self.assertTrue(all(x.get("version") and x.get("content_sha256") for x in lock["components"]))
            self.assertEqual("production", lock["case_channels"]["fallback-strategy-production-002"])
            self.assertEqual("production", lock["case_channels"]["fallback-interface-explicit-production-002"])
            self.assertEqual("production", lock["case_channels"]["oaf-interface-natural-pl"])
            self.assertEqual(39, lock["core_case_count"])
            self.assertEqual(
                [
                    "oaf-decision-bottleneck-natural-pl",
                    "oaf-decision-rights-natural-pl",
                    "oaf-interface-natural-pl",
                ],
                lock["supplemental_case_ids"],
            )
            self.assertEqual(64, len(lock["campaign_definition_sha256"]))
            definitions = {item["id"]: item for item in lock["case_definitions"]}
            self.assertEqual(42, len(definitions))
            components = {(item["channel"], item["name"]): item for item in lock["components"]}
            self.assertEqual("1.5.0", components[("production", "oaf-health-check")]["version"])
            self.assertEqual("1.1.0", components[("production", "operating-model-review")]["version"])
            self.assertEqual("1.1.0", components[("production", "decision-bottleneck-analysis")]["version"])
            self.assertEqual("1.1.0", components[("production", "decision-rights-review")]["version"])
            strategy = definitions["fallback-strategy-production-002"]
            self.assertEqual("explicit", strategy["mode"])
            self.assertEqual("oaf-health-check", strategy["target"])
            self.assertEqual(64, len(strategy["input_sha256"]))
            self.assertEqual(64, len(strategy["rubric_sha256"]))

    def test_revised_fallback_identities_do_not_rewrite_historical_001_cases(self) -> None:
        active = load_campaign_cases(ROOT, campaign.config()["campaign"])
        self.assertIn("fallback-strategy-production-002", active)
        self.assertIn("fallback-interface-explicit-production-002", active)
        self.assertNotIn("fallback-strategy-production-001", active)
        self.assertNotIn("fallback-interface-production-001", active)
        historical_strategy = receipt.find_case(ROOT, "fallback-strategy-production-001")
        historical_interface = receipt.find_case(ROOT, "fallback-interface-production-001")
        self.assertEqual("oaf-health-check", historical_strategy[0])
        self.assertEqual("oaf-operating-model-redesign", historical_interface[0])

    def test_historical_receipt_identity_uses_recorded_behavior_revision(self) -> None:
        old_revision = "ff012e494f5b2f71803f850d71d20f54a3315e2b"
        for case_id, component_name, expected_version, current_expected_version in (
            ("fallback-strategy-production-001", "oaf-health-check", "1.0.0", "1.5.0"),
            ("fallback-interface-production-001", "oaf-operating-model-redesign", "1.0.0", "1.1.0"),
        ):
            target, case = receipt.find_case(ROOT, case_id)
            self.assertEqual(component_name, target)
            try:
                version, digest = receipt.component_identity_at_revision(ROOT, component_name, old_revision)
            except ValueError as exc:
                if "source revision unavailable in checkout" in str(exc):
                    self.skipTest("historical source commit unavailable in shallow checkout")
                raise
            self.assertEqual(expected_version, version)
            self.assertEqual(64, len(digest))
            current_version, current_digest = receipt.current_component_identity(ROOT, component_name)
            self.assertEqual(current_expected_version, current_version)
            self.assertNotEqual(digest, current_digest)


    def test_imported_r2_r3_r4_and_r5_runtime_statuses_remain_frozen(self) -> None:
        r2 = {
            "fallback-strategy-production-002": "FAIL",
            "fallback-interface-explicit-production-002": "PASS",
            "oaf-interface-natural-pl": "FAIL",
        }
        for case_id, status in r2.items():
            path = ROOT / "evals/results/runtime-campaign" / case_id / "2026-10-01-luna-r2" / "receipt.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(status, data["evaluation"]["status"])
            self.assertEqual("c0772e2e3727971b2e3fe8f9d56eccf6bdd87129", data["source_revision"])

        r3 = {
            "fallback-strategy-production-002": "FAIL",
            "fallback-interface-explicit-production-002": "PASS",
            "oaf-interface-natural-pl": "PASS",
            "oaf-decision-bottleneck-natural-pl": "PASS",
            "oaf-decision-rights-natural-pl": "PASS",
        }
        for case_id, status in r3.items():
            path = ROOT / "evals/results/runtime-campaign" / case_id / "2026-10-01-luna-r3" / "receipt.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(status, data["evaluation"]["status"])
            self.assertEqual("cde46f59c20a0d4313528185e5df079335633b10", data["source_revision"])

        r4_path = (
            ROOT / "evals/results/runtime-campaign/fallback-strategy-production-002"
            / "2026-10-01-luna-r4/receipt.json"
        )
        r4 = json.loads(r4_path.read_text(encoding="utf-8"))
        self.assertEqual("FAIL", r4["evaluation"]["status"])
        self.assertEqual("28a7681cf024bb7aaad7a979e7ce7253139d5bd4", r4["source_revision"])

        r5_path = (
            ROOT / "evals/results/runtime-campaign/fallback-strategy-production-002"
            / "2026-10-01-luna-r5/receipt.json"
        )
        r5 = json.loads(r5_path.read_text(encoding="utf-8"))
        self.assertEqual("FAIL", r5["evaluation"]["status"])
        self.assertEqual("a5c4001d28f45d3fb799f07a2c880f406f58cc65", r5["source_revision"])

    def test_historical_receipts_use_explicit_compatibility_profiles(self) -> None:
        self.assertEqual(
            "historical-r1",
            campaign.evidence_compatibility_profile(
                "ff012e494f5b2f71803f850d71d20f54a3315e2b"
            ),
        )
        self.assertEqual(
            "historical-r2",
            campaign.evidence_compatibility_profile(
                "c0772e2e3727971b2e3fe8f9d56eccf6bdd87129"
            ),
        )
        self.assertEqual(
            "historical-r3",
            campaign.evidence_compatibility_profile(
                "cde46f59c20a0d4313528185e5df079335633b10"
            ),
        )
        self.assertEqual(
            "historical-r4",
            campaign.evidence_compatibility_profile(
                "28a7681cf024bb7aaad7a979e7ce7253139d5bd4"
            ),
        )
        self.assertEqual(
            "historical-r5",
            campaign.evidence_compatibility_profile(
                "a5c4001d28f45d3fb799f07a2c880f406f58cc65"
            ),
        )
        self.assertEqual(
            "historical-r7",
            campaign.evidence_compatibility_profile(
                "008c9944cf3a8bc3e2d7231a4862aaf00e722889"
            ),
        )
        self.assertEqual(
            "historical-r8",
            campaign.evidence_compatibility_profile(
                "6a598a036133284852c1dcb9f295aaefbb69686d"
            ),
        )
        self.assertEqual(
            "historical-r9",
            campaign.evidence_compatibility_profile(
                "e301e7af458a2fb2461c7576960ba8415bf3435f"
            ),
        )
        self.assertEqual(
            "historical-r10",
            campaign.evidence_compatibility_profile(
                "0900bca7816341b1727285669fac88148ebc4174"
            ),
        )
        self.assertEqual(
            "historical-r11",
            campaign.evidence_compatibility_profile(
                "5a9968dc72fb21d2f36e4b9dbc76642cb11916a0"
            ),
        )
        self.assertEqual(
            "historical-r12",
            campaign.evidence_compatibility_profile(
                "63fd3fda0ab4931cc0652f0565aa29fc59b3b67d"
            ),
        )
        self.assertEqual(
            "historical-r13",
            campaign.evidence_compatibility_profile(
                "22219cae549a0588e08a887675f8cfc3c6758745"
            ),
        )
        self.assertEqual(
            "historical-r14",
            campaign.evidence_compatibility_profile(
                "a21dc626afe744bfb48dd96e29b9c7bda7cddf19"
            ),
        )
        with self.assertRaisesRegex(ValueError, "unsupported evidence source revision"):
            campaign.evidence_compatibility_profile("deadbeef")

    def test_visual_pass_requires_external_client_display_evidence(self) -> None:
        cfg = dict(campaign.config())
        case_id = "case-003-portfolio-review"
        cfg["client_display_validation_case_ids"] = [case_id]
        cfg["client_display_evidence_types"] = ["screenshot", "telemetry", "user_confirmation"]

        with patch.object(campaign, "config", return_value=cfg):
            missing = campaign.client_display_evidence_errors(case_id, {}, "PASS")
            self.assertTrue(any("external client-display evidence" in item for item in missing))

            pending = campaign.client_display_evidence_errors(
                case_id,
                {
                    "client_display_evidence": {
                        "status": "PENDING",
                        "type": "screenshot",
                        "reference": "shot-1",
                    }
                },
                "PASS",
            )
            self.assertTrue(any("must be CONFIRMED" in item for item in pending))

            valid = campaign.client_display_evidence_errors(
                case_id,
                {
                    "client_display_evidence": {
                        "status": "CONFIRMED",
                        "type": "screenshot",
                        "reference": "shot-1",
                    }
                },
                "PASS",
            )
            self.assertEqual([], valid)

            review = campaign.client_display_evidence_errors(case_id, {}, "REVIEW_REQUIRED")
            self.assertEqual([], review)

    def test_smoke_rejects_simultaneous_production_and_lab(self) -> None:
        lock = {
            "packages": {
                "production": {"name": "arek-ai-skills", "version": "1.8.0"},
                "lab": {"name": "arek-ai-skills-lab", "version": "0.3.0"},
            },
            "expected_catalogs": {"production": ["a", "b"], "lab": ["c"]},
        }
        observed = {
            "channel": "production",
            "package": {"name": "arek-ai-skills", "version": "1.8.0"},
            "enabled_packages": ["arek-ai-skills", "arek-ai-skills-lab"],
            "catalog": ["a", "b"],
            "runtime": {
                "provider": "provider",
                "model_id": "model",
                "reasoning": "medium",
                "available_tools": [],
            },
        }
        with tempfile.TemporaryDirectory() as td:
            lp = Path(td) / "lock.json"
            op = Path(td) / "observed.json"
            lp.write_text(json.dumps(lock), encoding="utf-8")
            op.write_text(json.dumps(observed), encoding="utf-8")
            errors = campaign.verify_smoke(lp, op)
        self.assertTrue(any("simultaneously enabled" in e for e in errors))

    def _observed_smoke(self, lock: dict, channel: str, *, origin: str = "offline") -> dict:
        package = dict(lock["packages"][channel])
        components = [
            {
                "name": item["name"],
                "version": item["version"],
                "content_sha256": item["content_sha256"],
            }
            for item in lock["components"]
            if item["channel"] == channel
        ]
        return {
            "evidence_origin": origin,
            "channel": channel,
            "package": package,
            "components": components,
            "enabled_packages": [package["name"]],
            "catalog": list(lock["expected_catalogs"][channel]),
            "runtime": {
                "provider": "offline-synthetic-provider",
                "model_id": "offline-synthetic-model",
                "reasoning": "offline",
                "available_tools": ["offline-fixture", "mcp__arek-chart-renderer__render_bar_chart"],
            },
        }

    def _import_args(
        self,
        *,
        case_id: str,
        run_id: str,
        lock: Path,
        smoke: Path,
        output: Path,
        trace: Path,
        status: str,
    ) -> SimpleNamespace:
        return SimpleNamespace(
            case_id=case_id,
            run_id=run_id,
            lock=str(lock),
            smoke=str(smoke),
            output=str(output),
            trace=str(trace),
            status=status,
            reviewer="offline-unit-test",
            assisted=False,
            evidence_origin="offline",
            note="synthetic offline campaign-path test; not runtime evidence",
        )

    def test_full_offline_path_prepare_smoke_import_validate_and_moved_checkout(self) -> None:
        cfg = dict(campaign.config())
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            td_path = Path(td)
            prepared = td_path / "prepared"
            campaign.prepare(prepared, require_pinned_commit=False)
            lock_path = prepared / "lock.json"
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            validated_lock = campaign.validate_lock_file(lock_path)
            self.assertEqual(lock["campaign_definition_sha256"], validated_lock["campaign_definition_sha256"])

            case_id = "case-001-premium-vs-generic"
            channel = lock["case_channels"][case_id]
            observed = self._observed_smoke(lock, channel)
            smoke_path = td_path / "smoke.json"
            smoke_path.write_text(json.dumps(observed, indent=2) + "\n", encoding="utf-8")
            self.assertEqual([], campaign.verify_smoke(lock_path, smoke_path))

            output = td_path / "output.md"
            trace = td_path / "trace.json"
            output.write_text("Synthetic offline response for import-path validation.\n", encoding="utf-8")
            trace.write_text(
                json.dumps({
                    "selected_capabilities": ["commerce-product-deep-dive"],
                    "tool_calls": [],
                    "notes": "offline synthetic trace",
                }),
                encoding="utf-8",
            )

            evidence_rel = f".tmp/{td_path.name}/evidence"
            patched_cfg = dict(cfg)
            patched_cfg["evidence_root"] = evidence_rel
            args = self._import_args(
                case_id=case_id,
                run_id="offline-good",
                lock=lock_path,
                smoke=smoke_path,
                output=output,
                trace=trace,
                status="REVIEW_REQUIRED",
            )
            with patch.object(campaign, "config", return_value=patched_cfg):
                receipt_path = campaign.import_run(args)
                self.assertEqual([], campaign.validate_evidence())

            record = json.loads(receipt_path.read_text(encoding="utf-8"))
            self.assertEqual("offline", record["execution"]["evidence_origin"])
            self.assertEqual([], record["execution"]["selection_findings"])
            self.assertEqual(
                receipt.current_component_identity(ROOT, case_id if False else "commerce-product-deep-dive")[1],
                record["component"]["content_sha256"],
            )
            self.assertNotEqual(
                record["component"]["content_sha256"],
                record["runtime_artifact"]["component_content_sha256"],
            )

            moved = td_path / "moved-checkout"
            shutil.copytree(
                ROOT,
                moved,
                ignore=shutil.ignore_patterns(".git", ".tmp", "__pycache__", "*.pyc"),
            )
            source_evidence = ROOT / evidence_rel
            moved_evidence = moved / evidence_rel
            moved_evidence.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source_evidence, moved_evidence)
            moved_record_path = (
                moved / evidence_rel / case_id / "offline-good" / "receipt.json"
            )
            moved_record = json.loads(moved_record_path.read_text(encoding="utf-8"))
            moved_errors = receipt.validate_receipt_data(
                moved_record,
                root=moved,
                current_revision=moved_record["source_revision"],
            )
            self.assertEqual([], moved_errors)
            moved_lock = moved / "lock.json"
            shutil.copyfile(lock_path, moved_lock)
            validated_moved_lock = campaign.validate_lock_file(moved_lock, root=moved)
            self.assertEqual(lock["campaign"], validated_moved_lock["campaign"])

    def test_import_rejects_stale_or_incomplete_lock_without_partial_evidence(self) -> None:
        cfg = dict(campaign.config())
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            td_path = Path(td)
            prepared = td_path / "prepared"
            campaign.prepare(prepared, require_pinned_commit=False)
            good_lock_path = prepared / "lock.json"
            good_lock = json.loads(good_lock_path.read_text(encoding="utf-8"))

            case_id = "fallback-strategy-production-002"
            channel = good_lock["case_channels"][case_id]
            observed = self._observed_smoke(good_lock, channel)
            smoke_path = td_path / "smoke.json"
            smoke_path.write_text(json.dumps(observed), encoding="utf-8")
            output = td_path / "output.md"
            trace = td_path / "trace.json"
            output.write_text("Synthetic offline lock-validation output.\n", encoding="utf-8")
            trace.write_text(
                json.dumps({"selected_capabilities": ["oaf-health-check"], "tool_calls": []}),
                encoding="utf-8",
            )

            evidence_rel = f".tmp/{td_path.name}/lock-negative-evidence"
            patched_cfg = dict(cfg)
            patched_cfg["evidence_root"] = evidence_rel

            strategy_index = next(
                i for i, item in enumerate(good_lock["case_definitions"])
                if item["id"] == case_id
            )

            variants = {}

            old_input = json.loads(json.dumps(good_lock))
            old_input["case_definitions"][strategy_index]["input_sha256"] = "0" * 64
            variants["old-input"] = old_input

            changed_rubric = json.loads(json.dumps(good_lock))
            changed_rubric["case_definitions"][strategy_index]["rubric_sha256"] = "1" * 64
            variants["changed-rubric"] = changed_rubric

            changed_campaign = json.loads(json.dumps(good_lock))
            changed_campaign["campaign_definition_sha256"] = "2" * 64
            variants["changed-campaign"] = changed_campaign

            missing_fields = json.loads(json.dumps(good_lock))
            missing_fields.pop("case_definitions")
            variants["missing-fields"] = missing_fields

            missing_case = json.loads(json.dumps(good_lock))
            missing_case["case_definitions"] = [
                item for item in missing_case["case_definitions"] if item["id"] != case_id
            ]
            variants["missing-case"] = missing_case

            unknown_case = json.loads(json.dumps(good_lock))
            unknown = json.loads(json.dumps(unknown_case["case_definitions"][0]))
            unknown["id"] = "unknown-runtime-case"
            unknown_case["case_definitions"].append(unknown)
            variants["unknown-case"] = unknown_case

            legacy_r2 = json.loads(json.dumps(good_lock))
            legacy_r2["schema_version"] = "1.0"
            legacy_r2.pop("campaign_definition_sha256")
            legacy_r2.pop("case_definitions")
            variants["legacy-r2-lock"] = legacy_r2

            for name, payload in variants.items():
                with self.subTest(name=name):
                    lock_path = td_path / f"{name}.lock.json"
                    lock_path.write_text(json.dumps(payload), encoding="utf-8")
                    run_id = f"offline-{name}"
                    dest = ROOT / evidence_rel / case_id / run_id
                    args = self._import_args(
                        case_id=case_id,
                        run_id=run_id,
                        lock=lock_path,
                        smoke=smoke_path,
                        output=output,
                        trace=trace,
                        status="REVIEW_REQUIRED",
                    )
                    with patch.object(campaign, "config", return_value=patched_cfg):
                        with self.assertRaisesRegex(ValueError, "invalid campaign lock"):
                            campaign.import_run(args)
                    self.assertFalse(dest.exists(), f"partial evidence written for {name}")

    def test_lock_rejects_unknown_active_import_case_before_writes(self) -> None:
        cfg = dict(campaign.config())
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            td_path = Path(td)
            prepared = td_path / "prepared"
            campaign.prepare(prepared, require_pinned_commit=False)
            lock_path = prepared / "lock.json"
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            observed = self._observed_smoke(lock, "production")
            smoke_path = td_path / "smoke.json"
            smoke_path.write_text(json.dumps(observed), encoding="utf-8")
            output = td_path / "output.md"
            trace = td_path / "trace.json"
            output.write_text("offline\n", encoding="utf-8")
            trace.write_text(json.dumps({"selected_capabilities": []}), encoding="utf-8")
            evidence_rel = f".tmp/{td_path.name}/unknown-import-evidence"
            patched_cfg = dict(cfg)
            patched_cfg["evidence_root"] = evidence_rel
            args = self._import_args(
                case_id="unknown-active-case",
                run_id="offline-unknown",
                lock=lock_path,
                smoke=smoke_path,
                output=output,
                trace=trace,
                status="REVIEW_REQUIRED",
            )
            with patch.object(campaign, "config", return_value=patched_cfg):
                with self.assertRaisesRegex(ValueError, "unknown active campaign case"):
                    campaign.import_run(args)
            self.assertFalse((ROOT / evidence_rel / "unknown-active-case").exists())

    def test_bad_routing_can_be_archived_as_fail_but_not_pass(self) -> None:
        cfg = dict(campaign.config())
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            td_path = Path(td)
            prepared = td_path / "prepared"
            campaign.prepare(prepared, require_pinned_commit=False)
            lock_path = prepared / "lock.json"
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            case_id = "career-role-eval-en"
            channel = lock["case_channels"][case_id]
            observed = self._observed_smoke(lock, channel)
            smoke_path = td_path / "smoke.json"
            smoke_path.write_text(json.dumps(observed), encoding="utf-8")
            output = td_path / "output.md"
            trace = td_path / "trace.json"
            output.write_text("Synthetic wrong-route output.\n", encoding="utf-8")
            trace.write_text(
                json.dumps({"selected_capabilities": [], "tool_calls": []}),
                encoding="utf-8",
            )
            evidence_rel = f".tmp/{td_path.name}/evidence-routing"
            patched_cfg = dict(cfg)
            patched_cfg["evidence_root"] = evidence_rel

            fail_args = self._import_args(
                case_id=case_id,
                run_id="offline-routing-fail",
                lock=lock_path,
                smoke=smoke_path,
                output=output,
                trace=trace,
                status="FAIL",
            )
            with patch.object(campaign, "config", return_value=patched_cfg):
                receipt_path = campaign.import_run(fail_args)
            data = json.loads(receipt_path.read_text(encoding="utf-8"))
            self.assertEqual("FAIL", data["evaluation"]["status"])
            self.assertTrue(data["execution"]["selection_findings"])
            self.assertEqual("offline", data["execution"]["evidence_origin"])

            pass_args = self._import_args(
                case_id=case_id,
                run_id="offline-routing-pass",
                lock=lock_path,
                smoke=smoke_path,
                output=output,
                trace=trace,
                status="PASS",
            )
            with patch.object(campaign, "config", return_value=patched_cfg):
                with self.assertRaisesRegex(ValueError, "PASS forbidden"):
                    campaign.import_run(pass_args)

    def test_smoke_rejects_old_release_with_same_name_version_and_catalog(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            prepared = Path(td) / "prepared"
            campaign.prepare(prepared, require_pinned_commit=False)
            lock_path = prepared / "lock.json"
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            observed = self._observed_smoke(lock, "production")
            observed["package"]["release_id"] = "1.8.0+stale0000000"
            observed_path = Path(td) / "stale-smoke.json"
            observed_path.write_text(json.dumps(observed), encoding="utf-8")
            errors = campaign.verify_smoke(lock_path, observed_path)
        self.assertTrue(any("package.release_id" in e for e in errors), errors)


    def test_receipt_paths_are_portable_and_trace_is_hashed(self) -> None:
        cfg = campaign.config()
        cases = load_campaign_cases(ROOT, campaign.config()["campaign"])
        case = cases["case-001-premium-vs-generic"]
        version, digest = receipt.current_component_identity(ROOT, case["target"])
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            run = Path(td)
            output = run / "output.md"
            trace = run / "trace.json"
            output.write_text("runtime output\n", encoding="utf-8")
            trace.write_text(json.dumps({"selected_capabilities": [case["target"]]}), encoding="utf-8")
            ns = argparse.Namespace(
                case_id=case["id"],
                status="REVIEW_REQUIRED",
                evidence_scope="current-version",
                source_revision=cfg["behavior_source_revision"],
                component=case["target"],
                component_version=version,
                component_digest=digest,
                provider="provider",
                model_id="model",
                reasoning="medium",
                catalog=[case["target"]],
                tools=["web"],
                prompt=(ROOT / case["input"]).read_text(encoding="utf-8"),
                output=str(output),
                tool_trace=str(trace),
                reviewer="unit-test",
                assisted=False,
                note=None,
            )
            old = os.environ.get("SOURCE_REVISION")
            os.environ["SOURCE_REVISION"] = cfg["behavior_source_revision"]
            try:
                record = receipt.create_receipt(ns)
            finally:
                if old is None:
                    os.environ.pop("SOURCE_REVISION", None)
                else:
                    os.environ["SOURCE_REVISION"] = old
            self.assertFalse(Path(record["execution"]["actual_output_path"]).is_absolute())
            self.assertFalse(Path(record["execution"]["tool_trace_path"]).is_absolute())
            self.assertEqual(64, len(record["execution"]["tool_trace_sha256"]))
            errors = receipt.validate_receipt_data(
                record,
                root=ROOT,
                current_revision=record["source_revision"],
            )
            self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
