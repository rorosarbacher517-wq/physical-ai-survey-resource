# Phase 10 — Documentation Site and Navigation

## Goal

Build a searchable, accessible documentation site from the repository without duplicating canonical data.

## Requirements

Use MkDocs or an equivalently maintainable static documentation system.

The site must include:

- home and scope;
- survey navigation;
- method taxonomy;
- application domains;
- paper library;
- code and reproduction;
- dataset library;
- benchmarks and evaluation;
- glossary;
- learning paths;
- geoscience/remote-sensing specialty;
- contribution and governance;
- audit and release status.

## Generation rules

- Resource tables are generated from metadata.
- Search indexes exclude private and unverified content.
- Every resource page displays evidence level and last verification date.
- Broken external links are visibly marked rather than silently removed.
- Avoid client-side dependencies that compromise offline readability.
- Ensure relative links work on GitHub Pages or the selected deployment target.
- Add alt text to diagrams and meaningful images.
- Mermaid diagrams must have text equivalents.

## README synchronization

README counts and navigation must be generated or checked against the same metadata. Do not manually maintain divergent counts.

## Acceptance criteria

- Site builds in a clean environment.
- No broken internal links.
- Search finds representative method, domain, paper, code, and dataset records.
- Mobile-width rendering is usable.
- Accessibility checks have no critical failures.
- Phase report status is `PASS`.

## Commit

`phase(10): add searchable documentation site`
