# Phase 13 acceptance report — Scientific / Physical AI Knowledge Base v2

Status: `PENDING_CI`

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

## Review completed during authoring

- verified that the feature branch is ahead of `main` and not behind it;
- reviewed new relative-link structure against the repository tree while creating the detailed index;
- reviewed new prose against `scripts/audit_claims.py` risky-claim vocabulary and removed/marked identified triggers;
- preserved the resource-count generated markers in the root README;
- preserved existing metadata/taxonomy files.

## Acceptance gates

- [ ] `python -m scripts.full_check` observed as passing
- [ ] external-link verification workflow observed as passing
- [ ] no broken internal links reported by CI
- [ ] no generated-file drift reported by CI
- [ ] no unsupported fast-moving claims reported during final review

The GitHub connector used for this update does not expose the push-triggered Actions check run for this branch, so the phase remains `PENDING_CI` rather than being marked `PASS` without evidence.
