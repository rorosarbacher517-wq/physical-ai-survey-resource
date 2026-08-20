# Physical AI / Scientific AI / Earth AI 系统知识库

> 面向 **Scientific Machine Learning、Physical AI、Earth Observation、Terrestrial Carbon Cycle、Weather & Climate AI** 的系统学习与研究知识库。  
> **知识基线：2026-08-20。**  
> 写作规则：**中文负责解释，英文负责不可替代的专业名称。** 模型名、论文标题、数据集名、变量名、公式、tensor shape、代码/API、标准缩写保留英文。

这个仓库不是“论文列表”，也不是“把 PINN、GraphCast、Prithvi、碳通量放在一起”。它的目标是建立一条可以从底层一路推到 Earth-system AI 的**知识依赖链**，并把每个知识点连接到可核实的 paper / code / dataset / benchmark / official source。

---

## 1. 从下到上的总知识图

```text
数学 / 概率 / 优化 / 数值分析
        ↓
ML / DL / Scientific Computing
        ↓
ODE / PDE / Dynamical Systems / Conservation / Numerical Solvers
        ↓
Physics-informed Learning / Neural Operators / Surrogates / Differentiable Simulation
        ↓
Observation Operator / Inverse Problems / Data Assimilation / UQ
        ↓
Spatiotemporal / Multiscale / Multimodal Learning
        ↓
┌──────────────────────────┬──────────────────────────┬──────────────────────────┐
│ Earth Observation / RS   │ Terrestrial Carbon AI   │ Weather & Climate AI     │
│ Optical/SAR/LiDAR/SIF    │ EC/Footprint/GPP/NEE    │ NWP/DA/Forecast/Ensemble │
└──────────────────────────┴──────────────────────────┴──────────────────────────┘
        ↓
Earth / Geospatial / Scientific Foundation Models
        ↓
Data Engineering / HPC / Evaluation / Reproducibility
        ↓
Cross-domain Physical AI / Digital Twins / Embodied Systems
        ↓
2026-08-20 Fast-moving Snapshot
```

核心原则只有一句：

> **先弄清 physical state、observation、support 和 governing process，再谈 neural network。**

---

## 2. 为什么重新这样组织

Scientific AI 与普通视觉/语言任务最容易混淆的地方，不在于网络结构，而在于“标签到底代表什么”。例如：

- satellite pixel 不是地面真实状态本身，而是经过 radiative transfer、sensor response、geometry 与 preprocessing 后得到的 observation；
- eddy-covariance flux 不是 tower point value，而是动态 upwind footprint 上的 turbulence-weighted integral；
- weather forecast 不是单个 network 的输出问题，而是 `observation → data assimilation → initial state → forecast → ensemble → post-processing → verification` 的系统；
- 一个 10 m / 30 m prediction 并不自动意味着存在同尺度的独立 ground truth。

因此，本仓库把 **observation physics、support/scale、inverse/DA/UQ、OOD evaluation** 作为横穿所有 Earth AI 模块的主线。

---

## 3. 模块地图

