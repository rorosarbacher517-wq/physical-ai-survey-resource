# 07 · Terrestrial Carbon Cycle / Carbon-flux AI

这一模块把**碳循环过程、Eddy Covariance、flux footprint、Earth Observation、meteorology、process constraints 与 AI**放在同一条观测—建模链里。

真正要解决的问题不是“用什么模型预测 GPP”，而是：

> **模型预测的物理场、塔实际观测到的 source area、遥感看到的 surface state，以及最终验证尺度是否一致？**

---

## 1. 从过程到 observation 的完整链

```text
photosynthesis / respiration / disturbance
              ↓
        GPP / RECO / NEE
              ↓
      turbulent transport
              ↓
       Eddy Covariance
              ↓
      dynamic flux footprint
              ↓
     tower-scale observation
              ↑
EO + meteorology + soil moisture + structure
              ↓
spatiotemporal / multimodal carbon model
              ↓
pixel/field-level latent flux prediction
              ↓
footprint observation operator
              ↓
tower-scale loss / supervision
              ↓
tower-to-grid inference + uncertainty
```

---

## 2. 三个核心 flux quantity

常见 convention：

```text
NEE = RECO - GPP
```

其中：
- `NEE`：Net Ecosystem Exchange；
- `GPP`：Gross Primary Production；
- `RECO`：Ecosystem Respiration。

**必须检查具体 dataset 的 sign convention。**

另外需要区分：
- EC directly estimates turbulent net CO₂ exchange after processing/QC；
- `GPP` 和 `RECO` 通常来自 flux partitioning，而不是两台传感器分别直接测量。

→ [Flux Partitioning / Uncertainty](flux-partitioning-uncertainty.md)

---

## 3. Eddy Covariance 不是 point observation

塔坐标只是 instrument location。一个 averaging interval 的 flux 来自动态 upwind source area：

```text
Y_t = ∬ w_t(x,y) F_t(x,y) dxdy + ε_t
```

离散到 raster：

```text
Y_t ≈ Σ_i w_{i,t} F_{i,t}
```

`w_t` 随 wind direction、turbulence、stability、measurement height、roughness 等变化。

这就是为什么固定 center pixel / uniform window 与真实 observation support 不是同一个问题。

→ [Flux Footprints](flux-footprints.md)

---

## 4. Carbon AI 的 input stack

### 2D Earth Observation
- optical reflectance / vegetation indices；
- thermal；
- SIF；
- SAR / microwave；
- land cover / disturbance。

### 3D structure
- LiDAR canopy height / profile；
- point cloud / waveform-derived structure。

### Meteorology / environment
- shortwave / longwave radiation；
- air/soil temperature；
- RH / VPD；
- precipitation；
- soil moisture；
- wind / turbulence；
- BLH / stability。

### Static context
- biome；
- soil；
- topography；
- management / disturbance history。

→ [Carbon Data Stack](carbon-data-stack.md)

---

## 5. 模型层级

```text
empirical / LUE
→ process model
→ classical ML
→ temporal / spatiotemporal DL
→ multimodal AI
→ physics-constrained learning
→ footprint-aware observation mapping
→ hybrid process–ML
→ Earth/EO foundation representations
```

不同层级解决的问题不同；不应该只按“模型复杂度”排序。

→ [Carbon Modeling Methods](carbon-modeling-methods.md)

---

## 6. Tensor-level 统一表示

一个典型 footprint-aware multimodal batch 可写成：

```text
EO pixels       X : [B,T,C,H,W]
meteorology     M : [B,T,P]
3D/static       S : [B,D_s] or [B,N,D]
footprint       W : [B,T,H,W]
pixel flux      F : [B,T,K,H,W]
tower target    Y : [B,T,K]
```

其中 `K` 可对应 `NEE/GPP/RECO`。

输出 observation mapping：

```text
Y_hat[b,t,k] = Σ_h Σ_w W[b,t,h,w] · F_hat[b,t,k,h,w]
```

这使得**pixel field prediction**与**tower supervision**可以同时成立。

→ [Footprint-aware AI](footprint-aware-ai.md)

---

## 7. Physics 可以放在哪里

- carbon balance；
- light / water / temperature response prior；
- positivity / bounds（仅在定义上成立时）；
- phenology；
- footprint observation operator；
- process-model residual correction；
- carbon–water–energy coupling；
- Data Assimilation；
- process-aware evaluation。

→ [Process-constrained Carbon AI](process-constrained-carbon-ai.md)

---

## 8. 从 tower 到 map 的关键限制

即使模型内部输出 30 m / 500 m spatial flux：

```text
fine-resolution prediction ≠ fine-resolution independent validation
```

如果 training/reference 主要来自 tower footprint 或 coarse products，必须明确 latent map 的 validation support。

→ [Tower-to-grid Upscaling](tower-to-grid-upscaling.md)

---

## 9. Extremes 与 OOD

carbon response 在：
- drought；
- heatwave；
- compound hot–dry event；
- wildfire / disturbance；
- phenological transition；
- management event

下可能与 normal conditions 完全不同。

因此 evaluation 应从 overall RMSE 扩展到 event/regime/OOD diagnostics。

→ [Extremes / Climate Response](extremes-climate-response.md)

---

## 10. 截至 2026-08-20 应重点跟踪的方向

- dynamic footprint 与 remote sensing/model support matching；
- footprint-weighted spatial/graph modeling；
- joint NEE/GPP/RECO physics-constrained learning；
- SIF + soil moisture + EO + EC integration；
- ML-assisted process-model parameter optimization；
- EO foundation representations 向 ecohydrology/carbon regression 迁移；
- climate/biome/extreme OOD；
- uncertainty propagation from measurement → partitioning → footprint → model → map。

当前版本与论文见 [2026 Snapshot](../13-2026-snapshot/index.md)。

---

## 11. Primary anchors

- Baldocchi (2003), *Assessing the eddy covariance technique for evaluating carbon dioxide exchange rates of ecosystems*.
- Kljun et al. (2015), footprint parameterisation: https://doi.org/10.5194/gmd-8-3695-2015
- Pastorello et al. (2020), FLUXNET2015: https://doi.org/10.1038/s41597-020-0534-3
- Chu et al. (2026), *Flux Footprints: A Critical Link to Bridge Eddy-Covariance Measurements With Models, Remote Sensing, and Other Observations*: https://doi.org/10.1111/gcb.70887
