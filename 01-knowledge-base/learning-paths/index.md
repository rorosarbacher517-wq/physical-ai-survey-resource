# Learning Paths · 从下到上的学习路线

不同目标不需要按文件夹编号机械学习。下面按“依赖关系”安排。

## 路线 A：完整 Scientific / Physical AI

适合希望建立完整体系的人。

```text
1. Linear Algebra / Probability / Optimization
2. ODE/PDE / Dynamical Systems / Numerical Methods
3. Classical ML / Deep Learning / Autograd
4. CNN / Transformer / GNN
5. Conservation / Symmetry / Observation Operator
6. PINN / Neural Operator / Surrogate / Differentiable Simulation
7. Inverse Problems / Data Assimilation / UQ
8. Spatiotemporal / Multiscale / Multimodal AI
9. Earth Observation / Carbon / Weather
10. Earth Foundation Models
11. Data Engineering / HPC / Evaluation
12. Cross-domain Physical AI
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

重点不是记模型，而是理解：**不同 modality 为什么不能简单当作 channel concat。**

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

必须掌握的三个“尺度问题”：
1. tower location ≠ flux source area；
2. satellite pixel size ≠ tower observation support；
3. output grid resolution ≠ independent validation support。

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

学习模型时建议按方法族，而不是年份背名字：

- grid/spectral/operator：`FourCastNet`；
- graph/mesh：`GraphCast`；
- 3D Transformer：`Pangu-Weather`；
- cascade / multi-stage：`FuXi`；
- multimodal/multitask + replay：`FengWu`；
- hybrid differentiable dynamics：`NeuralGCM`；
- probabilistic generative：`GenCast`；
- operational deterministic + ensemble：`AIFS Single / ENS`；
- data-to-forecast：`Aardvark Weather`, `FuXi Weather`；
- Earth-system foundation model：`Aurora`。

---

## 路线 E：Earth / Geospatial Foundation Models

```text
ViT / SSL / MAE / contrastive learning
→ EO-specific tokenization
→ multi-temporal pretraining
→ multimodal pretraining
→ encoder weights vs ready-made embedding products
→ frozen probe / PEFT / full fine-tuning
→ PANGAEA-style evaluation
→ process-sensitive Earth-system downstream tasks
```

核心页：[09 Earth Foundation Models](../09-earth-foundation-models/index.md)

截至 2026-08-20，建议重点理解：`Prithvi-EO-2.0`, `TerraMind`, `AlphaEarth Foundations`, `TESSERA`, `MaRS`, `Aurora` 的**接口差异**，而不是只比较参数量。

---

## 路线 F：从 ML 转入 Scientific AI

如果已经熟悉 Transformer/CNN，可跳过基础神经网络，从以下开始：

1. [Dynamical Systems / PDE](../00-foundations/dynamical-systems-pde.md)
2. [Numerical Methods](../00-foundations/numerical-methods.md)
3. [Observation Operators](../02-physics-ai-core/observation-operators.md)
4. [Hybrid Modeling](../02-physics-ai-core/hybrid-modeling-design.md)
5. [Neural Operators](../04-neural-operators-simulation/neural-operator-family.md)
6. [Data Assimilation](../10-data-assimilation-inverse-uq/data-assimilation.md)
7. 一个 Earth-system domain。

---

## 路线 G：从遥感/地学转入 AI

1. [Classical ML Baselines](../01-ml-dl-scientific-computing/classical-ml-scientific-baselines.md)
2. [Deep Learning Architectures](../01-ml-dl-scientific-computing/deep-learning-architectures.md)
3. [Transformer / GNN for Science](../01-ml-dl-scientific-computing/transformer-gnn-for-science.md)
4. [Spatiotemporal Learning](../05-spatiotemporal-multiscale-ai/temporal-modeling.md)
5. [Multiscale / Multimodal Fusion](../05-spatiotemporal-multiscale-ai/multiscale-multimodal-fusion.md)
6. [Data/HPC](../11-data-hpc-evaluation/index.md)

---

## 每篇论文怎么学

不要只写摘要。建议做一张 study card：

```text
Problem
→ Data / observation
→ Spatial & temporal support
→ Input / output / shape
→ Architecture
→ Physics integration
→ Loss
→ Train / inference
→ Validation split
→ Metrics
→ Main finding
→ Failure / limitation
→ What is reusable
→ Primary source
```
