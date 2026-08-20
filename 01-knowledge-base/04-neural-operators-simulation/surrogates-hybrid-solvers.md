# Surrogate Modeling 与 Hybrid Solvers

## 1. Surrogate 是什么

用便宜模型近似 expensive simulator：

```text
x / parameter / forcing
→ expensive simulator
→ y
```

训练后：

```text
x → surrogate f_θ(x) ≈ y
```

---

## 2. Surrogate 类型

### Parameter-to-output
例如 material parameter → scalar response。

### Field-to-field
initial/forcing field → solution field。

### Temporal surrogate
state_t → state_{t+Δt}。

### Emulator for parameter search
用于 Bayesian optimization、calibration、sensitivity analysis。

---

## 3. Learned residual

```text
ŷ = solver(x) + residual_θ(x)
```

优点：保留 solver baseline；
风险：residual 可能只学 training-regime bias。

---

## 4. Learned closure

resolved dynamics 已知，小尺度 unresolved process 由 ML 学：

```text
large-scale solver
+ learned subgrid closure
→ next state
```

核心风险是 closed-loop stability。

---

## 5. Multi-fidelity

组合：
- cheap coarse simulation；
- sparse expensive high-fidelity simulation；
- observations。

目标是在 compute budget 下最大化 generalization。

---

## 6. 评测

不能只看 test-set RMSE，还要看：
- parameter OOD；
- geometry OOD；
- long rollout；
- conservation；
- spectrum；
- rare/extreme regime；
- wall-clock speedup。
