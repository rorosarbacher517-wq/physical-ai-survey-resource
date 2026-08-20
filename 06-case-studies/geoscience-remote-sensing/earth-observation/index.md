# Earth Observation / Remote Sensing AI Specialty Track

## Goal

Build a chain from **sensor/observation physics → preprocessing → spatial-spectral-temporal representation → multimodal AI → geophysical/ecological target → scale-aware validation**.

Main knowledge page: [Earth Observation AI](../../../01-knowledge-base/06-earth-observation-ai/index.md).

## 1. Observation physics

Start with [Radiative transfer and observation physics](../../../01-knowledge-base/06-earth-observation-ai/radiative-transfer-observation-physics.md).

Study by modality:

- [optical/hyperspectral](../../../01-knowledge-base/06-earth-observation-ai/optical-hyperspectral.md);
- [SAR/microwave](../../../01-knowledge-base/06-earth-observation-ai/sar-microwave.md);
- [LiDAR/3D](../../../01-knowledge-base/06-earth-observation-ai/lidar-3d.md);
- [thermal/SIF](../../../01-knowledge-base/06-earth-observation-ai/thermal-sif.md).

## 2. Data and representation

- [preprocessing/QC](../../../01-knowledge-base/06-earth-observation-ai/eo-preprocessing-quality.md);
- [time-series learning](../../../01-knowledge-base/06-earth-observation-ai/remote-sensing-time-series.md);
- [multisensor fusion](../../../01-knowledge-base/06-earth-observation-ai/multisensor-fusion.md);
- [super-resolution/reconstruction](../../../01-knowledge-base/06-earth-observation-ai/super-resolution-reconstruction.md).

## 3. AI problem families

Classification/segmentation/detection, retrieval/regression, change detection, temporal forecasting, reconstruction/downscaling, multimodal fusion, cross-modal generation and geospatial embeddings.

See [EO models and tasks](../../../01-knowledge-base/06-earth-observation-ai/eo-models-tasks.md).

## 4. Physical-AI integration points

- observation/retrieval operators;
- spectral-response and radiative-transfer priors;
- geometry-aware representations;
- temporal/phenological structure;
- multi-resolution consistency;
- sensor uncertainty;
- process-sensitive downstream evaluation.

## 5. Foundation-model path

```text
task-specific model
→ self-supervised EO encoder
→ global/temporal pretraining
→ multimodal Earth representation
→ foundation-model transfer / geospatial embeddings
```

See [EO foundation models](../../../01-knowledge-base/06-earth-observation-ai/eo-foundation-models.md), [Earth foundation models](../../../01-knowledge-base/09-earth-foundation-models/index.md) and [2026 Snapshot](../../../01-knowledge-base/13-2026-snapshot/index.md).

## 6. Validation safeguards

Use [Geospatial validation/OOD](../../../01-knowledge-base/06-earth-observation-ai/geospatial-validation.md). Always record native resolution, resampling, label support, temporal aggregation, split axis and independent validation support.

## 7. Repository resources

Use the [dataset library](../../../04-dataset-library/index.md), [paper library](../../../02-paper-library/index.md) and [benchmark library](../../../05-benchmarks-and-evaluation/index.md) for canonical records.
