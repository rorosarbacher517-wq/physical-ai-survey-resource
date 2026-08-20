# 12 · Cross-domain Physical AI

Earth-system 是本仓库的重点，但 Scientific / Physical AI 的方法具有跨领域共性：

```text
state
→ dynamics / governing laws
→ observations
→ inverse/estimation
→ prediction/control
→ uncertainty
```

## 1. 领域地图

### Fluids / Aerodynamics
PDE、turbulence、operator learning、surrogate、control。

### Energy / Materials
molecular/graph/equivariant models、property prediction、inverse design、active learning。

### Biomedical Mechanics
imaging/measurement、fluid/solid mechanics、digital patient/twin、inverse parameter estimation。

### Digital Twins / Embodied Systems
perception → state estimation → world model → planning/control → observation feedback。

---

## 2. 共享方法

- PINN；
- Neural Operator；
- GNN / equivariance；
- differentiable simulation；
- inverse problem；
- Bayesian UQ；
- surrogate；
- hybrid solver；
- active learning；
- foundation model。

---

## 3. 为什么跨领域学习有价值

例如：
- weather 的 learned parameterization 与 turbulence closure 有共同问题；
- EO retrieval 与 medical imaging inverse problem 有共同结构；
- carbon footprint observation operator 与 tomography/sensor integration 都属于 state→observation mapping；
- digital twin 与 DA 都需要不断用 observations 更新 latent state。

---

## Pages

- [Fluids / Aerodynamics](fluids-aerodynamics.md)
- [Energy / Materials](energy-materials.md)
- [Biomedical Mechanics](biomedical-mechanics.md)
- [Digital Twins / Embodied Physical AI](digital-twins-embodied.md)
