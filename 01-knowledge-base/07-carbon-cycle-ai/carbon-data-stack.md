# Carbon AI Data Stack

## 1. Tower observations

### Flux networks
- `FLUXNET2015`；
- `AmeriFlux`；
- `ICOS`；
- regional networks。

常见 flux：`NEE`, `GPP`, `RECO`, `LE`, `H` 等。

---

## 2. Optical EO

- `HLS`：30 m harmonized Landsat/Sentinel-2；
- Landsat / Sentinel-2；
- MODIS / VIIRS；
- high-resolution commercial/public imagery where licensed。

信息：vegetation spectral state、phenology、disturbance、surface heterogeneity。

---

## 3. Meteorology / Reanalysis

- tower meteorology；
- `ERA5 / ERA5-Land`；
- other regional/global forcing。

典型 variables：

```text
Tair, radiation, precipitation,
RH/VPD, wind, pressure,
soil temperature/moisture,
BLH/stability-related variables
```

注意 accumulated vs instantaneous variable semantics。

---

## 4. Soil moisture / microwave

`SMAP`, `SMOS` 等可提供 water-state constraint，但 spatial support 常比 tower/30 m EO 粗得多。

---

## 5. SIF / Thermal

SIF：photosynthesis-related radiative signal；
Thermal：temperature / energy balance / stress context。

二者都需要 scale matching。

---

## 6. LiDAR / structure

- airborne LiDAR；
- GEDI；
- NEON AOP；
- canopy height products。

用于 structure：height、vertical profile、biomass-related geometry。

---

## 7. Static/context data

- land cover；
- soil properties；
- topography；
- disturbance history；
- management；
- climate normals。

---

## 8. Sample construction

一个 site-day / site-window sample 可包含：

```text
site_id
time window
EO scene IDs + QA
meteorology sequence
flux target + QC
partitioning version
footprint sequence
static context
split fold
```

---

## 9. Leakage safeguards

- same site 不跨 train/test；
- normalization stats 只从 train；
- EO temporal interpolation 不偷看 test future；
- foundation pretraining overlap 单独记录；
- duplicated tower products/version 不重复算独立样本。

## Sources

- FLUXNET2015: https://doi.org/10.1038/s41597-020-0534-3
- AmeriFlux: https://ameriflux.lbl.gov/
- HLS: https://www.earthdata.nasa.gov/data/projects/hls
- ERA5: https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5
