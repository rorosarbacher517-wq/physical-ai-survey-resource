# Multimodal Earth Representations

## 1. Goal

A multimodal Earth representation should encode complementary observations and physical context while preserving modality identity, time, location, scale and uncertainty.

It should not simply concatenate every available channel onto one image tensor.

## 2. Modalities

Possible sources include:

- optical/hyperspectral;
- SAR/microwave;
- thermal;
- LiDAR/3D;
- SIF;
- weather/reanalysis fields;
- topography/soil/land cover;
- station/tower observations;
- text/metadata where scientifically useful.

## 3. Representation choices

### Shared-grid tokens

```text
X: [B,T,C,H,W]
→ patchify
→ [B,T,P,D]
```

Works when modalities can be meaningfully aligned to a common grid.

### Modality-specific encoders

```text
EO optical → z_opt
SAR        → z_sar
3D         → z_3d
weather    → z_met
→ shared latent space / cross-attention
```

This preserves sensor-specific structure before fusion.

### Query-based representation

A decoder/query requests information for a location, time or variable from a shared latent state.

Useful when downstream tasks have different output supports.

## 4. Metadata embeddings

Earth tokens often need more than position in an image:

- latitude/longitude or spherical coordinates;
- acquisition time/day-of-year;
- sensor/modality identity;
- spectral wavelength/band metadata;
- vertical level;
- spatial resolution/support;
- quality/missingness.

## 5. Pretraining objectives

- masked reconstruction;
- cross-modal prediction;
- temporal prediction;
- contrastive alignment;
- cross-modal generation;
- variable-conditioned prediction;
- multi-scale reconstruction.

A cross-modal objective should preserve physical differences rather than forcing every modality into identical features.

## 6. Missing modalities

Real coverage is incomplete. Models should define behavior when a modality is absent through masking, modality dropout, conditional routing or sparse experts.

## 7. Process-sensitive transfer

Semantic mapping is not enough to establish scientific usefulness. Evaluate transfer to:

- carbon/water/energy fluxes;
- soil moisture/hydrology;
- weather/extremes;
- vegetation function;
- disturbance/recovery;
- geophysical retrieval.

## 8. Observation physics

A multimodal model should know which variables are observations, retrieved products, model/reanalysis fields or latent targets. See [Observation operators](../02-physics-ai-core/observation-operators.md) and [multisensor EO fusion](../06-earth-observation-ai/multisensor-fusion.md).

## 9. Failure modes

- location/season shortcut dominates the learned representation;
- resampling erases modality support differences;
- one dense modality overwhelms sparse modalities;
- missing-modality behavior is never tested;
- pretraining data overlap with benchmark regions/times;
- representation quality is judged only on land-cover classification.
