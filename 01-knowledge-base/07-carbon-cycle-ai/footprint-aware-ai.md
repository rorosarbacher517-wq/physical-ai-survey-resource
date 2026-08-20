# Footprint-aware AI：把 Source-area Physics 放进 Learning

## 1. 问题定义

固定遥感 window：

```text
all valid pixels → equal/static treatment
```

真实 EC observation：

```text
pixels → dynamic turbulence-dependent weights
```

在 homogeneous surface 上差异可能很小；在 heterogeneous landscape 上可能产生显著 representativeness mismatch。

---

## 2. Tensor design

```text
EO input       X [B,T,C,H,W]
meteorology    M [B,T,P]
footprint      W [B,T,H,W]
pixel flux     F [B,T,K,H,W]
tower target   Y [B,T,K]
```

要求每个 timestep：

```text
Σ_h Σ_w W[b,t,h,w] = 1
```

（在 normalized valid-footprint convention 下）。

---

## 3. Output-side observation operator

model：

```text
F_hat = f_θ(X,M,...)
```

operator：

```text
Y_hat[b,t,k]
= Σ_h Σ_w W[b,t,h,w] F_hat[b,t,k,h,w]
```

loss：

```text
L_obs = ||Y_hat - Y_obs||²_masked
```

优点：pixel latent field 保留下来；tower supervision 通过真实 support 映射。

---

## 4. Input-side aggregation

另一种路线：

```text
X_bar[t,c] = Σ_i W[t,i] X[t,c,i]
X_bar → tower model
```

更简单，但模型只在 footprint-aggregated feature space 工作，无法直接产生由 tower supervision 验证的 pixel latent flux structure。

---

## 5. Nonlinear predictor trap

若 vegetation index `g` 非线性：

```text
Σ_i w_i g(x_i) ≠ g(Σ_i w_i x_i)
```

例如：

```text
weighted mean of pixel NDVI
≠
NDVI of weighted mean Red/NIR
```

两者都可能有用途，但科学含义不同。

---

## 6. Paired ablation

最干净的验证设计：

```text
Baseline: identical model/data/split + uniform weights
FAT-like: identical model/data/split + dynamic footprint weights
```

定义 paired error gain，例如：

```text
Δ|AE| = |AE_uniform| - |AE_footprint|
```

正值表示 footprint-aware 误差更小（按此 convention）。

---

## 7. 什么时候 footprint 更可能重要

需要三个条件共同出现：

```text
spatial flux-relevant heterogeneity
× dynamic source-area movement
× environmental forcing that creates patch contrast
```

如果 surface 高度 homogeneous，即使 footprint 移动，weighted field 也变化不大。

---

## 8. Diagnostic variables

- NDVI/reflectance heterogeneity；
- land-cover edges；
- canopy roughness/height variation；
- footprint–uniform vegetation mismatch；
- wind direction variability；
- stability / turbulence；
- radiation / soil moisture / VPD；
- season/daytime。

---

## 9. 当前 evidence

- 2025 RSE：footprint-weighted spatial features + GNN residual modeling：https://doi.org/10.1016/j.rse.2025.114952
- 2026 footprint synthesis：https://doi.org/10.1111/gcb.70887

## 10. Failure modes

- footprint 与 satellite grid misregistration；
- invalid pixels renormalized incorrectly；
- footprint mass 超出 patch 被忽略；
- wind direction convention 错；
- 同日/static EO 被误描述为 half-hourly canopy observation；
- tower-scale gain 被误写成 pixel-map independent validation。
