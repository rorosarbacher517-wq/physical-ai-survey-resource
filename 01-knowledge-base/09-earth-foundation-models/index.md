# 09 · Earth / Geospatial / Scientific Foundation Models

Earth Foundation Model (FM) 不能只按参数量理解。更有用的分类是看它向下游提供什么**接口**。

## 1. 三种主要接口

### A. Downloadable pretrained encoder

```text
raw EO / Earth data
→ pretrained model
→ embeddings/features
→ downstream head / fine-tuning
```

代表：`Prithvi-EO-2.0`, `TerraMind`, `MaRS`。

### B. Embedding-as-data / global embedding field

```text
precomputed annual/global embeddings
→ directly read as geospatial dataset
→ classifier/regressor/change analysis
```

代表：`AlphaEarth Foundations Satellite Embedding`, `TESSERA`。

这类场景下，用户甚至不需要本地运行 foundation encoder。

### C. Dynamical / forecast foundation model

```text
Earth-system state
→ pretrained dynamics model
→ task adaptation / rollout
```

代表：`Aurora`。

---

## 2. Earth data 为什么需要专门的 FM

Earth observations 具有：
- geolocation；
- time / season；
- multi-resolution；
- multi-sensor；
- cloud/missingness；
- physical observation differences；
- sparse labels；
- regional/climate distribution shift。

因此 natural-image pretraining recipe 不能原样照搬。

---

## 3. Pretraining objective

- masked reconstruction；
- contrastive / self-distillation；
- temporal prediction；
- multimodal alignment；
- cross-modal generation；
- autoregressive field prediction；
- multi-task supervised targets。

→ [Earth FM Pretraining](earth-fm-pretraining.md)

---

## 4. Multimodal representation

需要统一：
- Optical；
- SAR；
- elevation/terrain；
- land cover / labels；
- climate/weather context；
- temporal sequences。

但“统一”不等于忽略 sensing physics。

→ [Multimodal Earth Representations](multimodal-earth-representations.md)

---

## 5. 当前 representative families

### Prithvi-EO-2.0
HLS-based spatiotemporal masked-autoencoder route。

### TerraMind
9-modality generative multimodal route，dual token/pixel representations。

### AlphaEarth Foundations
annual global Satellite Embedding dataset，64-dimensional embedding field。

### TESSERA
pixel-wise annual embedding route；2026 `TESSERA v2` 继续研究 scaling/distillation/Matryoshka representations。

### MaRS
VHR SAR–optical multimodal foundation model。

### Aurora
Earth-system dynamics FM，跨 weather/air quality/waves 等任务 adaptation。

→ [Model-family Guide](model-family-guide.md)

---

## 6. Foundation Model 最大的评测陷阱

- pretraining region/time overlap；
- geolocation leakage；
- easy classification dominance；
- frozen vs full fine-tune 混比；
- sensor mismatch；
- output resolution 与 label support mismatch；
- classification skill 被外推成 quantitative-process skill。

→ [Earth FM Evaluation](earth-fm-evaluation.md)

---

## 7. Carbon / weather 为什么要单独验证

### Carbon
需要 continuous regression、process sensitivity、biome/climate OOD、footprint/support awareness。

### Weather
需要 rollout、initialization、vertical variables、probabilistic calibration、extremes。

所以“EO benchmark 强”不能直接推导为“carbon/weather task 强”。

---

## Sources

- Prithvi-EO-2.0: https://github.com/NASA-IMPACT/Prithvi-EO-2.0
- TerraMind ICCV 2025: https://openaccess.thecvf.com/content/ICCV2025/html/Jakubik_TerraMind_Large-Scale_Generative_Multimodality_for_Earth_Observation_ICCV_2025_paper.html
- AlphaEarth Satellite Embedding: https://developers.google.com/earth-engine/guides/aef_on_gcs_readme
- TESSERA: https://geotessera.org/
- MaRS AAAI 2026: https://doi.org/10.1609/aaai.v40i14.38153
- Aurora: https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/
