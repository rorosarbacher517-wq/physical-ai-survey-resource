# Linear Algebra, Probability and Optimization for Scientific AI

## 1. Linear algebra as the language of fields

Scientific data are often vectors or tensors that discretize continuous fields.

```text
scalar: temperature at one point
vector: wind [u, v, w]
matrix: 2D raster H×W
tensor: time × variable × level × latitude × longitude
```

### Dot product

`x · y = Σ_i x_i y_i`

Interpretations:

- similarity/projection;
- work or energy-like contractions in physics;
- attention score before normalization;
- weighted spatial aggregation.

### Matrix multiplication

If `A ∈ R^(m×n)` and `x ∈ R^n`, then `Ax ∈ R^m` transforms one representation into another. In discretized physics, a matrix can represent derivatives, interpolation, diffusion, graph propagation or an observation operator.

### Eigenvalues and eigenvectors

`A v = λ v`

They reveal characteristic modes and stability. Applications include EOF/PCA, linearized dynamics, graph Laplacians and spectral PDE methods.

### SVD

`X = U Σ V^T`

Useful for low-rank approximation, reduced-order models, data compression and diagnosing effective rank.

## 2. Probability

### Random variables and distributions

Scientific measurements include noise and unresolved variability. A deterministic target can still require a probabilistic observation model.

### Conditional probability

`p(x | y)` is central to inverse problems and data assimilation: infer a hidden state `x` after seeing observation `y`.

### Bayes rule

```text
posterior ∝ likelihood × prior
p(x|y) ∝ p(y|x) p(x)
```

- prior: knowledge before observation;
- likelihood: observation/error model;
- posterior: updated state/parameter uncertainty.

### Covariance

Covariance describes co-variation between variables or locations. In weather DA, covariance determines how one observation updates nearby/unobserved state variables.

## 3. Statistical estimation

Know the difference between:

- sample mean and population expectation;
- variance and standard deviation;
- correlation and causation;
- confidence interval and predictive interval;
- interpolation error and OOD error.

Spatial and temporal autocorrelation reduces the effective amount of independent information.

## 4. Optimization

### Gradient descent

```text
θ_{k+1} = θ_k - η ∇L(θ_k)
```

Scientific objectives can contain terms with very different units/scales, making gradient balance important.

### Adam / AdamW

Adaptive moment estimates help deep optimization, but they do not solve poor loss scaling, ill-conditioning or conflicting objectives.

### Constrained optimization

A generic problem:

```text
minimize    f(θ)
subject to  g(θ) = 0
            h(θ) ≤ 0
```

Physics-informed learning often converts constraints into penalties, parameterizations or differentiable solver components.

### Lagrange multipliers

`L(θ, λ) = f(θ) + λ g(θ)` provides a bridge between constrained optimization and physical constraints.

## 5. Numerical conditioning

A problem is ill-conditioned when small perturbations in input produce large changes in solution. Inverse problems, PDE solvers and multi-loss PINNs can all suffer from conditioning issues.

Check:

- variable scales;
- normalization;
- condition numbers;
- gradient magnitudes;
- sensitivity to noise;
- parameter identifiability.

## 6. What to be able to derive

- dot product and matrix multiplication shapes;
- gradient/Jacobian/Hessian dimensions;
- Bayes rule and likelihood interpretation;
- covariance matrix meaning;
- gradient update;
- why loss terms with incompatible scales can dominate optimization.
