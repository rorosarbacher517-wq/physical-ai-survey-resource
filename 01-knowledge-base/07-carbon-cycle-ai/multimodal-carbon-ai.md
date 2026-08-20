# Multimodal Carbon AI

## 1. 为什么需要 multimodal

carbon exchange 同时依赖：
- canopy spectral state；
- 3D structure；
- radiation / temperature / humidity；
- soil moisture；
- disturbance / land cover；
- atmospheric transport/source area。

单一 optical modality 无法完整观测这些过程。

---

## 2. 一个可解释的 architecture

```text
2D EO [B,T,C,H,W]
→ spatial encoder ───────────┐
                             │
3D structure [B,N,D]
→ 3D encoder ────────────────┼→ fusion → temporal model → pixel flux field
                             │                         ↓
meteorology [B,T,P]           │                   footprint H_t
→ temporal/MLP encoder ──────┘                         ↓
                                                   tower loss
```

---

## 3. Optical + SAR

潜在互补：
- cloud gaps；
- moisture/structure sensitivity；
- different observation physics。

必须处理 acquisition-time mismatch 与 incidence/polarization metadata。

---

## 4. Optical + LiDAR

Optical：动态 spectral/phenological state；
LiDAR：较慢变化 structural prior。

适合：
- forest structure；
- biomass / canopy heterogeneity；
- roughness / footprint context。

但 sparse LiDAR campaign 可能导致 small-sample overfitting。

---

## 5. SIF + Optical + Meteorology

SIF 增加 photosynthesis-related observation；optical 提供 canopy state；meteorology 提供 forcing。

2025 transfer-learning work 使用 SIF + EC data 进行 GPP estimation：
https://doi.org/10.1016/j.jag.2025.104503

---

## 6. Soil moisture

coarse SMAP/ERA soil moisture 可提供 water limitation context，但需要处理 coarse support。

可把 coarse variable 作为 regional forcing/context，而不是假装是 30 m pixel measurement。

---

## 7. Foundation embeddings

```text
EO FM embedding
+ meteorology
+ structural/process variables
→ carbon head
```

必须做：
- raw-band baseline；
- frozen embedding baseline；
- fine-tuned model；
- label-efficiency curve；
- biome/climate OOD。

---

## 8. Negative transfer

如果加入一个 modality 后性能下降，并不矛盾。可能原因：
- temporal mismatch；
- noisy modality；
- insufficient samples；
- scale mismatch；
- redundant feature；
- optimization imbalance。

因此每个 modality 都需要 paired ablation。
