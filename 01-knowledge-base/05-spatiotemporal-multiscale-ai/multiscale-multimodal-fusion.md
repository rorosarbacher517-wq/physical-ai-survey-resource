# Multiscale 与 Multimodal Fusion

## 1. Fusion 之前先对齐

```text
modality A
modality B
modality C
→ spatial/temporal/physical alignment
→ representation
→ fusion
```

如果 observation support 不一致，直接 concat 只是把 mismatch 交给网络。

---

## 2. Early Fusion

原始/浅层 feature concat：

```text
X = concat(X_A,X_B,...)
```

简单，但要求 resolution/time/geometry 已较好对齐。

---

## 3. Late Fusion

各 modality 独立 encoder：

```text
z_A=f_A(X_A)
z_B=f_B(X_B)
→ fuse(z_A,z_B)
```

适合 sensing physics 差异大的 modality。

---

## 4. Cross-attention

一个 modality 用 query 选择另一 modality 信息：

```text
Q=z_A, K/V=z_B
```

适合异构 token，但要处理 missing modality 与 compute。

---

## 5. Hierarchical Fusion

不同尺度分别融合：
- pixel/patch；
- object/region；
- temporal sequence；
- global context。

---

## 6. Missing modality

真实 Earth data 常出现：
- optical cloud；
- LiDAR only one campaign；
- sensor outage；
- missing station data。

训练时应测试：
- modality dropout；
- mask-aware fusion；
- graceful degradation。

---

## 7. Negative transfer

多 modality 不保证提升。额外 modality 可能：
- temporal mismatch；
- noisy；
- redundant；
- sample size 太小导致 overfit。

因此必须做 paired ablation。
