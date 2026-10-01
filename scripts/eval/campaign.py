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

from common import load_campaign_cases
import receipt
import validate_routing
import build_plugin
import artifact_validation

CONFIG = ROOT / "evals/campaigns/runtime-validation-2026-10/campaign.yaml"


def config():
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}


def behavior_changes(pinned: str) -> list[str]:
    out = subprocess.check_output(
        ["git", "diff", "--name-only", pinned, "HEAD", "--", "skills", "workflows", "release/package.yaml"],
        cwd=ROOT, text=True,
    ).strip()
    return [x for x in out.splitlines() if x]


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
    changed = behavior_changes(pinned)
    if changed:
        errors.append("behavior changed after pinned SHA: " + ", ".join(changed))
    return errors


def ordered_cases():
    cfg = config()
    rank = {name: i for i, name in enumerate(cfg.get("execution_order", []))}
    return sorted(load_campaign_cases(ROOT).values(), key=lambda x: (rank.get(x.get("suite"), 99), x["id"]))


def queue_text() -> str:
    out = [
        "# Runtime validation queue",
        "",
        "Executor-only inputs. Never provide the referenced rubric to the executor session.",
        "",
    ]
    for i, case in enumerate(ordered_cases(), 1):
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


def prepare(out: Path) -> None:
    errors = validate_campaign()
    if errors:
        raise ValueError("; ".join(errors))
    cfg = config()
    pinned = cfg["behavior_source_revision"]
    package = out / "production-plugin"
    out.mkdir(parents=True, exist_ok=True)

    old = os.environ.get("SOURCE_REVISION")
    os.environ["SOURCE_REVISION"] = pinned
    try:
        build_plugin.build(ROOT, package, "production")
    finally:
        if old is None:
            os.environ.pop("SOURCE_REVISION", None)
        else:
            os.environ["SOURCE_REVISION"] = old

    artifact_errors = artifact_validation.validate_tree(package)
    if artifact_errors:
        raise ValueError("; ".join(artifact_errors))

    caps = json.loads((package / "capabilities.json").read_text(encoding="utf-8"))
    rel = json.loads((package / "release-manifest.json").read_text(encoding="utf-8"))
    plugin = json.loads((package / "plugin.json").read_text(encoding="utf-8"))
    by_name = {x["name"]: x for x in caps.get("capabilities", [])}
    for unavailable in ("strategy-to-execution-diagnostic", "organizational-interface-review"):
        if unavailable in by_name:
            raise ValueError(f"fallback campaign precondition changed: {unavailable} is now in production")
    subjects = sorted({x["target"] for x in load_campaign_cases(ROOT).values()})
    locked = []
    for name in subjects:
        item = by_name.get(name)
        if item is None:
            raise ValueError(f"campaign subject absent from production package: {name}")
        locked.append({
            "name": name,
            "kind": item.get("kind"),
            "version": item.get("version"),
            "maturity": item.get("maturity"),
            "content_sha256": item.get("content_sha256"),
        })

    lock = {
        "schema_version": "1.0",
        "campaign": cfg["campaign"],
        "behavior_source_revision": pinned,
        "package": {
            "name": plugin.get("name"),
            "version": plugin.get("version"),
            "release_id": rel.get("release_id"),
            "source_revision": rel.get("source_revision"),
        },
        "expected_catalog": sorted(by_name),
        "components": locked,
    }
    (out / "lock.json").write_text(json.dumps(lock, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "QUEUE.md").write_text(queue_text(), encoding="utf-8")
    smoke = {
        "package": {"name": lock["package"]["name"], "version": lock["package"]["version"]},
        "enabled_packages": ["arek-ai-skills"],
        "catalog": [],
        "runtime": {
            "provider": None,
            "model_id": None,
            "reasoning": None,
            "available_tools": [],
        },
    }
    (out / "smoke-template.json").write_text(json.dumps(smoke, indent=2) + "\n", encoding="utf-8")


def verify_smoke(lock_path: Path, observed_path: Path) -> list[str]:
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    obs = json.loads(observed_path.read_text(encoding="utf-8"))
    errors = []
    pkg = obs.get("package") or {}
    runtime = obs.get("runtime") or {}
    enabled = list(obs.get("enabled_packages") or [])
    catalog = list(obs.get("catalog") or [])

    if pkg.get("name") != lock["package"]["name"] or pkg.get("version") != lock["package"]["version"]:
        errors.append("installed package name/version does not match lock")
    if "arek-ai-skills" not in enabled:
        errors.append("production package is not enabled")
    if "arek-ai-skills-lab" in enabled:
        errors.append("production and Lab are simultaneously enabled")
    if len(catalog) != len(set(catalog)):
        errors.append("observed catalog contains duplicate capability names")
    if set(catalog) != set(lock.get("expected_catalog") or []):
        errors.append("observed catalog differs from locked production catalog")
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
    if suite == "routing":
        expected = rubric.get("expected_target")
        return [] if expected in selected else [f"expected routing target absent: {expected}"]
    return [] if case["target"] in selected else [f"invoked subject absent from trace: {case['target']}"]


def import_run(args) -> Path:
    cfg = config()
    cases = load_campaign_cases(ROOT)
    case = cases[args.case_id]
    smoke_errors = verify_smoke(Path(args.lock), Path(args.smoke))
    if smoke_errors:
        raise ValueError("; ".join(smoke_errors))
    trace = json.loads(Path(args.trace).read_text(encoding="utf-8"))
    sel_errors = selection_errors(case, trace)
    if sel_errors:
        raise ValueError("; ".join(sel_errors))

    lock = json.loads(Path(args.lock).read_text(encoding="utf-8"))
    obs = json.loads(Path(args.smoke).read_text(encoding="utf-8"))
    component = {x["name"]: x for x in lock["components"]}[case["target"]]
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
        component_version=component["version"],
        component_digest=component["content_sha256"],
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
        text = queue_text()
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
