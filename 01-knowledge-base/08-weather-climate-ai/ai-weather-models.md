# AI Weather-model Families

这页按**representation 与 scientific role**组织，而不是按 leaderboard。

## 1. FourCastNet：Spectral / Operator route

`FourCastNet` 使用 Adaptive Fourier Neural Operator 思路处理 global weather field。

学习重点：
- Fourier modes；
- global receptive field；
- autoregressive step；
- high-frequency/extreme preservation。

Source: https://arxiv.org/abs/2202.11214

---

## 2. GraphCast：Graph / Mesh route

结构概念：

```text
lat-lon grid
→ grid-to-mesh encoder
→ multiscale mesh GNN
→ mesh-to-grid decoder
→ next weather state
```

优势在于 global communication 与 spherical geometry-friendly mesh representation。

Source: https://doi.org/10.1126/science.adi2336

---

## 3. Pangu-Weather：3D Transformer route

Pangu-Weather 将 upper-air + surface weather 组织为 3D Earth-specific representation，并用 hierarchical temporal aggregation 降低长 forecast 所需 autoregressive steps。

学习重点：
- 3D Earth-specific Transformer；
- vertical dimension；
- 1h/3h/6h/24h models；
- rollout scheduling。

Source: https://doi.org/10.1038/s41586-023-06185-3

---

## 4. FuXi：Cascade route

FuXi 使用：

```text
FuXi-Short → FuXi-Medium → FuXi-Long
```

分别针对不同 lead range，目标是减轻单一 autoregressive model 在长 lead 的 error accumulation。

论文输入示例包含连续两个 time steps、70 variables、`721×1440` global grid。

Source: https://doi.org/10.1038/s41612-023-00512-1

---

## 5. FengWu：Multimodal / Multitask + Replay

FengWu 处理多 atmospheric variables，并用 replay-buffer-related training strategy 处理 long rollout；`FengWu-Ensemble` 使用 conditional diffusion 生成 ensemble members。

Source: https://doi.org/10.1038/s43247-025-02502-y

---

## 6. NeuralGCM：Hybrid differentiable route

```text
resolved fluid dynamics
+ learned subgrid physics
→ differentiable global model
```

它不是纯 data-driven forecast surrogate，而是保留 dynamical core 的 hybrid route。

2026 的 precipitation extension 进一步结合 satellite precipitation observations 训练 learned physics component。

Sources:
- https://doi.org/10.1038/s41586-024-07744-y
- https://research.google/blog/neuralgcm-harnesses-ai-to-better-simulate-long-range-global-precipitation/

---

## 7. GenCast：Probabilistic generative route

GenCast 学 conditional distribution，并 autoregressively sample 15-day ensemble trajectories：

```text
P(X^{1:T}|X^0,X^-1)
= Π_t P(X^{t+1}|X^t,X^{t-1})
```

论文使用 0.25° global grid 和多个 pressure-level/surface variables。

Source: https://doi.org/10.1038/s41586-024-08252-9

---

## 8. AIFS：Operational AI route

截至 2026-08-20：
- `AIFS Single v2`：current ECMWF operational deterministic AI forecast；
- `AIFS ENS v2`：current ECMWF operational AI ensemble；
- 两者均在 **2026-05-12** operational upgrade。

AIFS v2 还扩展了 wave/snow-related output capabilities。

Official: https://confluence.ecmwf.int/spaces/UDOC/pages/599165907/AIFS+Version+History

---

## 9. WeatherNext 2：Functional Generative Network route

Google `WeatherNext 2` 使用 `Functional Generative Network (FGN)` 路线生成 coherent probabilistic scenarios，并提供 0–15 day medium-range forecast family。

截至 2026-08-20，Google 已开放 WeatherNext 2 code/weights，并提供 operational/mini/cyclone-related variants。

Official: https://deepmind.google/science/weathernext/

---

## 10. Aurora：Earth-system Foundation Model route

Aurora 使用 large-scale heterogeneous geophysical pretraining，然后适配：
- weather；
- air quality；
- ocean waves；
- tropical cyclone/high-resolution tasks。

2026-07 发布 `Aurora 1.5` open extension。

Source: https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/

---

## 11. 比较模型时统一记录

```text
initialization source
input variables/levels
spatial grid/mesh
architecture
forecast step
training objective
rollout strategy
deterministic/probabilistic
lead time
verification reference
compute
operational/research status
```

不匹配这些条件时，不比较 headline metric。
