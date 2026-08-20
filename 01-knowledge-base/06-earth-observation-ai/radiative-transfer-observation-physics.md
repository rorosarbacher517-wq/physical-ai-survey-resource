# Radiative Transfer 与 Remote-sensing Observation Physics

## 1. 为什么要从这里学

AI 看到的 `reflectance`、`backscatter`、`brightness temperature`、`SIF` 并不是 surface state 本身，而是经过 observation process 的结果。

统一形式：

```text
y = H(x; geometry, atmosphere, sensor) + ε
```

---

## 2. Optical radiative transfer

简化 chain：

```text
solar irradiance E0
→ atmospheric transmittance
→ surface/canopy absorption + scattering
→ upward radiance L
→ sensor spectral response
```

Top-of-atmosphere radiance 与 surface reflectance 之间还受到：
- aerosol；
- water vapor；
- ozone；
- adjacency effect；
- sun-view geometry。

### AI 意义
同一个 surface state 在不同 geometry/atmosphere 下可能产生不同 observation。

---

## 3. BRDF

Bidirectional Reflectance Distribution Function 描述反射随 illumination/view geometry 变化。

因此 multi-date optical time series 中的变化可能同时来自：
- vegetation/process change；
- sun angle；
- view angle；
- atmosphere。

模型若不处理 geometry，可能把观测几何当成 phenology。

---

## 4. Thermal emission

理想 blackbody 的 spectral radiance 与 temperature 由 Planck law 关联；真实 surface 还需要 emissivity：

```text
L_λ ≈ ε_λ B_λ(T) + atmospheric terms
```

所以 brightness temperature ≠ land surface temperature 的完全等价物。

---

## 5. Microwave / SAR scattering

SAR observation 受：
- wavelength；
- polarization；
- incidence angle；
- roughness；
- dielectric constant；
- vegetation structure；
- moisture。

因此“光学模型换 channel 直接用 SAR”通常缺少正确 inductive bias。

---

## 6. LiDAR ranging

理想 range：

```text
R = c Δt / 2
```

实际还涉及 waveform、multiple returns、scan geometry、geolocation error、canopy penetration。

---

## 7. SIF

Solar-induced chlorophyll fluorescence 是 photosynthetic machinery 释放的弱辐射信号，但 observed SIF 还受到：
- absorbed PAR；
- fluorescence yield；
- canopy structure；
- reabsorption；
- viewing geometry；
- atmosphere。

所以 SIF 与 GPP 有过程联系，但**不是 GPP 的直接 measurement**。

---

## 8. AI 中的四种使用方式

1. 直接用 corrected product 作为 input；
2. 把 geometry/atmosphere metadata 作为 feature；
3. 用 physical simulator 生成 training/synthetic data；
4. 将 radiative-transfer model 作为 differentiable forward operator 做 retrieval/inverse learning。

## Sources

- Rodgers, *Inverse Methods for Atmospheric Sounding*.
- MODTRAN / 6S / PROSAIL 等 radiative-transfer family 的官方/原始文献用于具体应用。
- ESA/NASA 各 sensor product guide 用于 product-specific observation semantics。
