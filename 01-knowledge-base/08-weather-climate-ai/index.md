# 08 · Weather & Climate AI

Weather AI 不是一个“forecast neural network 排行榜”。完整系统是：

```text
atmospheric / land / ocean state
        ↓
global observing system
        ↓
QC + observation operators
        ↓
Data Assimilation / analysis
        ↓
initial condition
        ↓
forecast dynamics
        ↓
deterministic / probabilistic rollout
        ↓
ensemble / post-processing / downscaling
        ↓
extremes / impacts
        ↓
verification / calibration
        ↓
coupled Earth-system / climate simulation
```

AI 可以替代其中一个 block，也可以把多个 block 端到端学习。

---

## 1. Atmospheric state：模型到底在预测什么

一个 global weather state 通常包含：

### Surface / near-surface
- `T2M`；
- `U10/V10`；
- `MSLP`；
- precipitation；
- land/ocean surface variables。

### Upper air
在多个 pressure/model levels 上：
- geopotential / height (`Z`)；
- temperature (`T`)；
- specific humidity (`Q`)；
- wind (`U/V`)；
- vertical-motion-related variables。

Tensor 可写为：

```text
surface       [B,C_s,H,W]
upper-air     [B,C_u,L,H,W]
```

或 flatten 为统一 channel dimension。

→ [Atmospheric State & Dynamics](atmospheric-state-dynamics.md)

---

## 2. Classical NWP 是 AI weather 的坐标系

NWP 不是“老方法”，而是理解 forecast task 的物理基础：
- governing equations；
- discretization；
- parameterization；
- initialization；
- time integration；
- boundary/coupling；
- ensemble。

→ [NWP Basics](nwp-basics.md)

---

## 3. Observing system 与 DA

真实 observations 包括：
- satellite radiance / microwave sounding；
- radiosonde；
- surface stations；
- aircraft；
- ships/buoys；
- weather radar；
- GNSS-related observations 等。

它们不是天然规则 grid，需要 observation operator + DA 映射到 atmospheric analysis state。

→ [Weather Observing System](weather-observing-system.md)  
→ [Weather Data Assimilation](weather-data-assimilation.md)

---

## 4. AI forecast backbone 方法族

| 方法族 | 代表系统 | 核心思想 |
|---|---|---|
| spectral/operator | `FourCastNet` | global spectral/operator computation |
| graph/mesh | `GraphCast` | grid ↔ multiscale mesh message passing |
| 3D Transformer | `Pangu-Weather` | 3D Earth-specific representation + hierarchical temporal models |
| cascade | `FuXi` | short/medium/long models 分段降低 rollout accumulation |
| multimodal/multitask | `FengWu` | 多 atmospheric fields + replay strategy |
| hybrid | `NeuralGCM` | differentiable dynamical core + learned subgrid physics |
| probabilistic generative | `GenCast` | stochastic conditional weather distribution |
| operational AI | `AIFS Single / AIFS ENS` | ECMWF operational deterministic + ensemble ML forecasting |
| end-to-end observation→forecast | `Aardvark Weather`, `FuXi Weather` | 将 observation/state-estimation 链纳入 ML system |
| Earth-system FM | `Aurora` | large-scale pretraining + task adaptation |
| current probabilistic family | `WeatherNext 2` | Functional Generative Network route |

→ [AI Weather-model Families](ai-weather-models.md)

---

## 5. Rollout 是 weather DL 的核心问题

很多模型学习：

```text
X_{t-1}, X_t → X_{t+Δt}
```

然后 autoregressive：

```text
X_hat_{t+1} → X_hat_{t+2} → ...
```

one-step RMSE 好，不代表 10–15 day rollout 稳定。需要研究：
- error accumulation；
- spectral drift；
- climatological bias；
- extreme smoothing；
- exposure bias；
- multi-step training。

→ [Weather Rollout & Training](rollout-training.md)

---

## 6. Deterministic ≠ Probabilistic

### Deterministic
输出一条 trajectory。

### Ensemble / probabilistic
输出：

```text
p(X_{1:T}|X_0)
```

或多个 members：

```text
X^(1), ..., X^(M)
```

后者用于 risk、tail event、forecast uncertainty，不能只用 deterministic RMSE 评估。

→ [Probabilistic / Ensemble Weather](probabilistic-ensemble-weather.md)

---

## 7. Data-to-Forecast 是新的系统边界

许多 AI forecast model 仍从 `ERA5 / operational analysis` 初始化，这意味着传统 observing+DA pipeline 仍在上游。

`Aardvark Weather` 与 `FuXi Weather` 则把 actual observations → state/forecast 纳入 learning system，因此它们回答的是不同问题。

→ [Data-to-Forecast](data-to-forecast.md)

---

## 8. Short-range / Regional / Downscaling

- radar/satellite nowcasting；
- precipitation；
- local station forecast；
- regional high-resolution forecast；
- deterministic/generative downscaling；
- bias correction。

→ [Nowcasting](nowcasting.md)  
→ [Downscaling / Super-resolution](downscaling-super-resolution.md)

---

## 9. Extremes 与 climate

weather skill 的平均值不能代表：
- tropical cyclone；
- heavy precipitation；
- heatwave/cold spell；
- atmospheric river；
- compound extremes。

climate model 又进一步要求：
- long-term distribution；
- conservation/balance；
- forcing response；
- stable multi-year rollout；
- coupled land/ocean/atmosphere behavior。

→ [Extreme-event Forecasting](extremes-forecasting.md)  
→ [Climate AI](climate-ai.md)  
→ [Earth-system Coupling](earth-system-coupling.md)

---

## 10. 截至 2026-08-20 的 current systems

- `AIFS Single v2` / `AIFS ENS v2`：ECMWF 于 **2026-05-12** operational implementation；
- `Aurora 1.5`：Microsoft 于 **2026-07-09** 发布 open extension，加入更多 variables、hourly resolution 与 probabilistic ensemble capability；
- `WeatherNext 2`：Google current medium-range probabilistic family，并于 **2026-08-06** 宣布开放 model/code/weights 以及 cyclone-related models；
- `NVIDIA Earth-2`：2026-01 发布面向 observation processing、global forecast、nowcasting/downscaling 的 open weather stack；
- `Aardvark Weather` / `FuXi Weather`：2025 peer-reviewed data-to-forecast/end-to-end systems，代表 forecast pipeline 边界向 observations 扩展。

具体版本只在 [2026 Snapshot](../13-2026-snapshot/index.md) 维护。

---

## 11. Primary / official anchors

- GraphCast: https://doi.org/10.1126/science.adi2336
- Pangu-Weather: https://doi.org/10.1038/s41586-023-06185-3
- FuXi: https://doi.org/10.1038/s41612-023-00512-1
- NeuralGCM: https://doi.org/10.1038/s41586-024-07744-y
- GenCast: https://doi.org/10.1038/s41586-024-08252-9
- Aardvark Weather: https://doi.org/10.1038/s41586-025-08897-0
- FuXi Weather: https://doi.org/10.1038/s41467-025-62024-1
- AIFS Version History: https://confluence.ecmwf.int/spaces/UDOC/pages/599165907/AIFS+Version+History
- WeatherNext: https://deepmind.google/science/weathernext/
