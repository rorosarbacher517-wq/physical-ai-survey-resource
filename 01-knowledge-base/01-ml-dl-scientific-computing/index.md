# 01 · ML / DL 与 Scientific Computing

这一层不是重新学一遍“通用 AI”，而是建立 Scientific AI 需要的模型语言：**baseline、representation、optimization、autograd、GPU 与 evaluation discipline。**

## 1. 从 baseline 开始

复杂模型必须与合理 baseline 比：
- Linear / Ridge / Lasso；
- Random Forest；
- Gradient Boosting / XGBoost / CatBoost；
- Gaussian Process；
- simple MLP / CNN / temporal model。

如果 foundation model + fine-tuning 只和弱 baseline 比，很难判断 pretraining 真正带来什么。

---

## 2. Deep Learning 基本模块

```text
Linear / Conv
→ activation
→ normalization
→ residual connection
→ attention / message passing
→ output head
```

需要理解的不只是名字，而是：
- receptive field；
- parameter sharing；
- inductive bias；
- memory complexity；
- variable resolution；
- missingness；
- rollout behavior。

---

## 3. Representation 决定 architecture

### Raster / image
`[B,C,H,W]` → CNN / ViT / U-Net。

### Time series
`[B,T,D]` → RNN / TCN / Transformer / state-space model。

### Spatiotemporal field
`[B,T,C,H,W]` → ConvLSTM / 3D CNN / factorized attention / operator。

### Graph / mesh
`nodes [B,N,D]` + `edges` → GNN / mesh processor。

### Point cloud
`[B,N,D]` → PointNet-style / sparse convolution / point Transformer。

---

## 4. Scientific Computing 能力

至少掌握：
- `NumPy` / `xarray`；
- `PyTorch` 或 `JAX`；
- automatic differentiation；
- mixed precision；
- GPU memory；
- distributed data parallel；
- chunking / sharding；
- reproducible seed / environment；
- profiler。

---

## 5. 本模块页面

- [Classical ML Scientific Baselines](classical-ml-scientific-baselines.md)
- [Deep Learning Architectures](deep-learning-architectures.md)
- [Transformer / GNN for Science](transformer-gnn-for-science.md)
- [PyTorch / JAX / HPC Basics](pytorch-jax-hpc-basics.md)

## 6. Sources

- Goodfellow, Bengio & Courville, *Deep Learning*: https://www.deeplearningbook.org/
- Vaswani et al. (2017), *Attention Is All You Need*: https://arxiv.org/abs/1706.03762
- Battaglia et al. (2018), *Relational inductive biases, deep learning, and graph networks*: https://arxiv.org/abs/1806.01261
- PyTorch docs: https://pytorch.org/docs/stable/
- JAX docs: https://docs.jax.dev/
