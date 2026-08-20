# Learning Paths · 从下到上的学习路线

不同目标不需要按文件夹编号机械学习。下面按依赖关系安排。

## 路线 A：完整 Scientific / Physical AI

```text
1. Linear Algebra / Probability / Optimization
2. ODE/PDE / Dynamical Systems / Numerical Methods
3. Classical ML / Deep Learning / Autograd
4. CNN / Transformer / GNN
5. Conservation / Symmetry / Observation Operator
6. PINN / Neural Operator / Surrogate / Differentiable Simulation
7. Inverse Problems / Data Assimilation / UQ
8. Spatiotemporal / Multiscale / Multimodal AI
9. 选择 domain branch
   ├─ Earth Observation / Carbon / Weather
   └─ Embodied Physical AI / Robotics
10. Foundation Models / World Models
11. Data Engineering / HPC / Evaluation
12. Cross-domain synthesis
```

建议入口：
- [00 Foundations](../00-foundations/index.md)
- [01 ML/DL](../01-ml-dl-scientific-computing/index.md)
- [02 Physical AI Core](../02-physics-ai-core/index.md)
- [10 DA / Inverse / UQ](../10-data-assimilation-inverse-uq/index.md)

---

## 路线 B：Remote Sensing / Earth Observation

```text
EM / radiation basics
→ radiative transfer / observation physics
→ Optical + Hyperspectral
→ SAR / Microwave
→ LiDAR / 3D
→ Thermal / SIF
→ preprocessing / QA / geometry / resampling
→ spatial-spectral-temporal learning
→ multisensor fusion
→ retrieval / inversion
→ EO foundation models / geospatial embeddings
→ geospatial OOD evaluation
```

核心页：[06 Earth Observation AI](../06-earth-observation-ai/index.md)

---

## 路线 C：Terrestrial Carbon / Carbon Flux

```text
carbon-cycle processes
→ GPP / RECO / NEE
→ eddy covariance
→ flux partitioning
→ flux footprint
→ EO + meteorology + soil moisture + 3D structure
→ carbon ML / DL / process constraints
→ footprint-aware observation operator
→ tower-to-grid upscaling
→ extremes / OOD / uncertainty
```

核心页：[07 Carbon-cycle AI](../07-carbon-cycle-ai/index.md)

三个尺度问题：tower location ≠ flux source area；satellite pixel size ≠ tower observation support；output grid resolution ≠ independent validation support。

---

## 路线 D：Weather & Climate AI

```text
atmospheric state + governing equations
→ NWP discretization / parameterization
→ global observing system
→ data assimilation
→ analysis / initial condition
→ AI forecast backbone
→ autoregressive rollout
→ probabilistic / ensemble forecast
→ nowcasting / regional downscaling
→ extremes
→ coupled Earth-system / climate
→ verification / calibration
```

核心页：[08 Weather & Climate AI](../08-weather-climate-ai/index.md)

---

## 路线 E：Earth / Geospatial Foundation Models

```text
ViT / SSL / MAE / contrastive learning
→ EO-specific tokenization
→ multi-temporal pretraining
→ multimodal pretraining
→ encoder weights vs ready-made embedding products
→ frozen probe / PEFT / full fine-tuning
→ geospatial/OOD evaluation
→ process-sensitive Earth-system downstream tasks
```

核心页：[09 Earth Foundation Models](../09-earth-foundation-models/index.md)

---

## 路线 F：从 ML 转入 Scientific AI

1. [Dynamical Systems / PDE](../00-foundations/dynamical-systems-pde.md)
2. [Numerical Methods](../00-foundations/numerical-methods.md)
3. [Observation Operators](../02-physics-ai-core/observation-operators.md)
4. [Hybrid Modeling](../02-physics-ai-core/hybrid-modeling-design.md)
5. [Neural Operators](../04-neural-operators-simulation/neural-operator-family.md)
6. [Data Assimilation](../10-data-assimilation-inverse-uq/data-assimilation.md)
7. 选择一个 domain branch。

---

## 路线 G：从遥感/地学转入 AI

1. [Classical ML Baselines](../01-ml-dl-scientific-computing/classical-ml-scientific-baselines.md)
2. [Deep Learning Architectures](../01-ml-dl-scientific-computing/deep-learning-architectures.md)
3. [Transformer / GNN for Science](../01-ml-dl-scientific-computing/transformer-gnn-for-science.md)
4. [Spatiotemporal Learning](../05-spatiotemporal-multiscale-ai/temporal-modeling.md)
5. [Multiscale / Multimodal Fusion](../05-spatiotemporal-multiscale-ai/multiscale-multimodal-fusion.md)
6. [Data/HPC](../11-data-hpc-evaluation/index.md)

---

## 路线 H：Embodied Physical AI / Robotics

建议不要从 VLA 模型表开始，而按真实机器人闭环学习：

```text
robot/environment/task
→ sensor observation physics
→ camera geometry / SE(3) / 3D representation
→ state estimation / sensor fusion / SLAM
→ kinematics / dynamics / contact
→ world model / physical reasoning
→ task & motion planning
→ feedback control / MPC / whole-body control
→ imitation learning / RL / generative policy
→ VLA / robot foundation models
→ simulation / synthetic data / sim-to-real
→ safety / OOD / deployment
```

核心页：[Embodied Physical AI / Robotics](../12-cross-domain-physical-ai/embodied-robotics/index.md)

必须区分：
1. `state ≠ observation`；
2. semantic plan ≠ kinematically/dynamically feasible motion；
3. offline action accuracy ≠ closed-loop task success；
4. simulation success ≠ real-robot robustness；
5. VLA capability ≠ complete safety system。

---

## 每篇论文怎么学

```text
Problem
→ Data / observation
→ Spatial/temporal or control support
→ Input / output / shape
→ Architecture
→ Physics / geometry / dynamics integration
→ Loss / reward
→ Train / inference / rollout
→ Validation split
→ Metrics
→ Main finding
→ Failure / limitation
→ What is reusable
→ Primary source
```
