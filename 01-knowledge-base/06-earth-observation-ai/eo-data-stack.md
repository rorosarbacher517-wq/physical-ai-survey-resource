# Earth Observation Data Stack

## 1. Product level

不同 mission 定义略有差异，但常见逻辑：

```text
raw telemetry
→ Level-1 calibrated/geolocated measurement
→ Level-2 geophysical variable / corrected reflectance
→ Level-3 gridded/composited product
→ Level-4 model-derived product
```

AI 使用 product 时必须记录 level，因为 `raw radiance` 与 `surface reflectance` 对 model 的物理要求不同。

---

## 2. 典型 Earth data family

### Optical
- Landsat；
- Sentinel-2；
- HLS；
- MODIS / VIIRS。

### SAR / microwave
- Sentinel-1；
- ALOS/PALSAR；
- SMAP/SMOS（passive/active microwave context）。

### LiDAR
- GEDI；
- ICESat-2；
- airborne LiDAR / NEON AOP。

### Thermal
- Landsat TIRS；
- ECOSTRESS；
- MODIS/VIIRS LST products。

### SIF
- OCO-2 / OCO-3；
- TROPOMI；
- tower spectrometer / regional products。

---

## 3. HLS 为什么常用于生态 AI

Harmonized Landsat and Sentinel-2 将 Landsat 与 Sentinel-2 数据 harmonize 到共同 30 m framework，适合：
- vegetation time series；
- disturbance；
- carbon/ecosystem modeling；
- multi-temporal foundation pretraining。

`Prithvi-EO-2.0` 官方资料说明其使用约 4.2M global HLS time-series samples 进行 pretraining。

---

## 4. Label stack

Remote-sensing label 可来自：
- field survey；
- inventory；
- polygon map；
- another satellite product；
- station/tower；
- simulation/reanalysis；
- manually annotated objects。

每一种 label 都有不同 support 和 uncertainty。

---

## 5. Sample manifest

建议每个 sample 至少记录：

```text
sample_id
sensor/product/version
acquisition_time
CRS / transform
native resolution
QA flags
valid fraction
label source
label support
split group
provenance
```

---

## 6. Sources

- NASA HLS project: https://www.earthdata.nasa.gov/data/projects/hls
- Prithvi-EO-2.0 official repo: https://github.com/NASA-IMPACT/Prithvi-EO-2.0
