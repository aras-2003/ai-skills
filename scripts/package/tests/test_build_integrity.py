from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys
import zipfile

HERE = Path(__file__).resolve()
PACKAGE_DIR = HERE.parents[1]
if str(PACKAGE_DIR) not in sys.path:
    sys.path.insert(0, str(PACKAGE_DIR))

from build_chatgpt_skills import _write_deterministic_zip
from build_utils import atomic_output, sha256_file, validate_output_path


class BuildIntegrityTests(unittest.TestCase):
    def test_source_root_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            (root / "skills").mkdir()
            with self.assertRaises(ValueError):
                validate_output_path(root, root)
            with self.assertRaises(ValueError):
                validate_output_path(root, root / "skills")

    def test_output_outside_repo_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as outside:
            with self.assertRaises(ValueError):
                validate_output_path(Path(td), Path(outside) / "artifact")

    def test_failed_build_preserves_previous_output(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            out = root / "dist" / "artifact"
            out.mkdir(parents=True)
            (out / "known.txt").write_text("good", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                with atomic_output(root, out) as stage:
                    (stage / "broken.txt").write_text("broken", encoding="utf-8")
                    raise RuntimeError("synthetic failure")
            self.assertEqual("good", (out / "known.txt").read_text(encoding="utf-8"))
            self.assertFalse((out / "broken.txt").exists())

    def test_deterministic_zip_ignores_source_mtime(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            src = root / "src"
            src.mkdir()
            f = src / "SKILL.md"
            f.write_text("same bytes\n", encoding="utf-8")
            zip1 = root / "a.zip"
            zip2 = root / "b.zip"
            _write_deterministic_zip(src, zip1, "skill")
            f.touch()
            _write_deterministic_zip(src, zip2, "skill")
            self.assertEqual(sha256_file(zip1), sha256_file(zip2))
            self.assertEqual(zip1.read_bytes(), zip2.read_bytes())

    def test_content_change_changes_zip_digest(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            src = root / "src"
            src.mkdir()
            f = src / "SKILL.md"
            f.write_text("one\n", encoding="utf-8")
            zip1 = root / "a.zip"
            zip2 = root / "b.zip"
            _write_deterministic_zip(src, zip1, "skill")
            f.write_text("two\n", encoding="utf-8")
            _write_deterministic_zip(src, zip2, "skill")
            self.assertNotEqual(sha256_file(zip1), sha256_file(zip2))

    def test_zip_permissions_and_timestamp_are_fixed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            src = root / "src"
            src.mkdir()
            (src / "SKILL.md").write_text("x", encoding="utf-8")
            zp = root / "a.zip"
            _write_deterministic_zip(src, zp, "skill")
            with zipfile.ZipFile(zp) as zf:
                info = zf.infolist()[0]
                self.assertEqual((1980, 1, 1, 0, 0, 0), info.date_time)
                self.assertEqual(0o100644, info.external_attr >> 16)


if __name__ == "__main__":
    unittest.main()
