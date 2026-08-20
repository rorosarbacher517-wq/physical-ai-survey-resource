# Carbon-flux Validation 与 Uncertainty

## 1. 误差来源链

```text
instrument / EC processing
→ gap filling
→ partitioning
→ footprint estimation
→ EO/reanalysis retrieval
→ spatial-temporal alignment
→ model
→ upscaling
```

最终 prediction error 是多层 uncertainty 的组合。

---

## 2. Split design

### 不推荐作为唯一验证
random half-hour / random day split within same sites。

### 推荐
- site-blocked CV；
- leave-one-biome/region-out；
- temporal block；
- event/extreme holdout；
- climate-range OOD。

---

## 3. Metrics

### Point/tower scale
- RMSE；
- MAE；
- bias；
- R² / correlation。

### Paired model comparison
在完全相同 samples 上比较 error difference。

### Physical
- NEE–GPP–RECO balance residual；
- day/night behavior；
- seasonal cycle；
- annual carbon balance。

### Probabilistic
- CRPS；
- coverage；
- calibration；
- ensemble spread-skill。

---

## 4. Stratified diagnostics

按：
- biome；
- heterogeneity；
- season；
- daytime；
- radiation；
- VPD；
- soil moisture；
- footprint variability；
- extreme regime

分层，能比一个 global metric 更好解释 model behavior。

---

## 5. Feature importance 的边界

Permutation importance / SHAP 可回答：

> 模型预测依赖哪些 features？

不能直接回答：

> ecosystem causal mechanism 是什么？

相关 predictors、spatial confounding 和 feature construction 都会影响 importance。

---

## 6. External validation

用另一 product 比较时，需要问：
- 它是否也由相同 tower data 训练？
- resolution/support？
- target definition/sign？
- temporal aggregation？

否则并非真正独立 reference。

---

## 7. Reporting checklist

```text
data versions
site count
sample count
split manifest
target definition
QC/partitioning
footprint method
input support
metric convention
confidence interval / uncertainty
OOD diagnostics
```
