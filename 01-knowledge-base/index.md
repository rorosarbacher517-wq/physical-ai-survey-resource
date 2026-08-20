# Scientific / Physical AI Knowledge Base

> Goal: build a **bottom-up knowledge dependency graph**, not a flat list of papers or model names.

## Start here

- [Detailed Knowledge Index](DETAILED_INDEX.md): fine-grained topic map.
- [Learning Paths](learning-paths/index.md): routes for Earth observation/carbon/weather/scientific ML.
- [Knowledge-unit Standard](KNOWLEDGE_UNIT_STANDARD.md): required depth for deep-dive pages.
- [2026 Snapshot](13-2026-snapshot/index.md): dated fast-moving developments.

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
| 00 | [Foundations](00-foundations/index.md) | ODE/PDE, conservation, boundary conditions, discretization, stability, scale/support |
| 01 | [ML/DL & scientific computing](01-ml-dl-scientific-computing/index.md) | regression, CNN/ViT/GNN/Transformer, optimization, tensor/GPU basics |
| 02 | [Physical AI core](02-physics-ai-core/index.md) | taxonomy of physics-data-model-observation coupling |
| 03 | [Physics-informed learning](03-physics-informed-learning/index.md) | soft/hard constraints, PINN, symmetry, physical regularization |
| 04 | [Neural operators & simulation](04-neural-operators-simulation/index.md) | operator learning, surrogates, differentiable/hybrid solvers |
| 05 | [Spatiotemporal & multiscale](05-spatiotemporal-multiscale-ai/index.md) | grids/graphs/meshes, temporal dynamics, multimodality, support mismatch |
| 06 | [Earth Observation AI](06-earth-observation-ai/index.md) | observation physics → modalities → time/fusion/reconstruction → EO FM/evaluation |
| 07 | [Carbon-cycle AI](07-carbon-cycle-ai/index.md) | carbon process → EC/partitioning/footprints → multimodal/process AI → upscaling/extremes |
| 08 | [Weather & climate AI](08-weather-climate-ai/index.md) | NWP/DA → AI/hybrid forecast → ensemble/extremes/downscaling → coupled climate |
| 09 | [Earth foundation models](09-earth-foundation-models/index.md) | pretraining, multimodal representations, transfer and leakage/OOD evaluation |
| 10 | [DA / inverse / UQ](10-data-assimilation-inverse-uq/index.md) | state estimation, retrieval, uncertainty and calibration |
| 11 | [Data / HPC / evaluation](11-data-hpc-evaluation/index.md) | scalable data pipelines, compute, OOD, reproducibility |
| 12 | [Cross-domain Physical AI](12-cross-domain-physical-ai/index.md) | fluids, energy/materials, digital twins, embodied bridges |
| 13 | [2026 Snapshot](13-2026-snapshot/index.md) | verified fast-moving developments |

## Central question: where does physics enter?

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

A model is not automatically physics-informed because it predicts a physical variable. The repository records the **integration stage** explicitly.

## Priority Earth-system tracks

- [Earth Observation / remote sensing](../06-case-studies/geoscience-remote-sensing/earth-observation/index.md)
- [Terrestrial carbon flux](../06-case-studies/geoscience-remote-sensing/carbon-flux/index.md)
- [Weather & climate](../06-case-studies/geoscience-remote-sensing/weather-and-climate/index.md)
- [Geospatial foundation models](../06-case-studies/geoscience-remote-sensing/geospatial-foundation-models/index.md)

## Resource layer

Educational pages point to, rather than duplicate, canonical records:

- [papers by method](../02-paper-library/by-method.md)
- [papers by domain](../02-paper-library/by-domain.md)
- [code](../03-code-library/index.md)
- [datasets](../04-dataset-library/index.md)
- [benchmarks](../05-benchmarks-and-evaluation/index.md)

## Unified method-reading template

```text
physical problem
→ state / observation / units
→ input-output shape and support
→ governing physics / prior
→ integration point
→ model computation
→ loss / constraint / likelihood
→ train vs inference/rollout
→ compute/memory
→ evaluation / OOD
→ uncertainty / failure modes
→ primary source
```
