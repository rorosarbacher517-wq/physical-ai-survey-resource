# Phase 05 — Verified Paper Library

## Goal

Build a high-quality paper corpus that represents the taxonomy and supports the survey. Quality and verifiability take priority over count.

## Collection targets

Use `metadata/content-targets.yaml` to configure targets. Recommended v1 targets:

- minimum public verified records: 80;
- preferred full v1 records: 150;
- at least 5 strong records for each major method family where the literature supports it;
- at least 15 records for geoscience/remote sensing;
- balanced milestone, recent, theory, application, and survey coverage.

Do not fill quotas with weakly relevant papers.

## Discovery and verification workflow

For each paper:

1. Identify a stable paper identifier.
2. Verify title, authors, year, and venue from an original or authoritative source.
3. Record DOI, arXiv, OpenReview, or publisher URL where applicable.
4. Determine open-access status without assuming redistribution permission.
5. Read at least the abstract and, when lawfully accessible, the relevant method and experiment sections.
6. Classify:
   - primary method;
   - secondary methods;
   - domain;
   - task;
   - physical knowledge source;
   - integration stage;
   - survey section.
7. Record why the paper belongs in the repository in one evidence-grounded sentence.
8. Link official code only when directly supported.
9. Link datasets and benchmarks only when confirmed.
10. Run duplicate checks before insertion.

## Paper notes

Create detailed notes only for milestone papers and papers central to the survey. A note must include:

- research problem;
- physical prior;
- integration mechanism;
- model and training;
- datasets and evaluation;
- main source-stated findings;
- limitations stated by authors;
- repository synthesis;
- relevance to survey;
- reproduction status;
- citations.

Never create a detailed note from title and abstract alone. In that case, create a metadata-only record and mark note status accordingly.

## Milestone handling

A “milestone” label requires evidence of foundational influence, historical priority, or broad adoption. Do not apply it because a paper is famous or highly cited without checking context. Avoid “first-ever” claims unless verified.

## Surveys

Separate broad surveys, domain surveys, benchmark reviews, and perspective papers with tags. Record their scope and publication date so readers do not treat an older survey as current coverage.

## Acceptance criteria

- Every public paper record is at least `single_source`, with core metadata verified.
- Every `verified` record is `primary_verified` or `cross_verified`.
- No duplicate DOI, arXiv ID, or normalized title.
- No fabricated code links.
- Distribution report shows taxonomy coverage and gaps.
- Random manual-style audit of at least 10% of records is documented.
- Phase report status is `PASS` or `PASS_WITH_DECLARED_GAPS`; the latter may proceed only if gaps are evidence-based, not test failures.

## Commit

`phase(05): curate verified paper library`
