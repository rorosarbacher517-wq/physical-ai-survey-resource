# Physical AI / Scientific AI Knowledge Base

> 面向 **Physical AI、Scientific Machine Learning、Earth AI 与时空智能** 的系统知识库。  
> 当前知识基线：**2026-08-20**。  
> 重点主线：**遥感 / Earth Observation → terrestrial carbon cycle / carbon flux → weather & climate AI**，同时覆盖流体、能源、材料、生物医学与 embodied systems。

这个仓库现在包含两个互补层：

1. **Knowledge layer**：从数学、数值计算、ML/DL、物理建模一路到 Scientific AI、Earth AI、foundation models、HPC 与评测。
2. **Evidence/resource layer**：经核实的 papers、code、datasets、benchmarks、case studies 与 provenance metadata。

它不把 “AI + Physics” 简化为 PINN，也不把 “Physical AI” 只理解为机器人。仓库明确区分：

- **Physics-informed scientific AI**：方程、守恒律、观测算子、数值模拟、数据同化、反问题、代理模型、神经算子、科学基础模型；
- **Embodied physical intelligence**：感知、世界模型、规划、控制、robot learning、VLA、sim-to-real。

---

## 1. Knowledge dependency map

```text
Math / Probability / Optimization / Numerical Methods
                    ↓
Machine Learning / Deep Learning / Scientific Computing
                    ↓
Physical Systems / PDEs / Dynamical Systems / Observation Physics
                    ↓
Physics-informed Learning / Constraints / Symmetry
                    ↓
Neural Operators / Surrogates / Differentiable Simulation
                    ↓
Data Assimilation / Inverse Problems / UQ
                    ↓
Spatiotemporal + Multiscale + Multimodal AI
                    ↓
┌────────────────────────┬────────────────────────┬────────────────────────┐
│ Earth Observation AI   │ Carbon-cycle AI        │ Weather & Climate AI   │
│ optical/SAR/LiDAR/SIF  │ EC/footprint/GPP/NEE   │ NWP/DA/ensemble/downsc.│
└────────────────────────┴────────────────────────┴────────────────────────┘
                    ↓
Earth / Scientific Foundation Models
                    ↓
Data Engineering / HPC / Evaluation / Reproducibility
                    ↓
Cross-domain Physical AI / Digital Twins / Embodied Systems
```

**学习入口：** [01 Knowledge Base](01-knowledge-base/index.md)  
**学习路线：** [Learning Paths](01-knowledge-base/learning-paths/index.md)  
**快速变化：** [2026 Snapshot](01-knowledge-base/13-2026-snapshot/index.md)

---

## 2. Core modules

| Layer | Module | Core questions |
|---|---|---|
| 00 | [Math, physics & numerical foundations](01-knowledge-base/00-foundations/index.md) | PDE/ODE、守恒、离散化、稳定性、尺度与单位 |
| 01 | [ML/DL & scientific computing](01-knowledge-base/01-ml-dl-scientific-computing/index.md) | regression、CNN/Transformer/GNN、optimization、GPU |
| 02 | [Physical AI core](01-knowledge-base/02-physics-ai-core/index.md) | physics 到底放在 data/input/architecture/loss/operator/eval 哪一层？ |
| 03 | [Physics-informed learning](01-knowledge-base/03-physics-informed-learning/index.md) | PINN、hard/soft constraints、symmetry、conservation |
| 04 | [Neural operators & simulation](01-knowledge-base/04-neural-operators-simulation/index.md) | FNO/DeepONet、surrogate、hybrid solver、differentiable simulation |
| 05 | [Spatiotemporal & multiscale AI](01-knowledge-base/05-spatiotemporal-multiscale-ai/index.md) | irregular grids、multi-resolution、temporal dynamics、support mismatch |
| 06 | [Earth Observation AI](01-knowledge-base/06-earth-observation-ai/index.md) | sensing physics、optical/SAR/LiDAR/SIF、EO foundation models |
| 07 | [Carbon-cycle AI](01-knowledge-base/07-carbon-cycle-ai/index.md) | EC、footprints、GPP/RECO/NEE、upscaling、process constraints |
| 08 | [Weather & climate AI](01-knowledge-base/08-weather-climate-ai/index.md) | NWP、DA、Graph/Transformer/operator、ensemble、nowcasting、downscaling |
| 09 | [Earth & scientific foundation models](01-knowledge-base/09-earth-foundation-models/index.md) | pretraining、multimodality、transfer、geospatial embeddings |
| 10 | [Data assimilation, inverse & UQ](01-knowledge-base/10-data-assimilation-inverse-uq/index.md) | state estimation、parameter retrieval、uncertainty、calibration |
| 11 | [Data/HPC/evaluation](01-knowledge-base/11-data-hpc-evaluation/index.md) | large-scale data、distributed training、OOD、reproducibility |
| 12 | [Cross-domain Physical AI](01-knowledge-base/12-cross-domain-physical-ai/index.md) | fluids、energy/materials、biomed、robotics、digital twins |
| 13 | [2026-08 Snapshot](01-knowledge-base/13-2026-snapshot/index.md) | only fast-moving, primary-source-confirmed developments |

