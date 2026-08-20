# Weather Evaluation / Verification

## 1. 比较前先对齐六件事

```text
variable
vertical level
lead time
initialization
verification reference
grid/resolution
```

少一个都可能让 headline comparison 失真。

---

## 2. Latitude-weighted RMSE

全球 lat-lon grid cell area 随 latitude 变化，所以常使用 latitude weighting。

概念：

```text
RMSE = sqrt(Σ_i w_i (f_i-o_i)^2 / Σ_i w_i)
w_i ∝ cos(latitude_i)
```

---

## 3. ACC

Anomaly Correlation Coefficient 比较 forecast anomaly 与 observed/reference anomaly 的 pattern correlation。

需要明确 climatology definition。

---

## 4. Probabilistic metrics

- CRPS；
- Brier Score；
- reliability；
- rank histogram；
- spread–skill；
- ensemble coverage。

不能用 deterministic RMSE 代替 probabilistic evaluation。

---

## 5. Extreme metrics

- cyclone track/intensity；
- precipitation threshold CSI/FSS；
- heat threshold probability；
- tail quantile error；
- event timing/duration。

---

## 6. Spectral / structural metrics

- power spectrum；
- kinetic-energy spectrum；
- spatial gradient；
- object displacement；
- precipitation structure。

用于识别 blurry/smoothing forecast。

---

## 7. Reference matters

### ERA5 verification
适合 benchmark/hindcast consistency，但 ERA5 本身是 reanalysis。

### Operational analysis
更接近 real-time forecast verification context。

### Stations / radar / satellite
更接近 observations，但 support/error/operator 各异。

所以“对 ERA5 更准”不能自动等价为“对 independent observations 更准”。

---

## 8. Hindcast vs real-time

应区分：
- archived ERA5-initialized hindcast；
- operational analysis initialization；
- raw-observation data-to-forecast；
- real-time service output。

---

## 9. WeatherBench 2

WeatherBench 2 为 data-driven global weather models 提供统一 benchmark infrastructure，并推动 standardized evaluation。

Source: https://research.google/blog/weatherbench-2-a-benchmark-for-the-next-generation-of-data-driven-weather-models/

---

## 10. Reporting template

```text
model/version
initialization
verification period
reference dataset
variables/levels
lead times
grid/regridding
metrics
ensemble size
compute
operational/research status
```
