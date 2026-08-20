# Climate AI：从 Forecast Skill 到 Long-term Statistics

## 1. Weather 与 Climate task 不同

Weather：给定 initial condition，预测具体 trajectory。

Climate：关注 external forcing 下的长期 distribution / statistics / variability。

```text
weather: X(t0) → X(t0+τ)
climate: forcing → p(long-term states/statistics)
```

---

## 2. Climate emulator

ML 可近似 expensive climate/ESM response：
- global temperature/precipitation fields；
- scenario response；
- parameter ensemble；
- subgrid process。

---

## 3. Long-run stability

一个 weather model 15-day skill 强，不代表 multi-year rollout 有正确 climate。

必须检查：
- mean climatology；
- seasonal cycle；
- variability spectrum；
- extremes；
- teleconnections；
- energy/water balance；
- drift。

---

## 4. Forced response

future climate 受：
- greenhouse gases；
- aerosols；
- land use；
- solar/volcanic forcing；
- ocean/ice feedback。

ML training 必须明确 forcing variables，否则只能学习 historical dynamics。

---

## 5. Hybrid route

`NeuralGCM` 说明 hybrid dynamics + learned physics 可跨 weather forecast 与 longer climate simulation 使用；但 climate evaluation 标准必须独立于 weather RMSE。

---

## 6. Downscaling

climate downscaling 还面临：
- future covariate shift；
- bias correction stationarity assumption；
- extreme tail extrapolation。

---

## 7. Causal / attribution boundary

ML association 不自动提供 climate attribution。attribution 通常需要 counterfactual forcing experiments / causal/physical framework。
