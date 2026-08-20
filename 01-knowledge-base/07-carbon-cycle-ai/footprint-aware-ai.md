# Footprint-aware AI for Tower-scale Flux Learning

## 1. One-sentence definition

Footprint-aware learning explicitly maps spatial predictors or spatial flux predictions to the dynamic source area represented by each eddy-covariance observation.

## 2. Physical problem

A fixed satellite window is static, while the EC source area changes with wind direction, turbulence, stability, measurement geometry and surface characteristics.

Over heterogeneous landscapes, a uniform window can weight pixels differently from the actual tower measurement.

Primary footprint-model anchor: Kljun et al. (2015), https://doi.org/10.5194/gmd-8-3695-2015

## 3. Inputs and shapes

A typical site-day representation may be:

```text
EO pixels:      X  [B,T,C,H,W]
meteorology:    M  [B,T,P]
footprints:     Wf [B,T,H,W]
tower targets:  Y  [B,T,F]
```

where `T` can represent half-hourly steps and `F` can contain NEE/GPP/RECO.

Footprint weights should be aligned to the same spatial grid/mask used by the predictions and normalized over valid contributing pixels.

## 4. Footprint roles

### Input-side predictor aggregation

```text
X_tower = Σ_i w_i X_i
→ tower-scale model
```

### Output-side aggregation / observation operator

```text
pixels → model → ŷ_i
ŷ_tower = Σ_i w_i ŷ_i
```

### Flux disaggregation

Changing footprints plus class fractions/latent classes are used to infer component/source-class fluxes.

### Representativeness analysis

Footprints quantify which land-cover/remote-sensing conditions are actually sampled.

### Footprint as model feature

Geometry/source-area descriptors enter the network as predictors. This is not equivalent to using the footprint as an observation operator.

## 5. Operator placement

```text
A) pixels
→ footprint-weight predictors
→ tower model
→ tower prediction

B) pixels
→ spatial/pixel model
→ predicted flux field
→ footprint observation operator
→ tower prediction
→ tower loss
```

Design B preserves a spatial latent prediction and separates **process model** from **measurement mapping**.

## 6. Nonlinear predictor issue

For nonlinear transformation `g`:

```text
Σ_i w_i g(x_i) ≠ g(Σ_i w_i x_i)
```

in general.

Therefore weighting raw spectral bands, vegetation indices or learned embeddings at different stages changes the modeling meaning.

## 7. Training objective

For tower observations `y_t` and footprint-aggregated predictions `ŷ_t`:

```text
L_data = mean_t mask_t · ||ŷ_t - y_t||²
```

A multi-task model can add process-consistency terms, but all ablation variants should keep data, splits, architecture and optimization fixed when isolating the footprint effect.

## 8. Inference

Two modes must be distinguished:

### Tower inference
Use the dynamic footprint and compare directly with EC support.

### Spatial-field inference
Use the learned pixel/field predictor on a regional grid without applying tower footprints; this requires separate spatial validation claims.

## 9. When gains are plausible

Footprint-aware aggregation has limited effect when spatially relevant conditions are homogeneous. Its potential increases when:

- flux-relevant spatial contrast is strong;
- source-area position/shape varies;
- environmental forcing causes neighboring patches to respond differently.

## 10. Diagnostics

Useful diagnostics include:

- spatial NDVI/reflectance variability;
- land-cover/edge heterogeneity;
- roughness/3D structure variation;
- difference between footprint-weighted and uniform vegetation state;
- footprint centroid/extent/orientation variability;
- wind/stability/turbulence regime.

## 11. Paired evaluation

With identical held-out samples:

```text
Δ|AE| = |AE_uniform| - |AE_footprint|
```

Positive values indicate lower absolute error for the footprint-aware variant under this convention.

Report site-blocked CV and stratify by ecosystem, season, time of day, heterogeneity and climate regime.

## 12. Failure modes

- footprint raster and EO grid misalignment;
- weights not renormalized after cloud/quality masking;
- footprint variables leaking target construction;
- comparing variants with different data/splits/backbones;
- assuming a spatial latent field is independently validated because tower aggregation matches observations;
- interpreting footprint gain as a universal property rather than a context-dependent effect.

## 13. Connections

Prerequisites: [Observation operators](../02-physics-ai-core/observation-operators.md) and [support-aware learning](../05-spatiotemporal-multiscale-ai/support-aware-learning.md).

Continue to [tower-to-grid upscaling](tower-to-grid-upscaling.md), [multimodal carbon AI](multimodal-carbon-ai.md) and [process-constrained carbon AI](process-constrained-carbon-ai.md).
