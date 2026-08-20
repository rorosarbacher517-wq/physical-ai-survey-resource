# Tower-to-grid Carbon-flux Upscaling

## 1. The task

Flux towers provide dense temporal observations at sparse locations. Upscaling learns relationships between tower observations and spatially continuous predictors, then applies them across grids/regions.

## 2. Core support problem

The tower target and predictor grid do not automatically represent the same area.

```text
gridded predictors
→ support/footprint mapping around tower
→ tower training target
```

During regional inference, the desired output may instead be a pixel/grid-cell flux estimate.

## 3. Two modeling designs

### Tower-representation model

```text
pixels → aggregate predictors → tower model → tower flux
```

Good for tower prediction but does not inherently produce a fine spatial latent field.

### Spatial-field model with tower observation operator

```text
pixels → pixel/field predictions
→ footprint-weight aggregation
→ tower loss
```

This preserves spatially explicit latent predictions while supervising them through tower support.

## 4. Training tensor example

```text
EO patch:      [B,T,C,H,W]
meteo:         [B,T,M]
footprint:     [B,T,H,W]
tower target:  [B,T,F]
```

A field model may output:

```text
flux field: [B,T,F,H,W]
```

Then apply normalized footprint weights to obtain `[B,T,F]` tower predictions.

## 5. Regional inference

For gridded prediction define:

- required meteorology;
- EO observation/reconstruction schedule;
- static context;
- output cadence;
- uncertainty;
- domain mask;
- OOD diagnostics.

Regional prediction should not rely on tower-only variables unavailable away from towers unless a replacement is defined.

## 6. Validation hierarchy

### Tower held-out validation

Tests transfer to unseen sites.

### Regional/biome blocking

Tests stronger spatial extrapolation.

### Independent field/grid validation

When available, checks spatial predictions beyond the tower observation support.

A fine output pixel size should not be described as independently validated at that scale without suitable observations.

## 7. Coverage bias

Flux towers are not uniformly distributed across climate, land cover and management regimes. Training data density can shape apparent regional skill.

Track:

- biome coverage;
- climate coverage;
- geographic density;
- management/disturbance representation;
- extreme-event representation.

## 8. Uncertainty propagation

Regional uncertainty can include:

```text
measurement/partitioning
+ predictor/retrieval
+ footprint/support
+ model parameter/ensemble
+ domain shift
```

## 9. Failure modes

- random tower-time splitting;
- using site identity shortcuts;
- claiming pixel-scale validation from tower-scale supervision alone;
- training with unavailable regional predictors;
- ignoring representativeness gaps;
- confusing resampling with added information.

## 10. Related pages

See [Footprint-aware AI](footprint-aware-ai.md), [geospatial validation](../06-earth-observation-ai/geospatial-validation.md) and [validation/uncertainty](validation-uncertainty.md).
