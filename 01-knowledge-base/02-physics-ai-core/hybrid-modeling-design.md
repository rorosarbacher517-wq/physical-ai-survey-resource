# Hybrid Modeling Design · Numerical Model × Machine Learning

Hybrid model 的核心不是“physics + neural network”这几个字，而是明确：**哪部分由 equations/solver 负责，哪部分由 data-driven model 学。**

## 1. 五种常见结构

### A. Residual correction

```text
ŷ = y_physics + f_θ(x)
```

AI 修正 systematic bias。

### B. Learned parameterization / closure

```text
resolved dynamics
+ learned unresolved process
→ numerical integration
```

适合 cloud/turbulence/subgrid process 等。

### C. Surrogate

```text
input parameters/state
→ neural surrogate
→ approximate simulator output
```

用于加速 repeated simulation / optimization。

### D. Solver-in-the-loop

AI 给 solver 参数、forcing 或 correction，solver 继续推进 state。

### E. Observation-space hybrid

AI 预测 latent field，再通过 physical observation operator 与真实 measurement 比较。

---

## 2. 为什么 hybrid 常比纯 PINN 更实际

如果已有成熟 numerical solver：
- 不必重新学习已知 dynamics；
- 可保留 conservation / boundary handling；
- AI 聚焦 expensive/uncertain component；
- 更容易解释 failure domain。

---

## 3. 设计 checklist

1. 哪个 process 已知？
2. 哪个 process 计算贵？
3. 哪个 process 参数化误差大？
4. observation 是否足够约束 learned component？
5. learned component 是否会 destabilize solver？
6. extrapolation 时 physics 是否提供有效 inductive bias？

---

## 4. Training choices

- offline supervised；
- online / rollout training；
- differentiable end-to-end；
- multi-step loss；
- conservation regularization；
- teacher-forcing vs closed-loop。

---

## 5. Failure modes

- learned correction 只在 training climate 有效；
- one-step accuracy 好但 closed-loop unstable；
- numerical solver 与 learned component timestep mismatch；
- correction 吸收了错误 observation bias；
- hidden compensation 导致 parameter 不可解释。

## Sources

- Reichstein et al. (2019), *Deep learning and process understanding for data-driven Earth system science*, Nature.
- Karniadakis et al. (2021), physics-informed machine learning review.
- Kochkov et al. (2024), NeuralGCM: https://www.nature.com/articles/s41586-024-07744-y
