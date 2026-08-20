# Multimodal Earth Representations

## 1. Representation 的目标

把不同 sensor/time/scale 的 observations 映射到可复用 latent space：

```text
{optical, SAR, temporal, terrain, ...}
→ E(x,y,t) or tokens Z
```

但 latent alignment 必须保留 downstream 所需的 physical information。

---

## 2. Patch representation

```text
X [B,T,C,H,W]
→ patchify
→ tokens [B,N,D]
```

适合 ViT-style FM。

---

## 3. Pixel-wise representation

```text
multi-sensor time series at pixel/area
→ embedding vector E ∈ R^D
```

优势：
- 易于作为普通 raster features 使用；
- global dataset 可预计算；
- downstream compute 低。

局限：
- embedding dimension 缺少直接 physical interpretation；
- annual compression 可能丢失 sub-seasonal detail；
- fine process target 仍需 task-specific variables。

---

## 4. AlphaEarth Foundations

截至 2026-08-20，official GCS dataset：
- annual embeddings 2017–2025；
- 64 channels；
- COG files / UTM zones；
- CC-BY 4.0 dataset license；
- Earth Engine / GCS access。

官方 data catalog 还说明当前 embedding collection 由 `AlphaEarth Foundations v2.1` 生成，并记录了 training-data更新。

Sources:
- https://developers.google.com/earth-engine/guides/aef_on_gcs_readme
- https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL

---

## 5. TESSERA

`TESSERA` 将 Sentinel-1/2 temporal observations 压缩成 annual pixel-wise embeddings。

`TESSERA v2` 2026 preprint 进一步研究：
- encoder/data scaling；
- distillation；
- Matryoshka representation；
- embedding storage/serving efficiency。

Preprint: https://arxiv.org/abs/2607.03949

---

## 6. Multimodal generation

`TerraMind` 的 any-to-any formulation 让模型可用某些 modalities 生成/辅助另一些 modalities。

对 downstream 来说，要区分：
- real observation；
- model-generated modality；
- shared latent representation。

生成出来的数据不是新增 independent observation。

---

## 7. Process-sensitive representation

对于 carbon/water/energy task，需要测试 embedding 是否保留：
- phenology；
- moisture；
- canopy structure；
- disturbance；
- continuous biophysical gradients；
- extreme response。

这通常比 land-cover classification 更严格。
