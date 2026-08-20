# Temporal Modeling

## 1. 任务类型

### Sequence-to-one
过去序列 → 一个 target。

### Sequence-to-sequence
过去/当前序列 → 同步或未来序列。

### Autoregressive forecast

```text
x_t → x_{t+1} → x_{t+2} → ...
```

### Direct multi-horizon
一次输出多个 lead times。

---

## 2. Irregular Earth observations

EO 很少是完美 regular sequence：
- cloud；
- revisit interval；
- sensor availability；
- orbit；
- quality mask。

因此模型应显式考虑：
- timestamp；
- time gap；
- validity mask；
- sensor ID；
- acquisition geometry。

---

## 3. Seasonal / cyclic time

DoY、hour 可用周期 encoding：

```text
sin(2πt/P), cos(2πt/P)
```

避免把 Dec 31 与 Jan 1 当作数值距离很远。

---

## 4. Teacher forcing vs rollout

训练 one-step：

```text
true x_t → predict x_{t+1}
```

推理时：

```text
pred x_t → pred x_{t+1}
```

distribution 不一致会导致 exposure bias / rollout drift。

---

## 5. Extreme events

如果 loss 由大量 normal conditions 主导，模型可能对 rare extremes 学得差。

可考虑：
- stratified sampling；
- tail-aware metric；
- event-based evaluation；
- probabilistic forecast。
