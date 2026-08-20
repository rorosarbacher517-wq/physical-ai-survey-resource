# 09 · Earth and Scientific Foundation Models

A scientific foundation model should provide reusable representations or generative/forecast capability across tasks, regions, variables or modalities—not merely be a large task-specific network.

## 1. Why Earth foundation models are different

Earth data are:

- georeferenced;
- multi-resolution;
- multi-sensor;
- multi-temporal;
- physically structured;
- seasonally and regionally non-stationary;
- often sparsely labeled.

Therefore natural-image recipes need adaptation.

## 2. Pretraining objectives

Common strategies:

- masked reconstruction;
- contrastive learning;
- temporal prediction;
- multimodal alignment;
- cross-modal generation;
- autoregressive field prediction;
- supervised multi-task pretraining.

## 3. Representation questions

For every model ask:

1. What sensors/modalities were seen in pretraining?
2. What spatial resolution(s)?
3. What temporal sampling?
4. How are location and time encoded?
5. Are spectral channels fixed or flexible?
6. How are missing modalities handled?
7. Is the output an embedding, reconstruction, generated modality or physical forecast?
8. What transfers zero-shot/few-shot versus requiring full fine-tuning?

## 4. Important model families

### Earth-observation encoders
Prithvi-EO, masked-autoencoder and contrastive EO models, multimodal encoders.

### Multimodal generative EO
TerraMind represents the move toward any-to-any multimodal Earth-observation generation and representation learning.

### Global geospatial embeddings
AlphaEarth Foundations represents a different interface: pretrained global embedding fields that downstream systems can use as geospatial features.

### Earth-system forecast foundation models
Aurora demonstrates large-scale pretraining/fine-tuning across atmospheric/Earth-system forecasting tasks.

## 5. Physics and foundation models

Large pretraining does not remove the need for physics. Key opportunities:

- physics-aware tokens/coordinates;
- conservation-aware fine-tuning;
- observation operators;
- retrieval constraints;
- process-informed task heads;
- hybrid coupling to simulators;
- physically stratified evaluation.

## 6. Foundation-model failure modes

- pretraining-domain leakage into benchmarks;
- strong interpolation but weak climate/biome/extreme OOD transfer;
- scale mismatch;
- hidden preprocessing dependence;
- sensor-specific artifacts;
- expensive fine-tuning masked by headline zero-shot results;
- embeddings correlated with location rather than transferable process information.

## 7. Current verified examples

Fast-moving releases are tracked with primary sources in [13 · 2026 Snapshot](../13-2026-snapshot/index.md).

Domain view: [Geospatial foundation models](../../06-case-studies/geoscience-remote-sensing/geospatial-foundation-models/index.md).
