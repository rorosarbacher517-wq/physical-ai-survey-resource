# Footprint-aware AI for Tower-scale Flux Learning

## 1. The mismatch

A fixed satellite window is static. An EC footprint changes every averaging period.

If the landscape is heterogeneous, the satellite pixels with the strongest flux contribution can differ from the fixed-window mean.

## 2. Four footprint roles

### Predictor aggregation
Use weights to aggregate satellite predictors before training.

### Prediction aggregation / observation operator
Predict a spatial field, then aggregate outputs to tower support.

### Flux disaggregation
Use changing footprints and class fractions to infer latent class-specific fluxes.

### Representativeness analysis
Use footprints to quantify which land-cover/remote-sensing conditions the tower samples.

A separate role is using footprint geometry as a model feature; that is not equivalent to applying the weights as an operator.

## 3. Operator placement

```text
A) pixels → footprint-weight predictors → tower model

B) pixels → pixel model → footprint-weight outputs → tower loss
```

B preserves spatially explicit latent predictions and puts the observation mapping between model field and tower supervision.

## 4. Nonlinear predictor issue

For nonlinear index `g(x)`:

`Σ w_i g(x_i) != g(Σ w_i x_i)` in general.

Therefore weighting raw bands versus derived indices can produce different physical/statistical meanings.

## 5. Where gains should appear

Footprint-aware aggregation has limited effect over homogeneous surfaces because different weights see similar conditions. It has greater potential when:

- spatial flux-relevant contrast is strong;
- footprint location/shape changes;
- environmental forcing makes patch responses diverge.

## 6. Diagnostic variables

Potential diagnostics:

- spatial NDVI/reflectance variability;
- edge/land-cover heterogeneity;
- roughness/structure variability;
- difference between footprint-weighted and uniform vegetation state;
- wind/stability/footprint variability.

## 7. Paired evaluation

Keep all else identical and compute paired errors:

`Δ|AE| = |AE_uniform| - |AE_footprint|`

Positive values indicate footprint-aware improvement under that convention.

## 8. Generalization

Use site-blocked CV and stratify by ecosystem, season, daytime, heterogeneity and climate regime.
