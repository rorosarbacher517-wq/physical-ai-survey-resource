# Inverse Problems

## 1. Forward vs Inverse

Forward：

```text
x → H(x) → y
```

Inverse：

```text
y → infer x
```

例如：
- radiance → atmospheric profile；
- waveform → canopy structure；
- flux observation → ecosystem parameter；
- scattering observation → soil moisture/structure。

---

## 2. Ill-posedness

Inverse problem 可能：
- 无解；
- 多解；
- 对 noise 极敏感。

因此需要 prior / regularization。

### Regularized objective

```text
x* = argmin_x ||H(x)-y||² + λR(x)
```

---

## 3. Bayesian inverse

```text
posterior ∝ likelihood × prior
```

它不只给 point estimate，还可给 uncertainty。

---

## 4. Amortized inference

训练 neural network：

```text
y → q_θ(x|y)
```

一次训练后可快速处理大量 observations，但 distribution shift 时可能失效。

---

## 5. Identifiability

如果多个 `x` 产生相似 `H(x)`，单纯提高 network capacity 不能解决不可辨识问题。

需要：
- additional modality；
- stronger prior；
- temporal information；
- experimental design；
- uncertainty reporting。
