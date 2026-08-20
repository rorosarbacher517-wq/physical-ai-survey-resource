# 13 · 2026-08-20 Fast-moving Snapshot

> **Knowledge cutoff: 2026-08-20.**  
> 这一页只记录容易随版本/发布日期变化的内容。稳定概念仍放在各知识模块。  
> 状态标签：`Official` = 官方机构/产品；`Peer-reviewed` = 已正式发表；`Preprint` = 未按正式期刊论文处理。

---

# A. Weather / Climate AI

## A1. ECMWF AIFS 已进入 v2 operational generation

截至 2026-08-20：

| System | Status | Date | 需要记住什么 |
|---|---|---:|---|
| `AIFS Single v2` | Official operational | 2026-05-12 | ECMWF deterministic AI forecast v2 |
| `AIFS ENS v2` | Official operational | 2026-05-12 | ECMWF AI ensemble v2 |

ECMWF 的 implementation pages 明确说明 2026-05-12 与 `IFS Cycle 50r1` 联合升级；AIFS v2 还扩展了 wave/snow-related forecast capability。

Official sources:
- https://confluence.ecmwf.int/spaces/FCST/pages/620418808/Implementation+of+AIFS+Single+v2
- https://confluence.ecmwf.int/spaces/FCST/pages/620418893/Implementation+of+AIFS+ENS+v2
- https://confluence.ecmwf.int/spaces/UDOC/pages/599165907/AIFS+Version+History

### 学习意义

AI weather 已不能只讨论“research benchmark 是否超过 HRES”。至少要单独讨论：

```text
research model
vs
operational deterministic model
vs
operational ensemble
```

---

## A2. WeatherNext 2 在 2026-08 进一步开放

`WeatherNext 2` 是 Google 当前 WeatherNext family 的主要模型路线，采用 `Functional Generative Network (FGN)` 生成 probabilistic scenarios。

**2026-08-06** Google DeepMind 发布 cyclone research/open-source update，并说明开放 `WeatherNext 2`、`WeatherNext Cyclones` 相关 code/model weights；developer docs 当前还列出 operational 0.25° 与 mini 1° variants。

Official:
- https://deepmind.google/science/weathernext/
- https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/
- https://developers.google.com/weathernext/guides/models

### 学习意义

weather FM/model evaluation 正从 deterministic global RMSE 走向：
- probabilistic scenarios；
- cyclone-specific structure/intensity；
- operational/product integration；
- open model access。

---

## A3. Aurora 1.5

原始 `Aurora`：Nature 2025，Earth-system foundation model，pretraining 超过 1 million hours diverse geophysical data。

**2026-07-09** Microsoft 发布 `Aurora 1.5`：
- open-source extension；
- additional weather variables；
- hourly temporal resolution；
- probabilistic ensemble capability；
- 与 broader Microsoft Weather deployment 连接。

Official:
- https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/
- https://www.microsoft.com/en-us/research/blog/aurora-1-5-extending-open-foundation-models-for-weather-and-earth-system-applications/

---

## A4. NVIDIA Earth-2 open weather stack

**2026-01-26** NVIDIA 发布 Earth-2 family of open weather models/libraries/frameworks，覆盖：

```text
observation/data processing
→ global forecasting
→ nowcasting
→ regional/downscaling tools
```

这类 platform 的意义是把单模型扩展成 deployable weather-AI stack。

Official:
- https://blogs.nvidia.com/blog/nvidia-earth-2-open-models/
- https://www.nvidia.com/en-us/high-performance-computing/earth-2/

---

## A5. Data-to-Forecast 已成为独立路线

### Aardvark Weather
`Peer-reviewed`, Nature 2025。

关注：remote sensing + in-situ observations → gridded/global + local forecast，deployment 时不依赖 conventional NWP product input。

https://doi.org/10.1038/s41586-025-08897-0

### FuXi Weather
`Peer-reviewed`, Nature Communications 2025。

关注：raw observations → cycling ML DA → forecast every 6 h；包含 instrument/variable-specific observation encoders。

https://doi.org/10.1038/s41467-025-62024-1

### 为什么重要

它们与 GraphCast/Pangu/FuXi forecast-core 解决的是不同 system boundary：

```text
analysis-to-forecast
vs
observation-to-analysis-to-forecast
```

---

## A6. Hybrid weather/climate 在继续扩展

`NeuralGCM` Nature 2024 建立 differentiable dynamical core + learned physics route。

