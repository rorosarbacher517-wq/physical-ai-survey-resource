# PyTorch、JAX 与 HPC Basics

## 1. Automatic Differentiation

Scientific ML 很多方法依赖 gradient：
- training；
- PINN derivatives；
- inverse problem；
- differentiable simulation；
- adjoint-like sensitivity。

### PyTorch
动态图 + autograd，生态成熟。

### JAX
函数式 transformations：`grad`, `jit`, `vmap`, `pmap/pjit`，适合高性能 scientific computing 与 differentiable programming。

---

## 2. Tensor layout

常见 shape：

```text
image:       [B,C,H,W]
time series: [B,T,D]
video/EO:    [B,T,C,H,W]
weather:     [B,C,L,H,W]
point:       [B,N,D]
```

要明确：
- contiguous / stride；
- channel-first vs channel-last；
- dtype；
- device；
- mask shape；
- broadcasting。

---

## 3. GPU memory

训练显存大致来自：
- parameters；
- gradients；
- optimizer states；
- activations；
- attention matrix；
- temporary buffers。

常用手段：
- mixed precision；
- gradient checkpointing；
- accumulation；
- activation recomputation；
- sharding；
- chunked inference。

---

## 4. Distributed Training

### DDP
每 GPU 一份 model，data parallel。

### FSDP / ZeRO
切分 parameters / gradients / optimizer states。

### Tensor / Pipeline Parallelism
超大模型进一步切 model computation。

Scientific fields 的额外瓶颈往往是 **I/O**：大规模 NetCDF/Zarr/HDF5/GeoTIFF 读取可能比 GPU 本身更慢。

---

## 5. Data pipeline

Earth data 推荐关注：
- chunk size；
- compression；
- lazy loading；
- `xarray` / `Dask` / `Zarr`；
- spatial window sampling；
- temporal sequence sampling；
- deterministic preprocessing；
- train-only normalization statistics。

---

## 6. Reproducibility

至少记录：

```text
code commit
random seed
environment / package versions
data version
split manifest
normalization statistics
hyperparameters
checkpoint
hardware
```

## Sources

- PyTorch docs: https://pytorch.org/docs/stable/
- JAX docs: https://docs.jax.dev/
- xarray docs: https://docs.xarray.dev/
- Zarr docs: https://zarr.readthedocs.io/
