# Carbon–Water–Energy Coupling

Terrestrial carbon flux 不能脱离 water 和 energy 单独理解。

## 1. Photosynthesis 与 stomata

CO₂ uptake 与 water vapor loss 通过 stomatal conductance 耦合：

```text
CO2 enters leaf
H2O exits leaf
```

因此 VPD、soil moisture、radiation 会共同调节 GPP。

---

## 2. Surface energy balance

概念形式：

```text
R_n = H + LE + G + storage
```

- `R_n`：net radiation；
- `H`：sensible heat；
- `LE`：latent heat；
- `G`：ground heat flux。

water stress 降低 transpiration 时，可改变 `LE` 与 canopy temperature。

这解释了为什么 thermal EO 对 vegetation stress 有补充价值。

---

## 3. Soil moisture × VPD

### Atmospheric drought
高 `VPD` 增强 evaporative demand，可能引起 stomatal closure。

### Soil drought
低 soil moisture 限制 plant water supply。

两者可能：
- 独立；
- 同时发生；
- 对不同 biome 产生不同 response。

所以不能用一个“dry”变量概括所有 drought mechanism。

---

## 4. Radiation × heterogeneity

在空间异质 landscape 中，相邻 patches 若具有不同 vegetation/water status：

```text
radiation / VPD / soil moisture forcing
→ patch-specific GPP/RECO contrast
→ dynamic footprint changes patch contribution
→ tower observation changes
```

这说明 weather forcing 可以**放大或抑制** footprint spatial mismatch 的影响，而不是 footprint 与 meteorology 完全独立。

---

## 5. Model design

可做：
- joint carbon/water/energy prediction；
- multi-task loss；
- shared latent state；
- process constraints；
- thermal + soil moisture + optical fusion；
- stress-regime stratification。

---

## 6. Failure modes

- 用 NDVI 单独代表 water stress；
- 只看 soil moisture 不看 atmospheric demand；
- 把 correlation with radiation 直接解释成 mechanism；
- day/night 混合导致 driver importance 难解释；
- coarse soil-moisture support 与 tower/EO mismatch。

## Sources

- ecosystem physiology / stomatal conductance literature；
- FLUXNET energy/carbon flux observations；
- 2026 XGBoost EC gap-filling study: https://doi.org/10.1016/j.agrformet.2025.110987
