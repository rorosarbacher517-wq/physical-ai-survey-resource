# Energy / Materials AI

## 1. Materials representation

材料不是普通 tabular feature，可表示为：
- crystal graph；
- atomic graph；
- 3D coordinates；
- composition；
- electron/field descriptors。

---

## 2. GNN / Equivariance

原子系统应尊重：
- permutation invariance；
- translation；
- rotation/equivariance。

能量通常要求 invariant，force 与 rotation 具有 vector equivariance。

---

## 3. Task

- energy / force prediction；
- property prediction；
- molecular/material generation；
- inverse design；
- reaction/transition prediction；
- battery/catalyst/material discovery。

---

## 4. Interatomic potential

```text
atomic structure
→ learned potential energy
→ forces = -∇_r E
```

如果能量模型可微，可通过 gradient 得到 forces。

---

## 5. Active Learning

高精度 quantum calculation 贵，可循环：

```text
train surrogate
→ identify high-uncertainty candidate
→ expensive simulation/experiment
→ add data
→ retrain
```

---

## 6. Energy systems

另一类问题包括：
- load / renewable forecasting；
- power-grid state estimation；
- optimization/control；
- weather-to-energy coupling。

这与 Weather AI 的 probabilistic forecast 有直接联系。

---

## 7. Evaluation

除了 test MAE：
- composition/structure OOD；
- force consistency；
- physical stability；
- downstream MD rollout；
- uncertainty；
- discovery hit rate。
