# Geospatial Validation、OOD 与 Foundation-model Evaluation

## 1. Random pixel split 为什么危险

相邻 pixel 高度相关：

```text
train pixel ── 30 m ── test pixel
```

模型可能只是在 spatial interpolation，而不是真正 generalization。

---

## 2. Split hierarchy

从容易到困难：

```text
random samples
→ spatial blocks
→ unseen scenes/tiles
→ unseen regions
→ unseen biomes/climates
→ unseen years/events
→ future distribution shift
```

---

## 3. Foundation-model transfer protocols

必须明确：
- frozen embeddings；
- linear probe；
- shallow MLP；
- adapter/PEFT；
- full fine-tune。

参数更新程度不同，结果不能直接放在同一列比较。

---

## 4. Geographic leakage

如果 pretraining 已覆盖 downstream test region/time，zero-shot/frozen performance 并不等价于“完全未见过该 geography”。

应尽可能记录：
- pretraining coverage；
- temporal cutoff；
- geolocation metadata；
- downstream overlap。

---

## 5. Regression 比分类更难

Land-cover classification 主要测 semantic separability；
biomass、soil moisture、GPP 等 quantitative regression 更要求 representation 保留 continuous physical information。

2026-08 的 emerging biomass benchmarking 进一步强调 embedding-as-data 与 downloadable encoders 在 quantitative regression 上可能表现不同；这类结果仍应结合具体 benchmark、pretraining overlap 与 reference uncertainty 阅读。

---

## 6. Scale-aware metrics

不要只报告 overall RMSE/F1，还可按：
- biome；
- land cover；
- region；
- sensor；
- resolution；
- season；
- cloudiness；
- label density；
- extreme/event；
- object size。

---

## 7. PANGAEA

PANGAEA 提供跨 datasets/tasks/sensors/resolutions 的标准化 EO FM evaluation framework，是截至 2026-08-20 最值得持续跟踪的 GFM benchmark 之一。

Source: https://arxiv.org/abs/2412.04204
