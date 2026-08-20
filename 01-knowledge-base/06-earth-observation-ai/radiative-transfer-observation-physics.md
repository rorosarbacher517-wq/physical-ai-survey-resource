# Radiative Transfer and Observation Physics for EO AI

## 1. Core idea

Remote-sensing AI learns from sensor observations produced by radiation interacting with the atmosphere and surface. The model therefore sees an observation of the physical state, not the state itself.

## 2. Observation chain

```text
source radiation
→ atmosphere
→ surface/canopy interaction
→ atmosphere
→ sensor spectral/spatial response
→ digital measurement
→ calibration/correction
→ ML tensor
```

For passive optical sensing the source is commonly sunlight; thermal sensing includes emitted radiation. Active systems such as radar and LiDAR provide their own transmitted energy.

## 3. Radiance versus reflectance

Radiance is sensor-observed radiant energy in a viewing geometry. Surface reflectance is a retrieved property intended to reduce illumination/atmospheric effects.

A generic retrieval can be viewed as an inverse problem:

```text
sensor radiance y = H(surface, atmosphere, geometry, sensor) + ε
→ estimate surface quantity x
```

The retrieval is not exact; uncertainty propagates into downstream AI.

## 4. BRDF and geometry

Reflectance changes with solar zenith, view zenith and relative azimuth because real surfaces are anisotropic.

Implications for AI:

- repeated observations can change even when the surface state is similar;
- angular metadata can be useful input;
- cross-sensor harmonization should consider geometry, not only band names;
- temporal models can learn geometry artifacts unless explicitly controlled.

## 5. Spectral response functions

Two sensors labeled with similar bands can integrate different wavelength ranges.

A band measurement can be conceptualized as:

```text
band_value ≈ ∫ spectral_signal(λ) · response(λ) dλ
```

This matters for cross-sensor transfer, synthetic-band generation and foundation models that accept variable spectral channels.

## 6. Atmospheric effects

Scattering, absorption, aerosols, water vapor and clouds alter the signal. Atmospheric correction is itself a physical inversion/retrieval step.

Useful distinction:

```text
TOA radiance/reflectance
≠ surface reflectance
≠ vegetation biochemical/process variable
```

## 7. Observation operator view

Represent the whole sensing/retrieval process as `H`:

```text
physical state x
→ H_sensor(x, atmosphere, geometry)
→ y
```

A physics-aware ML system may:

- learn the inverse mapping `y → x`;
- emulate parts of `H`;
- differentiate through an approximate `H`;
- use `H` to generate synthetic observations;
- evaluate predictions in observation space.

## 8. Tensor view

A multispectral sequence might be:

```text
X:       [B,T,C,H,W]
angles:  [B,T,G]
quality: [B,T,H,W]
time:     [B,T]
```

The mask is part of the observation state and should not be silently discarded.

## 9. Failure modes

- training on cloud-contaminated pixels;
- treating surface reflectance as direct carbon flux;
- ignoring viewing/illumination effects in time-series learning;
- assuming equal spectral bands across sensors;
- interpreting retrieval uncertainty as ecological variability;
- evaluating a derived high-resolution field as if it had independent ground truth at the same support.

## 10. Prerequisites and next links

Prerequisite: [Observation operators](../02-physics-ai-core/observation-operators.md).

Continue to [Optical and hyperspectral sensing](optical-hyperspectral.md), [SAR and microwave](sar-microwave.md), [Thermal and SIF](thermal-sif.md) and [multisensor fusion](multisensor-fusion.md).
