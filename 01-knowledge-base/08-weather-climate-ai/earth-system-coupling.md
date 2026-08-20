# Coupled Earth-system AI

## 1. 大气不是孤立系统

```text
atmosphere
↕
ocean
↕
land / vegetation / soil
↕
cryosphere
↕
waves / chemistry / carbon
```

medium-range weather 某些系统可使用 prescribed boundary variables，但 seasonal/climate/Earth-system prediction 需要更强 coupling。

---

## 2. Atmosphere–Ocean

coupling 影响：
- SST；
- heat flux；
- tropical variability；
- subseasonal/seasonal predictability。

---

## 3. Atmosphere–Land

land state：
- soil moisture；
- snow；
- vegetation；
- surface temperature；
- albedo

影响 boundary-layer development、heatwave、precipitation feedback。

---

## 4. Weather–Carbon

meteorological forcing 调节：
- GPP；
- respiration；
- drought stress；
- fire/disturbance；
- turbulent footprint/source area。

因此 carbon AI 与 weather/climate AI 应共享 forcing representation 与 extreme diagnostics。

---

## 5. Foundation-model route

`Aurora` 的价值之一是跨 weather、air quality、ocean waves 等 Earth-system tasks 做 pretraining/adaptation，而不是为每个 domain 从零训练独立模型。

---

## 6. Coupled training 难点

- variables/units 差异；
- timescale separation；
- resolution mismatch；
- conservation；
- interface flux；
- sparse observations；
- error propagation between components。

---

## 7. Evaluation

除了单 component RMSE，还要检查：
- interface flux balance；
- phase relationships；
- coupled extremes；
- long-run drift；
- seasonal/interannual variability。
