# Earth FM Pretraining

## 1. Pretraining data 的五个轴

```text
space × time × sensor × variable × resolution
```

再加上 geography/climate distribution。

---

## 2. Masked Autoencoding

```text
visible patches
→ encoder
→ latent
→ decoder
→ reconstruct masked patches
```

EO 中 masking 可以跨：
- space；
- spectral bands；
- time；
- modality。

`Prithvi-EO-2.0` 是 HLS spatiotemporal MAE route 的重要例子。

---

## 3. Contrastive learning

目标是让 related views/observations embedding 接近：

```text
sim(z_i,z_j) high for positive pair
```

Earth-specific positive pair 可以来自：
- same location different time；
- same location different sensor；
- augmented views。

风险：season/change 本身可能是 task signal，不应被全部强制 invariant。

---

## 4. Multimodal generative pretraining

```text
subset of modalities
→ shared representation/generator
→ reconstruct/generate other modalities
```

`TerraMind` 使用 multimodal generative route，并结合 token-level 与 pixel-level representations。

---

## 5. Pixel-wise annual embedding

目标不是输出 patch feature，而是生成：

```text
E(year, x, y) ∈ R^D
```

适合全球 geospatial embedding products。

`AlphaEarth Foundations` 与 `TESSERA` 代表该 interface。

---

## 6. Time / location metadata

可加入：
- DoY / timestamp；
- latitude/longitude；
- sensor ID。

但 absolute location 带来 geographic memorization/leakage 风险。

Prithvi-EO-2.0 提供 temporal/location embedding variants，并在 pretraining 中设计 metadata dropout 以处理 metadata 缺失。

---

## 7. Scaling 不只看 training loss

`TESSERA v2` 2026 preprint 报告的 controlled scaling study 强调：pretraining loss 与 downstream performance 的相关性可能很弱，因此 model selection 应加入 downstream evaluation，而不只是最低 pretraining objective。

Preprint: https://arxiv.org/abs/2607.03949

---

## Sources

- Prithvi-EO-2.0 official: https://github.com/NASA-IMPACT/Prithvi-EO-2.0
- TerraMind: https://openaccess.thecvf.com/content/ICCV2025/html/Jakubik_TerraMind_Large-Scale_Generative_Multimodality_for_Earth_Observation_ICCV_2025_paper.html
- TESSERA v2 preprint: https://arxiv.org/abs/2607.03949
