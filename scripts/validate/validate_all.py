from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(script: Path, *args: str) -> int:
    print(f"\n==> {script.name} {' '.join(args)}".rstrip())
    return subprocess.run([sys.executable, str(script), *args], check=False).returncode


def main() -> int:
    here = Path(__file__).resolve().parent
    scripts = [here / "validate_skill.py", here / "validate_tests.py", here / "validate_catalog.py"]
    results = [run(script) for script in scripts]
    results.append(run(here.parent / "eval" / "validate_eval_protocol.py"))
    print("\n==> eval protocol unit tests")
    results.append(
        subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(here.parent / "eval" / "tests")],
            check=False,
        ).returncode
    )
    return 1 if any(results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
