# 11 · Scientific Data Engineering、HPC 与 Evaluation

一个 Scientific AI 项目能否可信，往往不是由 architecture 决定，而是由：

```text
data lineage
→ sample construction
→ split
→ scalable training
→ reproducible inference
→ evaluation
→ audit
```

决定。

---

## 1. Data Engineering

Scientific data 常见特性：
- TB–PB 级；
- NetCDF / HDF5 / Zarr / GeoTIFF；
- 多变量、多分辨率、多时间尺度；
- missing / QA；
- CRS/coordinate；
- versioned products。

→ [Scientific Data Engineering](data-engineering.md)

---

## 2. HPC / Distributed Scientific ML

主要瓶颈可能是：
- GPU memory；
- all-reduce communication；
- storage bandwidth；
- decompression；
- random spatial I/O；
- dataloader；
- checkpoint size；
- long rollout inference。

→ [Distributed Scientific ML](distributed-scientific-ml.md)

---

## 3. Evaluation / Benchmarking

Scientific benchmark 不只比较一个 score，还要固定：
- data version；
- support/resolution；
- split；
- initialization；
- adaptation protocol；
- metric convention；
- compute；
- uncertainty；
- physical diagnostics。

→ [Evaluation / Benchmarking](evaluation-benchmarking.md)

---

## 4. Reproducibility levels

### Level A · Result provenance
能知道结果对应哪个 data/model/code version。

### Level B · Re-runnable
给定环境和数据可重新运行 inference/evaluation。

### Level C · Re-trainable
训练脚本、split、seed、hyperparameters 完整。

### Level D · Reproduced
独立运行实际成功，metrics 被记录并与报告一致。

**“代码公开”不等于“结果已复现”。**

---

## 5. Earth-system 特殊要求

- geospatial split；
- temporal cutoff；
- sensor/product version；
- observation support；
- reanalysis vs observation；
- climate/extreme OOD；
- foundation pretraining overlap。

---

## 6. 推荐工具栈

```text
NumPy / pandas
xarray / Dask
Zarr / NetCDF / HDF5 / GeoTIFF
PyTorch / JAX
CUDA / NCCL
SLURM / Kubernetes where appropriate
Weights & Biases / MLflow or simple structured logs
Git + environment lock
```

工具只是手段，核心是 provenance 与 deterministic sample definition。
