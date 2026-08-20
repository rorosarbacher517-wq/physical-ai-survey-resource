# 02 · Physical AI Core：Physics 到底放在哪里？

`Physics-informed AI` 不等于“在 loss 里加 PDE residual”。更系统的做法是先判断 physics/measurement knowledge 进入 learning pipeline 的哪一层。

## 1. Physics integration map

```text
Data / Labels
  ↓
Input features / coordinates
  ↓
Representation / Architecture
  ↓
Loss / Regularization
  ↓
Hard constraint / Projection
  ↓
Simulator / Solver loop
  ↓
Observation operator / DA
  ↓
Evaluation / physical diagnostics
```

---

## 2. 七种常见入口

### 1) Data / labels
用 process model、simulator、retrieval 或 synthetic data 产生训练样本。

### 2) Inputs
加入 solar geometry、topography、stability、roughness、physical parameter 等。

### 3) Architecture
使用 graph geometry、equivariance、conservative layer、operator architecture。

### 4) Loss
加入 PDE residual、balance、boundary、energy/carbon constraint。

### 5) Hard constraint
通过 parameterization/projection 直接保证 constraint。

### 6) Simulator loop
AI 学 residual / closure / parameterization，solver 保留主 dynamics。

### 7) Observation / evaluation
即使 model 本体完全 data-driven，也可以用真实 observation operator 做 supervision，并用 conservation/spectrum/balance 做评测。

---

## 3. 为什么 Observation Operator 单独重要

Scientific model 预测的是 latent state/field，但 supervision 往往是 observation：

```text
x̂ = model(input)
ŷ = H(x̂)
loss = L(ŷ, y_obs)
```

`H` 可以是：
- sensor response；
- radiative transfer；
- spatial integration；
- flux footprint；
- interpolation to station；
- retrieval operator。

这类 physics 不需要写进 neural network hidden layers，也能改变 learning problem。

---

## 4. 页面

- [Observation Operators](observation-operators.md)
- [Conservation / Symmetry / Dimensional Priors](conservation-symmetry-dimensional-priors.md)
- [Hybrid Modeling Design](hybrid-modeling-design.md)

Next：
- [Physics-informed Learning](../03-physics-informed-learning/index.md)
- [Neural Operators](../04-neural-operators-simulation/index.md)
- [DA / Inverse / UQ](../10-data-assimilation-inverse-uq/index.md)
