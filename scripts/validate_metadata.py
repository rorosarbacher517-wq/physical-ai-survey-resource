from __future__ import annotations

from scripts.common import ROOT, fail, load_yaml, validate_items

def main() -> int:
    errors: list[str] = []
    tax = load_yaml(ROOT / "metadata" / "taxonomy.yaml")
    methods = set(tax.get("method_families", []))
    domains = set(tax.get("domains", []))
    evidence = set(tax.get("evidence_levels", []))
    statuses = set(tax.get("content_statuses", []))

    papers = load_yaml(ROOT / "metadata" / "papers.yaml").get("papers", [])
    codes = load_yaml(ROOT / "metadata" / "code.yaml").get("code", [])
    datasets = load_yaml(ROOT / "metadata" / "datasets.yaml").get("datasets", [])
    benchmarks = load_yaml(ROOT / "metadata" / "benchmarks.yaml").get("benchmarks", [])

    errors += validate_items(papers, "paper.schema.json")
    errors += validate_items(codes, "code.schema.json")
    errors += validate_items(datasets, "dataset.schema.json")
    errors += validate_items(benchmarks, "benchmark.schema.json")

    seen_ids: set[str] = set()
    seen_dois: set[str] = set()
    seen_titles: set[str] = set()
    for p in papers:
        pid = p["paper_id"]
        if pid in seen_ids:
            errors.append(f"duplicate paper_id: {pid}")
        seen_ids.add(pid)
        doi = (p.get("identifiers") or {}).get("doi")
        if doi:
            if doi in seen_dois:
                errors.append(f"duplicate DOI: {doi}")
            seen_dois.add(doi)
        title_key = " ".join(str(p.get("title", "")).lower().split())
        if title_key in seen_titles:
            errors.append(f"duplicate normalized title: {p.get('title')}")
        seen_titles.add(title_key)
        if p.get("primary_method") not in methods:
            errors.append(f"unknown method {p.get('primary_method')} in {pid}")
        for d in p.get("domains", []):
            if d not in domains:
                errors.append(f"unknown domain {d} in {pid}")
        if p.get("evidence_level") not in evidence:
            errors.append(f"unknown evidence level in {pid}")
        if p.get("content_status") not in statuses:
            errors.append(f"unknown content status in {pid}")

    dataset_ids = {d["dataset_id"] for d in datasets}
    for b in benchmarks:
        for did in b.get("dataset_ids", []):
            if did not in dataset_ids:
                errors.append(f"benchmark {b['benchmark_id']} references missing dataset {did}")

    relationships = load_yaml(ROOT / "metadata" / "relationships.yaml").get("relationships", [])
    all_ids = seen_ids | {c["code_id"] for c in codes} | dataset_ids | {b["benchmark_id"] for b in benchmarks}
    for rel in relationships:
        if rel["source_id"] not in all_ids:
            errors.append(f"relationship source missing: {rel['source_id']}")
        if rel["target_id"] not in all_ids:
            errors.append(f"relationship target missing: {rel['target_id']}")
        if rel["source_id"] == rel["target_id"]:
            errors.append(f"self relationship not allowed: {rel['source_id']}")
    return fail(errors)

if __name__ == "__main__":
    raise SystemExit(main())
