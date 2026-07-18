from __future__ import annotations

from collections import Counter, defaultdict

from scripts.common import GENERATED_NOTICE, ROOT, load_yaml, public_records, write_csv, write_text


def link_card(rid: str) -> str:
    return f"[{rid}](cards/{rid}.md)"


def md_table(headers: list[str], rows: list[list[object]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(x).replace("\n", " ") for x in row) + " |")
    return "\n".join(out) + "\n"


def main() -> int:
    papers = public_records(load_yaml(ROOT / "metadata" / "papers.yaml").get("papers", []))
    codes = public_records(load_yaml(ROOT / "metadata" / "code.yaml").get("code", []))
    datasets = public_records(load_yaml(ROOT / "metadata" / "datasets.yaml").get("datasets", []))
    benchmarks = public_records(load_yaml(ROOT / "metadata" / "benchmarks.yaml").get("benchmarks", []))

    write_csv(ROOT / "02-paper-library" / "paper-index.csv", papers, ["paper_id", "title", "year", "venue", "primary_method", "evidence_level", "content_status", "last_verified"])
    write_csv(ROOT / "03-code-library" / "code-index.csv", codes, ["code_id", "name", "canonical_url", "status", "language", "framework", "reproduction_level", "evidence_level", "content_status"])
    write_csv(ROOT / "04-dataset-library" / "dataset-index.csv", datasets, ["dataset_id", "name", "provider", "official_url", "license", "evidence_level", "content_status"])
    write_csv(ROOT / "05-benchmarks-and-evaluation" / "benchmark-index.csv", benchmarks, ["benchmark_id", "name", "task_definition", "split_definition", "evidence_level", "content_status"])

    paper_rows = [[link_card(p["paper_id"]), p["title"], p["year"], p.get("venue") or "", p["primary_method"], ", ".join(p["domains"])] for p in papers]
    write_text(ROOT / "02-paper-library" / "index.md", f"# Paper library\n\n{GENERATED_NOTICE}\n\n{md_table(['ID', 'Title', 'Year', 'Venue', 'Method', 'Domains'], paper_rows)}")

    code_rows = [[link_card(c["code_id"]), c["name"], c["status"], c["language"], c["reproduction_level"]] for c in codes]
    write_text(ROOT / "03-code-library" / "index.md", f"# Code library\n\n{GENERATED_NOTICE}\n\n{md_table(['ID', 'Name', 'Status', 'Language', 'Reproduction'], code_rows)}")

    dataset_rows = [[link_card(d["dataset_id"]), d["name"], d["provider"], d["license"], d["access_conditions"]] for d in datasets]
    write_text(ROOT / "04-dataset-library" / "index.md", f"# Dataset library\n\n{GENERATED_NOTICE}\n\n{md_table(['ID', 'Name', 'Provider', 'License', 'Access'], dataset_rows)}")

    benchmark_rows = [[link_card(b["benchmark_id"]), b["name"], b["task_definition"], ", ".join(b["metrics"])] for b in benchmarks]
    write_text(ROOT / "05-benchmarks-and-evaluation" / "index.md", f"# Benchmarks and evaluation\n\n{GENERATED_NOTICE}\n\n{md_table(['ID', 'Name', 'Task', 'Metrics'], benchmark_rows)}")

    by_method = defaultdict(list)
    by_domain = defaultdict(list)
    by_year = defaultdict(list)
    for p in papers:
        by_method[p["primary_method"]].append(p)
        for domain in p["domains"]:
            by_domain[domain].append(p)
        by_year[str(p["year"])].append(p)
    for name, groups in [("method", by_method), ("domain", by_domain), ("year", by_year)]:
        lines = [f"# Papers by {name}\n\n{GENERATED_NOTICE}\n"]
        for key in sorted(groups):
            lines.append(f"\n## {key}\n")
            for p in sorted(groups[key], key=lambda x: (x.get("year") or 0, x["title"])):
                lines.append(f"- [{p['paper_id']}](cards/{p['paper_id']}.md): {p['title']} ({p.get('year')})")
        write_text(ROOT / "02-paper-library" / f"by-{name}.md", "\n".join(lines) + "\n")

    counts = f"{GENERATED_NOTICE}\n\n- Public papers: {len(papers)}\n- Public code records: {len(codes)}\n- Public datasets: {len(datasets)}\n- Public benchmarks: {len(benchmarks)}\n"
    write_text(ROOT / "docs" / "resource-counts.md", counts)

    relationship_count = len(load_yaml(ROOT / "metadata" / "relationships.yaml").get("relationships", []))
    write_text(ROOT / "audits" / "relationship-report.md", f"{GENERATED_NOTICE}\n\nRelationship integrity is checked by scripts.validate_metadata.\n\nRelationships: {relationship_count}\n")
    pending = load_yaml(ROOT / "audits" / "pending-verification.yaml").get("items", [])
    write_text(ROOT / "audits" / "unresolved-verification.md", f"{GENERATED_NOTICE}\n\nPending verification items: {len(pending)}\n")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    start = "<!-- resource-counts:start -->"
    end = "<!-- resource-counts:end -->"
    if start in readme and end in readme:
        before = readme.split(start)[0]
        after = readme.split(end)[1]
        readme = before + start + "\n" + counts.strip() + "\n" + end + after
        write_text(ROOT / "README.md", readme)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