| 存储模块 | 学习位置 | 主要内容 |
|---|---:|---|
| [00 Foundations](01-knowledge-base/00-foundations/index.md) | ① | Linear Algebra、Probability、Optimization、ODE/PDE、Numerical Methods、Scale/Support |
| [01 ML/DL & Scientific Computing](01-knowledge-base/01-ml-dl-scientific-computing/index.md) | ② | Classical ML、CNN、Transformer、GNN、Autograd、PyTorch/JAX、GPU |
| [02 Physical AI Core](01-knowledge-base/02-physics-ai-core/index.md) | ③ | Observation operators、conservation、symmetry、dimensional priors、hybrid design |
| [03 Physics-informed Learning](01-knowledge-base/03-physics-informed-learning/index.md) | ④ | PINN、hard/soft constraints、optimization failure modes |
| [04 Neural Operators & Simulation](01-knowledge-base/04-neural-operators-simulation/index.md) | ④ | FNO、DeepONet、surrogates、hybrid solvers、differentiable simulation |
| [10 DA / Inverse / UQ](01-knowledge-base/10-data-assimilation-inverse-uq/index.md) | ⑤ | Bayesian inverse、state estimation、4D-Var/EnKF、uncertainty/calibration |
| [05 Spatiotemporal / Multiscale AI](01-knowledge-base/05-spatiotemporal-multiscale-ai/index.md) | ⑥ | grid/mesh/point/sequence、multiresolution、multimodality、support-aware learning |
| [06 Earth Observation AI](01-knowledge-base/06-earth-observation-ai/index.md) | ⑦ | sensing physics、Optical、SAR、LiDAR、Thermal、SIF、multisensor、EO FM |
| [07 Carbon-cycle AI](01-knowledge-base/07-carbon-cycle-ai/index.md) | ⑧ | EC、flux footprint、GPP/RECO/NEE、process constraints、tower-to-grid |
| [08 Weather & Climate AI](01-knowledge-base/08-weather-climate-ai/index.md) | ⑧ | NWP、DA、AI forecast、probabilistic ensemble、nowcasting、downscaling、climate |
| [09 Earth Foundation Models](01-knowledge-base/09-earth-foundation-models/index.md) | ⑨ | EO FM、geospatial embeddings、Earth-system FM、pretraining/adaptation/evaluation |
| [11 Data/HPC/Evaluation](01-knowledge-base/11-data-hpc-evaluation/index.md) | ⑩ | data lineage、distributed training、benchmarking、reproducibility |
| [12 Cross-domain Physical AI](01-knowledge-base/12-cross-domain-physical-ai/index.md) | ⑪ | fluids、energy/materials、digital twins、embodied systems |
| [13 2026 Snapshot](01-knowledge-base/13-2026-snapshot/index.md) | ⑫ | 只记录截至 2026-08-20 可由 primary/official source 确认的快速变化 |

> 文件夹编号为了保持已有链接兼容；**真正学习顺序以上表和 Learning Paths 为准。**

---

## 4. 三条重点 Earth-system 主线

### 4.1 Earth Observation / Remote Sensing

```text
Electromagnetic radiation / ranging
→ atmosphere + surface/canopy interaction
→ sensor geometry / response
→ radiance / reflectance / backscatter / waveform / SIF
→ calibration / correction / retrieval / QA
→ spatial-spectral-temporal representation
→ multisensor fusion / foundation representation
→ downstream geophysical or ecological inference
→ geospatial/OOD/scale-aware validation
```

入口：[Earth Observation AI](01-knowledge-base/06-earth-observation-ai/index.md)

### 4.2 Terrestrial Carbon Cycle / Carbon Flux

```text
photosynthesis / respiration / disturbance
→ GPP / RECO / NEE
→ turbulent transport
→ eddy-covariance measurement
→ dynamic flux footprint
→ EO + meteorology + soil moisture + structure
→ process-aware / multimodal learning
→ observation operator
→ tower-scale supervision
→ tower-to-grid upscaling
→ uncertainty / extremes / OOD
```

入口：[Carbon-cycle AI](01-knowledge-base/07-carbon-cycle-ai/index.md)

### 4.3 Weather & Climate AI

```text
observing system
→ QC / observation operator
→ data assimilation / state estimation
→ analysis / initial condition
→ forecast dynamics
→ deterministic / probabilistic rollout
→ ensemble / post-processing / downscaling
→ extremes / impact-relevant diagnostics
→ verification / calibration
→ coupled Earth-system / climate
```

入口：[Weather & Climate AI](01-knowledge-base/08-weather-climate-ai/index.md)

---

## 5. 每个知识点统一回答什么

每一篇核心知识页尽量回答以下问题：

1. **问题是什么**：physical system 与 target 是什么？
2. **观测是什么**：sensor/tower/model product 真正测到什么？
3. **输入输出与 shape**：`[B,T,C,H,W]`、`[B,N,D]`、grid/mesh/point 如何变化？
4. **数学与物理**：equation、conservation、symmetry、boundary condition、observation operator 是什么？
5. **模型结构**：CNN / Transformer / GNN / operator / hybrid 分别在做什么？
6. **训练**：label、loss、mask、sampling、normalization、split 如何定义？
7. **推理/rollout**：train 与 inference 有什么区别？误差如何传播？
8. **scale/support**：native resolution、prediction grid、observation support、validation support 是否一致？
9. **evaluation**：IID、site/region/time blocked、OOD、extreme、probabilistic、physical diagnostics 怎么做？
10. **failure modes**：哪些情况下“指标好”但科学结论仍不可信？
11. **来源**：优先给 original paper、DOI、official repo/model card/dataset provider。

