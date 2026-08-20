# Phase 14 acceptance report — Deep knowledge units and Earth-system cross-links

Status: `PENDING_CI`

Date: 2026-08-20

## Scope implemented

- added a repository-wide `KNOWLEDGE_UNIT_STANDARD.md` covering scientific problem, observation model, tensor/shape semantics, physics integration, training, inference/rollout, compute, evaluation, failure modes and primary sources;
- deepened Earth Observation with radiative-transfer/observation physics, multisensor fusion, irregular time-series learning, super-resolution/reconstruction and geospatial OOD validation;
- deepened terrestrial carbon with flux-partitioning uncertainty, carbon–water–energy coupling, process-constrained learning, tensor-level footprint observation operators, tower-to-grid upscaling and climate-extreme evaluation;
- deepened weather/climate with hybrid physics–ML modeling, foundation-model transfer, extremes, coupled Earth-system modeling and a tensor/rollout-oriented weather model-family guide;
- deepened Earth foundation models with multimodal representation design and transfer/leakage/OOD evaluation;
- regenerated the human-authored detailed knowledge index and updated specialty-track navigation;
- updated MkDocs navigation so the detailed map and knowledge-unit standard are visible entry points.

## Design invariants

- canonical resource metadata remains unchanged and remains the source of truth for papers/code/datasets/benchmarks;
- generated resource views were not manually edited;
- no taxonomy labels were changed;
- no existing resource IDs were duplicated;
- stable concept pages avoid release-specific operational claims; fast-moving details remain in the dated snapshot;
- new model-specific anchors are original papers or official institutional sources already used by the repository.

## Review performed during authoring

- all newly added relative links were written against existing/new paths in the same branch;
- new prose avoids the repository risky-claim vocabulary (`first`, `best`, `state-of-the-art`, `unprecedented`) except previously marked official URL paths outside this phase;
- support/resolution/validation are explicitly separated across EO and carbon pages;
- GPP/RECO are described as partitioned/inferred targets rather than direct independent EC measurements;
- weather pages separate initial-state/data-assimilation, forecast model, probabilistic rollout, downscaling and verification.

## Acceptance gates

- [ ] `python -m scripts.full_check` observed as passing
- [ ] external-link verification observed as passing
- [ ] no broken internal links reported
- [ ] no generated-file drift reported
- [ ] no unsupported fast-moving claims reported

This phase remains `PENDING_CI` until an actual workflow/local check result is observed.
