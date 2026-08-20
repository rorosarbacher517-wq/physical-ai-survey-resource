# Observation Operators · 从 latent state 到真实 measurement

## 1. 基本形式

```text
y = H(x) + ε
```

- `x`：latent physical state；
- `H`：observation operator；
- `y`：measurement；
- `ε`：measurement / representation error。

很多 Scientific AI 问题真正难的是 `H`，不是 neural network。

---

## 2. Remote Sensing

```text
surface/atmosphere state
→ radiative transfer / scattering
→ sensor spectral response + geometry
→ radiance/backscatter/waveform
→ calibration/retrieval
→ product
```

因此 reflectance、SAR backscatter、SIF、LST 都不是“直接地面状态”。

---

## 3. Eddy Covariance

连续形式：

```text
Y_t = ∬ w_t(x,y) F_t(x,y) dxdy + ε_t
```

离散到 satellite grid：

```text
Y_t ≈ Σ_i w_{i,t} F_{i,t}
```

`w_{i,t}` 是 footprint weights。它把 pixel-level field 映射到 tower observation support。

---

## 4. Weather / Data Assimilation

weather observation operator 把 atmospheric state 映射到：
- station temperature/wind；
- radiosonde profile；
- satellite radiance；
- radar reflectivity；
- GNSS-related observation 等。

很多 satellite observations 并不是先 retrieval 成 temperature 再同化，而是可能直接在 radiance space 使用复杂 forward operator。

---

## 5. Learning 中的三种位置

### Input-side
先把 observation 转成 feature，再训练 model。

### Output-side
model 预测 field，再通过 `H` 与 observation 比较。

### End-to-end differentiable
`H` 可微，gradient 从 observation-space loss 传回 latent model。

---

## 6. Failure modes

- 把 point coordinate 当 observation support；
- 用错误 unit/geometry；
- interpolation 后忘记 support 改变；
- 忽略 observation error；
- retrieval product 与 raw observation 混淆；
- `H` 与真实 measurement process 不一致。

## Sources

- Tarantola, *Inverse Problem Theory*.
- Rodgers, *Inverse Methods for Atmospheric Sounding*.
- Kljun et al. (2015), flux footprint parameterisation: https://doi.org/10.5194/gmd-8-3695-2015
