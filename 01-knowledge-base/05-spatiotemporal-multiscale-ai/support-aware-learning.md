# Support-aware Learning

## 1. The support problem

Supervised learning assumes input and target describe compatible phenomena. In Earth systems, their spatial/temporal supports often differ.

```text
latent fine field F(x,t)
→ observation operator H_t
→ observed target y_t
```

Instead of forcing `F` to equal `y` at one arbitrary pixel, compare `H_t(F)` with `y_t`.

## 2. Weighted aggregation

Discrete operator:

`ŷ_t = Σ_i w_{i,t} F_{i,t}`

Dynamic `w` can represent a moving footprint; fixed weights can represent static sensor response.

## 3. Point-to-area mismatch

A station coordinate does not imply the measurement represents an infinitesimal point. Instrument exposure, atmospheric transport and aggregation determine support.

## 4. Area-to-area mismatch

Satellite products at different resolutions may represent different native point-spread functions and retrieval assumptions. Regridding to identical cell size does not guarantee identical support.

## 5. Time-support mismatch

Daily predictor, instantaneous overpass and half-hour target can be aligned only with explicit assumptions about persistence/interpolation.

## 6. Learning designs

- aggregate predictors to observation support before model;
- predict fine field then aggregate outputs with `H`;
- latent disaggregation with class fractions;
- operator-aware loss;
- probabilistic support uncertainty.

Each design answers a different scientific question.

## 7. Validation

Evaluate at the support actually observed, while separately labeling any finer-resolution output as model resolution rather than independently verified resolution.
