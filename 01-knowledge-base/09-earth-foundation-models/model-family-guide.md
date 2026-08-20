# Earth Foundation-model Family Guide

This page organizes representative systems by interface.

## 1. Prithvi-EO-2.0

Type: EO time-series encoder/pretraining reference centered on HLS.

Use it to study:

- multispectral temporal patching;
- masked pretraining;
- global HLS sampling;
- downstream fine-tuning.

Primary: https://github.com/NASA-IMPACT/Prithvi-EO-2.0

## 2. TerraMind

Type: multimodal generative Earth-observation foundation model.

Use it to study:

- modality tokenization;
- cross-modal generation;
- any-to-any conditioning;
- multimodal fine-tuning.

Primary: https://github.com/IBM/terramind

## 3. AlphaEarth Foundations

Type: global geospatial embedding-field interface.

Use it to study:

- planetary embedding production;
- downstream use of precomputed embeddings;
- geographic/time transfer;
- embedding evaluation beyond classification.

Primary: https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/ <!-- manual-review: official source URL path -->

## 4. Aurora

Type: Earth-system forecast foundation model.

Use it to study:

- broad geophysical pretraining;
- task-specific fine-tuning;
- atmospheric/Earth-system variables;
- foundation-model transfer in forecasting.

Primary: https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/

## 5. Comparing interfaces

| Family | Main output/interface | Typical downstream use |
|---|---|---|
| EO encoder | latent embedding | mapping/regression |
| multimodal generator | modality/latent prediction | fusion/generation |
| embedding field | precomputed geospatial vector | downstream feature |
| forecast foundation model | physical future field | weather/Earth forecasting |

## 6. Research question for carbon/weather

The key test is whether general representations improve physically sensitive OOD tasks while preserving support, dynamics and uncertainty—not whether they only improve semantic EO benchmarks.
