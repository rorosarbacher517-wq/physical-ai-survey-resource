# 01 · Scientific / Physical / Earth AI Knowledge Base

这里是仓库的知识层。目标不是按年份堆模型，而是建立可以解释“为什么、怎么做、哪里会错”的知识依赖图。

## 1. 总学习结构

```text
A. 数学 / 概率 / 优化 / 数值分析
   ↓
B. ML / DL / Scientific Computing
   ↓
C. Physical System / Dynamics / Observation Operator
   ↓
D. Physics-informed Learning / Neural Operators / Differentiable Simulation
   ↓
E. Inverse Problems / Data Assimilation / UQ
   ↓
F. Spatiotemporal / Multiscale / Multimodal AI
   ↓
   ┌───────────────────────────────┴───────────────────────────────┐
   ↓                                                               ↓
G1. Scientific / Earth AI                              G2. Embodied Physical AI
    ├─ Earth Observation                                   ├─ Perception / 3D
    ├─ Carbon Cycle                                        ├─ State Estimation
    └─ Weather / Climate                                   ├─ Dynamics / Contact
   ↓                                                       ├─ World Models
H1. Earth / Geospatial FM                                 ├─ Planning / Control
                                                            ├─ Robot Learning / VLA
                                                            └─ Sim-to-Real / Safety
   └───────────────────────────────┬───────────────────────────────┘
                                   ↓
I. Data Engineering / HPC / Evaluation / Reproducibility
                                   ↓
J. Cross-domain Physical AI synthesis
```

Earth-system AI 仍然是仓库的重点特色；Embodied / Robotics 补齐 Physical AI 中“感知并作用于真实物理世界”的另一条主干。

---

## 2. 统一问题：state、observation、action

很多 AI 图会简化成：

```text
x → neural network → y
```

但 Physical AI 更常见：

```text
latent physical state x_t
        ↓ dynamics / process
observation operator H
        ↓
measurement o_t + noise / support / sensor effects
        ↓
estimation / representation z_t
        ↓
prediction or decision
        ↓
action a_t (active systems)
        ↓
new physical state x_{t+1}
```

Earth Observation、EC flux、weather DA、robot camera/LiDAR、SLAM 和 control 都可以放进这个统一框架，只是 observation physics、state definition、action interface 与 time scale 不同。

---

## 3. 模块入口

### 基础 / Scientific ML
- [00 Foundations](00-foundations/index.md)
- [01 ML/DL & Scientific Computing](01-ml-dl-scientific-computing/index.md)
- [02 Physical AI Core](02-physics-ai-core/index.md)
- [03 Physics-informed Learning](03-physics-informed-learning/index.md)
- [04 Neural Operators & Simulation](04-neural-operators-simulation/index.md)
- [10 Data Assimilation / Inverse / UQ](10-data-assimilation-inverse-uq/index.md)
- [05 Spatiotemporal / Multiscale AI](05-spatiotemporal-multiscale-ai/index.md)

### Earth-system 主干
- [06 Earth Observation AI](06-earth-observation-ai/index.md)
- [07 Terrestrial Carbon-cycle AI](07-carbon-cycle-ai/index.md)
- [08 Weather & Climate AI](08-weather-climate-ai/index.md)
- [09 Earth Foundation Models](09-earth-foundation-models/index.md)

### Embodied Physical AI 主干
- [12 Embodied Physical AI / Robotics](12-cross-domain-physical-ai/embodied-robotics/index.md)

### Systems / Evaluation / Cross-domain
- [11 Data / HPC / Evaluation](11-data-hpc-evaluation/index.md)
- [12 Cross-domain Physical AI](12-cross-domain-physical-ai/index.md)
- [13 2026-08-20 Snapshot](13-2026-snapshot/index.md)

---

## 4. Earth-system 内部耦合

```text
Earth Observation
↔ Weather / Climate
↔ Carbon / Water / Energy
```

EO 提供 spatial observations；weather 提供 atmospheric forcing 与 dynamics；carbon/water/energy processes 又反馈生态与地表状态。真正困难的是 observation support、scale、process coupling 与 OOD，而不是把更多 channels 输入同一个 network。

---

## 5. Embodied 与 Scientific AI 的桥

```text
Scientific AI                         Embodied Robotics
state                                 state
↓                                     ↓
observation operator                  sensor model
↓                                     ↓
inverse / DA                          state estimation / SLAM
↓                                     ↓
dynamics / simulator                  robot/world dynamics
↓                                     ↓
prediction                            world model
↓                                     ↓
optimization                          planning / MPC
                                      ↓
                                      action / feedback
```

机器人方向额外强调 action-induced distribution shift、contact、control latency、real-time constraints 与 physical safety。

---

## 6. 对每个方法至少问

1. physical state / target 是什么？
2. observation 如何产生？
3. input/output shape、units、coordinate frame 是什么？
4. dynamics / governing process 是什么？
5. physics/geometry 在哪一层进入？
6. network/operator/policy 为什么适合这个 representation？
7. loss/reward 与 uncertainty 是否合理？
8. train 与 inference/rollout/deployment 是否不同？
9. split 是否真正测试 OOD？
10. metric 是否对应最终 scientific/task objective？
11. 来源能确认哪些事实，哪些只是 synthesis？

详细规范见 [KNOWLEDGE_UNIT_STANDARD.md](KNOWLEDGE_UNIT_STANDARD.md)。

---

## 7. 快速入口

- [Detailed Knowledge Index](DETAILED_INDEX.md)
- [Learning Paths](learning-paths/index.md)
- [2026 Snapshot](13-2026-snapshot/index.md)
- [Paper Library](../02-paper-library/index.md)
- [Dataset Library](../04-dataset-library/index.md)
- [Benchmarks](../05-benchmarks-and-evaluation/index.md)
