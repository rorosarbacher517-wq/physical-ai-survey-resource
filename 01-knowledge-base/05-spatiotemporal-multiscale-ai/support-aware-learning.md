# Support-aware Learning

## 1. 核心问题

很多 Scientific AI label 不是 point value，而是某个 support 上的 aggregation：

```text
latent field F(x,t)
→ observation operator H_t
→ observed target y_t
```

---

## 2. 离散形式

```text
ŷ_t = Σ_i w_{i,t} F̂_{i,t}
```

要求：

```text
w_i ≥ 0
Σ_i w_i = 1
```

是否需要满足这两个条件取决于实际 operator definition，但 normalized spatial weights 常见。

---

## 3. Input aggregation vs Output aggregation

### Input-side

```text
pixels → weighted predictors → model → y
```

### Output-side

```text
pixels → field model → weighted outputs → y
```

后者保留 latent spatial field，更接近 observation mapping。

---

## 4. Nonlinear transformation

一般：

```text
Σ_i w_i g(x_i) ≠ g(Σ_i w_i x_i)
```

因此“先算 NDVI 再 footprint-weight”和“先 weight bands 再算 NDVI”含义不同。

---

## 5. Validation

如果 supervision 是 coarse/area support，就不能仅凭 model latent output grid 声称 fine-scale field 已被独立验证。

这条原则同时适用于：
- EC footprint；
- coarse satellite product；
- station/grid matching；
- polygon labels。
