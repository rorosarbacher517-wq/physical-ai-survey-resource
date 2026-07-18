# AGENTS.md

## Mission

Build and maintain a rigorous, reproducible, citation-aware knowledge and resource repository named `physical-ai-survey-resource`. The repository connects a Physical AI survey with papers, code, datasets, benchmarks, tutorials, and a geoscience/remote-sensing specialty track.

## Non-negotiable rules

1. Never fabricate a citation, DOI, author list, venue, year, metric, license, repository URL, dataset URL, benchmark score, quotation, or research conclusion.
2. When evidence is missing, use an explicit null value and add an item to `audits/pending-verification.yaml`.
3. Do not infer that a repository is official unless an author, paper page, venue page, or organization page directly links to it.
4. Do not store third-party paywalled PDFs. Store metadata and lawful public links only.
5. Do not store large raw datasets. Store data cards, download instructions, checksums for small test fixtures, and preprocessing code.
6. Do not expose secrets, tokens, credentials, personal data, private files, or unpublished user work.
7. Do not change taxonomy labels ad hoc. Update `metadata/taxonomy.yaml`, migrate affected records, regenerate derived files, and rerun validation.
8. A resource has one canonical record and one canonical storage location. Use tags and generated views for multiple classifications. Never duplicate the same resource into several folders.
9. `metadata/*.yaml` is the source of truth. CSV files, Markdown indexes, counts, dashboards, and navigation pages are generated artifacts.
10. Do not manually edit generated files. Every generated file must contain a generated-file notice.
11. Preserve provenance. Every externally sourced record must contain source URLs, verification date, and evidence level.
12. Research summaries must distinguish:
    - source-stated facts;
    - repository synthesis;
    - interpretation;
    - unresolved uncertainty.
13. Do not copy long passages from papers or surveys. Summarize in original language and respect licensing.
14. Do not claim that a result was reproduced unless commands were run successfully and metrics were recorded.
15. Never bypass failing tests, disable checks, or weaken schemas merely to obtain a passing build.
16. Do not proceed to a later phase when the current phase acceptance report is not `PASS`.
17. Use ISO 8601 dates (`YYYY-MM-DD`) and UTC for machine timestamps.
18. Use lowercase kebab-case for directories and files unless an ecosystem convention requires otherwise.
19. Keep paths portable across Windows, macOS, and Linux.
20. Maintain a clear audit trail through Git commits and `audits/`.

## Required workflow

For tasks expected to modify multiple areas:

1. Read `AGENTS.md`, `EXECPLAN.md`, `metadata/taxonomy.yaml`, and the relevant local README files.
2. Inspect the repository before changing anything.
3. Update the active execution plan in `audits/active-plan.md`.
4. Make the smallest coherent change set.
5. Run formatters, schema validation, tests, link checks, and generated-file consistency checks.
6. Review the diff for accidental deletions, generated noise, secrets, large files, and unsupported claims.
7. Write or update the phase acceptance report.
8. Commit only after all mandatory checks pass.

## Research source hierarchy

Prefer sources in this order:

1. Original paper page, DOI landing page, publisher page, arXiv, OpenReview, institutional repository.
2. Official project documentation, official organization repository, official dataset provider.
3. Author-maintained project or repository page.
4. Trusted bibliographic databases.
5. Secondary summaries only for discovery, never as the sole authority for core metadata or scientific claims.

For software behavior, use official documentation and the repository itself. For datasets, use the official provider and license page.

## Evidence levels

Use only these values:

- `primary_verified`: verified against an original or official source.
- `cross_verified`: verified against at least two independent reliable sources.
- `single_source`: one reliable source found; needs later review.
- `unverified`: discovered but not yet verified; must not be rendered as a confirmed fact.

## Content status

Use only:

- `draft`
- `verified`
- `needs_review`
- `deprecated`
- `archived`

Public generated views must exclude `unverified` records by default.

## Coding standards

- Python 3.12 unless repository constraints require another supported version.
- Use `pyproject.toml` for Python configuration.
- Add type hints to public functions.
- Use `ruff` for lint and formatting, `pytest` for tests, and `mypy` for typed modules.
- Scripts must provide useful exit codes and human-readable errors.
- Network-dependent tests must be separated from deterministic unit tests.
- Generated output must be deterministic for identical inputs.
- Do not introduce a production dependency without documenting why it is needed.

## Documentation standards

Each meaningful directory must contain a concise `README.md` or `index.md` that explains:

- purpose;
- source-of-truth files;
- generated files;
- how to contribute;
- related survey sections.

Every resource card must expose provenance, license status, verification date, and related IDs.

## Security and repository hygiene

Before every commit:

- scan for secrets;
- reject files larger than the configured threshold;
- reject binaries outside approved paths;
- reject private input paths;
- inspect dependency changes;
- confirm `.gitignore` coverage.

## Stop conditions

Stop the phase and record a blocker when:

- the requested fact cannot be verified;
- a license does not permit the proposed use;
- source materials conflict materially;
- the taxonomy cannot represent a resource without an unresolved conceptual decision;
- tests fail for reasons not understood;
- a change would expose private or unpublished material;
- a destructive operation is required without explicit authorization.

Do not hide blockers. Add them to `audits/blockers.md` with evidence and recommended resolution.
