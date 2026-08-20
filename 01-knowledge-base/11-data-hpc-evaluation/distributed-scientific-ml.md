# Distributed Scientific ML

## 1. Scaling dimensions

Scientific models scale along:

- sample count;
- spatial resolution;
- temporal length;
- number of variables/levels;
- ensemble size;
- model parameters.

## 2. Data parallelism

Each device processes different samples, gradients are synchronized.

Works well when each sample fits on one device.

## 3. Model/tensor parallelism

Split model weights/operations across devices when the model itself is too large.

## 4. Spatial/domain parallelism

Split a huge physical field/domain across devices. Communication at boundaries/global operations can dominate.

## 5. Pipeline parallelism

Split layers/stages across devices; useful for large sequential architectures but introduces scheduling bubbles/complexity.

## 6. Communication

Global attention, FFTs, graph exchange and distributed normalization can require substantial all-to-all/all-reduce communication.

Compute FLOPs alone do not predict runtime.

## 7. I/O

A training cluster can starve accelerators when remote raster/netCDF/Zarr data are decoded/reprojected on demand.

Mitigations:

- precomputed aligned shards;
- local caching;
- asynchronous loaders;
- compressed/chunked formats;
- parallel preprocessing.

## 8. Checkpointing

Large runs need:

- periodic checkpoints;
- optimizer/scheduler state;
- RNG state;
- data position/epoch;
- config and code commit;
- robust resume.

## 9. Efficiency metrics

Report throughput, memory, training wall time, device count and inference latency alongside scientific accuracy.
