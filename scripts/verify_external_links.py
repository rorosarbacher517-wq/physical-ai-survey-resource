from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from scripts.common import ROOT, load_yaml, write_text


def collect_urls() -> list[str]:
    urls: set[str] = set()
    for rel, key in [
        ("metadata/papers.yaml", "papers"),
        ("metadata/code.yaml", "code"),
        ("metadata/datasets.yaml", "datasets"),
        ("metadata/benchmarks.yaml", "benchmarks"),
    ]:
        data = load_yaml(ROOT / rel).get(key, [])
        for item in data:
            for field in ["source_urls"]:
                for url in item.get(field, []) or []:
                    if isinstance(url, str) and url.startswith(("http://", "https://")):
                        urls.add(url)
            for field in ["canonical_url", "official_url"]:
                url = item.get(field)
                if isinstance(url, str) and url.startswith(("http://", "https://")):
                    urls.add(url)
    return sorted(urls)


def check_url(url: str, timeout: float) -> dict[str, object]:
    headers = {"User-Agent": "physical-ai-survey-resource-link-check/1.0"}
    last_error = None
    for method in ["HEAD", "GET"]:
        req = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return {
                    "url": url,
                    "status": resp.status,
                    "ok": 200 <= resp.status < 400,
                    "category": "ok" if 200 <= resp.status < 400 else "permanent-failure",
                    "final_url": resp.geturl(),
                    "method": method,
                }
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in {405, 403, 400}:
                last_error = f"HTTP {exc.code} on HEAD"
                continue
            category = (
                "access-blocked"
                if exc.code in {401, 403, 429}
                else "transient"
                if 300 <= exc.code < 400
                else "transient"
                if exc.code in {408, 425, 500, 502, 503, 504}
                else "permanent-failure"
            )
            return {"url": url, "status": exc.code, "ok": 200 <= exc.code < 400, "category": category, "error": str(exc), "method": method}
        except Exception as exc:  # noqa: BLE001 - link checker reports all failures
            last_error = str(exc)
            if method == "HEAD":
                continue
    return {"url": url, "status": None, "ok": False, "category": "transient", "error": last_error or "unknown error", "method": "GET"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--respect-cache", action="store_true")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--timeout", type=float, default=8.0)
    parser.add_argument("--sleep", type=float, default=0.05)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()
    urls = collect_urls()
    if args.limit:
        urls = urls[: args.limit]
    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = []
        for url in urls:
            futures.append(pool.submit(check_url, url, args.timeout))
            time.sleep(args.sleep)
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: item["url"])
    report = {
        "generated": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "mode": "network",
        "checked": len(results),
        "ok": sum(1 for r in results if r["ok"]),
        "access_blocked": sum(1 for r in results if r.get("category") == "access-blocked"),
        "transient": sum(1 for r in results if r.get("category") == "transient"),
        "permanent_failure": sum(1 for r in results if r.get("category") == "permanent-failure"),
        "failed": sum(1 for r in results if not r["ok"]),
        "results": results,
    }
    (ROOT / "audits" / "external-link-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# External link report",
        "",
        f"Checked: {report['checked']}",
        f"OK: {report['ok']}",
        f"Access blocked or rate limited: {report['access_blocked']}",
        f"Transient timeout/server issues: {report['transient']}",
        f"Permanent failures: {report['permanent_failure']}",
        "",
    ]
    for r in results:
        mark = "OK" if r["ok"] else str(r.get("category", "failed")).upper()
        lines.append(f"- {mark} {r['url']} ({r.get('status')}; {r.get('error','')})")
    write_text(ROOT / "audits" / "external-link-report.md", "\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
