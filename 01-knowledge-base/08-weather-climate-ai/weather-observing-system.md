# Weather Observing System：AI Forecast 上游的数据从哪里来

## 1. 为什么 observation 层不能跳过

全球 atmospheric state 不可能被每个 grid cell/level 直接测量。

真实结构：

```text
heterogeneous observations
→ observation operators / QC
→ state estimation / DA
→ gridded analysis
```

很多 AI weather papers 从 ERA5 开始，因此输入已经是 assimilation product，而不是 raw observation。

---

## 2. Satellite radiances

polar-orbiting / geostationary satellites 提供大量 radiance observations。

它们通过 radiative-transfer operator 与：
- temperature profile；
- humidity；
- cloud；
- surface emission

联系。

在 operational DA 中，常可直接 assimilate radiances，而不是必须先 retrieval 成 temperature image。

---

## 3. Radiosonde

提供 vertical profile：
- temperature；
- humidity；
- wind；
- pressure/height。

空间覆盖稀疏但 vertical information 强。

---

## 4. Surface / marine observations

- weather stations；
- ships；
- drifting/moored buoys；
- automatic platforms。

提供 near-surface variables，但 geographic sampling 不均。

---

## 5. Aircraft observations

commercial/meteorological aircraft 提供 flight-level temperature/wind 等，是高空 observing system 的重要组成。

---

## 6. Radar

weather radar 提供：
- reflectivity；
- radial velocity；
- derived precipitation-related information。

适合 nowcasting 与 convective-scale DA，但 domain 主要是 regional。

---

## 7. GNSS / other observations

GNSS radio occultation 等可提供 atmospheric refractivity/profile constraints；具体 assimilated quantity 依 system。

---

## 8. AI representation

raw observation 是 irregular set：

```text
O = {(type_i, location_i, time_i, value_i, error_i, metadata_i)}
```

可用：
- pre-gridding；
- set/point encoder；
- PointPillars-style sparse encoder；
- cross-attention to latent grid；
- graph observation network。

`Aardvark Weather` 与 `FuXi Weather` 展示了不同 observation-to-state/forecast representation 路线。

## Sources

- ECMWF observation / DA documentation: https://www.ecmwf.int/en/research/data-assimilation
- Aardvark Weather: https://doi.org/10.1038/s41586-025-08897-0
- FuXi Weather: https://doi.org/10.1038/s41467-025-62024-1
