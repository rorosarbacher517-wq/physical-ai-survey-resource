# Multisensor Fusion：不是简单 Channel Concatenation

## 1. 先写 observation operators

```text
state x
├─ H_optical → reflectance
├─ H_SAR     → backscatter
├─ H_LiDAR   → point/height
├─ H_thermal → emitted radiance/LST
└─ H_SIF     → fluorescence observation
```

不同 `H` 决定不同 modality 的 information content。

---

## 2. 五种对齐

### Spatial
10 m、30 m、1 km、footprint/polygon 如何匹配？

### Temporal
same day、nearest date、window composite、asynchronous sequence？

### Geometric
optical/SAR parallax、terrain、view angle、LiDAR geolocation。

### Statistical
value range、noise distribution、missingness。

### Physical
modality 表达的是 structure、state、energy、moisture 还是 scattering？

---

## 3. Fusion architecture

### Early fusion

```text
concat channels → shared encoder
```

适合高度共注册、同尺度 modality。

### Late fusion

```text
encoder_A → z_A
encoder_B → z_B
→ fusion head
```

适合 physics 差异较大的 modality。

### Cross-attention

```text
Q from A, K/V from B
```

适合 heterogeneous tokens。

### Gated / modality-aware fusion
learn gate 控制每个 modality contribution，可减轻 noisy modality negative transfer。

---

## 4. 2D + 3D + Time 示例

```text
Optical [B,T,C,H,W] → 2D encoder ─┐
LiDAR  [B,N,D]       → 3D encoder ├→ fusion → temporal model → target
Mete    [B,T,P]       → MLP/encoder┘
```

如果 LiDAR 是 static campaign，可先编码为 structural latent，再广播/条件化时序，而不是假装它每个 timestep 都更新。

---

## 5. Negative transfer

多模态模型必须做：
- modality-only baselines；
- paired fusion ablation；
- missing-modality test；
- temporal-mismatch sensitivity；
- noise robustness。

---

## 6. 2026 context

`TerraMind`、`MaRS`、`AlphaEarth Foundations` 等表明 EO foundation modeling 正从 optical-only 向 multimodal representation 扩展，但 multimodality 仍需要 downstream task-specific evaluation。

## Sources

- TerraMind, ICCV 2025: https://openaccess.thecvf.com/content/ICCV2025/html/Jakubik_TerraMind_Large-Scale_Generative_Multimodality_for_Earth_Observation_ICCV_2025_paper.html
- MaRS, AAAI 2026: https://ojs.aaai.org/index.php/AAAI/article/view/38153