完整模板：[Knowledge-unit Standard](01-knowledge-base/KNOWLEDGE_UNIT_STANDARD.md)

---

## 6. 2026-08-20 当前应知道的前沿

截至本知识基线，Earth AI 需要特别关注：

- **operational AI weather**：ECMWF `AIFS Single v2` 与 `AIFS ENS v2` 已于 2026-05-12 operational；
- **probabilistic weather**：`GenCast`、`AIFS ENS`、generative ensemble 与 calibration 已成为独立问题，而不是 deterministic RMSE 的附属项；
- **end-to-end data-to-forecast**：`Aardvark Weather`、`FuXi Weather` 把 raw/near-raw observations 到 forecast 的链条纳入学习系统；
- **hybrid weather/climate**：`NeuralGCM` 代表 differentiable dynamics + learned components 的路线；
- **Earth-system FM**：`Aurora` 以跨 geophysical tasks 的 pretraining/adaptation 为核心；
- **EO multimodal FM**：`TerraMind`、`Prithvi-EO-2.0`、`MaRS` 等推动 optical/SAR/time/multimodal representation；
- **ready-to-use geospatial embeddings**：`AlphaEarth Foundations`、`TESSERA` 代表“预计算 embedding field”这一与传统 downloadable encoder 不同的使用接口；
- **EO FM evaluation**：`PANGAEA` 强调跨 sensor、resolution、task、geography 的统一评测，且 foundation models 并非在所有 downstream tasks 上都必然优于 supervised baselines；
- **carbon observation support**：2026 年 footprint synthesis 再次强调 flux footprint 是连接 EC、remote sensing 与 models 的关键 observation mapping；
- **carbon + multimodal/process AI**：footprint-aware spatial modeling、physics-constrained joint NEE/GPP/RECO、SIF/soil-moisture/EO integration 与 extreme/OOD evaluation 正在汇合。

所有快速变化的版本号、发布日期和官方链接统一放在 [2026 Snapshot](01-knowledge-base/13-2026-snapshot/index.md)，避免把易过时信息散落到基础知识页。

---

## 7. Evidence / Resource layer

知识层负责“理解”；资源层负责“证据与可追溯性”。

- [Paper Library](02-paper-library/index.md)
- [Code Library](03-code-library/index.md)
- [Dataset Library](04-dataset-library/index.md)
- [Benchmarks & Evaluation](05-benchmarks-and-evaluation/index.md)
- [Case Studies](06-case-studies/index.md)
- [Extended Resources](07-extended-resources/index.md)

### Current resource counts

<!-- resource-counts:start -->
Generated from canonical metadata. Do not edit manually.

- Public papers: 100
- Public code records: 8
- Public datasets: 8
- Public benchmarks: 5
<!-- resource-counts:end -->

---

## 8. 更新与可信度规则

- 基础数学/物理：以 textbook-level 共识与经典论文为主，不追版本。
- 方法：优先 original paper + official code。
- fast-moving model/system：必须带**日期**，优先 official institutional page / model card / paper。
- closed-source capability 不等于 internal architecture 已公开；未知就写 `unknown / not publicly disclosed`。
- preprint 与 peer-reviewed publication 分开标注。
- 不把 output resolution 等价为 independent validation resolution。
- 不把 feature importance / correlation 直接写成 causal mechanism。

详细规则：[Audit & Update Policy](AUDIT_AND_UPDATE_POLICY.md)

---

## 9. 仓库验证

```bash
python -m scripts.full_check
python -m scripts.verify_external_links --respect-cache --report
```

生成视图、canonical metadata 与 taxonomy 继续遵守 [AGENTS.md](AGENTS.md) 和 [CONTRIBUTING.md](CONTRIBUTING.md)。