2026 Google Research 又发布 precipitation-focused extension，使用 satellite precipitation observations 改进 learned physics，并重点评估 precipitation mean/extreme/daily cycle。

Sources:
- https://doi.org/10.1038/s41586-024-07744-y
- https://research.google/blog/neuralgcm-harnesses-ai-to-better-simulate-long-range-global-precipitation/

---

# B. Earth Observation / Geospatial Foundation Models

## B1. AlphaEarth Foundations public embedding dataset 已进入可直接使用阶段

截至 2026-08-20，Google official documentation 可确认：
- annual `Satellite Embedding` layers：**2017–2025**；
- **64 channels**；
- GCS COG + Earth Engine access；
- current catalog embeddings generated with `AlphaEarth Foundations v2.1`；
- dataset license `CC-BY 4.0`。

Official:
- https://developers.google.com/earth-engine/guides/aef_on_gcs_readme
- https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL

### 重要接口变化

这类 model 的 downstream workflow 可以是：

```text
read annual embedding raster
→ RF/XGBoost/MLP
→ task
```

而不是：

```text
download FM weights
→ run encoder
→ extract embedding
```

因此 benchmark 应把 **embedding-as-data** 与 **downloadable encoder** 分开。

---

## B2. TESSERA v2

`Preprint`, **2026-07-04**: *TESSERA v2: Scaling Pixel-wise Earth Foundation Models*。

论文报告 controlled scaling study，并研究：
- encoder/data scaling；
- downstream-based model selection；
- distillation；
- Matryoshka representations；
- storage-efficient embedding deployment。

论文中 v2 global embeddings 属于 planned release 描述，不能在当前仓库写成已完整公开产品。

Sources:
- https://arxiv.org/abs/2607.03949
- https://geotessera.org/papers/

---

## B3. MaRS

`Peer-reviewed`, AAAI 2026，published **2026-03-14**。

`MaRS` 面向 VHR SAR–optical multimodal pretraining，引入 cross-granularity contrastive learning 与 meta-modality attention。

Source: https://doi.org/10.1609/aaai.v40i14.38153

---

## B4. TerraMind / Prithvi-EO-2.0 仍是当前核心基线

### TerraMind
`Peer-reviewed`, ICCV 2025。

- nine geospatial modalities；
- generative multimodal any-to-any route；
- dual token/pixel representations。

https://openaccess.thecvf.com/content/ICCV2025/html/Jakubik_TerraMind_Large-Scale_Generative_Multimodality_for_Earth_Observation_ICCV_2025_paper.html

### Prithvi-EO-2.0
`Official/open model`。

- 4.2M global HLS time-series samples；
- 30 m HLS；
- 300M / 600M model variants；
- time/location embedding variants。

https://github.com/NASA-IMPACT/Prithvi-EO-2.0

---

## B5. EO FM 的研究重点正在从“模型数量”转向 evaluation

### PANGAEA
跨 datasets/tasks/sensors/resolutions/geography 的 standardized benchmark route。

https://arxiv.org/abs/2412.04204

### On the foundations of Earth foundation models
`Peer-reviewed Perspective`, Communications Earth & Environment, **2026-01-08**。

https://doi.org/10.1038/s43247-025-03127-x

### SAR foundation-model synthesis
2026 SAR-specific FM review 强调 SAR visual/multimodal/generative routes 与 sensor physics。

这一变化说明：未来重点不是“再列一个 FM”，而是**pretraining data、observation physics、adaptation protocol、OOD 与 uncertainty**。

---

## B6. WorldTensor

`Peer-reviewed Data Descriptor`, Scientific Data, **2026-07-24**。

`WorldTensor` 将 climate、land、ocean、cryosphere、infrastructure、hazards 与 socioeconomic variables harmonize 到 common **0.25° annual framework**，用于 Earth-system FM research。

Source: https://doi.org/10.1038/s41597-026-07913-w

### 学习意义

Earth FM 正从“EO imagery encoder”继续向：

```text
physical Earth system
+ human system
+ hazards / infrastructure
```

的 multimodal planetary representation 扩展。

---

# C. Terrestrial Carbon / Ecohydrology AI

## C1. Flux footprint 在 2026 被进一步系统化

`Peer-reviewed`, Global Change Biology 2026：Chu et al., *Flux Footprints: A Critical Link to Bridge Eddy-Covariance Measurements With Models, Remote Sensing, and Other Observations*。

https://doi.org/10.1111/gcb.70887

### 学习意义

footprint 应被看成**observation mapping / representativeness layer**，而不只是额外 predictor。

