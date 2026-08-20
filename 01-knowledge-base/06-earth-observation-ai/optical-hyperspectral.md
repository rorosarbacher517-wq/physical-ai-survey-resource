# Optical and Hyperspectral Earth Observation

## 1. Measurement chain

Optical remote sensing records reflected solar radiation after interaction with the atmosphere and surface.

```text
solar irradiance
→ atmosphere
→ surface/canopy interaction
→ atmosphere
→ sensor spectral response
→ digital number / radiance
→ calibrated reflectance product
```

A reflectance band is therefore an observation of electromagnetic response, not a direct measurement of biomass, GPP or soil moisture.

## 2. Radiance and reflectance

### Radiance
Energy received by the sensor per area, solid angle and wavelength interval.

### Reflectance
A normalized measure of reflected radiation. Surface-reflectance products attempt to remove major atmospheric effects, but residual uncertainty remains.

## 3. Spectral behavior

Vegetation signals commonly involve:

- visible absorption by pigments;
- strong near-infrared scattering by leaf/canopy structure;
- shortwave-infrared sensitivity to water and biochemical/structural properties.

Hyperspectral sensors sample many narrow bands, enabling richer spectral signatures but increasing dimensionality, calibration demands and data volume.

## 4. Spectral indices

Examples include NDVI and NIRv-like constructs.

Important distinction:

```text
index = nonlinear function of bands
```

Averaging an index is generally not equivalent to computing the index from averaged bands. This matters for footprint-weighted aggregation and mixed pixels.

## 5. Atmosphere and geometry

Optical observations vary with:

- aerosols/water vapor;
- cloud and cloud shadow;
- solar zenith/azimuth;
- view geometry;
- BRDF;
- topographic illumination;
- adjacency effects.

AI can learn some systematic effects, but preprocessing and geometry metadata should remain explicit.

## 6. Spatial resolution

A nominal 10 m or 30 m grid is not identical to an independent ground truth at that scale. Sensor point-spread function, resampling and geolocation contribute to effective support.

## 7. Temporal sampling

Cloud-free optical observations are intermittent. A daily ecosystem target may need temporal interpolation, multi-sensor harmonization or latent state reconstruction.

## 8. AI representations

Possible input shape:

```text
single image:      [B,C,H,W]
time series:       [B,T,C,H,W]
patch tokens:      [B,T,N,D]
hyperspectral cube:[B,Bands,H,W]
```

Models should preserve band semantics and acquisition time rather than blindly treating spectral bands as RGB channels.

## 9. Physical-AI opportunities

- radiative-transfer-informed features/losses;
- BRDF/illumination-aware normalization;
- spectral-response-aware transfer between sensors;
- cloud uncertainty;
- phenology-aware temporal modeling;
- support-aware aggregation for field/tower observations.
