# Flux Footprints · EC 的 Spatial Observation Support

## 1. Footprint 是什么

Flux footprint 描述不同 upwind surface locations 对某次 EC measurement 的相对贡献。

连续表示：

```text
f(x,y,t) ≥ 0
```

积分/归一化后得到 source contribution distribution。

---

## 2. 为什么 footprint 动态变化

主要相关因素包括：
- wind direction；
- friction velocity `u*`；
- atmospheric stability / Obukhov length `L`；
- cross-wind turbulence `σ_v`；
- measurement height；
- roughness / displacement height；
- boundary-layer conditions。

因此 footprint 的 location、extent、shape 每个 averaging period 都可不同。

---

## 3. Continuous footprint → raster weights

如果 satellite grid 为 `H×W`：

```text
continuous f(x,y)
→ integrate/sample per pixel
→ apply valid-data mask
→ normalize
→ W [H,W]
```

需注意：
- CRS；
- tower/sensor orientation；
- wind-direction convention；
- pixel area；
- clipped footprint mass；
- missing pixels。

---

## 4. Footprint 的五种角色

### A. Predictor aggregation

```text
pixels → footprint-weight features → tower model
```

### B. Prediction aggregation / Observation operator

```text
pixels → pixel flux field → footprint-weight output → tower loss
```

### C. Flux disaggregation
利用动态 footprint + land-cover fractions 推断 latent class-specific flux。

### D. Representativeness analysis
分析 tower 实际采样哪些 land-cover/vegetation conditions。

### E. Footprint geometry as feature
把 extent/shape/center 等作为 predictor。

**E 与真正使用 footprint weights 的 observation operator 不等价。**

---

## 5. Footprint uncertainty

来源：
- input meteorology；
- canopy displacement/roughness estimates；
- model assumptions；
- complex terrain / canopy；
- advection/non-stationarity。

未来模型可以把 `W` 作为 uncertain operator，而不是完全确定的 mask。

---

## 6. 2026 synthesis

Chu et al. (2026) 系统强调了 flux footprints 在连接 EC 与 models、remote sensing 和其他 observations 中的作用，说明 source-area matching 已成为跨数据整合中的核心问题。

## Sources

- Kljun et al. (2015): https://doi.org/10.5194/gmd-8-3695-2015
- Chu et al. (2026): https://doi.org/10.1111/gcb.70887
