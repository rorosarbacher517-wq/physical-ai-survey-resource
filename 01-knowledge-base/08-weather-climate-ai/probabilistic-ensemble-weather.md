# Probabilistic / Ensemble Weather

## 1. 为什么单条 forecast 不够

大气 chaotic，initial/model uncertainty 随 lead time 放大。

目标应从：

```text
X_hat_T
```

扩展为：

```text
p(X_T | observations/initial state)
```

---

## 2. Ensemble

```text
X^(1), X^(2), ..., X^(M)
```

ensemble 可来自：
- perturbed initial conditions；
- stochastic model；
- parameter perturbation；
- diffusion/generative sampling；
- multiple models。

---

## 3. Ensemble mean 不是全部

如果只看 ensemble mean RMSE，会丢失：
- spread；
- tail risk；
- multimodality；
- event probability。

---

## 4. CRPS

Continuous Ranked Probability Score 比较 predictive CDF 与 observation；越低通常越好。

它同时考虑 location 与 distribution sharpness/calibration。

---

## 5. Brier Score

对 binary event：

```text
BS = mean((p_i-o_i)^2)
```

适合：heavy rain、heat threshold、storm event probability。

---

## 6. Reliability / Rank

- reliability diagram；
- rank histogram；
- spread–skill relation；
- coverage。

ensemble spread 太窄 → underdispersive；太宽 → overdispersive。

---

## 7. 代表 AI ensemble routes

### GenCast
conditional generative distribution。

### FengWu-Ensemble
conditional diffusion from deterministic forecasts。

### AIFS ENS
ECMWF operational AI ensemble。

### WeatherNext 2
FGN probabilistic scenario generation。

### Aurora 1.5
2026 extension 增加 probabilistic ensemble functionality。

---

## 8. Extremes

probabilistic model 的价值尤其体现在 rare event：
- cyclone path/intensity；
- heavy precipitation；
- heatwave；
- renewable-energy risk。

必须评估 event probability，而不只是 deterministic trajectory distance。

## Sources

- GenCast: https://doi.org/10.1038/s41586-024-08252-9
- AIFS ENS v2: https://confluence.ecmwf.int/spaces/FCST/pages/620418893/Implementation+of+AIFS+ENS+v2
- WeatherNext: https://deepmind.google/science/weathernext/
