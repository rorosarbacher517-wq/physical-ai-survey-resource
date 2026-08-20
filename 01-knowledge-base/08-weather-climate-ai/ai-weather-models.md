# AI Weather-model Families

This page organizes models by representation and scientific role rather than by leaderboard position.

## 1. Grid/spectral operator models

FourCastNet-style systems use Fourier/operator-style computation on global gridded fields.

Primary anchor: https://arxiv.org/abs/2202.11214

Questions:

- spectral modes;
- spatial resolution;
- autoregressive step;
- variable/level encoding;
- high-frequency/extreme preservation.

## 2. Graph/mesh models

GraphCast maps atmospheric fields through a multi-scale graph/mesh representation that enables global information propagation.

Primary anchor: https://www.science.org/doi/10.1126/science.adi2336

Questions:

- grid-to-mesh encoding;
- mesh connectivity;
- message passing;
- rollout cadence;
- spherical geometry.

## 3. Transformer-style global forecasting

Pangu-Weather uses 3D Earth-specific Transformer-style processing and multi-step forecast organization.

Primary anchor: https://www.nature.com/articles/s41586-023-06185-3

Questions:

- 3D spatial representation;
- vertical levels;
- temporal hierarchy;
- memory/compute.

## 4. Hybrid differentiable atmosphere

NeuralGCM combines learned components with a differentiable dynamical core, illustrating a hybrid numerical–ML route.

Primary anchor: https://www.nature.com/articles/s41586-024-07744-y

## 5. Probabilistic generative forecast

GenCast uses generative modeling to produce ensemble weather forecasts rather than a single conditional-mean trajectory.

Primary anchor: https://www.nature.com/articles/s41586-024-08252-9

## 6. Foundation-model route

Aurora is an Earth-system foundation-model approach: pretraining over broad geophysical data followed by task adaptation.

Primary: https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/

## 7. Operational systems

ECMWF AIFS and current WeatherNext/Earth-2 releases represent rapidly changing operational/platform systems. Keep their dated details in [2026 Snapshot](../13-2026-snapshot/index.md).

## 8. Comparison template

For each model record:

`input source → variables/levels → grid/mesh → architecture → forecast step → loss → deterministic/probabilistic → rollout → verification → compute → operational status`.

Do not compare headline RMSE/ACC without matching verification data, variable, level, grid and lead time.
