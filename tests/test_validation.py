from __future__ import annotations

from scripts.validate_metadata import main as validate_main

def test_metadata_validates() -> None:
    assert validate_main() == 0
