# Atmospheric State & Dynamics

## 1. Weather model 的 state 是什么

大气状态不是一张 2D image，而是一个多变量 3D field 随时间演化。

```text
X(t) = {T, u, v, q, p/geopotential, ...}
```

### Pressure-level representation

```text
X_upper [B,C,L,H,W]
```

`L` 为 pressure levels，例如 1000–50 hPa 的某些离散层。

### Surface representation

```text
X_surface [B,C_s,H,W]
```

模型可 concat/encode 两者。

---

## 2. Governing equations

实际 primitive equations 很复杂，但学习时至少理解四类：

### Momentum
wind tendency 受 pressure-gradient、Coriolis、advection、friction 等影响。

概念：

```text
Du/Dt = pressure-gradient + Coriolis + friction + ...
```

### Mass continuity

```text
∂ρ/∂t + ∇·(ρu) = 0
```

### Thermodynamic energy

temperature/potential-temperature 随 advection、compression、radiation/latent heating 等变化。

### Moisture

```text
Dq/Dt = transport + phase-change/source-sink
```

---

## 3. Hydrostatic / vertical coordinate

global NWP 常采用 pressure/model/hybrid vertical coordinate。AI model 如果直接读取 pressure-level ERA5，已经继承了一个特定 vertical representation。

模型比较必须说明：
- pressure levels 数量；
- model levels vs pressure levels；
- surface variables；
- vertical interpolation。

---

## 4. Spherical geometry

全球大气位于 sphere 上：
- longitude periodic；
- lat-lon cell area 不同；
- vector wind 有 coordinate semantics；
- poles 存在 grid distortion。

因此使用：
- latitude weighting；
- graph/mesh；
- spherical harmonics；
- special padding/coordinate handling。

---

## 5. Resolved vs unresolved process

grid 不能显式 resolve 所有尺度，因此 NWP parameterizes：
- clouds/convection；
- radiation；
- turbulence/boundary layer；
- land-surface exchange；
- microphysics 等。

Hybrid AI 可学习这些 unresolved tendencies，而保留 resolved dynamical core。

---

## 6. Chaos 与 predictability

initial condition 小误差可增长：

```text
δx_{t+1} ≈ J_M(x_t) δx_t
```

这解释了：
- DA 重要；
- ensemble 重要；
- deterministic trajectory 长 lead 的意义受限；
- climate statistics 与 exact weather trajectory 是不同任务。

## Sources

- Holton & Hakim, *An Introduction to Dynamic Meteorology*.
- Kalnay, *Atmospheric Modeling, Data Assimilation and Predictability*.
