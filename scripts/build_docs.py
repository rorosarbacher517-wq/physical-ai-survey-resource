from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

from scripts.common import ROOT as PACKAGE_ROOT, write_text


ROOT = Path.cwd() if (Path.cwd() / "metadata").exists() else PACKAGE_ROOT


def safe_site_rel(path: Path) -> Path:
    return Path(*[part.lower().replace("_", "-") for part in path.parts])


def convert_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def markdown_to_html(md: str, title: str) -> str:
    lines = []
    in_list = False
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("# "):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<h1>{convert_inline(line[2:])}</h1>")
        elif line.startswith("## "):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<h2>{convert_inline(line[3:])}</h2>")
        elif line.startswith("### "):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<h3>{convert_inline(line[4:])}</h3>")
        elif line.startswith("- "):
            if not in_list:
                lines.append("<ul>")
                in_list = True
            lines.append(f"<li>{convert_inline(line[2:])}</li>")
        elif line.startswith("|"):
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<pre>{html.escape(line)}</pre>")
        elif line.strip():
            if in_list:
                lines.append("</ul>")
                in_list = False
            lines.append(f"<p>{convert_inline(line)}</p>")
    if in_list:
        lines.append("</ul>")
    body = "\n".join(lines)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 2rem auto; max-width: 980px; line-height: 1.55; padding: 0 1rem; }}
    code, pre {{ background: #f5f5f5; padding: .15rem .3rem; }}
    a {{ color: #075985; }}
  </style>
</head>
<body>
<nav><a href="index.html">Home</a> | <a href="02-paper-library/index.html">Papers</a> | <a href="06-case-studies/geoscience-remote-sensing/index.html">Geoscience track</a></nav>
{body}
</body>
</html>
"""


def main() -> int:
    site = ROOT / "site"
    if site.exists():
        shutil.rmtree(site)
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", "site", "_agent_bootstrap"} for part in md.parts):
            continue
        rel = md.relative_to(ROOT)
        out = site / safe_site_rel(rel.with_suffix(".html"))
        title = rel.as_posix()
        write_text(out, markdown_to_html(md.read_text(encoding="utf-8", errors="ignore"), title))
    if (site / "README.html").exists():
        shutil.copy2(site / "README.html", site / "index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
