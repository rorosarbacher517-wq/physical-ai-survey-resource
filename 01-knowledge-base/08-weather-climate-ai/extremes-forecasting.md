# Extreme-event Forecasting

## 1. 平均 skill 不能代表 extremes

需要单独研究：
- tropical cyclone；
- heavy precipitation；
- heatwave / cold spell；
- atmospheric river；
- severe wind；
- compound hazards。

---

## 2. Rare-event problem

training loss 中 extreme sample 占比低：

```text
L_mean ≈ dominated by normal weather
```

因此 model 可能优化 global RMSE，却 smoothing tail。

---

## 3. Tropical cyclone

评价：
- track error；
- intensity；
- central pressure；
- maximum wind；
- storm size/structure；
- genesis probability。

2026-08-06 Google 发布 WeatherNext cyclone research/open-source update，强调 track/intensity/structure 与 scenario forecasting。

Official: https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/

---

## 4. Heavy precipitation

问题：
- intermittency；
- skewed distribution；
- local convective scale；
- phase/location error。

metrics：
- threshold CSI；
- FSS；
- extreme percentile bias；
- CRPS / event probability。

---

## 5. Heatwave

需要：
- duration；
- spatial extent；
- threshold exceedance；
- nighttime temperature；
- humidity/heat-index-related variables。

---

## 6. Probabilistic importance

extreme decision 关心：

```text
P(event | current observations)
```

而不是只有 ensemble mean。

---

## 7. Distribution shift

climate change 会改变 tail distribution。historical extreme OOD 仍不完全代表 future-climate extremes，因此需要 hybrid/climate-aware evaluation。
