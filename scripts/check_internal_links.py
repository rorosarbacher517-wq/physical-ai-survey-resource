from __future__ import annotations

import re
from pathlib import Path

from scripts.common import ROOT, fail

def main() -> int:
    errors: list[str] = []
    pattern = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:)([^)#]+)(?:#[^)]+)?\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for target in pattern.findall(text):
            if target.startswith("<") or target.startswith("!"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} -> missing {target}")
    return fail(errors)

if __name__ == "__main__":
    raise SystemExit(main())
