# Geoscience, Remote Sensing and Earth-system AI

This is the repository's priority specialty track. It connects **observation physics, Earth-system processes, spatial-temporal AI, foundation models and scale-aware evaluation**.

## Knowledge dependency

```text
Scientific foundations
→ spatiotemporal/multiscale AI
→ Earth observation physics
      ├→ terrestrial carbon cycle
      ├→ weather/climate
      └→ geospatial foundation models
→ data assimilation / UQ
→ Earth-system evaluation
```

## Priority tracks

- [Earth Observation / Remote Sensing](earth-observation/index.md)
- [Terrestrial Carbon Flux](carbon-flux/index.md)
- [Weather and Climate](weather-and-climate/index.md)
- [Geospatial Foundation Models](geospatial-foundation-models/index.md)

## Core knowledge modules

- [Earth Observation AI](../../01-knowledge-base/06-earth-observation-ai/index.md)
- [Carbon-cycle AI](../../01-knowledge-base/07-carbon-cycle-ai/index.md)
- [Weather & Climate AI](../../01-knowledge-base/08-weather-climate-ai/index.md)
- [Earth Foundation Models](../../01-knowledge-base/09-earth-foundation-models/index.md)
- [Spatiotemporal & Multiscale AI](../../01-knowledge-base/05-spatiotemporal-multiscale-ai/index.md)
- [Data Assimilation / Inverse / UQ](../../01-knowledge-base/10-data-assimilation-inverse-uq/index.md)

## Shared scientific principles

1. **Observation is not state.** Sensor/retrieval/footprint physics matters.
2. **Resolution is not support.** A 30 m output can still be supervised by a much larger/variable observation footprint.
3. **Space and time are coupled.** Revisit, temporal aggregation and moving source areas can change the learning problem.
4. **Random splits are often invalid.** Site, region, event and time blocking are core design choices.
5. **Physics can enter at multiple layers.** Inputs, architecture, loss, operator, simulator, DA and evaluation should be distinguished.
6. **Uncertainty is part of the prediction.** Measurement, retrieval, model and scale uncertainty should be tracked.
