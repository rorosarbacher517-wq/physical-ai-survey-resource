# NWP Basics · AI Weather 的物理与数值基线

## 1. Operational NWP pipeline

```text
observations
→ QC
→ Data Assimilation
→ analysis
→ numerical model
→ time integration
→ ensemble / deterministic forecast
→ post-processing
```

AI weather 常替换 numerical model，但不一定替换上游 DA 或下游 post-processing。

---

## 2. Discretization

continuous atmosphere：

```text
PDEs on sphere
```

变成：

```text
discrete grid/mesh + vertical levels + timestep
```

需要满足 numerical stability、conservation、resolution 与 compute trade-off。

---

## 3. Dynamical core

负责 resolved large-scale atmospheric dynamics。

可能使用：
- spectral；
- finite-volume；
- finite-difference；
- semi-Lagrangian 等 numerical approaches。

---

## 4. Physical parameterizations

无法 resolve 的 process 用 parameterization：
- convection；
- cloud microphysics；
- radiation；
- boundary-layer turbulence；
- land-surface coupling。

AI 可学习 parameterization，而不是替代整个 NWP。

---

## 5. Initial condition

forecast 可以写：

```text
X_{t+Δt}=M(X_t)
```

但 `X_t` 不是直接 observation，而是 DA 得到的 analysis。

这就是为什么“ERA5-initialized AI forecast”与“observation-to-forecast model”必须分开。

---

## 6. Boundary / coupling

global atmosphere forecast 还依赖：
- SST / sea ice；
- land-surface state；
- soil moisture/snow；
- atmospheric composition（任务依系统而异）。

coupled prediction 会进一步加入 ocean/land/wave/chemistry dynamics。

---

## 7. Deterministic vs Ensemble NWP

### Deterministic
高分辨率的一条 trajectory。

### Ensemble
通过 initial-condition/model uncertainty 生成 members，估计 forecast distribution。

AI ensemble 必须与 ensemble NWP 按 probabilistic metrics 比较，而不只比较 ensemble mean RMSE。

## Sources

- ECMWF Forecast User Guide / IFS documentation: https://www.ecmwf.int/en/forecasts/documentation-and-support
- Kalnay, *Atmospheric Modeling, Data Assimilation and Predictability*.
