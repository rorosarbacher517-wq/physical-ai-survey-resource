# Extremes、Climate Response 与 Carbon OOD

## 1. 为什么 extremes 单独评估

overall RMSE 被大量 normal conditions 主导；而 carbon-cycle scientific interest 常集中在：
- drought；
- heatwave；
- compound hot–dry event；
- fire/disturbance；
- anomalous wet period；
- freeze/thaw；
- phenological transition。

---

## 2. Drought response 不是单变量

需要区分：

```text
soil drought      → low soil moisture
atmospheric drought → high VPD
heat stress       → high temperature
radiation anomaly → light/energy forcing
```

它们共同影响 stomata、photosynthesis、respiration 与 energy balance。

---

## 3. Compound extremes

例如 hot + dry：

```text
high T + high VPD + low soil moisture
→ stomatal limitation / thermal stress
→ GPP change
→ respiration response
→ NEE anomaly
```

response 可能 nonlinear，因此独立变量 importance 不能完整描述 mechanism。

---

## 4. Event definition

必须预先定义：
- percentile threshold；
- climatology baseline；
- duration；
- compound rule；
- recovery period。

避免看完结果再选择“最有提升”的 event threshold。

---

## 5. OOD types

### Temporal OOD
unseen year / future period。

### Spatial OOD
unseen site/region。

### Ecological OOD
unseen biome / management。

### Climate OOD
temperature/VPD/soil-moisture regime 超出 training range。

---

## 6. Metrics

除 RMSE/R²：
- anomaly correlation；
- event-specific bias；
- peak timing；
- cumulative carbon anomaly；
- recovery time；
- calibration / coverage；
- sign correctness for anomaly。

---

## 7. Future climate

未来 climate prediction 属于 distribution shift。一个模型在 historical held-out sites 表现好，不代表可以可靠 extrapolate 到未来 CO₂/climate regime。

hybrid process–ML 与 uncertainty-aware ensembles 在这类问题中尤其重要。
