# Thermal Infrared 与 Solar-induced Chlorophyll Fluorescence (SIF)

## 1. Thermal IR

Observed thermal radiance 主要受：
- surface temperature；
- emissivity；
- atmosphere；
- view geometry。

简化：

```text
L_λ ≈ ε_λ B_λ(T_s) + atmospheric contribution
```

Land Surface Temperature (LST) 是 retrieval product，不是 sensor 直接“测温计式”的 measurement。

---

## 2. Thermal 与 ecosystem

可提供：
- canopy/soil temperature；
- evapotranspiration constraints；
- water stress；
- surface energy balance information。

但空间尺度与 overpass time 很关键。

---

## 3. SIF

SIF 是 chlorophyll 在吸收光能后释放的一部分 fluorescence signal。

过程链：

```text
incoming PAR
→ absorbed PAR
→ photochemistry + heat dissipation + fluorescence
→ canopy radiative transfer
→ top-of-canopy / satellite SIF
```

因此：

```text
SIF ≠ GPP
```

但二者共享 photosynthetic energy partitioning 和 APAR 相关信息。

---

## 4. SIF + EC / GPP learning

可用于：
- GPP constraint；
- transfer learning；
- drought/heat response；
- sub-daily photosynthesis diagnostics。

2025 的 transfer-learning 工作展示了 combined SIF + EC information 用于 GPP estimation 的路线。

---

## 5. Failure modes

- coarse SIF footprint 与 tower support mismatch；
- cloud/quality filtering；
- fluorescence yield 与 GPP relationship regime-dependent；
- canopy structure / reabsorption；
- seasonal correlation 被误当直接 causality。

## Sources

- Ma et al. (2025), *GPP estimation by transfer learning with combined solar-induced chlorophyll fluorescence and eddy covariance data*, Int. J. Applied Earth Observation and Geoinformation, DOI: 10.1016/j.jag.2025.104503.
