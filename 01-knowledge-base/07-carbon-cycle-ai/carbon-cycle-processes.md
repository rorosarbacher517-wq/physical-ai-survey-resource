# Carbon-cycle Processes：先理解过程，再做预测

## 1. Carbon pool 与 flux

陆地碳循环可简化为多个 carbon pools 之间的 flux：

```text
atmosphere
   ↓ photosynthesis
vegetation carbon
   ↕ allocation / mortality
soil / litter carbon
   ↑ respiration / decomposition
atmosphere
```

AI 预测的是其中某个 flux/state，不等于学会了整个 carbon cycle。

---

## 2. GPP

`GPP` 表示 photosynthesis 固定的总碳量/速率。

主要受：
- absorbed radiation；
- canopy leaf area / chlorophyll；
- temperature；
- VPD / stomatal regulation；
- soil moisture；
- phenology；
- nutrient status；
- disturbance。

### Light-use-efficiency (LUE) 思路

概念形式：

```text
GPP ≈ APAR × ε
```

`APAR` 是 absorbed PAR，`ε` 是 effective light-use efficiency，受环境限制。

这解释了为什么 optical/SIF/radiation 与 GPP 联系较直接，但不是 deterministic one-to-one mapping。

---

## 3. RECO

`RECO` 包含 autotrophic + heterotrophic respiration。

常见控制：
- temperature；
- soil moisture；
- substrate/carbon availability；
- biomass；
- microbial activity；
- phenology。

相比 GPP，RECO 对 optical canopy state 的直接可观测性通常更弱，因此需要 soil/temperature/structure/process context。

---

## 4. NEE

常见 convention：

```text
NEE = RECO - GPP
```

因此 NEE 是两个大 flux 的净差，可能发生 cancellation：

```text
large GPP + large RECO → modest NEE
```

这意味着：
- NEE 小不等于 ecosystem processes 弱；
- 单独优化 NEE 可能掩盖 GPP/RECO compensation；
- joint modeling 可提供更强 physical diagnostic。

---

## 5. Disturbance / management

fire、harvest、drought mortality、cropping/irrigation 会改变：
- structure；
- LAI；
- carbon pool；
- albedo/temperature；
- soil moisture；
- photosynthesis/respiration。

模型如果只学习 smooth seasonal cycle，往往难以处理 abrupt regime shift。

---

## 6. Carbon–climate feedback

carbon cycle 与 climate 双向耦合：

```text
climate → GPP / RECO / disturbance → atmospheric CO2
atmospheric CO2 → radiative forcing / climate + CO2 fertilization
```

因此 future-climate carbon prediction 是 OOD problem，而不是普通时间外推。

## Sources

- Chapin et al., ecosystem carbon-cycle fundamentals.
- Friedlingstein et al., annual Global Carbon Budget series for current global carbon accounting.
- [Carbon–Water–Energy Coupling](carbon-water-energy-coupling.md)
