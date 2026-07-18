from __future__ import annotations

import subprocess
import sys

MODULES = [
    "scripts.generate_indexes",
    "scripts.validate_metadata",
    "scripts.check_internal_links",
    "scripts.check_generated_files",
    "scripts.check_large_files",
    "scripts.check_repository_hygiene",
    "scripts.audit_claims",
    "scripts.build_docs",
]

def main() -> int:
    for module in MODULES:
        code = subprocess.call([sys.executable, "-m", module])
        if code:
            return code
    return subprocess.call([sys.executable, "-m", "pytest"])

if __name__ == "__main__":
    raise SystemExit(main())
