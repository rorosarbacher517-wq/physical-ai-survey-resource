# 03 · Physics-informed Learning

Physics-informed learning injects equations, constraints, invariances or domain structure into optimization or model parameterization.

## 1. Canonical PINN idea

For a PDE written as

```text
N[u(x,t); θ] = 0
```

a neural network approximates `u`, and automatic differentiation computes derivatives needed for the residual.

A typical objective combines:

```text
L = λ_data L_data
  + λ_pde L_residual
  + λ_bc L_boundary
  + λ_ic L_initial
```

The key challenge is not writing this loss; it is balancing optimization, scales and sampling so all terms are actually learned.

## 2. What to study beyond the basic formula

- collocation-point sampling;
- multi-scale/stiff PDE optimization;
- spectral bias;
- adaptive loss weighting;
- domain decomposition;
- causal/time-marching training;
- noisy observations;
- inverse parameter estimation;
- uncertainty;
- hard boundary/positivity/conservation parameterizations.

## 3. Constraint families

### Conservation
Mass, energy, momentum, water/carbon budgets.

### Symmetry/equivariance
Translation, rotation, permutation, gauge or other known symmetries.

### Positivity and bounds
Concentrations, variances, probabilities, physical state ranges.

### Monotonicity / constitutive relationships
Useful when theory strongly supports directionality, but dangerous when the relationship changes by regime.

### Balance relationships
Examples include coupled component relationships such as carbon balance. Sign conventions and measurement definitions must be explicit.

## 4. When PINNs may be a poor fit

PINNs can be inefficient when high-quality simulation data already exist, the PDE is high-dimensional/stiff, the geometry is complex, or the main task is repeated field-to-field prediction over many initial conditions.

Alternatives:

- neural operators;
- surrogate modeling;
- learned closure/parameterization;
- differentiable solvers;
- hybrid residual correction;
- data assimilation.

## 5. Evaluation

Do not stop at pointwise RMSE. Check:

- equation residual on unseen locations/times;
- boundary/initial condition satisfaction;
- conservation error;
- spectral/gradient behavior;
- long-horizon stability;
- parameter recovery;
- OOD regimes.

## 6. Primary anchor

The original PINN framework is associated with Raissi, Perdikaris and Karniadakis, *Journal of Computational Physics* (2019): https://doi.org/10.1016/j.jcp.2018.10.045

For verified resources, use [papers by method](../../02-paper-library/by-method.md).

Next: [04 Neural Operators & Simulation](../04-neural-operators-simulation/index.md).
