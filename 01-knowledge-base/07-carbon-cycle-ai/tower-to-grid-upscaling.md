# Tower-to-grid Upscaling：从稀疏 EC 到 Spatial Carbon Field

## 1. 为什么需要 upscaling

Flux towers：
- temporal resolution 高；
- local process information 丰富；
- spatial coverage 稀疏且不均匀。

Earth Observation / meteorology：
- spatially continuous；
- temporal/resolution 各异。

upscaling 的目标是学习：

```text
local flux observations + spatial predictors
→ regional/global flux field
```

---

## 2. 传统 feature-based upscaling

```text
satellite/meteorology at tower
→ RF/XGBoost/NN
→ tower flux
→ apply model to every grid cell
```

关键假设：tower training relationship 可以 transfer 到 unsampled grid cells。

---

## 3. Support-aware upscaling

训练时：

```text
pixel predictions
→ observation operator
→ tower loss
```

推理时：

```text
pixel predictions → spatial map
```

这解决了 training observation support mismatch，但**不自动提供 pixel-level reference**。

---

## 4. Spatial extrapolation risk

tower network 通常存在 sampling bias：
- biome coverage 不均；
- temperate regions 更多；
- disturbance/management type 不均；
- climate extremes 样本少。

因此 global map 可能在 tower-sparse regions 依赖强 extrapolation。

---

## 5. Evaluation hierarchy

### Level 1: held-out observations
site-blocked tower metrics。

### Level 2: regional/biome OOD
unseen ecological/climate regions。

### Level 3: independent spatial product/field campaign
与其他 observations 比较，但要匹配 support。

### Level 4: process / budget consistency
annual balance、seasonal cycle、climate response、spatial pattern。

---

## 6. Pixel resolution ≠ validated resolution

如果模型输出 30 m：

```text
output grid = 30 m
```

但 supervision 是几百米尺度动态 footprint：

```text
validation support ≠ 30 m
```

论文应写：
- “30 m predictions/output grid”；
- 不直接写“30 m validated flux”除非存在同尺度 independent measurement。

---

## 7. Uncertainty map

理想 upscaling 除 mean map 外还应包含：
- ensemble spread；
- OOD indicator；
- data-density / distance-to-training；
- observation uncertainty；
- support uncertainty。

---

## Sources

- FLUXCOM/upscaling literature；
- Pastorello et al. (2020), FLUXNET2015；
- 2025 physics-constrained North America mapping: https://doi.org/10.1016/j.isprsjprs.2025.06.033
