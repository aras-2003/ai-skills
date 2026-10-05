from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EVAL_DIR = ROOT / "scripts" / "eval"
if str(EVAL_DIR) not in sys.path:
    sys.path.insert(0, str(EVAL_DIR))

import campaign
import skill_release_campaign


class SkillReleaseCampaignTests(unittest.TestCase):
    def test_campaign_has_complete_isolated_runtime_suite(self) -> None:
        self.assertEqual([], skill_release_campaign.validate(ROOT))
        cfg = skill_release_campaign.load_config(ROOT)
        self.assertEqual("skill-release-review", cfg["target"])
        self.assertEqual(6, len(cfg["cases"]))

    def test_only_separately_campaigned_skill_behavior_is_excluded_from_r16_pin(self) -> None:
        allowed = {"skills/meta/skill-release-review/SKILL.md"}
        changed = [
            "skills/meta/skill-release-review/SKILL.md",
            "skills/career/interview-brief/SKILL.md",
        ]
        self.assertEqual(
            ["skills/career/interview-brief/SKILL.md"],
            campaign.filter_behavior_paths(changed, allowed),
        )

    def test_candidate_source_version_matches_runtime_campaign(self) -> None:
        cfg = skill_release_campaign.load_config(ROOT)
        skill = (ROOT / "skills/meta/skill-release-review/SKILL.md").read_text(encoding="utf-8")
        self.assertIn(f'version: "{cfg["candidate_version"]}"', skill)


if __name__ == "__main__":
    unittest.main()
