# Data Assimilation

## 1. 目标

给定 background/forecast 与 observations，得到更合理的 state estimate：

```text
forecast/background x_b
+ observations y
+ error statistics
→ analysis x_a
```

---

## 2. Variational DA

典型 3D/4D-Var objective：

```text
J(x)=1/2(x-x_b)^T B^{-1}(x-x_b)
    +1/2(y-H(x))^T R^{-1}(y-H(x))
```

- `B`：background-error covariance；
- `R`：observation-error covariance；
- `H`：observation operator。

4D-Var 进一步通过 forecast model 连接时间窗口。

---

## 3. Kalman / Ensemble route

线性 Gaussian 情况 Kalman Filter 给出递推 posterior。

Ensemble Kalman Filter 用 ensemble sample 近似 covariance。

核心直觉：

> observation 只在观测位置出现，但 covariance 决定它如何更新其他位置和变量。

---

## 4. ML 在 DA 中的角色

- learned observation operator；
- learned covariance；
- learned analysis update；
- neural state estimator；
- end-to-end observation-to-forecast；
- surrogate forecast model；
- bias correction。

---

## 5. Weather 里的关键区别

很多 AI weather models 仍依赖 NWP analysis/reanalysis 初始化；这不等于“从 raw observations 端到端预测”。

`Aardvark Weather` 与 `FuXi Weather` 之所以重要，是因为它们把 observation/data-to-state/data-to-forecast 链条纳入 ML system。

---

## 6. Evaluation

DA 不能只看 analysis RMSE；还要看：
- forecast impact；
- observation-space residual；
- bias；
- calibration；
- sparse-region performance；
- robustness to missing sensors。

## Sources

- Evensen, *The Ensemble Kalman Filter*.
- ECMWF DA overview/workshop materials: https://www.ecmwf.int/en/newsletter/184/news/data-assimilation-workshop-probes-traditional-and-machine-learning-methods
- Aardvark Weather: https://www.nature.com/articles/s41586-025-08897-0
