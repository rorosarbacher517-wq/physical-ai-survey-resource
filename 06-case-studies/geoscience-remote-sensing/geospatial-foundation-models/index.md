# Geospatial / Earth Foundation Models Specialty Track

Main knowledge page: [Earth & Scientific Foundation Models](../../../01-knowledge-base/09-earth-foundation-models/index.md).

## 1. What makes an Earth foundation model useful?

It should transfer reusable representations or forecasting/generation capability across some combination of:

- regions;
- times;
- sensors/modalities;
- resolutions;
- tasks;
- geophysical variables.

Large parameter count alone is not enough.

## 2. Model families to distinguish

### EO encoders
Reusable spatial/spectral/temporal representations for mapping and retrieval tasks.

### Multimodal EO generation
Cross-modal representation and generation, e.g. optical/radar/land-cover style modality translation.

### Global embedding fields
Precomputed planetary embeddings that downstream users query as geospatial features.

### Earth-system forecast foundation models
Pretrain on broad geophysical datasets, then fine-tune to weather/atmospheric/Earth-system tasks.

## 3. Current primary-source examples

- Prithvi-EO-2.0: https://github.com/NASA-IMPACT/Prithvi-EO-2.0
- TerraMind: https://github.com/IBM/terramind
- AlphaEarth Foundations: https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/ <!-- manual-review: official source URL path -->
- Aurora: https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/

See [2026 Snapshot](../../../01-knowledge-base/13-2026-snapshot/index.md) for dated claims.

## 4. Evaluation questions

- pretraining/benchmark overlap?
- zero-shot vs linear probe vs full fine-tune?
- region/time/sensor OOD?
- label efficiency?
- resolution robustness?
- physical-process targets versus semantic mapping?
- compute/data cost?

## 5. Priority research question

Can general Earth representations improve **process-sensitive targets** such as GPP/NEE, hydrology, extremes and atmosphere-land coupling while preserving observation physics and scale? This is more scientifically demanding than standard land-cover classification alone.
