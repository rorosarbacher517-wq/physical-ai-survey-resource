# Uncertainty Quantification 与 Calibration

## 1. 不确定性来源

### Aleatoric
observation/process intrinsic variability。

### Epistemic
model/parameter knowledge 不足。

### Structural
model form 错误或遗漏 process。

### Observation / Retrieval
sensor noise、retrieval assumptions、partitioning uncertainty。

### Support / Scale
不同 spatial-temporal support 引入 representativeness uncertainty。

---

## 2. Predictive distribution

不要只输出：

```text
ŷ
```

也可输出：

```text
p(y|x)
```

或 ensemble：

```text
y^(1),...,y^(M)
```

---

## 3. Calibration

如果预测 90% interval，长期来看约 90% observations 应落入 interval（具体定义依 setting）。

常用：
- reliability diagram；
- coverage；
- PIT / rank histogram；
- spread-skill；
- Brier score；
- CRPS。

---

## 4. Ensemble 不等于 calibrated

多个 neural models / perturbations 产生 spread，不代表 uncertainty 正确。必须和 observation distribution 比较。

---

## 5. Conformal Prediction

可在较弱分布假设下构造 finite-sample coverage，但 Earth data 的 spatial/temporal dependence 与 distribution shift 会影响 naive exchangeability assumption。

---

## 6. OOD uncertainty

真正重要的问题是：
- new biome；
- new climate；
- unseen extreme；
- new sensor；
- future climate。

IID calibration 好不代表 OOD calibration 好。
