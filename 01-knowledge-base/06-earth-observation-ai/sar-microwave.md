# SAR / Microwave AI

## 1. SAR 测到什么

Synthetic Aperture Radar 主动发射 microwave 并接收 backscatter。

与 optical 最大区别：
- 主动 sensing；
- all-weather / day-night capability；
- phase / coherence 可提供额外信息；
- scattering mechanism 与 optical reflectance 完全不同。

---

## 2. 关键变量

### Wavelength
X/C/L/P band 对 vegetation penetration 与 scattering sensitivity 不同。

### Polarization
`HH`, `HV`, `VV`, `VH` 等反映不同 scattering path。

### Incidence angle
同一 surface 在不同 incidence angle 下 backscatter 会变化。

### Dielectric property
water strongly affects dielectric constant，因此 soil/vegetation moisture 与 microwave signal 强相关。

### Surface roughness / structure
roughness、orientation、canopy architecture 都会改变 scattering。

---

## 3. Speckle

SAR coherent imaging 产生 speckle。它不是普通 additive Gaussian noise。

处理选择：
- filtering；
- log transform；
- multi-look；
- network learned representation。

过度滤波会损失 edges/small objects。

---

## 4. Preprocessing

常见：

```text
radiometric calibration
→ speckle-aware processing
→ terrain correction
→ geocoding
→ incidence/geometry handling
```

如果与 optical fusion，还要 co-registration。

---

## 5. AI representation

- amplitude/backscatter channels；
- multi-polarization；
- complex-valued representation（特定任务）；
- interferometric coherence/phase；
- multi-temporal SAR sequence。

---

## 6. 2026 foundation-model context

截至 2026-08-20，SAR foundation modeling 已形成独立研究线：
- SAR-only self-supervised pretraining；
- SAR–optical multimodal pretraining；
- vision-language；
- generative cross-modal modeling。

`MaRS`（AAAI 2026）是 VHR SAR–optical multimodal foundation model 的代表之一；2026 年的 SAR foundation-model review 进一步系统化了 visual/multimodal/generative taxonomy。

## Sources

- MaRS, AAAI 2026: https://ojs.aaai.org/index.php/AAAI/article/view/38153
- Hou et al. (2026), *SAR foundation models: a comprehensive review of data, models, and applications*, Science China Information Sciences.
