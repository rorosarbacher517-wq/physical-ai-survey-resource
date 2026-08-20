# 05 · Spatiotemporal, Multiscale and Multimodal AI

Earth and physical systems combine space, time, multiple variables, multiple sensors and multiple scales. This layer connects generic AI to those structures.

## 1. Representation choices

### Regular grid
Efficient for CNN/U-Net and many vision-style models.

### Sequence / patch tokens
Useful for Transformer models, but token count can explode with high spatial resolution and long time series.

### Graph / mesh
Useful for irregular sampling, spherical geometry, stations and numerical meshes.

### Point set / point cloud
Useful for LiDAR, particles and sparse observations.

### Spectral representation
Useful for global/smooth fields and operator models, but local extremes and discontinuities require care.

## 2. Temporal modeling

Distinguish:

- static regression;
- sequence-to-one;
- sequence-to-sequence;
- autoregressive forecast;
- continuous-time dynamics;
- event-based prediction.

A satellite acquisition sequence, a half-hourly EC time series and a six-hourly global weather rollout are different temporal problems.

## 3. Multi-resolution data

Common issue:

```text
high spatial / low temporal resolution sensor
+ low spatial / high temporal resolution forcing
+ sparse point/footprint observations
```

Solutions include:

- resampling with explicit uncertainty;
- hierarchical encoders;
- super-resolution/downscaling;
- latent fusion;
- cross-attention;
- operator-based aggregation;
- data assimilation.

Never assume that resampling creates new physical information.

## 4. Spatial support mismatch

A central Earth-system issue:

```text
prediction grid ≠ sensor footprint ≠ station support ≠ validation support
```

Examples:

- EC tower footprint changes with turbulence/wind;
- satellite pixel integrates area and point-spread effects;
- weather station is local while model grid is areal;
- radar/radiometer retrievals have instrument-specific footprints.

Support-aware observation operators are often more scientifically important than adding another backbone layer.

## 5. Geospatial inductive biases

Potential information:

- latitude/longitude/projection;
- elevation/topography;
- solar geometry;
- season/time-of-day;
- land-cover/ecoregion;
- neighborhood/flow connectivity;
- spherical distance;
- periodic longitude.

Use them only when the scientific task justifies them and check for location leakage.

## 6. Evaluation splits

At minimum report whether validation is blocked by:

- site;
- spatial region;
- time;
- event/extreme;
- climate/biome regime;
- sensor;
- simulation parameter range.

## 7. Priority applications

- [Earth Observation AI](../06-earth-observation-ai/index.md)
- [Carbon-cycle AI](../07-carbon-cycle-ai/index.md)
- [Weather & Climate AI](../08-weather-climate-ai/index.md)
