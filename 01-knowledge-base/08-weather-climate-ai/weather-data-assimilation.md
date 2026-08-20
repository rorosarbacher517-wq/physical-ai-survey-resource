# Weather Data Assimilation

## 1. 目标

从 background forecast 与 heterogeneous observations 得到 atmospheric analysis：

```text
x_b + y_obs + B/R/H
→ x_a
```

`x_a` 是 forecast initial condition。

---

## 2. Variational view

概念 objective：

```text
J(x)=1/2(x-x_b)^T B^{-1}(x-x_b)
    +1/2(y-H(x))^T R^{-1}(y-H(x))
```

- `B`：background-error covariance；
- `R`：observation-error covariance；
- `H`：observation operator。

4D-Var 进一步把 forecast dynamics 放进 assimilation window。

---

## 3. Ensemble DA

ensemble 提供 flow-dependent covariance estimate，使 observation information 沿 dynamically correlated structures 传播。

---

## 4. Satellite radiance assimilation

核心不是“把 satellite image 填进 grid”，而是：

```text
model atmospheric state
→ radiative transfer H
→ simulated radiance
↔ observed radiance
```

因此 remote sensing observation physics 与 weather DA 是直接连接的。

---

## 5. ML 可以做什么

- learned observation encoder；
- learned covariance/update；
- surrogate radiative-transfer operator；
- neural analysis increment；
- end-to-end observation-to-state；
- differentiable DA；
- quality-control/bias model。

---

## 6. Data-to-forecast systems

### Aardvark Weather
使用 remote sensing + in-situ observations，deployment 时不依赖 conventional NWP products，生成 global grid + station forecasts。

### FuXi Weather
把 cycling ML DA 与 FuXi forecast 模型连接起来，并使用多类 raw observations；论文描述了 variable/instrument-specific encoders 与 sparse-observation processing。

这两者说明 AI weather 的 research frontier 已从 forecast core 扩展到 initial-state construction。

---

## 7. Evaluation

DA model 应看：
- analysis RMSE；
- observation residual；
- forecast impact after 1–N days；
- cycling stability；
- missing-observation robustness；
- satellite/instrument changes；
- bias / calibration。

## Sources

- ECMWF DA: https://www.ecmwf.int/en/research/data-assimilation
- Aardvark: https://doi.org/10.1038/s41586-025-08897-0
- FuXi Weather: https://doi.org/10.1038/s41467-025-62024-1
