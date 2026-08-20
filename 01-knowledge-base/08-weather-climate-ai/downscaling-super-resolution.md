# Weather Downscaling 与 Super-resolution

## 1. 问题

```text
coarse global forecast
→ local/high-resolution field
```

可能同时需要：
- spatial refinement；
- bias correction；
- local topography；
- probabilistic detail。

---

## 2. Dynamical downscaling

用 regional numerical model 嵌套 coarse boundary conditions。

优点：保留 regional physics；
代价：compute 高。

---

## 3. Statistical / ML downscaling

```text
coarse field + static terrain + context
→ fine field
```

模型：CNN/U-Net/Transformer/GNN。

---

## 4. Generative downscaling

Diffusion/generative method 适合恢复 plausible fine-scale variability：

```text
p(X_high | X_coarse, static)
```

但生成 realistic texture 不等于真实 event reconstruction。

---

## 5. CorrDiff / Earth-2

NVIDIA `CorrDiff` 是 generative regional downscaling route 的代表，Earth-2 将 global forecast、nowcasting/downscaling 组织为更完整的 weather AI stack。

Official Earth-2: https://www.nvidia.com/en-us/high-performance-computing/earth-2/

---

## 6. Orography / coast

高分辨率 temperature/wind/precipitation 强依赖：
- elevation；
- slope/aspect；
- coast；
- land cover；
- urban effects。

static features 应与 high-res grid 对齐。

---

## 7. Evaluation

不仅 RMSE：
- precipitation distribution；
- extremes；
- spectra；
- spatial correlation；
- topographic gradients；
- station verification；
- probabilistic calibration。

downscaled output resolution 也不自动等于 independent observation resolution。
