# 06 · Earth Observation / Remote Sensing AI

Remote Sensing AI 的正确学习顺序不是“CNN → ViT → foundation model”，而是：

```text
physical state
→ electromagnetic / ranging interaction
→ atmosphere / geometry / sensor response
→ measured signal
→ calibration / correction / retrieval / QA
→ spatiotemporal representation
→ AI model
→ geophysical/ecological inference
→ scale-aware / OOD validation
```

## 1. 五类核心 sensing modality

| Modality | 主要 measurement | 关键 physics | 典型 AI representation |
|---|---|---|---|
| Optical / Hyperspectral | radiance / reflectance | absorption, scattering, atmosphere, BRDF | raster / spectral-spatial tokens |
| SAR / Microwave | backscatter / brightness temperature | scattering, dielectric property, roughness, polarization | complex/real raster, multi-pol channels |
| LiDAR | range / waveform / return | time-of-flight, geometry | point cloud / voxel / height raster |
| Thermal IR | emitted radiance / temperature-related signal | Planck emission, emissivity, atmosphere | raster / temporal field |
| SIF | weak fluorescence radiance | photosynthesis-linked fluorescence + canopy/atmosphere transfer | spectral retrieval / raster/time series |

这些 modality **不能简单理解成多几个 channel**，因为 observation operator 不同。

---

## 2. 统一 observation chain

### Optical

```text
solar irradiance
→ atmosphere
→ canopy/surface interaction
→ atmosphere
→ sensor spectral response
→ radiance
→ atmospheric correction
→ surface reflectance
```

### SAR

```text
transmitted microwave
→ surface/volume scattering
→ polarization + incidence geometry
→ returned complex signal
→ calibration / terrain correction
→ backscatter representation
```

### LiDAR

```text
laser pulse
→ target interaction
→ return time / waveform
→ range
→ point cloud
→ height/profile/structure
```

---

## 3. Data stack

Earth Observation learning system通常包含：

```text
Level-1 measurement
→ Level-2 geophysical product / surface reflectance
→ QA mask
→ reprojection / resampling
→ temporal alignment
→ spatial crop / tile
→ feature/label pairing
→ train/val/test split
```

需要记录：sensor、product level、processing baseline/version、CRS、native resolution、revisit、quality flags。

→ [EO Data Stack](eo-data-stack.md)

---

## 4. AI task map

### Perception / mapping
- classification；
- semantic / instance segmentation；
- object detection；
- change detection。

### Quantitative retrieval / regression
- LAI / biomass / soil moisture；
- LST；
- atmospheric variables；
- ecological variables。

### Temporal tasks
- gap filling；
- reconstruction；
- forecasting；
- phenology/event detection。

### Generative / foundation
- masked reconstruction；
- cross-modal generation；
- representation learning；
- geospatial embedding；
- zero/few-shot / PEFT transfer。

---

## 5. Multisensor 的真正难点

不是 concat，而是五种 mismatch：

```text
spatial resolution mismatch
temporal acquisition mismatch
observation-physics mismatch
geometry mismatch
uncertainty / missingness mismatch
```

例如 optical + SAR 可互补 cloud/weather，但 backscatter 与 reflectance 的物理含义完全不同；LiDAR 可能多年只飞一次，而 flux/meteorology 每 30 min–1 h 变化。

---

## 6. Foundation-model 转变

截至 2026-08-20，需要区分两种接口：

### Downloadable encoder / weights
例如 `Prithvi-EO-2.0`, `TerraMind`, `MaRS`。

### Ready-made embedding field / embedding-as-data
例如 `AlphaEarth Foundations`, `TESSERA`。

第二种情况下，使用者可能根本不运行 foundation encoder，而是直接读取全球 embedding product。

---

## 7. 当前重点页面

- [Radiative Transfer / Observation Physics](radiative-transfer-observation-physics.md)
- [EO Data Stack](eo-data-stack.md)
- [Optical / Hyperspectral](optical-hyperspectral.md)
- [SAR / Microwave](sar-microwave.md)
- [LiDAR / 3D](lidar-3d.md)
- [Thermal / SIF](thermal-sif.md)
- [Preprocessing / QA](eo-preprocessing-quality.md)
- [Remote-sensing Time Series](remote-sensing-time-series.md)
- [Multisensor Fusion](multisensor-fusion.md)
- [Retrieval / Inverse](retrieval-inversion.md)
- [Super-resolution / Reconstruction](super-resolution-reconstruction.md)
- [EO Tasks / Models](eo-models-tasks.md)
- [EO Foundation Models](eo-foundation-models.md)
- [Geospatial Validation / OOD](geospatial-validation.md)

---

## 8. 统一 evaluation checklist

任何 EO claim 至少问：

1. native sensor resolution？
2. input product level？
3. spatial/temporal resampling？
4. cloud/QA/missingness？
5. label 来源与 support？
6. geographic split？
7. temporal split？
8. unseen sensor/region/biome？
9. frozen / linear probe / PEFT / full fine-tune？
10. output resolution 是否真的有同尺度 independent reference？

---

## 9. 当前 primary / official anchors

- Prithvi-EO-2.0 official repo: https://github.com/NASA-IMPACT/Prithvi-EO-2.0
- TerraMind, ICCV 2025: https://openaccess.thecvf.com/content/ICCV2025/html/Jakubik_TerraMind_Large-Scale_Generative_Multimodality_for_Earth_Observation_ICCV_2025_paper.html
- AlphaEarth Foundations official: https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/ <!-- manual-review: official source URL path -->
- TESSERA project: https://geotessera.org/
- PANGAEA benchmark: https://arxiv.org/abs/2412.04204

最新版本和日期见 [2026 Snapshot](../13-2026-snapshot/index.md)。
