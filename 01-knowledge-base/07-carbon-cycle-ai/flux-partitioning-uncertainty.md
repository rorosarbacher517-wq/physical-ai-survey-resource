# Flux Partitioning 与 Target Uncertainty

## 1. 为什么需要 partitioning

EC observation 给出的是 net CO₂ exchange，而生态研究常需要：

```text
NEE = RECO - GPP
```

因此需要从 NEE 推断 `GPP` 与 `RECO`。

---

## 2. 常见思路

### Nighttime partitioning
夜间 photosynthesis 近似为 0，在符合条件的夜间 observations 上拟合 respiration-temperature relationship，再外推 daytime RECO：

```text
night NEE ≈ RECO
```

之后：

```text
GPP = RECO - NEE
```

### Daytime partitioning
同时利用 daytime light-response 与 respiration relationships 估计 components。

不同 network/product 有具体实现与 uncertainty framework。

---

## 3. 为什么 partitioned target 不是 ground truth

`GPP/RECO` 依赖：
- partitioning assumptions；
- u* filtering；
- meteorological inputs；
- temporal window；
- response-function form；
- missing-data handling。

因此 AI 对 `GPP` 的误差包含：

```text
measurement/process noise
+ partitioning uncertainty
+ model error
```

---

## 4. Joint learning 的意义

如果分别训练三个独立 model，可能得到：

```text
NEE_hat ≠ RECO_hat - GPP_hat
```

joint model 可：
- shared representation；
- balance constraint；
- multi-task regularization。

但它不能消除 target partitioning uncertainty。

---

## 5. Evaluation 建议

- 明确 target product/version；
- 如果有多个 partitioning product，做 sensitivity；
- 报告 NEE/GPP/RECO separately；
- 检查 balance residual；
- 按 day/night、season、drought 分层；
- 不把 partitioned quantity 描述为 direct independent measurement。

## Sources

- Reichstein et al. (2005), nighttime partitioning framework.
- Lasslop et al. (2010), daytime partitioning approach.
- Pastorello et al. (2020), FLUXNET2015 data product.
