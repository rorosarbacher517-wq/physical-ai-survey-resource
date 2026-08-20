# 06 · Earth Observation / Remote Sensing AI

Remote-sensing AI should start from **what the sensor measures**, then move to model architecture.

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

This prevents the common mistake of treating reflectance, SIF, SAR or thermal observations as direct measurements of downstream ecological processes.

## 2. Modalities and physical meaning

### Optical multispectral / hyperspectral
Key ideas: radiance, reflectance, absorption/scattering, atmospheric correction, BRDF, cloud/shadow, spectral response, sun-view geometry.

### Thermal infrared
Brightness/surface temperature, emissivity and atmospheric effects.

### SAR / microwave
Backscatter depends on wavelength, polarization, geometry, roughness, dielectric properties and structure. Microwave observations can provide information under clouds but are not “optical images with another channel”.

### LiDAR
3D ranging/waveform geometry provides structure such as canopy height/profile and terrain.

### Solar-induced chlorophyll fluorescence
A weak radiative signal associated with photosynthetic processes; interpretation still depends on canopy/radiative transfer and scale.

## 3. Core AI tasks

- classification;
- semantic/instance segmentation;
- object detection;
- change detection;
- regression/retrieval;
- spatial-temporal forecasting;
- gap filling/reconstruction;
- super-resolution/downscaling;
- cross-modal generation;
- retrieval and geospatial embeddings.

## 4. Core architectures

- CNN / U-Net / ResNet;
- ViT / Swin-style encoders;
- temporal Transformer / ConvLSTM;
- GNN for irregular geospatial structures;
- contrastive/self-supervised pretraining;
- masked autoencoding;
- multimodal fusion;
- generative models.

The model must handle spectral channels, spatial scale, geolocation and time—not just RGB semantics.

## 5. Resolution questions

For every dataset/model record:

1. sensor native resolution?
2. output resolution?
3. resampling method?
4. temporal revisit/aggregation?
5. label/support resolution?
6. validation resolution?

Prediction at 10–30 m does not imply independent ground validation at 10–30 m.

## 6. Physics + AI opportunities

- radiative-transfer-informed learning;
- sensor/spectral response-aware encoders;
- cloud/atmospheric uncertainty;
- BRDF/illumination normalization;
- SAR scattering priors;
- geometry-aware LiDAR fusion;
- multi-sensor observation operators;
- physically meaningful temporal reconstruction.

## 7. Foundation-model transition

EO foundation models increasingly emphasize:

- global pretraining;
- multi-sensor/multimodal data;
- temporal context;
- resolution/scale robustness;
- geospatial embeddings;
- zero/few-shot transfer;
- generative cross-modal capabilities.

See [Earth & Scientific Foundation Models](../09-earth-foundation-models/index.md) and the [EO specialty track](../../06-case-studies/geoscience-remote-sensing/earth-observation/index.md).
