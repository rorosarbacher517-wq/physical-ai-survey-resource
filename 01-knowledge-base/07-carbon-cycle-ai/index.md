# 07 · Terrestrial Carbon-cycle / Carbon-flux AI

This is a priority track of the repository. The organizing principle is the complete chain from **measurement physics → multimodal predictors → model → scale-aware validation**.

## 1. Carbon-flux targets

Common tower-scale quantities:

- **NEE**: net ecosystem exchange measured/estimated from EC processing;
- **GPP**: gross primary productivity, usually obtained through partitioning/model assumptions rather than direct EC measurement;
- **RECO**: ecosystem respiration, also partitioned/estimated.

A commonly used balance convention is:

```text
NEE = RECO - GPP
```

but sign conventions must always be checked against the dataset/product definition.

## 2. Eddy covariance is an area-support observation

A half-hourly EC measurement is not a point sample. It integrates turbulent contributions from an upwind **flux footprint** whose position and weighting vary with atmospheric conditions.

Therefore:

```text
satellite pixels around tower
        ↓
footprint / observation operator
        ↓
area-weighted representation
        ↓
tower-scale supervision
```

is scientifically different from simply pairing a tower value with one center pixel or a uniformly averaged fixed window.

## 3. Input modalities

### Remote sensing
- optical reflectance / vegetation indices;
- thermal data;
- SIF;
- SAR/microwave;
- LiDAR/3D canopy structure;
- land cover and disturbance.

### Meteorology / environment
- radiation;
- air/soil temperature;
- humidity/VPD;
- precipitation;
- soil moisture;
- wind and turbulence;
- boundary-layer/stability variables.

### Static context
- biome/land cover;
- soil;
- topography;
- management where available.

## 4. Modeling hierarchy

```text
empirical / LUE / process model
→ classical ML upscaling
→ deep spatiotemporal models
→ hybrid process-ML
→ physics-constrained learning
→ footprint-aware observation operators
→ foundation-model embeddings + task-specific heads
```

No single level dominates every task. Data volume, scale, interpretability, process fidelity and transfer determine the appropriate design.

## 5. Where physics can enter

- carbon-balance constraints;
- light/water/temperature process priors;
- positivity/bounds where scientifically valid;
- phenology and radiation geometry;
- EC footprint as observation operator;
- process-model residual learning;
- carbon-water coupling;
- data assimilation.

## 6. Major scientific traps

### Target uncertainty
GPP/RECO partitioning uncertainty can be comparable to modeling differences.

### Scale mismatch
Tower footprints, satellite pixels and gridded products represent different spatial supports.

### Site leakage
Nearby dates from the same tower are highly dependent. Random half-hour/day splitting can overstate generalization.

### Optical observability
Strong predictive correlation with vegetation indices does not prove that reflectance is the causal controller of carbon exchange.

### Temporal mismatch
Fluxes vary sub-daily; clear-sky optical observations may be intermittent.

## 7. Validation hierarchy

Prefer reporting:

- site-blocked cross-validation;
- biome/climate-region transfer;
- temporal/event blocking;
- extreme heat/drought performance;
- tower-scale metrics;
- scale-aware independent validation where available;
- uncertainty and physical consistency.

## 8. Research frontier

High-value directions include:

- dynamic footprint-aware learning;
- 2D optical + 3D LiDAR + meteorology fusion;
- reconstruction of dense optical/biophysical time series;
- process-informed multimodal foundation models;
- causal/process diagnostics beyond feature importance;
- uncertainty propagation from measurements/partitioning to gridded flux products;
- cross-site and cross-biome OOD evaluation.

See the [Carbon-flux specialty track](../../06-case-studies/geoscience-remote-sensing/carbon-flux/index.md) and [papers by method](../../02-paper-library/by-method.md).
