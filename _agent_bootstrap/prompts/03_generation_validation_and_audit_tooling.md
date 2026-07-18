# Phase 03 — Generation, Validation, and Audit Tooling

## Goal

Implement deterministic tooling so the repository is maintained from canonical metadata rather than hand-edited copies.

## Required commands

Expose commands through Python modules or a task runner for:

- `validate-metadata`
- `generate-indexes`
- `generate-views`
- `check-generated-files`
- `check-internal-links`
- `verify-external-links`
- `check-duplicates`
- `check-large-files`
- `check-repository-hygiene`
- `audit-claims`
- `build-docs`
- `full-check`

## Generated outputs

Generate:

- `02-paper-library/paper-index.csv`
- `03-code-library/code-index.csv`
- `04-dataset-library/dataset-index.csv`
- `05-benchmarks-and-evaluation/benchmark-index.csv`
- Markdown views by method, domain, year, survey section, reproduction level, and verification status;
- resource-count snippets for README and documentation;
- relationship reports;
- unresolved-verification reports.

Each generated file must start with a notice equivalent to:

> Generated from canonical metadata. Do not edit manually.

For CSV, include the notice in a neighboring `.generated.md` manifest rather than corrupting tabular data.

## External-link verification

Implement polite, cached verification:

- configurable concurrency and timeout;
- user-agent string;
- exponential backoff;
- domain rate limiting;
- HEAD with GET fallback;
- redirect capture;
- transient vs permanent failure distinction;
- cache with verification timestamp;
- no repeated hammering of publisher or dataset servers.

Do not automatically delete a record due to one transient failure.

## Claim audit

Create a lightweight auditable convention for scientific prose:

- every claim paragraph includes citations or a `repository-synthesis` marker;
- unsupported numerical claims are rejected;
- citation IDs must resolve to verified records;
- quoted text over the configured threshold is flagged;
- statements about “first”, “state of the art”, or “best” require explicit evidence and manual review.

## Determinism

- sort records by stable IDs or explicit keys;
- normalize line endings;
- avoid timestamps in generated content except verification metadata;
- verify that a second generation produces no diff.

## Acceptance criteria

- Running generation twice produces a clean Git diff.
- Invalid fixtures fail with useful messages.
- Generated views exclude unverified records by default.
- Internal links pass.
- Network failure does not erase previous verification data.
- Phase report status is `PASS`.

## Commit

`phase(03): add deterministic generation and audit tooling`
