from __future__ import annotations

import re

from scripts.common import ROOT, fail

def main() -> int:
    errors = []
    risky = re.compile(r"\b(first|best|state[- ]of[- ]the[- ]art|unprecedented)\b", re.I)
    for path in [ROOT / "01-knowledge-base", ROOT / "06-case-studies"]:
        for md in path.rglob("*.md"):
            text = md.read_text(encoding="utf-8", errors="ignore")
            for line_no, line in enumerate(text.splitlines(), start=1):
                if risky.search(line) and "manual-review" not in line:
                    errors.append(f"{md.relative_to(ROOT)}:{line_no}: risky claim needs manual-review marker")
    return fail(errors)

if __name__ == "__main__":
    raise SystemExit(main())
