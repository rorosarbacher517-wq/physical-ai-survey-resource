# Weather Rollout、Training 与 Error Accumulation

## 1. One-step model

```text
X_t → f_θ → X_{t+Δt}
```

如果 train 总使用真实 `X_t`，但 inference 使用自己上一步 prediction：

```text
X_hat_t → X_hat_{t+Δt}
```

会产生 train–inference distribution gap。

---

## 2. Autoregressive rollout

```text
X0
→ X1_hat
→ X2_hat
→ ...
→ XT_hat
```

误差来源：
- state bias；
- phase error；
- numerical-like instability；
- high-frequency damping；
- spectrum distortion；
- physical imbalance。

---

## 3. Multi-step loss

训练时展开多步：

```text
L = Σ_{τ=1}^K w_τ L(X_hat_{t+τ}, X_{t+τ})
```

可以更接近 inference behavior，但 memory/compute 更高。

---

## 4. Cascade / hierarchical strategies

### Pangu-Weather
多个 temporal interval model，减少长 forecast 的 autoregressive step count。

### FuXi
short/medium/long lead model cascade，使不同阶段使用针对性 model。

### FengWu
通过 replay-related mechanism 增强 long rollout training。

---

## 5. Normalization drift

如果 model output 在 standardized space rollout：
- bias 可能逐步累积；
- rare variable range 易被压缩；
- precipitation/extreme tails 易 smoothing。

应检查 physical-space statistics。

---

## 6. Spectral diagnostics

RMSE 相同的两个 model 可能空间结构完全不同。

检查：
- kinetic-energy spectrum；
- power spectral density；
- scale-dependent error；
- gradient/front sharpness；
- precipitation structure。

---

## 7. Climate drift

weather model rollout 到 weeks/months 后可能 drift 到错误 climatology。用于 climate simulation 时需要更严格 long-run stability/balance evaluation。

## Sources

- Pangu-Weather: https://doi.org/10.1038/s41586-023-06185-3
- FuXi: https://doi.org/10.1038/s41612-023-00512-1
- FengWu: https://doi.org/10.1038/s43247-025-02502-y
