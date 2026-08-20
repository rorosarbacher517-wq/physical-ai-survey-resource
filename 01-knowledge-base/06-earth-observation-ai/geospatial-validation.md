# Geospatial Validation and OOD Evaluation

## 1. Why random splitting often fails

Nearby pixels, dates and sites share climate, land cover, sensor conditions and spatial context. Random splits can place highly correlated samples in both train and test sets.

## 2. Split axes

Choose the axis that matches the scientific claim:

- held-out site;
- held-out region;
- held-out biome/ecoregion;
- held-out year/time block;
- held-out event/disturbance;
- held-out sensor;
- held-out climate regime.

## 3. Interpolation versus extrapolation

A model can perform strongly when filling gaps inside the training domain while failing at spatial or climate extrapolation. State explicitly which regime the evaluation represents.

## 4. Spatial support

Validation data may represent:

- a point;
- plot;
- footprint;
- pixel;
- polygon;
- coarse grid cell.

Do not compare values without defining how supports are mapped.

## 5. Hierarchical metrics

Useful reporting levels:

```text
sample/pixel
→ site/scene
→ biome/region
→ global aggregate
```

A global metric can hide severe regional bias.

## 6. Paired comparisons

When testing one modeling change, keep data/splits/training fixed and compare paired predictions on identical held-out samples.

## 7. Uncertainty and calibration

For probabilistic outputs, evaluate coverage/calibration by region and regime, not only globally.

## 8. Error stratification

Stratify by:

- cloud/data quality;
- land-cover heterogeneity;
- observation density;
- topography;
- season;
- climate/extreme state;
- sensor.

## 9. Leakage checklist

Check whether the test target is indirectly accessible through:

- neighboring labels;
- temporal smoothing using future values;
- global normalization fitted on all data;
- duplicate/overlapping tiles;
- pretraining data containing evaluation labels or imagery;
- site identity encoded through static variables.

## 10. Related pages

See [Evaluation and benchmarking](../11-data-hpc-evaluation/evaluation-benchmarking.md), [support-aware learning](../05-spatiotemporal-multiscale-ai/support-aware-learning.md) and [carbon validation](../07-carbon-cycle-ai/validation-uncertainty.md).
