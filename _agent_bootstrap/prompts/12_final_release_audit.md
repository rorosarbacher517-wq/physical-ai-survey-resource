# Phase 12 — Final Release Audit

## Goal

Conduct an independent, adversarial audit before declaring v1 ready.

## Auditor role

Act as a skeptical reviewer. Do not rely on the implementation agent’s summaries. Re-run commands, inspect samples, and attempt to falsify the repository’s quality claims.

## Mandatory audits

### Structural

- path naming;
- depth and portability;
- required files;
- no empty decorative directories;
- no orphan resources;
- no duplicate canonical entities.

### Metadata

- schema validity;
- taxonomy validity;
- stable ID uniqueness;
- relationship integrity;
- verification dates;
- evidence levels;
- public filtering.

### Scientific content

Sample at least:

- 15 papers;
- 8 code records;
- 8 datasets;
- 5 benchmarks;
- 10 glossary terms;
- all user-specific carbon-flux claims.

For each sample, check source alignment and classification.

### Reproducibility

- clean environment install;
- deterministic generation;
- runnable smoke examples;
- stored logs;
- reproduction-level claims.

### Copyright and privacy

- no paywalled PDFs;
- no improperly copied text;
- no unlicensed code copies;
- no raw restricted data;
- no secrets;
- no private user materials;
- correct third-party notices.

### Links and documentation

- all internal links;
- cached external-link report;
- documentation build;
- README/site consistency;
- accessible diagrams.

### Git and release

- clean Git status;
- coherent commit history;
- no accidental binaries;
- changelog;
- citation metadata;
- release manifest;
- source archive reproducibility.

## Required outputs

- `audits/final-audit.md`
- `audits/final-audit.json`
- `audits/known-limitations.md`
- `audits/release-manifest.json`
- `audits/content-statistics.json`
- `RELEASE_NOTES.md`

## Severity levels

- `critical`: privacy, security, legal, fabricated scientific content, corrupted source of truth.
- `major`: broken schema, false reproduction claim, pervasive broken links, invalid taxonomy.
- `minor`: formatting, isolated stale link, non-critical wording.
- `advisory`: future improvement.

Release is prohibited with any critical or major finding.

## Final acceptance criteria

- all mandatory checks pass;
- no critical or major findings remain;
- known limitations are explicit;
- counts refer only to public verified records;
- release does not claim completeness of the field or zero defects;
- phase status is `PASS`.

## Release action

Create an annotated tag such as `v1.0.0` only after approval conditions are satisfied.

## Commit

`phase(12): complete independent release audit`
