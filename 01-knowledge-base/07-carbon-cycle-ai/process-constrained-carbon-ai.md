# Process-constrained Carbon AI

## 1. 为什么需要 process constraint

纯 data-driven model 可能在 training distribution 内预测准确，但产生：
- NEE/GPP/RECO inconsistency；
- impossible sign/range；
- extreme regime instability；
- compensation without process meaning。

process prior 的目标是减少这些自由度，而不是强行替代 observations。

---

## 2. Carbon balance constraint

常见 convention：

```text
NEE = RECO - GPP
```

### Soft loss

```text
L_bal = ||NEE_hat - (RECO_hat-GPP_hat)||²
```

### Hard construction

```text
predict GPP_hat, RECO_hat
NEE_hat = RECO_hat - GPP_hat
```

hard construction 一定满足 balance，但减少独立拟合 NEE 的 flexibility。

---

## 3. Nighttime GPP

在 physically appropriate nighttime definition 下可加入：

```text
GPP_hat ≈ 0
```

但 twilight、polar/high-latitude conditions 与 target product definitions 需要谨慎处理。

---

## 4. Positivity

某些 GPP/RECO product 定义为 non-negative magnitude，可使用 `softplus` 或 projection；但必须先确认 dataset convention。

NEE 本身通常可正可负。

---

## 5. Process-model residual

```text
F_hat = F_process + ΔF_θ
```

AI 学 process model systematic error。

风险：如果 process model 输入或 observations 有 bias，residual 可能吸收错误来源。

---

## 6. Parameter optimization / emulator

```text
θ_process
→ process model
→ compare multi-source observations
→ optimizer / emulator
→ improved parameter ensemble
```

2026 ESD 研究使用 genetic algorithm + Gaussian-process emulator + multiple global Earth observations 对 terrestrial carbon model 参数进行优化，并分析 equifinality：
https://doi.org/10.5194/esd-17-651-2026

---

## 7. Constraint ablation

必须比较：

```text
same data + same backbone + no constraint
vs
same data + same backbone + constraint
```

否则不能把提升归因于 physics constraint。

## Sources

- 2025 physics-constrained NEE/GPP/RECO model: https://doi.org/10.1016/j.isprsjprs.2025.06.033
- 2026 process-model parameter optimization: https://doi.org/10.5194/esd-17-651-2026
