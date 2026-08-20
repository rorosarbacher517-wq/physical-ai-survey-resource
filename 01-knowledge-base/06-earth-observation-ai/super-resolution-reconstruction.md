# EO Super-resolution, Downscaling and Reconstruction

## 1. Separate three problems

### Spatial super-resolution

Infer a finer grid from coarse observations.

### Statistical/physical downscaling

Estimate fine-scale variables conditioned on coarse fields plus high-resolution covariates.

### Temporal reconstruction

Fill or infer missing times using neighboring observations and auxiliary data.

These tasks can use similar neural architectures but have different scientific meanings.

## 2. Observation-limit principle

A finer output grid does not create new independent observations. The product's nominal pixel size must be separated from its validated information scale.

## 3. Typical mapping

```text
coarse dynamic field: [B,T,C,Hc,Wc]
high-res covariates:  [B,T?,K,Hf,Wf]
→ fusion / upsampling model
→ fine prediction:    [B,T,Y,Hf,Wf]
```

## 4. Architectures

- CNN/U-Net upsampling;
- residual super-resolution networks;
- Transformer-based image restoration;
- implicit neural representations;
- diffusion/score reconstruction;
- physics-guided statistical downscaling.

## 5. Training targets

Targets may come from:

- higher-resolution sensors;
- simulated degradation pairs;
- station/field observations;
- physical-model output;
- self-supervised masking.

Synthetic degradation should approximate the real sensor point-spread/sampling process when possible.

## 6. Multi-resolution fusion

A useful Earth-science case is combining high-frequency coarse data with sparse high-resolution observations:

```text
coarse/high-frequency sequence
+ fine/sparse observations
+ static fine-scale context
→ reconstructed fine/high-frequency field
```

This is attractive for cloud-prone optical time series, soil moisture, temperature and ecosystem monitoring.

## 7. Physical constraints

Depending on the variable:

- preserve spatial averages/integrals;
- conserve mass/water/energy where appropriate;
- enforce nonnegative quantities where definitions require it;
- maintain temporal consistency;
- respect land/water masks and topography.

## 8. Evaluation

Report:

- fine-grid pixel metrics;
- aggregated consistency back to coarse observations;
- spectral/texture statistics;
- event/extreme preservation;
- independent field/station validation;
- OOD region/time transfer.

## 9. Failure modes

- visually plausible texture without physical information;
- leakage from a fine-resolution target available near prediction time;
- comparing against resampled labels rather than independent observations;
- smoothing extremes;
- hallucinating boundaries that cannot be supported by input sensors.

## 10. Carbon connection

For carbon-flux applications, reconstructed EO time series should be treated as uncertain predictors. They do not remove the need to match EC measurement support or validate flux estimates independently.
