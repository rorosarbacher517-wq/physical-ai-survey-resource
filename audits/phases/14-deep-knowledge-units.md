# Phase 14 acceptance report — Deep knowledge units and Earth-system cross-links

Status: `PASS`

Date: 2026-08-20

## Scope implemented

- added a repository-wide `KNOWLEDGE_UNIT_STANDARD.md` covering scientific problem, observation model, tensor/shape semantics, physics integration, training, inference/rollout, compute, evaluation, failure modes and primary sources;
- deepened Earth Observation with radiative-transfer/observation physics, multisensor fusion, irregular time-series learning, super-resolution/reconstruction and geospatial OOD validation;
- deepened terrestrial carbon with flux-partitioning uncertainty, carbon–water–energy coupling, process-constrained learning, tensor-level footprint observation operators, tower-to-grid upscaling and climate-extreme evaluation;
- deepened weather/climate with hybrid physics–ML modeling, foundation-model transfer, extremes, coupled Earth-system modeling and a tensor/rollout-oriented weather model-family guide;
- deepened Earth foundation models with multimodal representation design and transfer/leakage/OOD evaluation;
- updated the human-authored detailed knowledge index and specialty-track navigation;
- updated MkDocs navigation so the detailed map and knowledge-unit standard are visible entry points.

## Design invariants

- canonical resource metadata remains unchanged and remains the source of truth for papers/code/datasets/benchmarks;
- generated resource views were not manually edited;
- no taxonomy labels were changed;
- no existing resource IDs were duplicated;
- stable concept pages avoid release-specific operational claims; fast-moving details remain in the dated snapshot;
- new model-specific anchors are original papers or official institutional sources already used by the repository.

## Acceptance gates

- [x] `python -m scripts.full_check` passed in GitHub Actions
- [x] external-link verification passed in GitHub Actions
- [x] no broken internal links reported
- [x] no generated-file drift reported
- [x] no unsupported fast-moving claims reported by repository checks

Validation evidence: GitHub Actions workflow `ci`, run 32. The preceding failure identified two risky-claim wording triggers; both were corrected and the subsequent run passed all steps.
