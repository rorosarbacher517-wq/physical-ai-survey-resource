# LiDAR / 3D Earth Observation

## 1. Observation chain

```text
laser pulse
→ travel time / waveform
→ range
→ georeferenced returns
→ point cloud
→ terrain/canopy/structure metrics
```

基本 range：

```text
R = cΔt/2
```

---

## 2. Data representation

### Raw point cloud

```text
P [N,D]
```

feature 可含 xyz、intensity、return number、classification 等。

### Voxel

```text
[Vx,Vy,Vz,C]
```

便于 3D convolution，但 memory 大。

### Rasterized structure

例如：
- canopy height model；
- height percentiles；
- vegetation density profile；
- terrain model。

适合与 2D EO 对齐。

---

## 3. Model family

- PointNet / PointNet++；
- sparse convolution；
- point Transformer；
- voxel encoder；
- raster CNN/ViT；
- 2D–3D cross-attention。

---

## 4. Ecological meaning

LiDAR 更接近 vegetation **structure**：height、vertical distribution、canopy gap、biomass-related geometry。

Optical 更接近 spectral/phenological state。两者互补，但时间尺度差异很大。

---

## 5. Temporal mismatch

常见问题：

```text
LiDAR: one campaign/year or several years
Optical: days–weeks
Meteorology/EC: 30 min–hourly
```

如果直接把静态 LiDAR 当成每个 timestep 的动态信息，需要明确它表达的是 slowly varying structural prior。

---

## 6. Evaluation

2D+3D fusion 必须做 paired ablation：

```text
optical-only
vs
optical + LiDAR
```

保持 split、training、sample 完全一致，才能判断 3D modality 的实际增益。

## Sources

- NASA GEDI mission/data documentation: https://gedi.umd.edu/
- PointNet: https://arxiv.org/abs/1612.00593
