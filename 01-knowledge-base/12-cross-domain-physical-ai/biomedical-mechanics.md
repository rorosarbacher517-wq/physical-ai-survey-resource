# Biomedical Mechanics / Biomedical Physical AI

## 1. 统一问题结构

```text
biological state / anatomy / physiology
→ imaging / sensors / assays
→ inverse inference
→ mechanics / dynamics model
→ diagnosis / prediction / intervention
```

这与 Earth Observation 的 state→observation→inverse chain 非常相似。

---

## 2. Imaging as observation

MRI、CT、ultrasound、microscopy 等不是“真实组织状态本身”，而是通过不同 physical forward processes 得到的 measurements。

因此 reconstruction 常是 inverse problem：

```text
measurement y
→ reconstruct image/state x
```

---

## 3. Biomechanics

可以模拟：
- blood flow；
- heart mechanics；
- soft tissue deformation；
- bone mechanics；
- respiratory flow。

AI 可作为：
- PDE surrogate；
- parameter estimator；
- segmentation-to-mesh pipeline；
- personalized boundary-condition model。

---

## 4. Patient-specific modeling

```text
imaging + measurements
→ geometry/state estimation
→ calibrated physical model
→ intervention simulation
```

核心挑战是 parameter identifiability 与 uncertainty。

---

## 5. Digital patient / twin

如果持续用 new measurements 更新 latent physiological state，就与 Data Assimilation / digital twin 有共同结构。

---

## 6. Safety / validation

高风险 biomedical task 需要：
- external clinical validation；
- subgroup analysis；
- uncertainty；
- calibration；
- failure detection；
- regulatory/context-specific evidence。

研究 benchmark 指标不能直接等价为 clinical utility。
