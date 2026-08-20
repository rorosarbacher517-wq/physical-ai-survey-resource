# Super-resolution、Downscaling 与 Time-series Reconstruction

## 1. 三个问题要分开

### Image super-resolution
低分辨率 observation → 高分辨率 image-like field。

### Statistical/dynamical downscaling
coarse environmental/climate field → local/high-resolution target distribution。

### Temporal reconstruction
稀疏/缺测时间序列 → dense time series。

它们都“变细”，但 scientific meaning 不同。

---

## 2. Spatial SR

```text
X_lr [B,C,H,W]
→ model
→ X_hr [B,C,sH,sW]
```

必须问：高频细节来自真实 information，还是 learned prior/hallucination？

---

## 3. Multi-sensor SR

可以用 high-temporal coarse sensor + low-temporal high-resolution sensor：

```text
coarse dense time series
+ sparse high-res observations
→ high-res dense reconstruction
```

适用于 HLS 与更高频 coarse product 的融合思路。

---

## 4. Generative reconstruction

Diffusion/generative model 能生成 realistic fine detail，但 scientific task 必须评估：
- conditional consistency；
- conservation/aggregate consistency；
- uncertainty；
- event/extreme preservation。

---

## 5. Carbon/eco 应用

高时频 coarse reflectance/biophysical product 可帮助填补 HLS clear-sky gaps，但重建后的 canopy state 仍是 model estimate，不能当真实 acquisition。

---

## 6. Evaluation

除了 PSNR/SSIM，还应检查：
- spectral consistency；
- aggregate conservation；
- downstream flux/task impact；
- temporal phase/phenology；
- extreme change；
- unseen region/year。
