# Earth Observation / Remote Sensing AI Specialty Track

## Goal

Build a chain from **sensor physics → preprocessing → spatial/spectral/temporal representation → AI model → geophysical/ecological target → validation**.

## 1. Observation physics

Study by modality:

- optical multispectral/hyperspectral: radiance, reflectance, atmospheric correction, BRDF, clouds, spectral response;
- thermal infrared: emission, emissivity, surface temperature;
- SAR/microwave: backscatter, polarization, geometry, roughness/moisture/structure;
- LiDAR: range/waveform, canopy/terrain geometry;
- SIF: fluorescence signal, canopy/radiative effects and photosynthetic interpretation.

Main knowledge page: [Earth Observation AI](../../../01-knowledge-base/06-earth-observation-ai/index.md).

## 2. AI problem families

- classification / segmentation / detection;
- retrieval/regression;
- change detection;
- temporal forecasting;
- missing-data reconstruction;
- super-resolution/downscaling;
- multimodal fusion;
- geospatial retrieval/embeddings;
- foundation-model transfer.

## 3. Physical-AI integration points

- retrieval/observation operators;
- spectral response and radiative-transfer priors;
- geometry-aware representations;
- temporal/phenological constraints;
- multi-resolution consistency;
- sensor uncertainty;
- physically meaningful downstream evaluation.

## 4. Key datasets in this repository

Use the [dataset library](../../../04-dataset-library/index.md), especially HLS, MODIS, ERA5-Land, SMAP and flux-network records where relevant.

## 5. Foundation-model path

Learn the progression:

```text
task-specific CNN/ViT
→ self-supervised EO encoder
→ global/temporal EO pretraining
→ multimodal EO foundation model
→ geospatial embedding fields / cross-modal generation
```

See [Geospatial Foundation Models](../geospatial-foundation-models/index.md) and [2026 Snapshot](../../../01-knowledge-base/13-2026-snapshot/index.md).

## 6. Validation safeguards

Always record native resolution, resampling, label support, temporal aggregation and independent validation support. Avoid claiming field-scale accuracy solely from pixel-resolution output.
