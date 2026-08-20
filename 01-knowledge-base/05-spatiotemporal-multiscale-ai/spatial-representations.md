# Spatial Representations

## 1. Regular raster

```text
X [B,C,H,W]
```

适合 EO、regional weather、land-surface fields。

优点：卷积/FFT/GPU 高效。

---

## 2. Latitude–longitude grid

global Earth 常用，但存在：
- pole distortion；
- cell area 随 latitude 变化；
- longitude periodicity。

metric 计算时常需要 area weighting。

---

## 3. Sphere / mesh

例如 icosahedral/multiresolution mesh，可减弱 lat-lon distortion，并支持 graph message passing。

`GraphCast` 是重要示例。

---

## 4. Point cloud

```text
P [B,N,D]
```

LiDAR 中 `D` 可含：
- xyz；
- intensity；
- return number；
- classification；
- waveform-derived attributes。

---

## 5. Station network

station 不规则分布，且 sampling density spatially biased。

可用：
- graph；
- set encoder；
- cross-attention；
- interpolation + grid model。

---

## 6. Patch/token

ViT 将 raster 切成 patch：

```text
[B,C,H,W]
→ [B,N,D]
```

patch size 越大，token 越少、compute 越低，但 small-scale detail 可能损失。
