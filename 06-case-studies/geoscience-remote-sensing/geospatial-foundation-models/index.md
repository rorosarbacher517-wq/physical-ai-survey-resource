# Geospatial / Earth Foundation Models 专题

## 1. 不按参数量分类，按接口分类

```text
A. downloadable encoder
   Prithvi-EO-2.0 / TerraMind / MaRS

B. ready-made embedding field
   AlphaEarth Foundations / TESSERA

C. dynamical Earth-system FM
   Aurora
```

## 2. 学习顺序

1. [Earth FM Pretraining](../../../01-knowledge-base/09-earth-foundation-models/earth-fm-pretraining.md)
2. [Multimodal Earth Representations](../../../01-knowledge-base/09-earth-foundation-models/multimodal-earth-representations.md)
3. [Model-family Guide](../../../01-knowledge-base/09-earth-foundation-models/model-family-guide.md)
4. [Earth FM Evaluation](../../../01-knowledge-base/09-earth-foundation-models/earth-fm-evaluation.md)

## 3. 评测重点

- pretraining overlap；
- geography/time OOD；
- sensor transfer；
- frozen vs PEFT/full FT；
- label efficiency；
- process-sensitive regression；
- scale/support；
- compute/storage。

## 4. 当前趋势

截至 2026-08-20：
- `AlphaEarth Foundations` 已提供 2017–2025 annual 64-d Satellite Embedding dataset；
- `TESSERA v2` 是 2026-07 preprint，聚焦 pixel-wise FM scaling/distillation；
- `MaRS` 是 AAAI 2026 SAR–optical multimodal FM；
- `WorldTensor` 2026 将 Earth-system FM data 扩展到 environmental + socioeconomic variables；
- ecohydrology/carbon 开始出现专门讨论 EOFM process inference 的 2026 preprint。

详见 [Snapshot](../../../01-knowledge-base/13-2026-snapshot/index.md)。
