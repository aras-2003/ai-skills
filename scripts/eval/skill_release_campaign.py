from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG_REL = Path("evals/campaigns/skill-release-review-2026-10/release-review-campaign.yaml")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_config(root: Path = ROOT) -> dict:
    return yaml.safe_load((root / CONFIG_REL).read_text(encoding="utf-8")) or {}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    cfg = load_config(root)
    if cfg.get("campaign") != "skill-release-review-2026-10":
        errors.append("unexpected campaign identity")
    if cfg.get("target") != "skill-release-review":
        errors.append("campaign must target skill-release-review")
    if cfg.get("out_of_scope_behavior_paths") != ["skills/meta/skill-release-review/SKILL.md"]:
        errors.append("campaign must declare only the exact skill-release-review behavior path")
    skill = root / "skills/meta/skill-release-review/SKILL.md"
    if not skill.is_file() or f'version: "{cfg.get("candidate_version")}"' not in skill.read_text(encoding="utf-8"):
        errors.append("campaign candidate version does not match the skill source")
    cases = cfg.get("cases") or []
    if len(cases) != 6:
        errors.append(f"expected 6 runtime cases, got {len(cases)}")
    ids: set[str] = set()
    for case in cases:
        cid = str(case.get("id") or "")
        if not cid or cid in ids:
            errors.append(f"missing or duplicate case id: {cid or '<missing>'}")
        ids.add(cid)
        input_path = root / str(case.get("input") or "")
        rubric_path = root / str(case.get("rubric") or "")
        if not input_path.is_file() or not input_path.name.endswith(".input.md"):
            errors.append(f"{cid}: missing executor input")
        if not rubric_path.is_file() or not rubric_path.name.endswith(".rubric.yaml"):
            errors.append(f"{cid}: missing evaluator rubric")
        if rubric_path.is_file():
            rubric = yaml.safe_load(rubric_path.read_text(encoding="utf-8")) or {}
            assertions = rubric.get("assertions") or {}
            if not assertions.get("must") or not assertions.get("must_not"):
                errors.append(f"{cid}: rubric must include must and must_not assertions")
    expected = {
        "release-review-digest-mismatch",
        "release-review-missing-identity",
        "release-review-stale-authorization",
        "release-review-missing-channel",
        "release-review-positive-control",
        "release-review-queued-runtime",
    }
    if ids != expected:
        errors.append("runtime case set does not match the campaign contract")
    return errors


def prepare(lab: Path, out: Path, root: Path = ROOT) -> None:
    errors = validate(root)
    if errors:
        raise ValueError("; ".join(errors))
    if not lab.is_dir():
        raise ValueError(f"Lab artifact is missing: {lab}")
    plugin = json.loads((lab / "plugin.json").read_text(encoding="utf-8"))
    release = json.loads((lab / "release-manifest.json").read_text(encoding="utf-8"))
    capabilities = json.loads((lab / "capabilities.json").read_text(encoding="utf-8"))
    target = str(load_config(root)["target"])
    capability = next((x for x in capabilities.get("capabilities", []) if x.get("name") == target), None)
    if capability is None:
        raise ValueError(f"target is absent from Lab package: {target}")
    source_revision = str(release.get("source_revision") or "")
    expected_revision = os.environ.get("SOURCE_REVISION") or subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=root, text=True
    ).strip()
    if source_revision != expected_revision:
        raise ValueError("Lab package source revision does not match the checked-out candidate")

    out.mkdir(parents=True, exist_ok=False)
    executor = out / "executor-inputs"
    executor.mkdir()
    definitions = []
    cfg = load_config(root)
    for case in cfg["cases"]:
        src = root / case["input"]
        dest = executor / f"{case['id']}.input.md"
        shutil.copyfile(src, dest)
        rubric = root / case["rubric"]
        definitions.append({
            "id": case["id"],
            "input": dest.name,
            "input_sha256": sha256(dest),
            "rubric_path": case["rubric"],
            "rubric_sha256": sha256(rubric),
        })
    shutil.copytree(lab, out / "lab-plugin")
    lock = {
        "schema_version": "1.0",
        "campaign": cfg["campaign"],
        "campaign_definition_sha256": sha256(root / CONFIG_REL),
        "source_revision": source_revision,
        "skill": {
            "name": target,
            "version": capability.get("version"),
            "content_sha256": capability.get("content_sha256"),
        },
        "package": {
            "name": plugin.get("name"),
            "version": plugin.get("version"),
            "release_id": release.get("release_id"),
            "payload_content_sha256": release.get("payload_content_sha256"),
        },
        "case_inputs": sorted(definitions, key=lambda x: x["id"]),
    }
    (out / "lock.json").write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")
    queue = ["# skill-release-review runtime campaign", "", "Run each prompt in a fresh session with this exact Lab package enabled. Do not provide evaluator rubrics.", ""]
    for case, definition in zip(cfg["cases"], definitions, strict=True):
        queue.extend([f"## {case['id']}", "", "```text", (executor / definition["input"]).read_text(encoding="utf-8").rstrip(), "```", ""])
    (out / "QUEUE.md").write_text("\n".join(queue), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["validate", "prepare"])
    parser.add_argument("--lab", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            errors = validate()
            for error in errors:
                print(f"[BLOCKER] {error}")
            if not errors:
                print("skill-release-review campaign: OK (6 cases)")
            return int(bool(errors))
        if not args.lab or not args.output:
            parser.error("prepare requires --lab and --output")
        prepare(args.lab, args.output)
        print(args.output)
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"[BLOCKER] {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
