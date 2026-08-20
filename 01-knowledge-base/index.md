# Scientific / Physical AI Knowledge Base

> Goal: build a **bottom-up knowledge dependency graph**, not a flat list of papers or model names.

**Fine-grained navigation:** [Detailed Knowledge Index](DETAILED_INDEX.md) contains the full second-level topic map beneath the 00–13 modules.

## Knowledge map

```text
00 Foundations
   math + physics + numerical methods + units/scales
        ↓
01 ML/DL + Scientific Computing
        ↓
02 Physical AI Core
   where and how physics enters learning
        ↓
03 Physics-informed Learning
04 Neural Operators / Simulation
10 Data Assimilation / Inverse / UQ
        ↓
05 Spatiotemporal / Multiscale AI
        ↓
06 Earth Observation ──→ 07 Carbon Cycle
        └──────────────→ 08 Weather & Climate
                         ↓
09 Earth / Scientific Foundation Models
                         ↓
11 Data / HPC / Evaluation
                         ↓
12 Cross-domain Physical AI
                         ↓
13 Current Snapshot
```

## Modules

| # | Module | What you should be able to explain |
|---|---|---|
| 00 | [Foundations](00-foundations/index.md) | ODE/PDE, conservation, boundary conditions, discretization, stability, scale |
| 01 | [ML/DL & scientific computing](01-ml-dl-scientific-computing/index.md) | regression, CNN/ViT/GNN/Transformer, optimization, tensor/GPU basics |
| 02 | [Physical AI core](02-physics-ai-core/index.md) | taxonomy of physics-data-model coupling |
| 03 | [Physics-informed learning](03-physics-informed-learning/index.md) | soft/hard constraints, PINN, symmetry, physical regularization |
| 04 | [Neural operators & simulation](04-neural-operators-simulation/index.md) | operator learning, surrogates, differentiable/hybrid solvers |
| 05 | [Spatiotemporal & multiscale](05-spatiotemporal-multiscale-ai/index.md) | grids/graphs/meshes, temporal dynamics, irregular sampling, scale mismatch |
| 06 | [Earth Observation AI](06-earth-observation-ai/index.md) | sensing physics → representations → EO learning/foundation models |
| 07 | [Carbon-cycle AI](07-carbon-cycle-ai/index.md) | EC/footprints → multimodal predictors → flux learning/upscaling |
| 08 | [Weather & climate AI](08-weather-climate-ai/index.md) | NWP/DA → deterministic/probabilistic AI → downscaling/climate |
| 09 | [Earth foundation models](09-earth-foundation-models/index.md) | pretraining, multimodality, embeddings, transfer and limitations |
| 10 | [DA / inverse / UQ](10-data-assimilation-inverse-uq/index.md) | state estimation, retrieval, uncertainty and calibration |
| 11 | [Data / HPC / evaluation](11-data-hpc-evaluation/index.md) | scalable data pipelines, compute, OOD, reproducibility |
| 12 | [Cross-domain Physical AI](12-cross-domain-physical-ai/index.md) | fluids, energy/materials, biomedical, robotics/digital twins |
| 13 | [2026 Snapshot](13-2026-snapshot/index.md) | verified fast-moving developments |

## The central question: where does physics enter?

```text
raw observations
  ↓
measurement / observation physics
  ↓
inputs + physical features
  ↓
physics-aware representation / architecture
  ↓
physical losses / hard constraints
  ↓
operator / simulator / data-assimilation loop
  ↓
predictions
  ↓
scale-aware + physically meaningful evaluation
```

A model is not automatically “physics-informed” because it predicts a physical variable. The repository therefore records the **integration stage** explicitly.

## Priority domain tracks

- [Earth Observation / remote sensing](../06-case-studies/geoscience-remote-sensing/earth-observation/index.md)
- [Terrestrial carbon flux](../06-case-studies/geoscience-remote-sensing/carbon-flux/index.md)
- [Weather & climate](../06-case-studies/geoscience-remote-sensing/weather-and-climate/index.md)
- [Geospatial foundation models](../06-case-studies/geoscience-remote-sensing/geospatial-foundation-models/index.md)

## Resource layer

The educational modules should point to, not duplicate, canonical records:

- [papers by method](../02-paper-library/by-method.md)
- [papers by domain](../02-paper-library/by-domain.md)
- [code](../03-code-library/index.md)
- [datasets](../04-dataset-library/index.md)
- [benchmarks](../05-benchmarks-and-evaluation/index.md)

## Recommended answer template

For every method/model/system:

```text
physical problem
→ state / observation / units
→ spatial-temporal representation
→ governing physics / prior
→ integration point
→ model computation
→ loss / constraint / likelihood
→ train vs inference
→ scale / support
→ evaluation / OOD
→ uncertainty / failure modes
→ primary source
```

## Learning routes

See [Learning paths](learning-paths/index.md).
