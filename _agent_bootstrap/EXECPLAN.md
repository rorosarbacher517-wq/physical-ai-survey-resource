# EXECPLAN.md

## Objective

Create a public-ready, maintainable repository that aligns a Physical AI survey with a structured resource database, reproducible code references, dataset cards, benchmark definitions, learning materials, and a distinctive geoscience/remote-sensing track.

## Execution model

The build is divided into gated phases. Each phase produces:

1. implementation outputs;
2. tests or validators;
3. an audit report at `audits/phases/<phase-id>.md`;
4. one focused Git commit.

A phase passes only when all mandatory acceptance criteria are satisfied.

## Global deliverables

- Repository governance and licensing files.
- Scope, definitions, inclusion criteria, and taxonomy.
- Canonical YAML metadata stores.
- JSON Schemas and validation tooling.
- Generated CSV and Markdown views.
- Knowledge-base structure and writing templates.
- Curated, verified paper, code, dataset, and benchmark records.
- Reproduction standards and example project.
- Geoscience/remote-sensing and carbon-flux case-study navigation.
- MkDocs documentation site.
- Continuous integration, link checking, secret scanning, and large-file protection.
- Final audit and release package.

## Phase state machine

Allowed phase states:

- `NOT_STARTED`
- `IN_PROGRESS`
- `BLOCKED`
- `PASS`
- `FAIL`

The agent must update `audits/state.yaml` after each meaningful action.

## Global quality gates

The following must remain true after Phase 2:

```bash
python -m scripts.validate_metadata
python -m scripts.check_internal_links
python -m scripts.check_generated_files
python -m scripts.check_large_files
python -m scripts.check_repository_hygiene
pytest
ruff check .
ruff format --check .
mypy scripts
```

Network verification is run separately:

```bash
python -m scripts.verify_external_links --respect-cache --report
```

A temporary network failure must not corrupt records. Preserve the last verified state and record the retry.

## Git policy

- Work on `build/v1-autonomous`.
- Commit format: `phase(<id>): <concise outcome>`.
- No force-push.
- No history rewriting.
- No generated bulk commit mixed with source schema changes unless the phase explicitly requires regeneration.
- Tag the completed release only after Phase 12 passes.

## Definition of done

See `README_USE.md`. The repository must be usable by a human reader, a contributor, and another coding agent without relying on hidden context.
