# Eddy Covariance (EC)

## 1. EC 测量的核心

EC 利用 turbulent covariance 估计垂直 scalar flux。CO₂ flux 的概念形式：

```text
F_c = ρ · overline(w' c')
```

其中：
- `w'`：vertical wind fluctuation；
- `c'`：CO₂ concentration/mixing-ratio fluctuation；
- averaging 常为约 30 min（network/site processing may vary）。

真实 processing 还涉及 coordinate rotation、time lag、frequency response、density corrections、QC 等。

---

## 2. 为什么 EC 不是 point measurement

turbulence 把 upwind surface exchange 搬运到 sensor。

因此 observation 对应动态 source area，而不是 tower base coordinate。

```text
surface flux field
→ turbulent transport
→ instrument
→ half-hourly integrated flux
```

source area 由 footprint model 描述。

---

## 3. NEE、GPP、RECO 的关系

EC CO₂ exchange 经 processing 得到 NEE-like net ecosystem exchange quantity（具体 convention 依 network/product）。

`GPP` 与 `RECO` 通常通过 partitioning method 推断。

所以训练 AI 时应区分：

```text
measured/processed net flux
vs
partitioned component targets
```

---

## 4. 常见 QC / gap 问题

- instrument failure；
- precipitation / condensation；
- low turbulence；
- stationarity；
- advection；
- footprint contamination；
- missing meteorology。

Flux networks 通常提供 QC flag 和 gap-filled/partitioned products；不同字段不能混用。

---

## 5. u* 与 low-turbulence filtering

弱湍流条件下，夜间 flux measurement 可能无法充分代表 surface exchange。常见 workflow 会用 friction velocity `u*` threshold 做过滤/uncertainty analysis。

这会影响：
- NEE time series；
- partitioned RECO/GPP；
- long-term carbon balance。

---

## 6. AI 配对前必须记录

```text
site ID
measurement height
averaging interval
flux variable/version
QC flag
u* filtering convention
partitioning method
footprint inputs
local time/UTC
```

---

## Sources

- Baldocchi (2003), Global Change Biology.
- Aubinet et al., *Eddy Covariance: A Practical Guide to Measurement and Data Analysis*.
- Pastorello et al. (2020), FLUXNET2015: https://doi.org/10.1038/s41597-020-0534-3
