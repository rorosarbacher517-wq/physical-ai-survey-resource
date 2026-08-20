# Multisensor and Multimodal Fusion in Earth Observation

## 1. Why fusion is difficult

Different Earth-observation modalities do not provide redundant copies of the same information. They measure different physical responses at different spatial, temporal and vertical supports.

Examples:

- optical: surface/canopy spectral reflectance;
- SAR: microwave scattering sensitive to structure, roughness and dielectric properties;
- thermal: emitted radiance/temperature information;
- LiDAR: 3D geometry and vertical structure;
- SIF: weak fluorescence signal related to vegetation photosynthetic functioning;
- meteorology: environmental forcing rather than surface imagery.

## 2. Alignment problem

Before model fusion, align:

```text
coordinate reference
pixel/grid support
time stamp / compositing interval
sensor geometry
quality mask
units / normalization
```

A model cannot recover physical consistency that was destroyed by incorrect co-registration.

## 3. Common fusion levels

### Early fusion

Resample modalities to a shared grid/time and concatenate channels.

```text
X = concat(X_optical, X_sar, X_thermal, ...)
```

Simple, but assumes alignment and compatible support.

### Feature-level fusion

Separate encoders produce embeddings:

```text
z_opt = E_opt(X_opt)
z_sar = E_sar(X_sar)
z_3d  = E_3d(X_3d)
→ fusion(z_opt,z_sar,z_3d)
```

This allows modality-specific processing before interaction.

### Cross-attention

One modality queries another:

```text
Q = z_target
K,V = z_context
→ cross-attention
```

Useful when token counts/resolutions differ.

### Late fusion

Independent predictions are combined by stacking, weighting or probabilistic aggregation.

## 4. Missing modalities

Real Earth data are incomplete. Training should distinguish:

- cloud-induced missing optical data;
- unavailable sensor coverage;
- irregular revisit times;
- missing 3D acquisitions;
- station data gaps.

Approaches include modality dropout, masked modeling, mixture-of-experts routing and conditional encoders.

## 5. Shape example: 2D + 3D + meteorology

```text
optical patch: [B,T,C,H,W]
LiDAR points:  [B,N,C3d]
meteorology:   [B,T,M]
```

A possible system:

```text
optical → 2D encoder → [B,T,P,D]
LiDAR   → point/voxel encoder → [B,P3,D]
meteo   → MLP/temporal encoder → [B,T,D]
        → spatial/temporal fusion
        → prediction head
```

The spatial correspondence between `P` and `P3` must be defined explicitly.

## 6. Physics-aware fusion

Useful physical structure includes:

- sensor-specific observation operators;
- radiometric/geometry metadata;
- energy/water/carbon constraints;
- known vertical relationships;
- temporal causality of environmental forcing;
- footprint/support weighting for field observations.

## 7. Training objectives

Possible combinations:

```text
L = L_task
  + λ_align L_cross_modal
  + λ_recon L_masked_reconstruction
  + λ_phys L_physical_consistency
```

Alignment loss should not force physically different modalities to become identical representations.

## 8. Evaluation

Report:

- single-modality baselines;
- fusion gain with identical splits;
- missing-modality robustness;
- cross-region/time transfer;
- sensor-specific ablations;
- calibration/uncertainty;
- compute and storage cost.

## 9. Failure modes

- fusion gain caused by leakage from one modality;
- resampling artifacts mistaken for information;
- temporal mismatch between acquisitions;
- one modality dominating due to scale/normalization;
- evaluating only scenes where every sensor is available;
- using static structural data as if it changed at every time step.

## 10. Carbon connection

Continue to [Multimodal carbon AI](../07-carbon-cycle-ai/multimodal-carbon-ai.md), where 2D EO, 3D structure, meteorology and EC observations are connected through support-aware learning.
