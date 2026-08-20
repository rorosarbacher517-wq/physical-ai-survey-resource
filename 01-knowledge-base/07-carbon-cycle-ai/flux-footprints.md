# Flux Footprints

## 1. Definition

A flux footprint describes how upwind surface locations contribute to an eddy-covariance measurement.

It is a spatial weighting function, not simply a circular buffer around the tower.

## 2. Why it changes

Footprints vary with conditions such as:

- wind direction;
- wind speed/turbulence;
- friction velocity;
- atmospheric stability;
- measurement height;
- roughness/displacement;
- boundary-layer state.

## 3. Continuous-to-grid mapping

A footprint model may produce a continuous or fine-grid contribution field. To combine it with 30 m imagery:

```text
footprint surface
→ rotate/georeference
→ sample/integrate to satellite grid
→ apply valid-pixel mask
→ renormalize weights
→ aggregate field/predictions
```

## 4. Output-side observation operator

If the model predicts pixel flux `F_i,t`:

`Y_hat_t = Σ_i w_i,t F_i,t`

This preserves pixel-level latent predictions while matching supervision to the tower support.

## 5. Input-side aggregation

An alternative is to footprint-average satellite predictors before model fitting.

This directly creates tower-support predictors but removes fine-scale spatial information before the model and can interact poorly with nonlinear indices.

## 6. Dynamic versus uniform weights

Uniform aggregation assumes all valid pixels contribute equally. Dynamic footprint aggregation uses contribution-specific weights.

A paired comparison can isolate this choice if inputs, architecture, loss, training samples and splits remain identical.

## 7. Missing pixels

Cloud/quality masks change the set of usable pixels. Weights must be handled explicitly so missing pixels do not silently bias totals.

## 8. Uncertainty

Footprint models are approximations. Wind/turbulence inputs, canopy assumptions and model validity affect the source-area estimate.

## 9. Primary anchor

Kljun et al. (2015) provides a widely used parameterization for flux-footprint prediction: https://doi.org/10.5194/gmd-8-3695-2015
