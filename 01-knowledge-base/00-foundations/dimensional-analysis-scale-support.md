# Dimensional Analysis、Scale 与 Observation Support

这一页是 Earth AI 最重要的基础页之一。

## 1. Unit 与 dimension

模型输入常被 standardize：

```text
x' = (x-μ)/σ
```

但 physical loss 可能仍要求真实单位。因此训练时必须知道：
- normalization 在哪一层；
- constraint 在 normalized space 还是 physical space；
- unit conversion 是否一致。

### Dimensional consistency

等式两边必须单位一致。例如：

```text
NEE = RECO - GPP
```

三个 flux 必须共享一致的 sign convention 与 units。

---

## 2. Resolution 不等于 Support

### Spatial resolution
输出或 sensor pixel 的 nominal grid size，例如 10 m、30 m、0.25°。

### Observation support
一次 observation 实际整合的空间范围与权重。

### Coverage
数据覆盖的地理范围。

### Validation support
独立 reference 实际能够验证的尺度。

这四者不能混用。

---

## 3. Earth Observation 示例

Sentinel-2 10 m pixel 表示 sensor/grid support，但一个 downstream label 可能来自：
- field polygon；
- coarse product；
- station；
- manually mapped object。

因此“输出 10 m”不代表“10 m independent accuracy”。

---

## 4. Eddy Covariance 示例

塔在坐标 `(x0,y0)`，但 observation 可写为：

```text
Y_t = ∬ w_t(x,y) F_t(x,y) dxdy + ε_t
```

`w_t(x,y)` 是 dynamic footprint。tower coordinate 只是 reference location，不是 point-support flux。

---

## 5. Weather 示例

一个 `0.25°` gridded field 可能是：
- reanalysis；
- interpolated model output；
- native reduced Gaussian grid 再映射；
- postprocessed forecast。

这些 representation 的 information support 不完全一样。

---

## 6. Temporal support

同样要区分：
- instantaneous；
- 30-min mean；
- hourly mean；
- accumulation；
- daily mean；
- composite。

`precipitation accumulation` 不能当作 instantaneous rate 直接比较。

---

## 7. Scale-aware checklist

对任何 Earth AI 数据，记录：

```text
native spatial resolution
native temporal sampling
preprocessing/resampling
model input grid
model output grid
observation support
label support
validation support
```

## Sources

- Schmid (2002), footprint / source-area concepts for micrometeorological measurements.
- Kljun et al. (2015), flux footprint parameterisation: https://doi.org/10.5194/gmd-8-3695-2015
- OGC/CF-style geospatial conventions and official sensor product documentation for dataset-specific resolution semantics.
