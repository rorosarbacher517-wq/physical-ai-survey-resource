# Deep Learning Architectures for Scientific Data

## 1. CNN

适合 regular grid 和 local spatial pattern。

```text
input [B,C,H,W]
→ Conv blocks
→ [B,D,H',W']
```

核心 inductive bias：locality + weight sharing。

### U-Net
encoder-decoder + skip connections，适合 dense prediction：segmentation、retrieval、downscaling。

---

## 2. RNN / LSTM / GRU

适合 sequence，但 long-range dependency 与 parallelism 较弱。

```text
h_t = f(x_t, h_{t-1})
```

仍常用于小规模 ecological / hydrological time series。

---

## 3. Transformer

核心 self-attention：

```text
Attention(Q,K,V)=softmax(QK^T/√d_k)V
```

优势：global interaction；
主要代价：标准 attention 对 token 数量约为 `O(N²)`。

Scientific data 中 token 可以是：
- image patch；
- grid cell；
- pressure-level patch；
- time step；
- station；
- modality token。

---

## 4. GNN

适合 irregular graph / mesh：

```text
node features
→ message passing over edges
→ updated node states
```

典型应用：
- global weather mesh；
- unstructured CFD mesh；
- river/road/network；
- irregular sensors。

---

## 5. Generative Models

### VAE
学习 latent distribution。

### Diffusion / Score-based
从 noise 逐步生成 sample，适合 ensemble、downscaling、uncertainty-aware field generation。

### Flow Matching
学习连续 probability path 的 vector field，是 2024–2026 generative modeling 中的重要训练框架之一。

---

## 6. Scientific architecture 选择原则

不要问“哪个模型最新”，先问：

1. grid 还是 irregular geometry？
2. local pattern 还是 long-range interaction？
3. one-shot prediction 还是 autoregressive dynamics？
4. deterministic 还是 probabilistic？
5. fixed resolution 还是 cross-resolution/operator learning？
6. observation missingness 是否严重？

## Sources

- He et al. (2016), ResNet.
- Ronneberger et al. (2015), U-Net: https://arxiv.org/abs/1505.04597
- Vaswani et al. (2017), Transformer: https://arxiv.org/abs/1706.03762
- Ho et al. (2020), DDPM: https://arxiv.org/abs/2006.11239