---

## 3. Priority Earth-system tracks

### Earth Observation / Remote Sensing
从**传感器和观测物理**开始，而不是直接从 ResNet/ViT 开始：radiance/reflectance、atmospheric effects、BRDF、SAR scattering、thermal emission、LiDAR geometry、SIF，再进入 spatial-spectral-temporal learning、multimodal fusion 与 foundation models。

→ [Earth Observation specialty track](06-case-studies/geoscience-remote-sensing/earth-observation/index.md)

### Terrestrial carbon cycle / carbon flux
把 **EC measurement support → footprint → satellite/meteorology → GPP/RECO/NEE → process constraints → tower-to-grid upscaling → uncertainty** 串成完整观测-模型链。

→ [Carbon-flux specialty track](06-case-studies/geoscience-remote-sensing/carbon-flux/index.md)

### Weather & climate
从 **observations → data assimilation → initial state → forecast → ensemble → post-processing/downscaling** 理解 AI weather，而不是只背 GraphCast/Pangu/GenCast 模型名。

→ [Weather & climate specialty track](06-case-studies/geoscience-remote-sensing/weather-and-climate/index.md)

---

## 4. Unified reasoning template

面对任何 Scientific/Physical AI 方法，优先回答：

1. **Physical system**：系统状态、目标变量、空间/时间尺度是什么？
2. **Observation**：传感器真正测到什么？观测算子和 support 是什么？
3. **Representation**：grid/mesh/graph/point/sequence/token 如何表示？shape 与单位是什么？
4. **Physics**：方程、守恒、边界条件、对称性或 process knowledge 是什么？
5. **Integration point**：physics 放在 input、architecture、loss、simulation loop、DA 还是 evaluation？
6. **Learning objective**：supervision、residual、likelihood、score/reward 怎么定义？
7. **Numerics**：离散化、稳定性、误差传播、autoregressive drift 怎么处理？
8. **Scale**：训练、预测、观测、验证的 spatial/temporal support 是否一致？
9. **Generalization**：site/time/region/regime/OOD 怎么划分？
10. **Uncertainty**：aleatoric、epistemic、ensemble、calibration、physical consistency 怎么评估？

---

## 5. Resource libraries

- [Paper library](02-paper-library/index.md)
- [Code library](03-code-library/index.md)
- [Dataset library](04-dataset-library/index.md)
- [Benchmarks and evaluation](05-benchmarks-and-evaluation/index.md)
- [Case studies](06-case-studies/index.md)
- [Extended resources](07-extended-resources/index.md)

### Current resource counts

<!-- resource-counts:start -->
Generated from canonical metadata. Do not edit manually.

- Public papers: 100
- Public code records: 8
- Public datasets: 8
- Public benchmarks: 5
<!-- resource-counts:end -->

---

## 6. Freshness and evidence

The repository separates:

- **Stable fundamentals**: math, physics, numerical methods, ML basics;
- **Evolving methods**: neural operators, foundation-model recipes, hybrid solvers;
- **Fast-moving systems**: operational weather AI, Earth foundation models, new releases.

Fast-moving claims must be supported by an original paper, official project/repository, official model card, or institutional source. Unknown implementation details remain **unknown** rather than being inferred from marketing language.

See [Audit & Update Policy](AUDIT_AND_UPDATE_POLICY.md).

---

## 7. Build and validation

```bash
python -m scripts.generate_indexes
python -m scripts.validate_metadata
python -m scripts.check_internal_links
python -m scripts.check_generated_files
python -m scripts.check_large_files
python -m scripts.check_repository_hygiene
pytest
```

Network checks are separated:

```bash
python -m scripts.verify_external_links --respect-cache --report
```

New canonical resources still follow the metadata/provenance rules in [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
