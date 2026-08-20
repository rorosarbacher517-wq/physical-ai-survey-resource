# Transformer 与 GNN for Science

## 1. Transformer 的 scientific interpretation

对 sequence `X ∈ R^(B×N×D)`：

```text
Q=XW_Q
K=XW_K
V=XW_V
A=softmax(QK^T/√d)
Y=AV
```

这里 `A_ij` 表示 token `i` 对 token `j` 信息的 data-dependent weighting。

### 在 Earth data 中 token 是什么
可能是：
- HLS patch；
- weather grid patch；
- vertical column；
- time step；
- station；
- spectral band group。

所以注意力的物理解释取决于 tokenization，而不是 attention 公式本身。

---

## 2. Position / coordinate encoding

Earth AI 不能只用 generic 1D position。

可编码：
- latitude / longitude；
- spherical coordinates；
- altitude / pressure level；
- time-of-day；
- day-of-year；
- sensor geometry；
- relative spatial offset。

注意：直接给 absolute geolocation 可能导致 geographic leakage。

---

## 3. GNN 的核心

```text
m_ij = φ_e(h_i,h_j,e_ij)
h_i' = φ_v(h_i, Σ_j m_ij)
```

- `h_i`：node state；
- `e_ij`：edge geometry/relationship；
- `m_ij`：message。

GNN 把 geometry/connectivity 显式放进计算图。

---

## 4. Mesh / graph vs grid

### Grid
优点：GPU-friendly；CNN/FFT 易用。

### Mesh/graph
优点：
- irregular geometry；
- spherical tessellation；
- adaptive resolution；
- physical connectivity。

`GraphCast` 是 graph/mesh weather modeling 的代表性例子。

---

## 5. Equivariance

如果旋转输入应产生可预测的旋转输出，可以使用 rotation-equivariant representation。

这比单纯 data augmentation 更强，因为 symmetry 进入 architecture。

---

## 6. Failure modes

- token 数过多导致 attention memory 爆炸；
- patch 太大丢失小尺度 extremes；
- positional encoding 让模型记住 location 而不是 process；
- graph edges 与真实 physical interaction 不一致；
- attention map 被误解释为 causal mechanism。

## Sources

- Vaswani et al. (2017): https://arxiv.org/abs/1706.03762
- Battaglia et al. (2018): https://arxiv.org/abs/1806.01261
- Lam et al. (2023), GraphCast: https://www.science.org/doi/10.1126/science.adi2336
