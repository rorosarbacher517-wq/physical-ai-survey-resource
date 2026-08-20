# Phase 13 acceptance report — Scientific / Physical AI Knowledge Base v2

Status: `PASS`

Date: 2026-08-20

## Scope implemented

- bottom-up 00–13 knowledge dependency map;
- fine-grained `DETAILED_INDEX.md` beneath the top-level roadmap;
- dedicated foundations for linear algebra/probability/optimization, dynamical systems/PDEs, numerical methods, dimensional analysis, scale and observation support;
- ML/DL scientific-computing foundations including classical baselines, CNN/Transformer/GNN and PyTorch/JAX/HPC concepts;
- Physical-AI core pages for observation operators, conservation/symmetry/dimensional priors and hybrid numerical–ML design;
- PINN, hard/soft constraints, neural operators, surrogates and differentiable simulation;
- spatial, temporal, multiscale, multimodal and support-aware learning;
- deep Earth Observation track covering optical/hyperspectral, SAR/microwave, LiDAR/3D, thermal/SIF, preprocessing, model tasks and EO foundation models;
- deep terrestrial-carbon track covering carbon processes, EC, flux footprints, data stack, modeling families, footprint-aware AI, multimodal carbon AI and uncertainty/validation;
- deep weather/climate track covering NWP, data assimilation, AI weather-model families, probabilistic ensembles, nowcasting, downscaling, climate AI and verification;
- Earth/scientific foundation-model pretraining and model-family guide;
- inverse problems, data assimilation, uncertainty/calibration;
- scientific data engineering, distributed/HPC training, evaluation/benchmarking;
- broader fluids, energy/materials, digital-twin and embodied Physical-AI bridges;
- dated 2026 snapshot and update policy;
- expanded Earth-system specialty-track and MkDocs navigation.

## Invariants preserved

- canonical metadata remains source of truth;
- no generated paper/code/dataset/benchmark view was manually edited;
- no taxonomy label was changed;
- existing resource IDs and counts were preserved;
- fast-moving snapshot claims use original/official source URLs;
- promotional wording in an official AlphaEarth URL is explicitly marked for the repository claim-audit rule rather than repeated as a scientific claim.

## Acceptance gates

- [x] `python -m scripts.full_check` passed in GitHub Actions
- [x] external-link verification passed in GitHub Actions
- [x] no broken internal links reported
- [x] no generated-file drift reported
- [x] no unsupported fast-moving claims reported by the repository checks

Validated by GitHub Actions workflow `ci`, run 32, after claim-audit wording fixes.
