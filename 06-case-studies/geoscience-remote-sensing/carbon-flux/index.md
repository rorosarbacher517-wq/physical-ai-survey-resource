# Carbon-flux resource map

This track connects terrestrial carbon-flux estimation with observation physics and scale-aware AI. It is organized around a practical chain from measurement to model evaluation.

## Scientific question

How can AI estimate GPP, ecosystem respiration and NEE while preserving process meaning, measurement support and validation scope?

## Measurement and observation process

- Eddy covariance estimates net turbulent exchange over a dynamic footprint.
- EC does not directly measure GPP or ecosystem respiration; component fluxes require partitioning assumptions.
- Satellite observations provide radiance, reflectance, fluorescence, temperature or microwave signals, not carbon exchange itself.
- A fixed pixel and a tower footprint are different supports.

## Physical priors and observation operators

- Process priors: radiation absorption, phenology, water stress, respiration sensitivity and carbon-water coupling.
- Observation priors: EC footprint weighting, satellite retrieval physics, SIF-GPP interpretation and data-assimilation constraints.
- Scale priors: site-blocked validation, biome extrapolation, resolution compatibility and uncertainty propagation.

## End-to-end verified resource chain

- Scientific question: support-aware carbon-flux estimation.
- Measurement process: `dataset-fluxnet` and `dataset-ameriflux`.
- Physical prior: footprint support and carbon-water coupling.
- Model integration: `observation-operator-methods`, `machine-learning-upscaling`, `hybrid-numerical-machine-learning`.
- Code: `code-repo-examples`, `code-ffp`, `code-google-earth-engine`.
- Datasets: `dataset-hls`, `dataset-era5-land`, `dataset-modis`, `dataset-smap`.
- Benchmarks: `benchmark-carbon-flux-site-blocked`, `benchmark-carbon-flux-footprint-support`, `benchmark-remote-sensing-gpp`.
- Limitations: site leakage, footprint-pixel mismatch, uncertain partitioning and limited independent field-scale validation.

## Navigation views

- [Carbon-flux papers](../../../02-paper-library/by-domain.md)
- [Papers by method](../../../02-paper-library/by-method.md)
- [Dataset library](../../../04-dataset-library/index.md)
- [Benchmark library](../../../05-benchmarks-and-evaluation/index.md)

## Safeguards

Repository synthesis: claims about 30 m or field-scale products should distinguish prediction resolution from validation resolution. Optical observability should not be treated as causal process control without additional evidence. Sign conventions and units must be recorded in benchmark cards before comparing scores.
