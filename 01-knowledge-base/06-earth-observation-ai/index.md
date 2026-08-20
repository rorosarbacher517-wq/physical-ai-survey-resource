# 06 · Earth Observation / Remote Sensing AI

Remote-sensing AI should start from **what the sensor measures**, then move through preprocessing, representation, fusion and model architecture.

## Knowledge path

```text
Observation physics
→ sensor modality
→ calibration / QC / retrieval
→ spatial-spectral-temporal representation
→ multisensor fusion
→ task model / foundation model
→ reconstruction/downscaling if needed
→ scale-aware geospatial validation
```

## 1. Observation chain

```text
surface / atmosphere state
→ electromagnetic interaction
→ sensor response + geometry
→ radiance / backscatter / waveform
→ calibration / correction / retrieval
→ ML-ready representation
→ geophysical/ecological target
```

Start with [Radiative transfer and observation physics](radiative-transfer-observation-physics.md).

## 2. Modalities

- [Optical and hyperspectral](optical-hyperspectral.md): radiance, reflectance, spectral response, atmosphere, BRDF.
- [SAR and microwave](sar-microwave.md): scattering, polarization, geometry, moisture/structure sensitivity.
- [LiDAR and 3D](lidar-3d.md): ranging, point clouds, canopy/terrain structure.
- [Thermal and SIF](thermal-sif.md): emitted radiation, temperature/emissivity and fluorescence observations.

These modalities measure different physical responses; they are not interchangeable image channels.

## 3. Data quality and preprocessing

See [EO preprocessing and quality control](eo-preprocessing-quality.md).

For every dataset record track:

1. native sensor resolution;
2. projection/grid;
3. resampling;
4. temporal acquisition/composite interval;
5. cloud/quality mask;
6. spectral response;
7. label/support resolution;
8. validation scale.

## 4. Temporal learning

Satellite sequences are often irregular because of orbit, cloud and sensor availability.

See [Remote-sensing time-series learning](remote-sensing-time-series.md).

Typical representations include:

```text
image sequence: [B,T,C,H,W]
patch tokens:   [B,T,P,D]
quality mask:   [B,T,H,W]
metadata:       [B,T,G]
```

## 5. Multisensor / multimodal fusion

See [Multisensor fusion](multisensor-fusion.md).

Important fusion questions:

- are modalities aligned in space/time/support?
- early, feature, cross-attention or late fusion?
- how are missing modalities handled?
- does one sensor dominate because of normalization/data density?
- are modality gains tested with paired ablations?

## 6. Core AI tasks and architectures

See [EO models and tasks](eo-models-tasks.md).

Tasks include classification, segmentation, detection, change detection, retrieval/regression, forecasting, reconstruction, downscaling and cross-modal generation.

Architectures include CNN/U-Net, ViT/Swin-style encoders, temporal models, GNNs, self-supervised encoders and generative models.

## 7. Reconstruction and resolution enhancement

See [Super-resolution, downscaling and reconstruction](super-resolution-reconstruction.md).

Always distinguish output pixel spacing from independently validated information scale.

## 8. Foundation models

See [EO foundation models](eo-foundation-models.md) and [Earth/scientific foundation models](../09-earth-foundation-models/index.md).

Key design axes are modality, spectral flexibility, time, geolocation, spatial scale, pretraining objective and transfer protocol.

## 9. Physics + AI opportunities

- radiative-transfer-aware learning;
- spectral-response-aware encoders;
- cloud/atmospheric uncertainty;
- BRDF/illumination normalization;
- SAR scattering priors;
- geometry-aware LiDAR fusion;
- support-aware observation operators;
- physically constrained temporal reconstruction.

## 10. Validation

See [Geospatial validation and OOD evaluation](geospatial-validation.md).

A 10–30 m prediction is not automatically validated at 10–30 m. Explicitly record the support of ground truth and how it maps to model output.

## 11. Priority downstream connections

```text
EO sensing / representation
├→ terrestrial carbon-cycle AI
├→ weather/climate observation and downscaling
├→ hydrology/agriculture/disaster mapping
└→ Earth foundation models
```

Continue to [Carbon-cycle AI](../07-carbon-cycle-ai/index.md) and the [EO specialty track](../../06-case-studies/geoscience-remote-sensing/earth-observation/index.md).
