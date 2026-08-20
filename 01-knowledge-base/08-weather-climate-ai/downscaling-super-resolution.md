# Weather Downscaling and Super-resolution

## 1. Goal

Map coarse atmospheric/climate fields to finer spatial detail using high-resolution static/dynamic predictors and learned conditional structure.

```text
coarse field
+ topography / land / fine predictors
→ high-resolution conditional field
```

## 2. Statistical downscaling

Learn relationships between large-scale circulation and local observations/climate variables.

## 3. Dynamical downscaling

Run a regional numerical model nested inside coarse boundary conditions. More physically explicit but computationally expensive.

## 4. ML downscaling

CNN/U-Net/Transformer/generative models learn coarse-to-fine mappings.

## 5. Deterministic super-resolution

Produces one fine field. Pixel losses may smooth extremes.

## 6. Generative downscaling

Samples fine-scale fields conditioned on coarse context, allowing unresolved variability and uncertainty.

## 7. Conservation and consistency

Fine-grid output should remain consistent with coarse constraints where relevant.

Examples:

- area-mean precipitation consistency;
- mass/energy-related aggregation;
- large-scale atmospheric state.

## 8. Static features

Topography, coastlines, land cover and urban structure can explain systematic local patterns.

## 9. Evaluation

Check:

- mean bias;
- spatial spectra;
- extremes/tails;
- event structure;
- station-level skill;
- cross-region transfer;
- coarse-to-fine consistency;
- probabilistic calibration.

## 10. Key caution

A fine output grid does not guarantee fine-scale independent truth. Verification must match station/radar/high-resolution reference support.
