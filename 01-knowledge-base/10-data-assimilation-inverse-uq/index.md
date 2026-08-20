# 10 · Inverse Problems、Data Assimilation 与 UQ

> 虽然目录编号是 10，但**学习顺序应在 Earth Observation / Carbon / Weather 之前。**

这层解决一个共同问题：

```text
真实 state 不可完全观测
→ observations 稀疏/有噪声/间接
→ 如何推断 state / parameter / uncertainty？
```

## 1. 统一形式

```text
y = H(x) + ε
```

我们想求：

```text
p(x|y) ∝ p(y|x)p(x)
```

如果 `x` 随时间演化：

```text
x_{t+1}=M(x_t)+η_t
y_t=H_t(x_t)+ε_t
```

这就是 state-space / DA 的核心结构。

---

## 2. 三个分支

### Inverse Problems
从 observation 反推 parameter/state。

### Data Assimilation
随时间不断融合 forecast/model 与 new observations。

### Uncertainty Quantification
描述 observation、model、parameter、prediction 不确定性。

---

## 3. Earth AI 为什么必须懂

### Remote sensing
很多 retrieval 本质是 inverse problem。

### Weather
forecast quality 高度依赖 analysis / initial condition；DA 是 operational NWP 的核心。

### Carbon
EC measurement、partitioning、footprint、satellite retrieval、process parameters 都有 uncertainty。

---

## 页面

- [Inverse Problems](inverse-problems.md)
- [Data Assimilation](data-assimilation.md)
- [Uncertainty / Calibration](uncertainty-calibration.md)

## Sources

- Tarantola, *Inverse Problem Theory*.
- Evensen, *Data Assimilation: The Ensemble Kalman Filter*.
- Kalnay, *Atmospheric Modeling, Data Assimilation and Predictability*.
