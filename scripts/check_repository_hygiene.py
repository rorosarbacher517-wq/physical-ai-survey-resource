from __future__ import annotations

import re

from scripts.common import ROOT, fail

SECRET_PATTERNS = [re.compile(r"AKIA[0-9A-Z]{16}"), re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,}")]

def main() -> int:
    errors = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() in {".docx", ".png", ".jpg"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"possible secret in {path.relative_to(ROOT)}")
    return fail(errors)

if __name__ == "__main__":
    raise SystemExit(main())
