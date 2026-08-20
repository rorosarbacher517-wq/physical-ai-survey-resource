# Earth-observation Preprocessing and Quality Control

## 1. Data-quality pipeline

```text
raw/product access
→ calibration/product-level checks
→ QA masks
→ cloud/shadow/snow/water handling
→ atmospheric/terrain correction as applicable
→ reprojection/resampling
→ spatial crop/tiling
→ temporal pairing/compositing
→ missing-data mask
→ sample construction
```

## 2. QA flags are data

Do not convert all invalid observations to zero without a mask. Zero may be a physically meaningful value.

Track:

- cloud;
- cloud shadow;
- snow/ice;
- saturation;
- fill values;
- water if excluded by task;
- sensor-specific artifacts.

## 3. Reprojection

A CRS change involves resampling. The correct method depends on variable type:

- continuous reflectance/temperature;
- categorical land cover;
- extensive totals;
- probability/fraction.

## 4. Multi-sensor harmonization

Landsat/Sentinel-style combined series require attention to:

- spectral-response differences;
- spatial resolution;
- acquisition geometry;
- product processing version;
- duplicate/near-synchronous acquisitions.

## 5. Temporal compositing

Composites reduce clouds/noise but alter temporal support. A monthly median is not an instantaneous measurement.

## 6. Normalization

Options:

- global train-set mean/std;
- per-band robust scaling;
- physically defined transforms;
- log transform for skewed positive variables.

Compute statistics from training data only to avoid leakage.

## 7. Patch quality

For patch-based learning record:

- valid-pixel percentage;
- center validity if required;
- mask propagation;
- spatial extent;
- whether all time steps share the same spatial mask.

## 8. Data lineage

Every sample should be traceable to sensor/product/date/tile/version and preprocessing code. This is essential when EO products are reprocessed over time.
