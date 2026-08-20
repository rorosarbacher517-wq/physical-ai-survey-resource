# Carbon-flux Modeling Methods

## 1. Empirical / process-inspired baseline

### Light-use-efficiency

```text
GPP ≈ APAR × ε(environment)
```

优点：过程含义清楚；
限制：复杂 ecosystem response 被简化。

---

## 2. Process-based ecosystem / land-surface models

显式模拟：
- photosynthesis；
- respiration；
- phenology；
- soil carbon；
- water/energy balance；
- vegetation dynamics。

优势：process consistency 与 future scenario coupling；
挑战：parameter uncertainty、structural error、compute、equifinality。

---

## 3. Classical ML upscaling

- Random Forest；
- XGBoost / Gradient Boosting；
- Gaussian Process。

输入通常是 tower-matched meteorology + EO features。

2026 Agricultural and Forest Meteorology 的研究展示了 XGBoost 结合 remote sensing / environmental / SIF information 改进 EC flux gap filling：
https://doi.org/10.1016/j.agrformet.2025.110987

---

## 4. Deep temporal model

```text
EO + meteorology sequence
→ LSTM / Transformer / TCN
→ flux sequence
```

适合 phenology 与 delayed response。

---

## 5. Spatial / graph model

显式建模 footprint 内 spatial heterogeneity。

2025 RSE 研究使用 footprint-weighted spatial features 与 `DeeperGCN` residual correction 研究 vegetation heterogeneity：
https://doi.org/10.1016/j.rse.2025.114952

---

## 6. Physics-constrained joint model

共同预测：

```text
[NEE, GPP, RECO]
```

并加入：

```text
NEE = RECO - GPP
```

2025 ISPRS JPRS 代表工作：
https://doi.org/10.1016/j.isprsjprs.2025.06.033

---

## 7. Footprint-aware field model

```text
EO pixel field
→ pixel flux prediction
→ dynamic footprint operator
→ tower supervision
```

它与“先把所有 pixels average 成 feature”不同，因为保留 spatial latent field。

---

## 8. Hybrid process–ML

AI 可以：
- optimize process parameters；
- learn residual；
- emulate expensive process model；
- learn uncertain submodule。

2026 ESD 工作使用 global Earth observations + optimization + Gaussian-process emulator 研究 land-carbon model parameter uncertainty：
https://doi.org/10.5194/esd-17-651-2026

---

## 9. Foundation representation

```text
EO foundation embedding
+ meteorology/process context
→ carbon task head
```

真正要测试的是：label efficiency、quantitative regression、biome/climate OOD，而不只是 classification transfer。