---

## C2. Footprint-aware ML 从输入 weighting 向 spatial modeling 扩展

### RSE 2025 footprint + GNN
`Peer-reviewed`：footprint-weighted spatial features + `DeeperGCN` residual correction，研究 tower footprint 内 vegetation heterogeneity。

https://doi.org/10.1016/j.rse.2025.114952

### Science of Remote Sensing 2026
`Peer-reviewed`, June 2026：flux footprint + Random Forest + SHAP 用于 hourly carbon-flux upscaling。

https://doi.org/10.1016/j.srs.2026.100393

这些工作说明 footprint-aware carbon ML 已逐步从 representativeness 分析进入 explicit spatial modeling/upscaling。

---

## C3. Process-constrained joint flux learning

`Peer-reviewed`, ISPRS JPRS 2025：physics-constrained deep learning joint modeling `NEE/GPP/RECO`，展示 carbon-balance constraint 与 large-scale EO/meteo learning 的结合。

https://doi.org/10.1016/j.isprsjprs.2025.06.033

---

## C4. Process-model parameter optimization + EO

`Peer-reviewed`, Earth System Dynamics, **2026-06-01**：*Improving terrestrial carbon flux simulations with machine learning and global Earth observations*。

使用 genetic algorithm + Gaussian-process emulator 与多个 global observations 研究 terrestrial carbon model parameter optimization 和 equifinality。

https://doi.org/10.5194/esd-17-651-2026

### 学习意义

Carbon AI 不只是“直接预测 flux”；另一条路线是：

```text
Earth observations
→ optimize/calibrate process model
→ uncertainty ensemble
→ physically structured simulation
```

---

## C5. Remote sensing + SIF + EC / gap filling

2026 Agricultural and Forest Meteorology：XGBoost 结合 remote sensing/environment/SIF information 用于 EC carbon-flux gap filling。

https://doi.org/10.1016/j.agrformet.2025.110987

2025 JAG：transfer learning with SIF + EC for GPP estimation。

https://doi.org/10.1016/j.jag.2025.104503

说明 carbon multimodality 正从 optical+meteo 扩展到 photosynthesis-related observations 与 water/energy context。

---

## C6. EO Foundation Models × Ecohydrology：刚出现系统 synthesis

`Preprint`, **2026-08-15**：*Earth Observation Foundation Models for Terrestrial Ecohydrology: From Representation Learning to Process Inference*。

https://arxiv.org/abs/2608.15282

该 preprint 关注 EOFM 与 water–energy–carbon process inference 的适配、scale mismatch、reference uncertainty 与 evaluation gap。

### 仓库处理原则

这是 cutoff 前很新的 preprint，因此：
- 可放进 Snapshot；
- 不把其 synthesis 结论写成 settled consensus；
- 后续若正式发表再更新 stable pages。

---

## C7. 2026 的 carbon / ecohydrology hybrid signal

还值得跟踪：
- physically constrained remote-sensing ET，RSE 2026：https://doi.org/10.1016/j.rse.2026.115460
- differentiable ecohydrological land model `ADELM v1.0`，2026 preprint：https://egusphere.copernicus.org/preprints/2026/egusphere-2026-3294/
- knowledge-guided global carbon prediction，KDD 2026：https://doi.org/10.1145/3770855.3818927

这些路线共同指向：

```text
EO representations
+ process constraints / differentiable land models
+ multimodal observations
+ uncertainty/OOD
```

---

# D. 2026-08-20 后续更新 watchlist

之后新增知识时优先检查：

1. `AIFS` operational version changes；
2. `WeatherNext` open/model/service changes；
3. `Aurora` version/model cards；
4. `Earth-2` model releases；
5. `AlphaEarth` annual embedding layer/version；
6. `TESSERA v2` planned embedding release 是否真正完成；
7. EO FM benchmark 对 quantitative ecohydrology/carbon tasks 的新 evidence；
8. footprint-aware carbon public benchmark / multi-site studies；
9. data-to-forecast systems 对 real observations / cycling robustness 的新验证；
10. coupled Earth-system FM datasets/models。

---

# E. 来源规则

本页每次更新必须：
- 写绝对日期；
- 标记 `Official / Peer-reviewed / Preprint`；
- 优先 original paper / official docs；
- closed details 不猜；
- 不把 preprint 当正式发表；
- 不把 product marketing claim 直接改写成 scientific conclusion。

见 [Audit & Update Policy](../../AUDIT_AND_UPDATE_POLICY.md)。
