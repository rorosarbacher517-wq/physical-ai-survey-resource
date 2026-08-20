# Earth-observation Foundation Models

## 1. Why pretrain on Earth data?

EO archives contain global, repeated and multi-sensor observations, while high-quality labels are sparse. Pretraining can learn reusable spatial-spectral-temporal representations.

## 2. Important design axes

- sensor/modalities;
- band flexibility;
- spatial resolution;
- patch/token scale;
- temporal context;
- geolocation/time encoding;
- pretraining objective;
- global sampling balance;
- adaptation method.

## 3. Encoder-style models

Masked-autoencoding and contrastive EO encoders produce embeddings later fine-tuned for mapping/regression.

Prithvi-EO-2.0 is a useful public reference for global HLS time-series pretraining.

Primary: https://github.com/NASA-IMPACT/Prithvi-EO-2.0

## 4. Multimodal generative models

TerraMind uses a multimodal generative approach and exposes any-to-any Earth-observation workflows.

Primary: https://github.com/IBM/terramind

## 5. Geospatial embedding fields

AlphaEarth Foundations exposes annual Satellite Embedding data through Earth Engine, representing a different interface from downloading a task encoder and fine-tuning it.

Primary: https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/

> Note: the source URL contains a promotional phrase that is part of the official page path; repository prose should still avoid repeating promotional superlatives as scientific claims.

## 6. Evaluation

Distinguish:

- frozen embedding + shallow head;
- linear probe;
- parameter-efficient fine-tuning;
- full fine-tuning;
- zero-shot retrieval/classification;
- cross-region/time/sensor transfer.

## 7. Carbon-cycle opportunity

A general EO embedding is useful only if it improves process-sensitive tasks under site/biome/OOD validation. Pairing such embeddings with meteorology, footprints and process constraints is an open research direction.
