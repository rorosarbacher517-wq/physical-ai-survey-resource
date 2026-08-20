# Multiscale and Multimodal Fusion

## 1. The core difficulty

Different modalities observe different physics at different supports.

Example:

```text
30 m optical every few days
+ coarse hourly meteorology
+ sparse tower flux every 30 min
+ LiDAR structure from occasional campaigns
```

Fusion is not just channel concatenation.

## 2. Early fusion

Resample/align modalities and concatenate before the encoder.

Pros: simple. Risks: forces a common grid/time, can hide support differences.

## 3. Late fusion

Encode each modality separately, then combine latent features.

Useful when modalities have different native structures.

## 4. Cross-attention

One modality queries another in latent/token space. Flexible for asynchronous observations and variable modality availability.

## 5. Hierarchical fusion

Fuse at multiple scales: local image features, regional context, temporal drivers and global/static context.

## 6. Missing modalities

Training should consider missing sensors/campaigns:

- modality dropout;
- masks;
- conditional encoders;
- robust fallback paths;
- uncertainty increase when evidence is absent.

## 7. Super-resolution/downscaling

A coarse variable can guide high-resolution prediction, but the fine pattern must be supported by additional predictors/priors. Upsampling alone creates no new physical information.

## 8. Fusion evaluation

Ablate each modality under identical splits and report where it helps:

- ecosystem/land-cover type;
- weather regime;
- season;
- spatial heterogeneity;
- OOD sites;
- missing-data conditions.
