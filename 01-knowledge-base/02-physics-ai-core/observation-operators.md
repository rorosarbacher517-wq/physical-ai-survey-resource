# Observation Operators

## 1. Core idea

A sensor rarely observes the model state directly.

```text
state x
→ observation operator H
→ expected observation H(x)
→ measurement y = H(x) + ε
```

`H` maps from state space to observation space.

## 2. Operator types

### Spatial sampling
Point/station sampling, area averaging, pixel response and flux-footprint weighting.

### Radiative transfer
State variables produce radiance/reflectance/brightness temperature through electromagnetic interactions.

### Retrieval operator
A measurement may be inverted into a derived geophysical variable before ML sees it.

### Temporal aggregation
Instantaneous, interval average, accumulation or composite.

## 3. Why it matters for AI

Without support matching, a model may be supervised with predictors that do not describe the same physical area/time as the target.

This creates representation error even when the neural network is optimized correctly.

## 4. Discrete form

A common area-weighted operator:

```text
ŷ = Σ_i w_i f_i
Σ_i w_i = 1
```

where `f_i` are pixel/field predictions and `w_i` represent contribution weights.

Uniform averaging is a special case. Dynamic weights can encode sensor footprint or physical source-area contribution.

## 5. Differentiability

If `H` is differentiable, supervision can be applied after observation mapping while the latent state/field model remains spatially explicit.

This pattern is useful when labels exist only at a coarser or differently supported scale.

## 6. Uncertainty

Observation error can come from:

- instrument noise;
- retrieval assumptions;
- representativeness/support mismatch;
- geolocation;
- missing-data/QC;
- uncertain operator parameters.

## 7. Domain examples

- EC footprint weighting for carbon flux;
- satellite point-spread/radiative transfer;
- weather station versus model-grid interpolation;
- radar observation operators in DA;
- line-of-sight measurements in tomography.

## 8. Design questions

For every target ask:

1. What physical quantity is measured?
2. What state does the model predict?
3. What maps state to measurement?
4. Is the mapping linear/nonlinear?
5. Is it fixed/dynamic?
6. Is it differentiable?
7. How is operator uncertainty represented?
