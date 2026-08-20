# Earth Observation Foundation Models · 截至 2026-08-20

这一页讲**稳定的模型接口与方法族**；具体当前版本见 Snapshot。

## 1. 什么是 EO Foundation Model

不是“参数很大”就算。更关键是：
- broad pretraining data；
- reusable representation；
- multiple downstream tasks；
- low-label transfer；
- multi-region/sensor/time generalization。

---

## 2. Pretraining route

### Masked reconstruction
`MAE` 路线，代表：`Prithvi-EO-2.0`。

### Contrastive / self-distillation
学习 invariant embedding。

### Multimodal generative
输入某些 modality，生成/表示其他 modality，代表：`TerraMind`。

### Pixel-wise annual embedding
将长时间、多源 observation 压缩为 per-pixel embedding，代表：`TESSERA`、`AlphaEarth Foundations` 的使用接口。

---

## 3. Prithvi-EO-2.0

官方 NASA-IMPACT repo 可确认：
- HLS 30 m；
- 约 4.2M global time-series training samples；
- ViT + MAE；
- 3D spatiotemporal patch embedding；
- 300M / 600M model variants；
- 可选 time/location embedding。

Source: https://github.com/NASA-IMPACT/Prithvi-EO-2.0

---

## 4. TerraMind

ICCV 2025 paper：
- generative multimodal EO FM；
- pretraining across nine geospatial modalities；
- dual token-level + pixel-level representation；
- 支持 any-to-any multimodal use case。

Source: https://openaccess.thecvf.com/content/ICCV2025/html/Jakubik_TerraMind_Large-Scale_Generative_Multimodality_for_Earth_Observation_ICCV_2025_paper.html

---

## 5. AlphaEarth Foundations

与 downloadable encoder 不同，它的重要接口是 global annual **Satellite Embedding** dataset。

官方资料截至 2026-08：
- 64-dimensional embeddings；
- annual layers 2017–2025；
- 可通过 Earth Engine / GCS 使用；
- 输入融合多类 EO/public data source。

Source: https://developers.google.com/earth-engine/guides/aef_on_gcs_readme

---

## 6. TESSERA

TESSERA 是 pixel-wise Earth representation 路线：
- Sentinel-1 + Sentinel-2 temporal information；
- global annual 10 m embeddings（v1 route）；
- 128-dimensional embedding；
- 2026-07 `TESSERA v2` preprint 系统研究 scaling 与 Matryoshka representation。

Sources:
- https://geotessera.org/
- https://arxiv.org/abs/2607.03949

---

## 7. MaRS

AAAI 2026 的 `MaRS` 面向 very-high-resolution SAR–optical multimodal pretraining，并发布 `MaRS-16M` paired data setup。

Source: https://ojs.aaai.org/index.php/AAAI/article/view/38153

---

## 8. 最重要的 evaluation 结论

Foundation model 不能只测 EuroSAT-style easy classification。

`PANGAEA` 强调：
- multiple tasks；
- multiple sensors；
- multiple resolutions；
- geography diversity；
- supervised baseline comparison；
- label efficiency。

其公开结果也提醒：GFMs **并非在所有条件下稳定优于 supervised baselines**。

Source: https://arxiv.org/abs/2412.04204

---

## 9. Carbon / ecohydrology 迁移问题

EO FM 对 carbon task 真正有价值，需要证明 embedding 保留：
- vegetation state；
- structure；
- water stress；
- disturbance；
- phenology；
- quantitative regression information；
- OOD biome/climate transfer。

不能仅凭 land-cover benchmark 很强，就推断对 GPP/NEE 同样强。
