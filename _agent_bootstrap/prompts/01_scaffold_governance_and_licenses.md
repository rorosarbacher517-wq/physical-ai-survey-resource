# Phase 01 — Scaffold, Governance, and Licenses

## Goal

Create the stable repository skeleton, governance documents, and licensing boundaries without creating empty decorative depth.

## Required root files

- `README.md`
- `README_zh-CN.md`
- `LICENSE-CODE`
- `LICENSE-DOCS`
- `THIRD_PARTY_LICENSES.md`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `pyproject.toml`
- `.editorconfig`
- `.gitattributes`
- `.pre-commit-config.yaml`

## Required top-level directories

```text
00-overview/
01-knowledge-base/
02-paper-library/
03-code-library/
04-dataset-library/
05-benchmarks-and-evaluation/
06-case-studies/
07-extended-resources/
metadata/
schemas/
templates/
scripts/
tests/
docs/
audits/
.github/
inputs/
```

Create a directory only when it has a clear purpose and at least one meaningful index file. Do not pre-create hundreds of empty method folders.

## Governance requirements

1. Explain repository scope and non-goals.
2. Explain that code and documentation use different licenses.
3. State third-party resources retain their original licenses.
4. Explain that bibliographic links do not imply redistribution rights.
5. Define contribution routes for:
   - adding a paper;
   - adding official code;
   - reporting reproduction;
   - adding a dataset;
   - reporting a broken link;
   - proposing taxonomy changes.
6. Define review requirements and conflict-of-interest disclosure.
7. Define deprecation and archival policy.
8. Define how unpublished user work is handled.
9. Add a machine-readable repository version in `metadata/repository.yaml`.

## README requirements

The README must include:

- one-paragraph repository purpose;
- scope distinction between physics-informed scientific AI and embodied physical intelligence;
- architecture diagram placeholder generated from Mermaid, not a fake PNG;
- navigation to each major library;
- geoscience/remote-sensing specialty entry;
- resource counts generated later;
- citation instructions;
- contribution instructions;
- copyright and data-size policy;
- build and validation commands;
- explicit status badge placeholders only if the corresponding workflow exists.

## Acceptance criteria

- All paths use lowercase kebab-case.
- No Chinese characters, spaces, or bracket annotations occur in actual paths.
- Licenses do not claim ownership of third-party content.
- Root navigation contains no broken internal links.
- Repository structure remains no deeper than necessary.
- Phase report status is `PASS`.

## Commit

`phase(01): add repository scaffold and governance`
