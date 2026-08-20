# 01 · Scientific / Physical / Earth AI Knowledge Base

这里是仓库的**知识层**。目标不是把模型按年份堆在一起，而是建立一条可以解释“为什么、怎么做、哪里会错”的知识依赖图。

## 1. 推荐学习顺序

```text
A. 数学 / 概率 / 优化 / 数值分析
   ↓
B. ML / DL / Scientific Computing
   ↓
C. 物理系统 / PDE / 数值模拟 / Observation Operator
   ↓
D. Scientific ML
   ├─ Physics-informed Learning
   ├─ Neural Operators
   ├─ Surrogate / Hybrid Solver
   └─ Differentiable Simulation
   ↓
E. Inverse Problems / Data Assimilation / UQ
   ↓
F. Spatiotemporal / Multiscale / Multimodal AI
   ↓
G. Earth-system Domains
   ├─ Earth Observation / Remote Sensing
   ├─ Terrestrial Carbon Cycle / Carbon Flux
   └─ Weather & Climate
   ↓
H. Earth / Geospatial / Scientific Foundation Models
   ↓
I. Data Engineering / HPC / Evaluation / Reproducibility
   ↓
J. Cross-domain Physical AI
```

> `10-data-assimilation-inverse-uq` 的目录编号较后，是历史路径兼容造成的；**学习时应在进入 Earth-system domains 之前掌握。**

---

## 2. 为什么 Observation Operator 是中轴

Scientific AI 中，最常见的错误是直接写：

```text
x → neural network → y
```

但真实系统通常更像：

```text
latent physical state x
        ↓
physical evolution / process model
        ↓
observation operator H
        ↓
measurement y + noise / support / retrieval effects
        ↓
ML-ready representation
        ↓
learning system
```

例如：

- Optical EO：surface/canopy state 经过 atmosphere + radiative transfer + sensor response 才得到 radiance/reflectance；
- SAR：backscatter 依赖 wavelength、polarization、incidence angle、roughness、dielectric property 与 structure；
- LiDAR：point cloud / waveform 来自 time-of-flight 与 geometry；
- Eddy covariance：半小时 flux 是动态 footprint 上的 weighted integral；
- Weather DA：satellite radiance、radiosonde、station、radar 等通过 observation operators 与 model state 发生联系。

因此，本库把 **state ≠ observation ≠ retrieval/product ≠ label** 作为最重要的统一原则。

---

## 3. 模块入口

### 基础层
- [00 Foundations](00-foundations/index.md)
- [01 ML/DL & Scientific Computing](01-ml-dl-scientific-computing/index.md)
- [02 Physical AI Core](02-physics-ai-core/index.md)

### Scientific ML 方法层
- [03 Physics-informed Learning](03-physics-informed-learning/index.md)
- [04 Neural Operators & Simulation](04-neural-operators-simulation/index.md)
- [10 Data Assimilation / Inverse / UQ](10-data-assimilation-inverse-uq/index.md)
- [05 Spatiotemporal / Multiscale AI](05-spatiotemporal-multiscale-ai/index.md)

### Earth-system 应用层
- [06 Earth Observation AI](06-earth-observation-ai/index.md)
- [07 Terrestrial Carbon-cycle AI](07-carbon-cycle-ai/index.md)
- [08 Weather & Climate AI](08-weather-climate-ai/index.md)

### Foundation / Systems 层
- [09 Earth Foundation Models](09-earth-foundation-models/index.md)
- [11 Data / HPC / Evaluation](11-data-hpc-evaluation/index.md)
- [12 Cross-domain Physical AI](12-cross-domain-physical-ai/index.md)
- [13 2026-08-20 Snapshot](13-2026-snapshot/index.md)

---

## 4. Earth Observation、Carbon、Weather 三者不是三座孤岛

```text
Earth Observation
  ├─ 提供 vegetation / soil / water / atmosphere / structure observations
  ├─ 为 weather DA 提供 satellite radiance / microwave / radar information
  └─ 为 carbon upscaling 提供 spatially explicit predictors

Weather / Climate
  ├─ radiation / temperature / humidity / precipitation / wind / BLH
  ├─ 决定 turbulent transport 与 footprint behavior
  └─ 调节 photosynthesis / respiration / water-energy balance

Terrestrial Carbon
  ├─ 与 water / energy / vegetation state 强耦合
  ├─ 用 EC 提供高频但空间稀疏的 ground observation
  └─ 需要 EO + meteorology + process knowledge 完成时空扩展
```

最终真正需要学习的是 **coupled Earth-system inference**。

---

## 5. 对每个方法至少问 11 个问题

1. target 是 state、flux、parameter、class、probability 还是 future trajectory？
2. observation 是什么？如何从 state 生成？
3. input/output shape 与单位是什么？
4. spatial/temporal support 是什么？
5. physics 在哪一层进入？
6. network/operator 为什么适合这个 representation？
7. loss 是否与物理量尺度和 uncertainty 匹配？
8. train 与 inference / rollout 是否不同？
9. split 是否真正测试了空间/时间/环境 OOD？
10. metric 是否与 scientific objective 一致？
11. 原始来源能确认哪些事实？哪些只是 repository synthesis？

详细写作规范见 [KNOWLEDGE_UNIT_STANDARD.md](KNOWLEDGE_UNIT_STANDARD.md)。

---

## 6. 快速入口

- [Detailed Knowledge Index](DETAILED_INDEX.md)：按知识点查页
- [Learning Paths](learning-paths/index.md)：按目标学习
- [2026 Snapshot](13-2026-snapshot/index.md)：查当前模型/系统版本
- [Paper Library](../02-paper-library/index.md)：查 evidence
- [Dataset Library](../04-dataset-library/index.md)：查数据
- [Benchmarks](../05-benchmarks-and-evaluation/index.md)：查评测
