# Phase 02 — Taxonomy, Metadata, and Schemas

## Goal

Create a controlled conceptual system and canonical data model before collecting resources.

## Taxonomy design

Create `metadata/taxonomy.yaml` with stable IDs, labels, definitions, parent relationships, aliases, inclusion rules, exclusion rules, and examples.

At minimum include these top-level conceptual branches:

1. `physics-informed-scientific-ai`
2. `embodied-physical-intelligence`

Physics-informed scientific AI method families should support, without forcing overlap into duplicate folders:

- physics-constrained objectives;
- physics-embedded architectures;
- differentiable simulation;
- neural operators;
- hybrid numerical–machine-learning methods;
- symmetry and equivariance;
- system identification and inverse problems;
- uncertainty quantification;
- scientific foundation models;
- theory, optimization, and generalization.

Embodied physical intelligence should support:

- physical perception;
- spatial and 3D reasoning;
- dynamics and physical reasoning;
- world models;
- planning and control;
- robot learning;
- vision-language-action models;
- sim-to-real and domain adaptation;
- safety and uncertainty.

Application domains should include:

- fluids and aerodynamics;
- energy and materials;
- climate, geoscience, and remote sensing;
- biomedical mechanics;
- robotics and embodied systems;
- other verified domains.

## Canonical entity stores

Create:

- `metadata/papers.yaml`
- `metadata/code.yaml`
- `metadata/datasets.yaml`
- `metadata/benchmarks.yaml`
- `metadata/glossary.yaml`
- `metadata/relationships.yaml`
- `metadata/repository.yaml`

Do not seed these files with fictional examples. Use clearly marked test fixtures under `tests/fixtures/`.

## Required schemas

Create JSON Schemas for all entity stores. Required fields must include:

### Paper

- `paper_id`
- `title`
- `authors`
- `year`
- `venue`
- stable identifiers
- `primary_method`
- `secondary_tags`
- `domains`
- `tasks`
- `physics_source`
- `physics_integration_stage`
- `survey_sections`
- `source_urls`
- `evidence_level`
- `content_status`
- `last_verified`
- license/open-access fields
- code and dataset relationships

### Code

- `code_id`
- canonical repository URL
- official/community/original status
- related paper IDs
- framework/language
- license
- last release or commit date when verified
- environment availability
- reproduction level
- tested commands
- evidence and verification fields

### Dataset

- `dataset_id`
- provider
- official URL
- DOI/provider identifier
- domains/tasks
- spatial/temporal coverage when verified
- modalities
- access conditions
- license
- redistribution policy
- related papers/code/benchmarks
- evidence and verification fields

### Benchmark

- `benchmark_id`
- task definition
- dataset IDs
- split definition
- metrics
- baseline references
- comparability warnings
- license/access
- evidence and verification fields

## Relationship model

Represent cross-links in `metadata/relationships.yaml` rather than embedding uncontrolled free text. Validate:

- referenced IDs exist;
- relationship type is controlled;
- reciprocal relationships are generated or checked;
- no self-links unless explicitly allowed.

## Validation tooling

Implement:

- schema validation;
- controlled-vocabulary validation;
- stable ID format checks;
- DOI/arXiv/URL normalization;
- duplicate detection by ID, DOI, arXiv ID, normalized title, and canonical URL;
- orphan relationship detection;
- date validation;
- public-view filtering of unverified records.

## Acceptance criteria

- All schemas have positive and negative tests.
- Test fixtures contain invalid edge cases.
- Duplicate and orphan detection tests pass.
- No public content is yet generated from unverified records.
- Phase report status is `PASS`.

## Commit

`phase(02): define taxonomy and canonical metadata schemas`
