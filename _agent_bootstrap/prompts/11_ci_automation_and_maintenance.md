# Phase 11 — CI, Automation, and Maintenance

## Goal

Make future changes safe, reviewable, and mostly self-validating.

## Required workflows

Create GitHub Actions or equivalent CI for:

1. metadata schema validation;
2. Python lint, format, type checking, and tests;
3. deterministic generated-file check;
4. internal link check;
5. scheduled external-link verification with cache;
6. documentation build;
7. secret scan;
8. large-file and forbidden-path scan;
9. dependency review;
10. release artifact build.

## Contribution forms

Create issue templates for:

- add a paper;
- correct metadata;
- add official code;
- submit reproduction evidence;
- add a dataset;
- add a benchmark;
- broken link;
- taxonomy proposal;
- security/private-data report.

Create a pull-request template with:

- resource IDs changed;
- source evidence;
- license checked;
- generated files refreshed;
- tests run;
- scientific claims reviewed;
- private material check;
- breaking taxonomy change declaration.

## Maintenance policy

Define:

- verification expiration windows by resource type;
- link retry policy;
- archived/deprecated handling;
- dataset version updates;
- code-repository archival handling;
- taxonomy migration procedure;
- release cadence;
- reviewer responsibilities;
- emergency removal process for copyright/privacy issues.

## Automated update safety

Scheduled jobs may propose updates in branches or pull requests, but must not silently alter verified scientific metadata on the default branch.

## Acceptance criteria

- CI succeeds from a clean checkout.
- A deliberately invalid metadata fixture fails CI.
- Generated-file drift fails CI.
- Secret and oversized-file fixtures are detected.
- Scheduled workflows do not require unscoped secrets.
- Phase report status is `PASS`.

## Commit

`phase(11): add CI and maintenance automation`
