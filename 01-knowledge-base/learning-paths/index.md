# Learning Paths

The same repository supports different entry points, but all routes share the same dependency graph.

## Route A — Complete Scientific / Physical AI

```text
00 Foundations
→ 01 ML/DL + Scientific Computing
→ 02 Physical AI Core
→ 03 Physics-informed Learning
→ 04 Neural Operators / Simulation
→ 10 Data Assimilation / Inverse / UQ
→ 05 Spatiotemporal / Multiscale AI
→ domain track
→ 09 Foundation Models
→ 11 Data/HPC/Evaluation
→ 12 Cross-domain Physical AI
```

**Pass standard:** for a new paper, you can identify the state variables, observations, equations/priors, integration point, spatial-temporal support, validation design and uncertainty without relying on the authors' marketing label.

## Route B — Remote sensing + carbon cycle (priority)

```text
00 → 01 → 02
→ 05 Spatiotemporal / Multiscale
→ 06 Earth Observation
→ 07 Carbon Cycle
→ 10 DA / Inverse / UQ
→ 09 Earth Foundation Models
→ 11 Evaluation
```

Must understand:

- radiance/reflectance vs biophysical/ecosystem targets;
- optical, SAR, thermal, LiDAR, SIF and meteorological modalities;
- pixel/grid support versus EC footprint support;
- NEE, GPP, RECO and partitioning assumptions;
- tower-to-grid upscaling and site-blocked validation;
- process/observation constraints and uncertainty propagation.

## Route C — Weather & climate AI

```text
00 Numerical/Physics
→ 01 ML/DL
→ 04 Neural Operators / Simulation
→ 05 Spatiotemporal / Spherical representations
→ 10 Data Assimilation / UQ
→ 08 Weather & Climate
→ 09 Foundation Models
→ 11 HPC / Evaluation
```

Must be able to draw:

```text
observations
→ QC / data assimilation
→ analysis / initial state
→ deterministic or ensemble forecast
→ post-processing / downscaling
→ verification
```

and explain where Graph/Transformer/operator/diffusion-style models fit in that chain.

## Route D — Domain scientist entering AI

Start with 02, then backfill 01 as needed.

Focus on:

- leakage and unfair splits;
- units, transformations and normalization;
- physical constraints;
- uncertainty;
- interpretability versus causal claims;
- reproducible benchmark design.

## Route E — ML researcher entering scientific computing

Prioritize 00 → 04 → 10.

Focus on:

- discretization and numerical error;
- mesh/grid invariance;
- PDE residuals;
- operator learning;
- differentiable solvers;
- inverse problems and identifiability;
- stability under autoregressive rollout.

## Route F — Embodied / broader Physical AI

```text
00/01 basics
→ 02 Physical AI Core
→ 05 Spatiotemporal representations
→ 12 Cross-domain Physical AI
```

Then connect to perception, world models, planning, control, sim-to-real and VLA resources as the embodied branch grows.

## How to study a paper

Do not start by memorizing the method name. Fill this card first:

| Question | Notes |
|---|---|
| Physical system / target | |
| Observations and sensors | |
| State variables / units | |
| Space-time resolution/support | |
| Governing physics / prior | |
| Where physics enters | |
| Architecture / representation | |
| Loss / likelihood / constraints | |
| Train/test split | |
| Baselines | |
| Uncertainty | |
| Failure modes | |
| Reproducibility | |

Then link the paper to the canonical [paper library](../../02-paper-library/index.md).
