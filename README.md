# Physical AI / Scientific AI / Earth AI 系统知识库

> 面向 **Scientific Machine Learning、Physical AI、Earth Observation、Terrestrial Carbon Cycle、Weather & Climate AI、Embodied AI / Robotics** 的系统学习与研究知识库。  
> **知识基线：2026-08-20。**  
> 写作规则：**中文负责解释，英文负责不可替代的专业名称。** 模型名、论文标题、数据集名、变量名、公式、tensor shape、代码/API、标准缩写保留英文。

这个仓库不是论文列表，也不按热门模型名称组织。目标是从数学、数值计算、观测与动力学出发，建立两条相互连接的 Physical AI 主干：

1. **Scientific / Earth AI**：理解、反演、模拟和预测物理/地球系统；
2. **Embodied Physical AI / Robotics**：感知真实物理环境、估计状态、预测后果、规划并执行动作。

每个知识点尽量连接到可核实的 paper / code / dataset / benchmark / official source。

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
┌──────────────────────────────────────┴──────────────────────────────────────┐
↓                                                                             ↓
Scientific / Earth AI                                             Embodied Physical AI
↓                                                                             ↓
┌────────────────────┬────────────────────┬────────────────────┐     Sensor / Perception
│ Earth Observation  │ Carbon-cycle AI    │ Weather/Climate AI │              ↓
│ RS / Retrieval     │ EC / Footprint     │ NWP / DA / Forecast│     Geometry / 3D / SE(3)
└────────────────────┴────────────────────┴────────────────────┘              ↓
↓                                                                    State Estimation / SLAM
Earth / Geospatial Foundation Models                                          ↓
                                                                     Kinematics / Dynamics
                                                                              ↓
                                                                   World Models / Reasoning
                                                                              ↓
                                                                    Planning / Control
                                                                              ↓
                                                                     Robot Learning / VLA
                                                                              ↓
                                                                   Simulation / Sim-to-Real
                                                                              ↓
                                                                    Safety / Real Feedback
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ↓
                    Data Engineering / HPC / Evaluation / Reproducibility
                                       ↓
                    Cross-domain Physical AI / Digital Twins
                                       ↓
                         2026-08-20 Fast-moving Snapshot
