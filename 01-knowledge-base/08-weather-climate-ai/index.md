# 08 · Weather and Climate AI

Weather AI should be understood as a **complete modeling and observing system**, not a list of model names.

## Knowledge path

```text
Atmospheric dynamics / NWP
→ observations + QC
→ data assimilation / initial state
→ AI or hybrid forecast model
→ deterministic / probabilistic rollout
→ extremes / nowcasting
→ downscaling / post-processing
→ coupled Earth-system applications
→ verification / calibration / operations
```

## 1. NWP foundation

Start with [NWP basics](nwp-basics.md).

Numerical weather prediction solves discretized atmospheric equations and parameterizes unresolved processes. AI may replace, accelerate or augment selected blocks.

## 2. Data assimilation

See [Weather data assimilation](weather-data-assimilation.md).

```text
observations + prior forecast
→ observation operators / QC
→ analysis / initial atmospheric state
```

Forecast quality depends strongly on the initial state; model architecture is only one part of the system.

## 3. Forecast model families

See [AI weather-model families](ai-weather-models.md).

Important representations include:

- latitude–longitude grids;
- spectral/operator spaces;
- spherical meshes/graphs;
- 3D patches/tokens;
- multi-variable foundation-model embeddings.

## 4. Hybrid physics–ML

See [Hybrid physics–ML weather](physics-hybrid-weather.md).

ML can learn parameterizations/tendencies/corrections while a numerical or differentiable dynamical core advances the atmosphere.

## 5. Deterministic, probabilistic and generative forecasts

See [Probabilistic and ensemble weather](probabilistic-ensemble-weather.md).

A deterministic forecast produces one trajectory. An ensemble/generative system represents multiple plausible trajectories and must be evaluated for calibration/spread as well as mean error.

## 6. Nowcasting and extremes

- [Nowcasting](nowcasting.md): short-horizon high-resolution precipitation/severe-weather prediction.
- [Weather extremes](extremes-forecasting.md): rare-event/tail evaluation, event objects and probabilistic skill.

## 7. Downscaling and super-resolution

See [Downscaling and super-resolution](downscaling-super-resolution.md).

Separate coarse-to-fine statistical inference from the creation of genuinely observed fine-scale information.

## 8. Weather/Earth foundation models

See [Weather and Earth-system foundation models](weather-foundation-models.md) and [Earth/scientific foundation models](../09-earth-foundation-models/index.md).

Transfer across tasks/variables/regions/resolutions is the key evaluation question.

## 9. Coupled Earth-system AI

See [Coupled Earth-system AI](earth-system-coupling.md).

Atmosphere, land, ocean and carbon processes operate on different grids/timescales but exchange energy, water, momentum and carbon.

## 10. Climate AI

See [Climate AI](climate-ai.md).

Climate applications require distributional/climatological fidelity, extremes, long rollout and regime shift—not only short forecast RMSE.

## 11. Evaluation

See [Weather evaluation](weather-evaluation.md).

Report:

- variable and pressure level;
- lead time;
- verification dataset;
- grid/remapping method;
- deterministic/probabilistic metric;
- regional/event stratification;
- physical consistency;
- compute/latency.

## 12. Earth-observation and carbon connections

```text
weather observations / reanalysis
→ environmental forcing
→ land/ecosystem response
→ carbon/water/energy flux
```

See [Carbon–water–energy coupling](../07-carbon-cycle-ai/carbon-water-energy-coupling.md) and [EO AI](../06-earth-observation-ai/index.md).

## 13. Current systems

Dated operational/deployment developments belong in [13 · 2026 Snapshot](../13-2026-snapshot/index.md) to keep the stable knowledge pages from becoming release-note lists.

See also the [Weather & climate specialty track](../../06-case-studies/geoscience-remote-sensing/weather-and-climate/index.md).
