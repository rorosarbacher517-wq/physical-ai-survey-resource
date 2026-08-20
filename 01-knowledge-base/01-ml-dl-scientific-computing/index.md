# 01 · Machine Learning, Deep Learning and Scientific Computing

This module contains the AI fundamentals needed before adding physical priors.

## 1. Classical ML

- linear/ridge/lasso regression;
- logistic regression;
- random forest and gradient boosting;
- SVM;
- clustering and dimensionality reduction;
- Gaussian processes;
- calibration and uncertainty basics.

Scientific relevance: strong baselines are often more informative than a large network when data are sparse, tabular or site-limited.

## 2. Deep-learning building blocks

### Tensor and representation
Always track shape and semantics.

Examples:

```text
remote-sensing patch: [B, T, C, H, W]
weather field:        [B, T, V, H, W]
mesh/graph:           [B, N, D]
flux time series:     [B, T, D]
point cloud:          [B, N, C]
```

### Core architectures

- MLP: point/tabular nonlinear mapping;
- CNN/U-Net: local spatial hierarchy and dense prediction;
- RNN/LSTM/GRU: recurrent temporal state;
- Transformer: content-dependent global interactions;
- GNN: irregular topology / mesh / relational structure;
- encoder-decoder: field-to-field mapping;
- diffusion/score models: probabilistic generation and ensembles.

## 3. Training

Know:

- supervised/self-supervised/semi-supervised learning;
- MSE/MAE/Huber/cross-entropy/likelihood;
- optimizer and learning-rate schedules;
- normalization and residual connections;
- regularization;
- mixed precision;
- gradient accumulation/clipping;
- checkpoint/resume and reproducibility.

## 4. Generalization in scientific data

Random sample splitting is often invalid when nearby samples share location, time, sensor, campaign or simulation trajectory.

Important split axes:

- site/location blocked;
- time blocked;
- region/biome/climate regime blocked;
- simulation parameter blocked;
- event/extreme blocked;
- sensor/domain blocked.

## 5. Scientific computing stack

Understand the practical relationship:

```text
NumPy/xarray/raster/geospatial arrays
→ PyTorch/JAX/TensorFlow
→ GPU kernels / CUDA
→ distributed data + model parallelism
→ checkpoint / experiment tracking
```

The repository does not require one framework, but every reproducible workflow should track software versions, hardware, random seeds, data lineage and exact split definitions.

## 6. Model complexity questions

For any architecture ask:

1. How does compute scale with spatial points/tokens?
2. How does memory scale with sequence/grid size?
3. Can it preserve local and global interactions?
4. Is the representation resolution-dependent?
5. Can it roll out stably?
6. Is the model equivariant/invariant to relevant transformations?

## 7. Minimum pass standard

You should be able to explain a CNN, Transformer and GNN at tensor-shape level; choose meaningful scientific splits; distinguish interpolation from extrapolation; and estimate the primary compute/memory bottleneck.

Next: [02 Physical AI Core](../02-physics-ai-core/index.md).
