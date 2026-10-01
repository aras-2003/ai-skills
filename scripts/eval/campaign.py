from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
PACKAGE_DIR = ROOT / "scripts" / "package"
if str(PACKAGE_DIR) not in sys.path:
    sys.path.insert(0, str(PACKAGE_DIR))

from common import load_campaign_cases, load_supplemental_cases
import receipt
import validate_routing
import build_plugin
import artifact_validation

CONFIG = ROOT / "evals/campaigns/runtime-validation-2026-10-r2/campaign.yaml"


def config():
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}


def behavior_changes(pinned: str, *, require_commit: bool = False) -> list[str]:
    exists = subprocess.run(
        ["git", "cat-file", "-e", pinned + "^{commit}"],
        cwd=ROOT, check=False, capture_output=True, text=True,
    )
    if exists.returncode:
        if require_commit:
            raise ValueError(f"pinned behavior commit is unavailable in this checkout: {pinned}")
        return []
    out = subprocess.check_output(
        ["git", "diff", "--name-only", pinned, "HEAD", "--", "skills", "workflows", "release/package.yaml"],
        cwd=ROOT, text=True,
    ).strip()
    changed = []
    for raw in out.splitlines():
        path = raw.strip()
        if not path:
            continue
        parts = Path(path).parts
        if "tests" in parts or "evals" in parts:
            continue
        if Path(path).name.lower().startswith("readme"):
            continue
        changed.append(path)
    return changed


def validate_campaign() -> list[str]:
    errors = []
    cfg = config()
    cases = load_campaign_cases(ROOT)
    expected = {"commerce": 6, "routing": 16, "executive-role": 14, "production-fallback": 2}
    counts = {k: 0 for k in expected}
    known = validate_routing.known_capability_names(ROOT)

    if len(cases) != 38:
        errors.append(f"expected 38 campaign cases, got {len(cases)}")

    for cid, case in cases.items():
        suite = str(case.get("suite") or "")
        if suite not in counts:
            errors.append(f"{cid}: unknown suite {suite}")
            continue
        counts[suite] += 1
        ip = ROOT / str(case.get("input") or "")
        rp = ROOT / str(case.get("rubric") or "")
        if not ip.is_file() or not ip.name.endswith(".input.md"):
            errors.append(f"{cid}: missing/invalid executor input")
            continue
        if not rp.is_file() or not rp.name.endswith(".rubric.yaml"):
            errors.append(f"{cid}: missing/invalid evaluator rubric")
            continue
        if case.get("mode") == "natural-routing":
            leaked = validate_routing.leaked_capabilities(ip.read_text(encoding="utf-8"), known)
            if leaked:
                errors.append(f"{cid}: executor input leaks capability names: {', '.join(leaked)}")

    for suite, count in expected.items():
        if counts[suite] != count:
            errors.append(f"{suite}: expected {count}, got {counts[suite]}")

    supplemental = load_supplemental_cases(ROOT)
    if len(supplemental) != 1:
        errors.append(f"supplemental routing: expected 1 case, got {len(supplemental)}")
    for cid, case in supplemental.items():
        ip = ROOT / str(case.get("input") or "")
        rp = ROOT / str(case.get("rubric") or "")
        if not ip.is_file() or not ip.name.endswith(".input.md"):
            errors.append(f"{cid}: missing/invalid supplemental executor input")
            continue
        if not rp.is_file() or not rp.name.endswith(".rubric.yaml"):
            errors.append(f"{cid}: missing/invalid supplemental evaluator rubric")
            continue
        leaked = validate_routing.leaked_capabilities(ip.read_text(encoding="utf-8"), known)
        if leaked:
            errors.append(f"{cid}: supplemental input leaks capability names: {', '.join(leaked)}")

    source = yaml.safe_load((ROOT / cfg["executive_source"]).read_text(encoding="utf-8")) or {}
    source_by_id = {str(x["id"]): x for x in source.get("cases", []) if isinstance(x, dict) and x.get("id")}
    for cid in cfg.get("executive_case_ids", []):
        case = cases.get(cid)
        original = source_by_id.get(cid)
        if not case or not original:
            errors.append(f"{cid}: missing split/source case")
            continue
        split_input = (ROOT / case["input"]).read_text(encoding="utf-8").strip()
        if split_input != str(original.get("input") or "").strip():
            errors.append(f"{cid}: executor split drifted from source")
        rub = yaml.safe_load((ROOT / case["rubric"]).read_text(encoding="utf-8")) or {}
        exp = original.get("expected") or {}
        if rub.get("should_trigger") != exp.get("should_trigger"):
            errors.append(f"{cid}: should_trigger drift")
        if list((rub.get("assertions") or {}).get("manual") or []) != list(exp.get("must") or []):
            errors.append(f"{cid}: must assertion drift")
        if list((rub.get("assertions") or {}).get("manual_not") or []) != list(exp.get("must_not") or []):
            errors.append(f"{cid}: must_not assertion drift")

    pinned = str(cfg.get("behavior_source_revision") or "")
    changed = behavior_changes(pinned, require_commit=False)
    if changed:
        errors.append("behavior changed after pinned SHA: " + ", ".join(changed))
    return errors


