# Weather-model Evaluation

## 1. Match the verification setup

Before comparing models, match:

- variable;
- vertical level;
- lead time;
- initialization time;
- grid/resolution;
- verification dataset/analysis;
- interpolation/regridding;
- geographic weighting.

## 2. Deterministic metrics

### RMSE
Measures average magnitude of error.

### MAE
Less sensitive to large outliers than RMSE.

### Anomaly correlation
Measures pattern skill relative to climatological anomaly definition.

## 3. Area weighting

Latitude-longitude cells have different physical areas. Global scores often require cosine-latitude or exact-area weighting.

## 4. Lead-time curves

Weather error grows with lead time. Report skill as a function of forecast horizon instead of one pooled number.

## 5. Probabilistic metrics

- CRPS;
- Brier score;
- reliability;
- rank histogram;
- spread-skill.

## 6. Extreme-event evaluation

Global average RMSE can hide hazard skill. Evaluate:

- tropical cyclones;
- heat/cold extremes;
- heavy precipitation;
- severe wind;
- atmospheric rivers or other event classes when relevant.

## 7. Physical diagnostics

- global budgets;
- balance relationships;
- kinetic-energy/spectral distribution;
- conservation drift;
- long-rollout stability.

## 8. Fair baseline

Compare with the appropriate operational/reanalysis baseline using the same verification protocol. Avoid mixing different initial conditions or post-processing.

## 9. Compute and latency

Operational value also depends on forecast generation time, accelerator requirements, ensemble cost and data-assimilation latency.
