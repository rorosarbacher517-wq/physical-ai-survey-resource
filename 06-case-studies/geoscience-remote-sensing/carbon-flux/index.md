# Terrestrial Carbon-flux AI Specialty Track

This priority track connects **eddy covariance, flux footprints, Earth observation, meteorological forcing, process constraints, deep learning and scale-aware upscaling**.

Main knowledge page: [Carbon-cycle AI](../../../01-knowledge-base/07-carbon-cycle-ai/index.md).

## 1. Scientific question

How can AI estimate terrestrial carbon exchange while preserving:

- the physical meaning of NEE/GPP/RECO;
- the actual source area represented by tower observations;
- the spatial-temporal support of satellite/meteorological predictors;
- process relationships and uncertainty;
- valid transfer to new sites/biomes/climate regimes?

## 2. Observation chain

```text
surface carbon exchange
→ turbulent transport
→ EC measurement
→ footprint / source-area weighting
→ tower-scale NEE
→ partitioned GPP / RECO
```

Satellite observations then provide spatially explicit predictors, not direct replacements for this measurement chain.

## 3. Multimodal predictor stack

```text
2D optical / thermal / SIF / SAR
+ 3D LiDAR structure
+ meteorology / soil moisture
+ static land/soil/topography
+ dynamic footprint / observation operator
→ spatiotemporal carbon model
```

## 4. Physics-informed opportunities

- footprint-weighted observation mapping;
- carbon balance consistency;
- light/water/temperature process priors;
- hybrid process-model residual learning;
- carbon-water-energy coupling;
- data assimilation;
- uncertainty propagation.

## 5. Evaluation hierarchy

Prefer:

1. site-blocked validation;
2. temporal/event/extreme stratification;
3. biome/climate-region transfer;
4. paired ablations for each physics component;
5. measurement/support-aware metrics;
6. uncertainty/calibration;
7. independent spatial validation where available.

## 6. End-to-end resource chain

- datasets: `dataset-fluxnet`, `dataset-ameriflux`, HLS, ERA5-Land, MODIS, SMAP;
- method views: `machine-learning-upscaling`, `observation-operator-methods`, `hybrid-numerical-machine-learning`;
- code/resources: FFP and geospatial preprocessing records where available;
- benchmarks: site-blocked and support-aware carbon-flux definitions.

Browse:

- [papers by method](../../../02-paper-library/by-method.md)
- [papers by domain](../../../02-paper-library/by-domain.md)
- [datasets](../../../04-dataset-library/index.md)
- [benchmarks](../../../05-benchmarks-and-evaluation/index.md)

## 7. Research frontier

Dynamic footprint-aware learning, multimodal 2D+3D fusion, dense temporal reconstruction, process-aware foundation representations, OOD climate/biome transfer and calibrated uncertainty are priority directions.
