# Numerical Methods for Scientific AI

## 1. Why numerics matter

Scientific AI often learns from numerical-model output, replaces a solver, couples to a solver or is evaluated against gridded fields. Numerical error therefore becomes part of the data/model system.

## 2. Discretization

A continuous derivative can be approximated on a grid. For example, a centered spatial derivative:

```text
∂u/∂x ≈ [u(x+Δx) - u(x-Δx)] / (2Δx)
```

The approximation has truncation error that depends on grid spacing and scheme order.

## 3. Major discretization families

### Finite difference

Approximates derivatives directly on grid points. Simple and efficient on structured grids.

### Finite volume

Evolves cell-integrated quantities and naturally expresses conservation through fluxes across cell faces.

### Finite element

Uses basis/test functions and is flexible on irregular geometry.

### Spectral methods

Represent fields using global basis functions such as Fourier modes. Powerful for smooth fields and periodic domains.

## 4. Time integration

Common concepts:

- explicit versus implicit update;
- step size;
- stability region;
- stiffness;
- accumulated phase/amplitude error.

An ML rollout is also an iterative numerical process when predictions are fed back as inputs.

## 5. Consistency, stability and convergence

- consistency: discretization approaches the continuous equation as resolution increases;
- stability: errors do not grow uncontrollably under the scheme;
- convergence: numerical solution approaches the true solution under refinement.

A low one-step ML error does not guarantee stable long-horizon rollout.

## 6. CFL-style reasoning

For transport problems, a time step must respect how far information moves relative to grid spacing. Even when a learned model does not explicitly enforce a CFL condition, the training cadence and spatial resolution define an implicit dynamical scale.

## 7. Interpolation and resampling

Nearest, bilinear, bicubic, conservative regridding and area-weighted aggregation answer different questions.

For Earth data ask:

- is the variable intensive or extensive?
- should mass/energy be conserved?
- are categorical classes being interpolated incorrectly?
- does resampling merely change grid spacing or genuinely add information?

## 8. Numerical error in AI datasets

Simulation-trained models inherit:

- discretization bias;
- parameterization bias;
- solver artifacts;
- grid dependence;
- boundary artifacts.

Therefore “more simulation data” does not eliminate systematic numerical bias.

## 9. Useful diagnostics

- resolution refinement;
- conservation residual;
- spectral energy distribution;
- gradient/extreme preservation;
- rollout error versus lead time;
- sensitivity to time step;
- cross-grid transfer.
