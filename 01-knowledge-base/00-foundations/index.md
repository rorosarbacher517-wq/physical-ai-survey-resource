# 00 · Math, Physics and Numerical Foundations

This layer supplies the language needed by every later module.

## 1. Mathematics

### Linear algebra
Vectors, matrices, tensors, basis changes, eigenvalues/eigenvectors, SVD, low-rank approximation, positive-definite matrices and quadratic forms.

Scientific-AI relevance:

- state vectors and covariance matrices;
- spectral methods and Fourier bases;
- PCA/EOF decomposition;
- attention and tensor contractions;
- reduced-order modeling.

### Calculus
Gradient, Jacobian, Hessian, chain rule, multivariable differentiation, automatic differentiation, vector calculus, divergence, gradient, curl and Laplacian.

### Probability and statistics
Conditional probability, likelihood, Bayes rule, Gaussian distributions, covariance, Monte Carlo, bias/variance, confidence intervals, hypothesis tests, calibration and probabilistic scores.

### Optimization
Gradient descent, momentum, Adam/AdamW, constrained optimization, Lagrange multipliers, multi-objective optimization and ill-conditioning.

## 2. Dynamical systems

Understand the difference between:

```text
state x(t)
→ dynamics dx/dt = f(x,t,θ)
→ observations y = H(x) + ε
```

Key ideas:

- initial-value and boundary-value problems;
- stability and attractors;
- chaotic sensitivity;
- state-space models;
- linearization and Jacobians;
- conservation and invariants.

## 3. ODE/PDE foundations

Know what the equation expresses before learning a neural surrogate.

Common forms:

- advection;
- diffusion;
- advection-diffusion;
- wave equations;
- Navier-Stokes;
- reaction-diffusion;
- energy/water/carbon balance equations.

For each equation identify:

1. state variables and units;
2. spatial and temporal derivatives;
3. parameters;
4. forcing;
5. initial/boundary conditions;
6. conservation/invariants.

## 4. Numerical methods

### Discretization
Finite difference, finite volume, finite element, spectral methods and particle/mesh-free ideas.

### Numerical quality
Consistency, stability, convergence, truncation error, CFL-like constraints, stiffness and error accumulation.

A learned model can have low test RMSE and still violate the numerical/physical structure needed for stable rollout.

## 5. Spatial geometry

Earth and physical systems are not always flat regular images.

Know:

- Cartesian versus spherical coordinates;
- latitude-longitude distortion;
- map projections;
- grids, meshes, graphs and point clouds;
- neighborhood and adjacency;
- interpolation/resampling;
- spatial autocorrelation.

## 6. Units, scale and support

Three different concepts must not be mixed:

- **resolution**: nominal grid/pixel spacing;
- **support**: area/time interval physically represented by an observation;
- **accuracy/validation scale**: scale at which predictions are actually verified.

This distinction is critical for remote sensing, EC carbon flux and weather verification.

## 7. Minimum pass standard

You should be able to:

- derive gradient/divergence/Laplacian meanings;
- explain why numerical stability matters in autoregressive ML;
- distinguish state, forcing, parameter and observation;
- explain grid/mesh/graph differences;
- inspect units and dimensions for an equation;
- identify whether a model predicts a field, scalar, trajectory or operator.

Next: [01 ML/DL & Scientific Computing](../01-ml-dl-scientific-computing/index.md).
