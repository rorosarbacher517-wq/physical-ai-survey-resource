# PyTorch, JAX and HPC Basics for Scientific AI

## 1. Tensor pipeline

A scientific training job is a systems pipeline:

```text
storage
→ CPU decode/QC/reprojection
→ batch construction
→ host-to-device transfer
→ forward
→ loss
→ backward
→ optimizer
→ checkpoint
```

The bottleneck may be I/O or preprocessing rather than GPU compute.

## 2. Autograd

Automatic differentiation records operations and computes gradients by the chain rule.

Physics-informed models may differentiate outputs with respect to coordinates. This can require higher-order derivatives and substantially increase memory/compute.

## 3. Memory accounting

GPU memory includes:

- parameters;
- gradients;
- optimizer states;
- activations;
- temporary kernels;
- input batches;
- attention matrices.

Mixed precision and gradient checkpointing reduce some components but add trade-offs.

## 4. PyTorch

Important concepts:

- Dataset/DataLoader;
- tensor device/dtype/layout;
- autograd graph;
- `no_grad` / inference mode;
- distributed data parallel;
- checkpoint state;
- deterministic/reproducible configuration.

## 5. JAX

Important concepts:

- pure functions;
- transformations such as `jit`, `grad`, `vmap`;
- XLA compilation;
- device sharding;
- functional state handling.

JAX is widely used in scientific/large-scale modeling because transformations compose naturally, but compilation and shape discipline matter.

## 6. Large arrays

Earth data often exceed RAM. Common strategies:

- xarray/Dask-style lazy access;
- Zarr/cloud-optimized chunking;
- spatial-temporal shards;
- streaming batches;
- caching frequently used metadata;
- preprocessing once when scientifically safe.

## 7. Distributed training

Distinguish:

- data parallelism;
- tensor/model parallelism;
- pipeline parallelism;
- domain/spatial decomposition.

Scientific models with huge fields may need spatial partitioning in addition to standard model parallelism.

## 8. Reproducibility

Record code commit, environment, GPU/accelerator type, random seed, exact data split, preprocessing version and checkpoint selection.
