# Distributed Scientific ML / HPC

## 1. 为什么 Scientific ML 特别吃 I/O

语言模型通常 token stream 结构相对统一；Earth/scientific data 常需要：
- 解压大 raster；
- 多文件时空配准；
- random patch crop；
- interpolation；
- mask；
- multi-source join。

所以瓶颈可能是 CPU/storage，而不是 GPU FLOPs。

---

## 2. Data Parallel

`DDP`：每个 rank 一份 model，不同 batch shard。

```text
GPU0: batch0
GPU1: batch1
...
→ gradient all-reduce
```

适合 model 能放进单 GPU。

---

## 3. Parameter / Optimizer Sharding

`FSDP / ZeRO`：切分 parameters、gradients、optimizer states。

适合 larger FM / weather model。

---

## 4. Model Parallel

### Tensor parallel
切矩阵计算。

### Pipeline parallel
切 layers/stages。

### Spatial/Domain parallel
scientific grids 还可按 spatial domain 切分，但边界通信与 global operators 需要特别处理。

---

## 5. Attention / Grid memory

如果 token 数 `N`：

```text
standard attention memory ~ O(N²)
```

global weather / high-res EO 中 N 很大，因此常用：
- patching；
- window attention；
- factorized space/time attention；
- graph/mesh；
- spectral operator；
- hierarchical resolution。

---

## 6. Mixed precision

`FP16/BF16` 可降低 memory/提高吞吐，但 scientific variables dynamic range 大时要检查：
- underflow/overflow；
- loss scaling；
- physical residual precision；
- reduction precision。

---

## 7. Rollout inference

weather/climate inference 成本不仅是 single forward：

```text
cost ≈ steps × ensemble members × resolution × variables
```

probabilistic 100-member forecast 与单 deterministic forecast 不是同一 compute budget。

---

## 8. Profiling

分开测：
- data wait；
- H2D transfer；
- forward；
- backward；
- communication；
- checkpoint I/O；
- evaluation/regridding。

---

## 9. Reproducibility

多 GPU 训练需记录：
- world size；
- global/local batch；
- gradient accumulation；
- precision；
- distributed seed；
- checkpoint resumption semantics。