```

核心原则：

> **先弄清 physical state、observation、dynamics、support/coordinate frame，以及 action 是否会反过来改变系统，再谈 neural network。**

---

## 2. 为什么这样组织

Physical AI 中最容易出错的地方往往不是 network layer，而是 system boundary：

- satellite pixel 是经过 radiative transfer、sensor response、geometry 与 preprocessing 后的 observation；
- eddy-covariance flux 是动态 upwind footprint 上的 turbulence-weighted integral；
- weather forecast 是 `observation → DA → initial state → forecast → ensemble → verification` 的系统；
- robot camera/LiDAR/IMU 只提供 partial observations，不等于完整 world state；
- VLA 输出 action 后，真实 robot dynamics、contact 与 controller 决定实际 state transition；
- prediction resolution、simulation success 或 offline action accuracy 都不自动等于真实部署有效性。

所以本仓库把 **observation physics、state estimation、dynamics、scale/support、OOD、uncertainty 与 closed-loop evaluation** 作为跨领域主线。

---

## 3. 模块地图

| 存储模块 | 学习位置 | 主要内容 |
|---|---:|---|
| [00 Foundations](01-knowledge-base/00-foundations/index.md) | ① | Linear Algebra、Probability、Optimization、ODE/PDE、Numerical Methods、Scale/Support |
| [01 ML/DL & Scientific Computing](01-knowledge-base/01-ml-dl-scientific-computing/index.md) | ② | Classical ML、CNN、Transformer、GNN、Autograd、PyTorch/JAX、GPU |
| [02 Physical AI Core](01-knowledge-base/02-physics-ai-core/index.md) | ③ | Observation operators、conservation、symmetry、dimensional priors、hybrid design |
| [03 Physics-informed Learning](01-knowledge-base/03-physics-informed-learning/index.md) | ④ | PINN、hard/soft constraints、optimization failure modes |
| [04 Neural Operators & Simulation](01-knowledge-base/04-neural-operators-simulation/index.md) | ④ | FNO、DeepONet、surrogates、hybrid solvers、differentiable simulation |
| [10 DA / Inverse / UQ](01-knowledge-base/10-data-assimilation-inverse-uq/index.md) | ⑤ | Bayesian inverse、state estimation、DA、uncertainty/calibration |
| [05 Spatiotemporal / Multiscale AI](01-knowledge-base/05-spatiotemporal-multiscale-ai/index.md) | ⑥ | grid/mesh/point/sequence、multiresolution、multimodality、support-aware learning |
| [06 Earth Observation AI](01-knowledge-base/06-earth-observation-ai/index.md) | ⑦ | sensing physics、Optical、SAR、LiDAR、Thermal、SIF、multisensor、EO FM |
| [07 Carbon-cycle AI](01-knowledge-base/07-carbon-cycle-ai/index.md) | ⑧ | EC、flux footprint、GPP/RECO/NEE、process constraints、tower-to-grid |
| [08 Weather & Climate AI](01-knowledge-base/08-weather-climate-ai/index.md) | ⑧ | NWP、DA、AI forecast、ensemble、nowcasting、downscaling、climate |
| [09 Earth Foundation Models](01-knowledge-base/09-earth-foundation-models/index.md) | ⑨ | EO FM、geospatial embeddings、Earth-system FM、pretraining/adaptation/evaluation |
| [12 Embodied Physical AI / Robotics](01-knowledge-base/12-cross-domain-physical-ai/embodied-robotics/index.md) | ⑨ | perception、3D、SLAM、dynamics、world model、planning/control、VLA、sim-to-real、safety |
| [11 Data/HPC/Evaluation](01-knowledge-base/11-data-hpc-evaluation/index.md) | ⑩ | data lineage、distributed training、benchmarking、reproducibility |
| [12 Cross-domain Physical AI](01-knowledge-base/12-cross-domain-physical-ai/index.md) | ⑪ | fluids、energy/materials、biomedical、digital twins、cross-domain synthesis |
| [13 2026 Snapshot](01-knowledge-base/13-2026-snapshot/index.md) | ⑫ | 截至 2026-08-20 的 fast-moving knowledge |

> 文件夹编号用于保持已有链接兼容；真正学习顺序以 [Learning Paths](01-knowledge-base/learning-paths/index.md) 为准。

---

## 4. 四条重点路线

### 4.1 Earth Observation / Remote Sensing

```text
radiation / ranging
→ atmosphere + surface interaction
→ sensor response / geometry
→ radiance / reflectance / backscatter / point cloud / SIF
→ calibration / retrieval / QA
→ spatial-spectral-temporal representation
→ multisensor / foundation representation
→ geophysical/ecological inference
→ geospatial/OOD/scale-aware validation
```

入口：[Earth Observation AI](01-knowledge-base/06-earth-observation-ai/index.md)

### 4.2 Terrestrial Carbon Cycle / Carbon Flux

```text
photosynthesis / respiration
→ GPP / RECO / NEE
→ EC measurement
→ dynamic flux footprint
→ EO + meteorology + structure
→ process-aware / multimodal learning
→ observation operator
→ tower supervision / upscaling
→ uncertainty / extremes / OOD
```

入口：[Carbon-cycle AI](01-knowledge-base/07-carbon-cycle-ai/index.md)

### 4.3 Weather & Climate AI

```text
observing system
→ QC / observation operator
→ data assimilation
→ initial state
→ forecast dynamics
→ deterministic / probabilistic rollout
→ ensemble / downscaling
→ extremes / coupled climate
→ verification / calibration
```

入口：[Weather & Climate AI](01-knowledge-base/08-weather-climate-ai/index.md)

### 4.4 Embodied Physical AI / Robotics

```text
robot + environment
→ RGB / Depth / LiDAR / IMU / Tactile / Proprioception
→ geometry / 3D representation
→ state estimation / SLAM
→ kinematics / dynamics / contact
→ world model / physical reasoning
→ task & motion planning
→ feedback control / MPC
→ imitation / RL / generative policy
→ VLA / robot foundation model
→ simulation / sim-to-real
→ safety / real-world feedback
```

入口：[Embodied Physical AI / Robotics](01-knowledge-base/12-cross-domain-physical-ai/embodied-robotics/index.md)

---

## 5. 统一知识单元模板

每篇核心知识页尽量回答：

1. physical system / task 是什么？
2. state、observation、action 分别是什么？
3. input/output shape、unit、coordinate frame 是什么？
4. governing process / dynamics / observation model 是什么？
5. model architecture 在解决什么表示问题？
6. training label/loss/reward/sampling 怎么定义？
7. inference/rollout/control loop 如何运行？
8. scale/support/time frequency/latency 是否匹配？
9. IID/OOD/blocked/closed-loop evaluation 怎么做？
10. uncertainty / calibration / safety 怎么处理？
11. failure modes 与 evidence boundary 是什么？

完整模板：[Knowledge-unit Standard](01-knowledge-base/KNOWLEDGE_UNIT_STANDARD.md)

---

## 6. 2026-08-20 当前前沿入口

Earth-system fast-moving 内容见 [2026 Snapshot](01-knowledge-base/13-2026-snapshot/index.md)。

Embodied / Robotics 当前快照见 [2026 Robotics Snapshot](01-knowledge-base/13-2026-snapshot/embodied-robotics.md)，重点包括：
- `Gemini Robotics 2` official release（2026-07-30）；
- `GR00T N1.6` 与 open simulation/evaluation stack（2026-01-05）；
- `V-JEPA 2` action-conditioned world-model route；
- 2026 video-world-model physics interpretability；
- current VLA / robot-foundation-model evaluation boundary。

快速变化内容只记录可由 primary/official source 确认的版本和论文状态；closed system details 未公开时保持 `unknown / not publicly disclosed`。

---

## 7. Evidence / Resource layer

知识层负责理解；资源层负责证据与可追溯性。

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

- 基础数学/物理/robotics mechanics：以 textbook-level 共识与经典论文为主；
- 方法：优先 original paper + official code；
- fast-moving system/model：必须带日期，优先 official institutional page / model card / paper；
- vendor demo/report 与 independent scientific evidence 分开；
- closed-source capability 不等于 internal architecture 已公开；
- preprint 与 peer-reviewed publication 分开；
- simulation benchmark 与 real-robot deployment 分开；
- 不把 feature importance / correlation 直接写成 causal mechanism。

详细规则：[Audit & Update Policy](AUDIT_AND_UPDATE_POLICY.md)

---

## 9. 仓库验证

```bash
python -m scripts.full_check
python -m scripts.verify_external_links --respect-cache --report
```

Canonical metadata 与 taxonomy 继续遵守 [AGENTS.md](AGENTS.md) 和 [CONTRIBUTING.md](CONTRIBUTING.md)。
