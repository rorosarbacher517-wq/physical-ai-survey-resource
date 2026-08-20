# 05 · Spatiotemporal、Multiscale 与 Multimodal AI

Earth data 的复杂性来自四个维度同时存在：

```text
space × time × variable/modality × scale
```

## 1. 常见 representation

- raster/grid；
- sphere；
- graph/mesh；
- point cloud；
- station network；
- patch/token；
- spectral representation。

---

## 2. 时间问题

- regular sequence；
- irregular observation；
- missing time step；
- multi-rate sensor；
- seasonal cycle；
- event/extreme；
- autoregressive forecast。

---

## 3. Multiscale

必须区分：
- sensor resolution；
- process scale；
- model grid；
- observation support；
- label scale；
- validation scale。

---

## 4. Multimodal

不同 modality 的差异不仅是 channels：
- imaging physics 不同；
- sampling time 不同；
- uncertainty 不同；
- missing pattern 不同；
- resolution 不同。

因此 fusion 前先做 semantic/physical alignment。

---

## 5. 页面

- [Spatial Representations](spatial-representations.md)
- [Temporal Modeling](temporal-modeling.md)
- [Multiscale / Multimodal Fusion](multiscale-multimodal-fusion.md)
- [Support-aware Learning](support-aware-learning.md)
