from __future__ import annotations

from scripts.common import ROOT, fail

def main() -> int:
    errors = []
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.stat().st_size > 10_000_000:
            errors.append(f"large file exceeds 10 MB: {path.relative_to(ROOT)}")
    return fail(errors)

if __name__ == "__main__":
    raise SystemExit(main())
