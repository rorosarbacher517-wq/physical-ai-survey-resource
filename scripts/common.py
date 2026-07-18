from __future__ import annotations

import csv
import json
import os
import re
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
GENERATED_NOTICE = "Generated from canonical metadata. Do not edit manually."

def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")

def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})
    write_text(path.with_suffix(path.suffix + ".generated.md"), GENERATED_NOTICE + "\n")

def public_records(records: list[dict[str, object]]) -> list[dict[str, object]]:
    return [r for r in records if r.get("evidence_level") != "unverified" and r.get("content_status") not in {"archived", "deprecated"}]

def validate_items(items: list[dict[str, object]], schema_name: str) -> list[str]:
    schema = json.loads((ROOT / "schemas" / schema_name).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    for item in items:
        for err in validator.iter_errors(item):
            errors.append(f"{item.get('paper_id') or item.get('code_id') or item.get('dataset_id') or item.get('benchmark_id')}: {err.message}")
    return errors

def fail(errors: list[str]) -> int:
    if errors:
        print("\n".join(errors))
        return 1
    return 0
