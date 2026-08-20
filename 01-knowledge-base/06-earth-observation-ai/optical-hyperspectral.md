# Optical Multispectral 与 Hyperspectral

## 1. Multispectral

典型输入：

```text
X [B,C,H,W]
```

`C` 不是 RGB，而可能是 Blue / Green / Red / NIR / SWIR1 / SWIR2 等具有不同 spectral response 的 band。

---

## 2. 为什么 NIR / SWIR 有用

### NIR
受 leaf internal scattering 与 canopy structure 影响，对 vegetation state 很敏感。

### SWIR
与 water content、dry matter、soil/mineral properties 等有关。

但“某 band 与某 process 相关”不等于“一一对应”。

---

## 3. Vegetation indices

### NDVI

```text
NDVI = (NIR-Red)/(NIR+Red)
```

### NIRv
常用于增强 vegetation contribution 的表征。

### 重要非线性问题

一般：

```text
Σ_i w_i NDVI_i ≠ NDVI(Σ_i w_i bands_i)
```

因此 footprint/polygon aggregation 时要先明确 scientific meaning。

---

## 4. Hyperspectral

高 spectral resolution：

```text
X [B,C_hyper,H,W], C_hyper >> multispectral C
```

挑战：
- high-dimensional；
- spectral redundancy；
- sensor noise；
- atmospheric absorption bands；
- limited labels。

常用：
- spectral CNN；
- 3D CNN；
- spectral-spatial Transformer；
- masked spectral pretraining。

---

## 5. Spectral response function

不同 sensor 即使 band 名相同，response function 也不同。跨 sensor fusion 必须考虑：
- central wavelength；
- bandwidth；
- response curve；
- calibration/harmonization。

---

## 6. Time series

Optical time series 的 missingness 不是 random：cloud、season、solar angle 会造成结构性缺测。

因此 reconstruction/phenology model 要输入 mask 与 timestamp，而不是简单 zero-fill。

## Sources

- Claverie et al. (2018), HLS description, Remote Sensing of Environment.
- NASA HLS: https://www.earthdata.nasa.gov/data/projects/hls
