# EO Retrieval 与 Inverse Problems

## 1. Retrieval 是什么

从 sensor observation 反推 geophysical variable：

```text
latent state x
→ forward model H(x)
→ observation y
```

retrieval 解决：

```text
y → estimate x
```

例如：
- radiance → temperature/humidity profile；
- reflectance → LAI/chlorophyll；
- microwave → soil moisture；
- thermal radiance → LST；
- LiDAR waveform → canopy structure。

---

## 2. Classical inverse

```text
x* = argmin_x ||H(x)-y||_R² + λR(x)
```

需要 forward model、prior/regularization、error model。

---

## 3. Neural retrieval

```text
y → f_θ(y) → x_hat
```

优点：推理快；
风险：training distribution 外可能 extrapolate badly。

---

## 4. Physics-informed retrieval

可组合：

```text
observation y
→ neural inverse x_hat
→ forward H(x_hat)
→ reconstruction in observation space
```

loss：

```text
L = L_target(x_hat,x_ref)
  + λ L_obs(H(x_hat),y)
```

---

## 5. Identifiability

一个 sensor channel 可能不足以唯一确定多个 physical variables。多传感器的价值往往是缩小 inverse ambiguity，而不仅是增加 feature count。

---

## 6. Evaluation

- retrieval bias；
- random error；
- uncertainty/calibration；
- regime/biome OOD；
- observation-space consistency；
- sensitivity to geometry/noise。

## Source

- Rodgers, *Inverse Methods for Atmospheric Sounding*.
- [Inverse Problems module](../10-data-assimilation-inverse-uq/inverse-problems.md)
