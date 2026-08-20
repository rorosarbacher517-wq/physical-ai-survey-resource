# Classical ML and Scientific Baselines

Deep learning is not automatically superior in scientific tasks. Sparse sites, tabular drivers and limited labels often make classical models strong baselines.

## 1. Linear models

### Ordinary least squares

Useful for interpretability and diagnosing whether complex nonlinear modeling is needed.

### Ridge

Adds `λ||w||²` and stabilizes correlated predictors.

### Lasso

Adds `λ||w||₁` and can produce sparse coefficients, though selected features may be unstable under collinearity.

## 2. Tree ensembles

### Random forest

Strengths:

- nonlinear interactions;
- mixed feature scales;
- little preprocessing;
- robust baseline for environmental tabular data.

Limitations:

- weak extrapolation outside training range;
- feature importance can be misleading under correlated predictors;
- no built-in physical consistency.

### Gradient-boosted trees

XGBoost/LightGBM-style methods are often strong for structured environmental predictors. Tune depth, learning rate and regularization with blocked validation rather than random sample CV.

## 3. Gaussian processes

Useful when data are limited and uncertainty matters. Kernels encode smoothness/similarity assumptions, but computational cost grows strongly with sample count unless approximations are used.

## 4. Baseline design

A fair baseline should use:

- the same train/test split;
- the same target/QC;
- comparable input information;
- explicit hyperparameter protocol;
- identical evaluation support.

## 5. Leakage in scientific baselines

Random row splits can leak:

- site identity;
- neighboring timestamps;
- seasonal cycle;
- sensor campaign;
- simulation trajectory;
- spatial neighborhood.

A simple RF with leakage can appear stronger than a sophisticated OOD-safe model.

## 6. Interpretability

Useful tools:

- permutation importance;
- partial dependence;
- SHAP-style attribution;
- stratified residual plots;
- sensitivity analysis.

These explain model associations, not physical causality.

## 7. Baseline ladder

```text
mean / climatology
→ linear model
→ RF / boosting
→ shallow MLP
→ domain architecture
→ physics-aware/hybrid model
```

A new method should beat relevant simpler levels under the same split and support.
