# AI Weather-model Families

This page organizes weather models by **representation, forecast role, learning objective and rollout behavior** rather than by a single score.

## 1. Common input/output abstraction

A global atmospheric state can be represented as:

```text
X_t: [B,V,L,H,W]
```

where `V` is variable type and `L` is vertical level. Surface-only variables may use a separate level or branch.

A learned forecast model approximates:

```text
X_t → X_(t+Δt)
```

or directly predicts several lead times.

## 2. Grid / spectral operator family

FourCastNet-style systems use Fourier/operator-style computation on global gridded fields.

Primary anchor: https://arxiv.org/abs/2202.11214

Study questions:

- how spectral/global mixing is implemented;
- which modes/resolutions are represented;
- forecast step and rollout;
- how high-frequency/extreme structure is preserved;
- compute scaling with grid size.

## 3. Graph / mesh family

GraphCast maps gridded atmospheric fields to a multi-scale mesh/graph and propagates information through message passing.

Primary anchor: https://www.science.org/doi/10.1126/science.adi2336

Forward abstraction:

```text
grid state
→ grid-to-mesh encode
→ graph processing
→ mesh-to-grid decode
→ next state
```

Study mesh topology, spherical geometry, edge messages and autoregressive rollout.

## 4. Transformer-style 3D Earth models

Pangu-Weather uses Earth-specific 3D Transformer-style processing across horizontal space and vertical levels.

Primary anchor: https://www.nature.com/articles/s41586-023-06185-3

Study:

- 3D patch/token representation;
- vertical levels;
- hierarchical temporal forecasting;
- memory/compute at global resolution.

## 5. Hybrid differentiable atmosphere

NeuralGCM combines learned components with a differentiable dynamical core.

Primary anchor: https://www.nature.com/articles/s41586-024-07744-y

See [Hybrid physics–ML weather](physics-hybrid-weather.md).

## 6. Probabilistic / generative forecast

GenCast uses generative modeling to produce an ensemble/distribution rather than one conditional-mean trajectory.

Primary anchor: https://www.nature.com/articles/s41586-024-08252-9

See [Probabilistic and ensemble weather](probabilistic-ensemble-weather.md).

## 7. Foundation-model route

Aurora illustrates broad geophysical pretraining followed by adaptation across Earth-system forecasting tasks.

Primary: https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/

See [Weather/Earth-system foundation models](weather-foundation-models.md).

## 8. Operational model families

Rapidly changing operational/platform details belong in [2026 Snapshot](../13-2026-snapshot/index.md), where they can be dated and sourced to official releases.

## 9. Training objective questions

For every model determine:

- one-step versus multi-step loss;
- normalized variable weighting;
- deterministic versus probabilistic objective;
- rollout curriculum;
- fine-tuning/adaptation;
- whether training uses analysis/reanalysis, forecasts or observations.

## 10. Inference questions

```text
initial analysis
→ one or multiple learned forecast steps
→ optional autoregressive rollout
→ ensemble sampling if probabilistic
→ post-processing/downscaling
```

Measure runtime together with hardware, resolution, variables and ensemble size.

## 11. Evaluation template

Record:

`input source → variables/levels → grid/mesh → architecture → forecast step → loss → deterministic/probabilistic → rollout → verification source/grid → extremes → compute → deployment context`.

Do not compare headline RMSE/ACC without matching variable, level, grid, verification source and lead time.

## 12. Failure modes

- stable one-step prediction but drifting rollout;
- normalization overweights easy variables;
- global metrics hide regional/extreme failures;
- probabilistic ensemble is under/over-dispersed;
- reanalysis skill is reported as direct observation skill;
- different grids are compared without careful remapping.
