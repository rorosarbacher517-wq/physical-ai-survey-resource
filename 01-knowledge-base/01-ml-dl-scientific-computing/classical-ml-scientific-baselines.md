# Classical ML Scientific Baselines

## 1. 为什么 baseline 很重要

Scientific AI 的数据量通常比互联网视觉/语言小，而且存在强空间时间自相关。复杂模型不一定天然占优。

一个可信实验应问：

> 复杂 architecture 的增益来自 representation、pretraining、physics prior，还是只是更多参数与更强 tuning？

---

## 2. Linear / Ridge / Lasso

```text
y = Xβ + ε
```

### Ridge

```text
L = ||y-Xβ||² + λ||β||²
```

适合 correlated predictors，常作为稳定 regression baseline。

### Lasso

```text
L = ||y-Xβ||² + λ||β||₁
```

产生 sparse coefficients，但高度相关变量下解释要谨慎。

---

## 3. Random Forest

优点：
- nonlinear；
- 对 scaling 不敏感；
- tabular environmental variables 强 baseline；
- 可做 permutation importance。

局限：
- 不自然表示长时序；
- high-dimensional imagery 需要先特征化；
- feature importance 不是 causality。

---

## 4. Gradient Boosting

`XGBoost / LightGBM / CatBoost` 在 tabular Earth data 上常非常强。

适合：
- flux gap filling；
- regional regression；
- environmental driver modeling；
- mixed continuous/categorical features。

---

## 5. Gaussian Process

```text
f(x) ~ GP(m(x), k(x,x'))
```

优势是 uncertainty 与 smoothness prior 清晰；主要限制是大样本计算扩展性。

---

## 6. 公平比较

必须保持：
- 相同 train/test split；
- 相同 target definition；
- 相同 leakage rule；
- 相同 evaluation samples；
- comparable preprocessing；
- paired metrics where possible。

### Earth-specific split
随机 sample split 往往不够。优先：
- site-blocked；
- region-blocked；
- temporal-blocked；
- biome/climate OOD。

## Sources

- Breiman (2001), *Random Forests*, Machine Learning.
- Friedman (2001), *Greedy Function Approximation: A Gradient Boosting Machine*.
- Rasmussen & Williams (2006), *Gaussian Processes for Machine Learning*: https://gaussianprocess.org/gpml/