def ordered_cases(include_supplemental: bool = False):
    cfg = config()
    rank = {name: i for i, name in enumerate(cfg.get("execution_order", []))}
    cases = list(load_campaign_cases(ROOT).values())
    if include_supplemental:
        cases.extend(load_supplemental_cases(ROOT).values())
    return sorted(cases, key=lambda x: (rank.get(x.get("suite"), 98 if x.get("suite") == "supplemental-routing" else 99), x["id"]))


def queue_text(include_supplemental: bool = False) -> str:
    out = [
        "# Runtime validation queue",
        "",
        "Executor-only inputs. Never provide the referenced rubric to the executor session.",
        "",
    ]
    for i, case in enumerate(ordered_cases(include_supplemental), 1):
        prompt = (ROOT / case["input"]).read_text(encoding="utf-8").rstrip()
        out += [
            f"## {i:02d}. {case['id']}",
            f"- suite: {case['suite']}",
            f"- subject: {case['target']}",
            f"- mode: {case['mode']}",
            "",
            "~~~text",
            prompt,
            "~~~",
            "",
        ]
    return "\n".join(out)


def prepare(out: Path, *, require_pinned_commit: bool = True) -> None:
    errors = validate_campaign()
    if errors:
        raise ValueError("; ".join(errors))
    cfg = config()
    pinned = cfg["behavior_source_revision"]
    changed = behavior_changes(pinned, require_commit=require_pinned_commit)
    if changed:
        raise ValueError("behavior changed after pinned SHA: " + ", ".join(changed))
    production = out / "production-plugin"
    lab = out / "lab-plugin"
    out.mkdir(parents=True, exist_ok=True)

    old = os.environ.get("SOURCE_REVISION")
    os.environ["SOURCE_REVISION"] = pinned
    try:
        build_plugin.build(ROOT, production, "production")
        env = dict(os.environ)
        subprocess.run(
            [sys.executable, str(ROOT / "scripts/package/build_lab_plugin.py"), "--output", str(lab)],
            cwd=ROOT, env=env, check=True,
        )
    finally:
        if old is None:
            os.environ.pop("SOURCE_REVISION", None)
        else:
            os.environ["SOURCE_REVISION"] = old

    for package_path, is_lab in ((production, False), (lab, True)):
        artifact_errors = artifact_validation.validate_tree(package_path, allow_lab_evals=is_lab)
        if artifact_errors:
            raise ValueError("; ".join(artifact_errors))

    packages = {}
    catalogs = {}
    components = []
    for channel, package_path in (("production", production), ("lab", lab)):
        caps = json.loads((package_path / "capabilities.json").read_text(encoding="utf-8"))
        rel = json.loads((package_path / "release-manifest.json").read_text(encoding="utf-8"))
        plugin = json.loads((package_path / "plugin.json").read_text(encoding="utf-8"))
        by_name = {x["name"]: x for x in caps.get("capabilities", [])}
        catalogs[channel] = by_name
        packages[channel] = {
            "name": plugin.get("name"),
            "version": plugin.get("version"),
            "release_id": rel.get("release_id"),
            "source_revision": rel.get("source_revision"),
            "payload_content_sha256": rel.get("payload_content_sha256"),
        }
        for item in by_name.values():
            components.append({
                "channel": channel,
                "name": item.get("name"),
                "kind": item.get("kind"),
                "version": item.get("version"),
                "maturity": item.get("maturity"),
                "content_sha256": item.get("content_sha256"),
            })

    for unavailable in ("strategy-to-execution-diagnostic", "organizational-interface-review"):
        if unavailable in catalogs["production"]:
            raise ValueError(f"fallback campaign precondition changed: {unavailable} is now in production")

    all_cases = {**load_campaign_cases(ROOT), **load_supplemental_cases(ROOT)}
    case_channels = {}
    for case in all_cases.values():
        target = case["target"]
        if target in catalogs["production"]:
            case_channels[case["id"]] = "production"
        elif target in catalogs["lab"]:
            case_channels[case["id"]] = "lab"
        else:
            raise ValueError(f"campaign subject absent from both package catalogs: {target}")

    lock = {
        "schema_version": "1.0",
        "campaign": cfg["campaign"],
        "behavior_source_revision": pinned,
        "packages": packages,
        "expected_catalogs": {name: sorted(items) for name, items in catalogs.items()},
        "case_channels": case_channels,
        "core_case_count": len(load_campaign_cases(ROOT)),
        "supplemental_case_ids": sorted(load_supplemental_cases(ROOT)),
        "components": components,
    }
    (out / "lock.json").write_text(json.dumps(lock, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "QUEUE.md").write_text(queue_text(), encoding="utf-8")
    for channel in ("production", "lab"):
        package_info = packages[channel]
        smoke = {
            "channel": channel,
            "package": {
                "name": package_info["name"],
                "version": package_info["version"],
                "release_id": None,
                "source_revision": None,
                "payload_content_sha256": None,
            },
            "components": [],
            "enabled_packages": [package_info["name"]],
            "catalog": [],
            "runtime": {
                "provider": None,
                "model_id": None,
                "reasoning": None,
                "available_tools": [],
            },
        }
        (out / f"smoke-{channel}-template.json").write_text(
            json.dumps(smoke, indent=2) + "\n", encoding="utf-8"
        )


def verify_smoke(lock_path: Path, observed_path: Path) -> list[str]:
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    obs = json.loads(observed_path.read_text(encoding="utf-8"))
    errors = []
    channel = obs.get("channel")
    if channel not in lock.get("packages", {}):
        return [f"unknown smoke channel: {channel}"]
    expected_package = lock["packages"][channel]
    pkg = obs.get("package") or {}
    runtime = obs.get("runtime") or {}
    enabled = list(obs.get("enabled_packages") or [])
    catalog = list(obs.get("catalog") or [])
    observed_components = obs.get("components")
    if not isinstance(observed_components, list):
        observed_components = []

    for field in ("name", "version", "release_id", "source_revision", "payload_content_sha256"):
        value = pkg.get(field)
        if not value:
            errors.append(f"installed artifact identity is not observed: package.{field}")
        elif value != expected_package.get(field):
            errors.append(f"installed artifact identity mismatch: package.{field}")

    if expected_package["name"] not in enabled:
        errors.append(f"{channel} package is not enabled")
    if "arek-ai-skills" in enabled and "arek-ai-skills-lab" in enabled:
        errors.append("production and Lab are simultaneously enabled")
    if len(catalog) != len(set(catalog)):
        errors.append("observed catalog contains duplicate capability names")
    if set(catalog) != set(lock.get("expected_catalogs", {}).get(channel, [])):
        errors.append(f"observed catalog differs from locked {channel} catalog")

    expected_components = {
        x["name"]: x for x in lock.get("components", []) if x.get("channel") == channel
    }
    observed_by_name = {
        str(x.get("name")): x for x in observed_components
        if isinstance(x, dict) and x.get("name")
    }
    if set(observed_by_name) != set(expected_components):
        errors.append("observed component identity set differs from locked artifact")
    else:
        for name, expected in expected_components.items():
            observed = observed_by_name[name]
            for field in ("version", "content_sha256"):
                value = observed.get(field)
                if not value:
                    errors.append(f"installed artifact identity is not observed: component {name}.{field}")
                elif value != expected.get(field):
                    errors.append(f"installed artifact identity mismatch: component {name}.{field}")

    for field in ("provider", "model_id", "reasoning"):
        if not runtime.get(field):
            errors.append(f"runtime metadata missing {field}")
    if not isinstance(runtime.get("available_tools"), list):
        errors.append("runtime available_tools must be a list")
    return errors


def selection_errors(case: dict, trace: dict) -> list[str]:
    selected = list(trace.get("selected_capabilities") or [])
    rubric = yaml.safe_load((ROOT / case["rubric"]).read_text(encoding="utf-8")) or {}
    suite = case["suite"]
    if suite == "executive-role":
        should = bool(rubric.get("should_trigger"))
        present = "executive-role-evaluator" in selected
        if should and not present:
            return ["expected executive-role-evaluator selection is absent"]
        if not should and present:
            return ["negative executive-role case selected executive-role-evaluator"]
        return []
    if suite in {"routing", "supplemental-routing"}:
        expected = rubric.get("expected_target")
        return [] if expected in selected else [f"expected routing target absent: {expected}"]
    return [] if case["target"] in selected else [f"invoked subject absent from trace: {case['target']}"]


def import_run(args) -> Path:
    cfg = config()
    cases = {**load_campaign_cases(ROOT), **load_supplemental_cases(ROOT)}
    case = cases[args.case_id]
    smoke_errors = verify_smoke(Path(args.lock), Path(args.smoke))
    if smoke_errors:
        raise ValueError("; ".join(smoke_errors))
    lock = json.loads(Path(args.lock).read_text(encoding="utf-8"))
    obs = json.loads(Path(args.smoke).read_text(encoding="utf-8"))
    required_channel = lock["case_channels"][args.case_id]
    if obs.get("channel") != required_channel:
        raise ValueError(f"case {args.case_id} requires {required_channel} session")
    trace = json.loads(Path(args.trace).read_text(encoding="utf-8"))
    sel_errors = selection_errors(case, trace)
    if sel_errors and args.status == "PASS":
        raise ValueError("PASS forbidden when runtime selection findings exist: " + "; ".join(sel_errors))

    component = {
        (x["channel"], x["name"]): x for x in lock["components"]
    }[(required_channel, case["target"])]
    source_version, source_digest = receipt.current_component_identity(ROOT, case["target"])
    dest = ROOT / cfg["evidence_root"] / args.case_id / args.run_id
    dest.mkdir(parents=True, exist_ok=False)
    out_dest = dest / "output.md"
    trace_dest = dest / "trace.json"
    shutil.copyfile(args.output, out_dest)
    shutil.copyfile(args.trace, trace_dest)

    runtime = obs["runtime"]
    ns = argparse.Namespace(
        case_id=args.case_id,
        status=args.status,
        evidence_scope="current-version",
        source_revision=lock["behavior_source_revision"],
        component=case["target"],
        component_version=source_version,
        component_digest=source_digest,
        provider=runtime["provider"],
        model_id=runtime["model_id"],
        reasoning=runtime["reasoning"],
        catalog=list(obs["catalog"]),
        tools=list(runtime.get("available_tools") or []),
        prompt=(ROOT / case["input"]).read_text(encoding="utf-8"),
        output=str(out_dest),
        tool_trace=str(trace_dest),
        reviewer=args.reviewer,
        assisted=args.assisted,
        runtime_artifact={
            "channel": required_channel,
            "package_name": obs["package"]["name"],
            "package_version": obs["package"]["version"],
            "release_id": obs["package"]["release_id"],
            "source_revision": obs["package"]["source_revision"],
            "payload_content_sha256": obs["package"]["payload_content_sha256"],
            "component_content_sha256": component["content_sha256"],
        },
        selection_findings=sel_errors,
        evidence_origin=str(getattr(args, "evidence_origin", "runtime")),
        note=args.note,
    )
    old = os.environ.get("SOURCE_REVISION")
    os.environ["SOURCE_REVISION"] = lock["behavior_source_revision"]
    try:
        rec = receipt.create_receipt(ns)
    finally:
        if old is None:
            os.environ.pop("SOURCE_REVISION", None)
        else:
            os.environ["SOURCE_REVISION"] = old
    path = dest / "receipt.json"
    path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def validate_evidence() -> list[str]:
    root = ROOT / config()["evidence_root"]
    if not root.exists():
        return []
    errors = []
    for path in sorted(root.rglob("receipt.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for err in receipt.validate_receipt_data(
            data, root=ROOT, current_revision=str(data.get("source_revision") or "")
        ):
            errors.append(f"{path.relative_to(ROOT)}: {err}")
    return errors


def main() -> int:
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="cmd", required=True)
    s.add_parser("validate")
    q = s.add_parser("queue")
    q.add_argument("--output", type=Path)
    q.add_argument("--include-supplemental", action="store_true")
    prep = s.add_parser("prepare")
    prep.add_argument("--output", type=Path, default=ROOT / ".tmp/runtime-campaign")
    smoke = s.add_parser("verify-smoke")
    smoke.add_argument("--lock", required=True, type=Path)
    smoke.add_argument("--observed", required=True, type=Path)
    imp = s.add_parser("import-run")
    imp.add_argument("--case-id", required=True)
    imp.add_argument("--run-id", required=True)
    imp.add_argument("--lock", required=True)
    imp.add_argument("--smoke", required=True)
    imp.add_argument("--output", required=True)
    imp.add_argument("--trace", required=True)
    imp.add_argument("--status", required=True, choices=["REVIEW_REQUIRED", "PASS", "FAIL"])
    imp.add_argument("--reviewer", required=True)
    imp.add_argument("--assisted", action="store_true")
    imp.add_argument("--evidence-origin", choices=["runtime", "offline"], default="runtime")
    imp.add_argument("--note")
    s.add_parser("validate-evidence")
    args = p.parse_args()

    if args.cmd == "validate":
        errors = validate_campaign()
        for e in errors:
            print("[BLOCKER]", e)
        if not errors:
            print("Runtime campaign definition: OK (38 cases)")
        return 1 if errors else 0
    if args.cmd == "queue":
        text = queue_text(args.include_supplemental)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text, end="")
        return 0
    if args.cmd == "prepare":
        prepare(args.output)
        print(args.output)
        return 0
    if args.cmd == "verify-smoke":
        errors = verify_smoke(args.lock, args.observed)
        for e in errors:
            print("[BLOCKER]", e)
        if not errors:
            print("Runtime smoke evidence: OK")
        return 1 if errors else 0
    if args.cmd == "import-run":
        print(import_run(args))
        return 0
    errors = validate_evidence()
    for e in errors:
        print("[BLOCKER]", e)
    if not errors:
        print("Runtime campaign evidence: OK")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
