# 12 · Cross-domain Physical AI

Earth-system AI 是本仓库的重点特色方向，但 Physical AI 还需要覆盖其他物理系统，以及“AI 在真实世界中行动”的 embodied branch。

统一抽象可以写成：

```text
physical state
→ dynamics / governing process
→ observation
→ estimation / representation
→ prediction / decision
→ uncertainty
→ action / control (if active system)
→ new physical state
```

---

## 1. 两类 Physical AI 问题

### Scientific / Engineering Physical AI
主要目标是解释、反演、预测、模拟、设计或优化物理系统。

代表领域：
- fluids / aerodynamics；
- energy / materials；
- biomedical mechanics；
- Earth-system AI；
- digital twins。

### Embodied Physical AI / Robotics
主要目标是形成：

```text
perception
→ state estimation
→ physical/world model
→ planning
→ control/action
→ feedback
```

这里 action 会改变后续 observation distribution，因此必须额外考虑 control loop、contact、latency、safety 与 recovery。

---

## 2. 领域地图

### Fluids / Aerodynamics
PDE、turbulence、operator learning、surrogate、control。

### Energy / Materials
molecular/graph/equivariant models、property prediction、inverse design、active learning。

### Biomedical Mechanics
imaging/measurement、fluid/solid mechanics、digital patient/twin、inverse parameter estimation。

### Digital Twins
sensor update、state estimation、simulation/prediction、decision/control 的持续闭环。

### Embodied Physical AI / Robotics
sensor physics、3D geometry、SLAM/state estimation、robot dynamics、world models、planning/control、robot learning、VLA、sim-to-real、safety。

→ [Embodied Physical AI / Robotics](embodied-robotics/index.md)

---

## 3. 共享方法

- Observation Operator；
- PINN / Neural Operator；
- GNN / equivariance；
- differentiable simulation；
- inverse problem / state estimation；
- Bayesian UQ / calibration；
- surrogate / world model；
- optimization / MPC；
- multimodal fusion；
- foundation model；
- OOD evaluation。

---

## 4. 跨领域学习为什么有价值

- weather learned parameterization 与 turbulence closure 都涉及 unresolved process；
- EO retrieval 与 medical imaging 都可表示成 observation/inverse problem；
- carbon footprint 与 robot camera/LiDAR 都要求明确 `state → observation` mapping；
- weather DA 与 robot sensor fusion 都通过 dynamics prior + observations 更新 latent state；
- differentiable simulator 可服务 fluid inverse problem，也可服务 robot system identification/control；
- Earth FM 与 robot FM 都面对 multimodal pretraining、adaptation 与 OOD，但数据生成机制和 evaluation boundary 不同。

---

## Pages

- [Fluids / Aerodynamics](fluids-aerodynamics.md)
- [Energy / Materials](energy-materials.md)
- [Biomedical Mechanics](biomedical-mechanics.md)
- [Digital Twins / Embodied bridge](digital-twins-embodied.md)
- [Embodied Physical AI / Robotics](embodied-robotics/index.md)
