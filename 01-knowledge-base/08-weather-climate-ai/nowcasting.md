# Nowcasting

## 1. 时间尺度

Nowcasting 通常关注 minutes 到 several hours 的短时天气演变，尤其：
- precipitation；
- convection；
- storm cells；
- cloud evolution。

它和 1–15 day global medium-range forecasting 是不同 problem。

---

## 2. Inputs

- weather radar sequence；
- geostationary satellite imagery；
- lightning；
- stations；
- short-range NWP context。

典型：

```text
X [B,T,C,H,W]
→ future fields [B,T_future,C_out,H,W]
```

---

## 3. Methods

- optical-flow / extrapolation；
- ConvLSTM；
- U-Net / encoder-decoder；
- Transformer；
- diffusion/generative models。

---

## 4. 为什么 generative useful

强对流未来存在多个 plausible evolutions。deterministic MSE 容易生成 blurry precipitation field。

generative model 可以 sample multiple scenarios，但必须 calibration。

---

## 5. NVIDIA Earth-2 context

2026-01 NVIDIA Earth-2 open weather stack 包含 nowcasting model，使用 satellite/radar information 预测 clouds/rainfall evolution。

Official: https://blogs.nvidia.com/blog/nvidia-earth-2-open-models/

---

## 6. Metrics

- CSI / FSS；
- thresholded precipitation skill；
- CRPS / ensemble metrics；
- object/storm tracking；
- displacement error；
- heavy-rain tail。

pixel RMSE 往往不能完整评价 storm structure。
