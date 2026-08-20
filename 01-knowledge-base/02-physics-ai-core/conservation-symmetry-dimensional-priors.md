# Conservation, Symmetry and Dimensional Priors

## 1. Conservation

A conservation law links storage, transport and sources/sinks.

Generic form:

`∂q/∂t + ∇·F = S`

AI integration options:

- residual penalty;
- conservative finite-volume-like architecture;
- output parameterization;
- projection onto a constraint set;
- learned correction that preserves a numerical core.

## 2. Global versus local conservation

A model can conserve a global total while violating local transport, or satisfy local relations yet drift globally due to boundaries/numerics.

Evaluate both when relevant.

## 3. Symmetry

If a physical law is unchanged by a transformation, the model can encode invariance/equivariance.

Examples:

- permutation symmetry in sets/graphs;
- translation in homogeneous domains;
- rotation in isotropic 3D systems;
- periodic longitude in global Earth grids.

## 4. Equivariance

For transformation `g`:

```text
f(g·x) = g·f(x)
```

The output transforms consistently with the input.

## 5. Dimensional priors

Use units and dimensionless groups to:

- detect invalid equations/features;
- normalize physically disparate variables;
- construct regime descriptors;
- reduce dependence on arbitrary unit systems.

## 6. Positivity and bounds

Some variables are physically nonnegative or bounded. Enforce with:

- output transforms such as softplus/sigmoid;
- truncated/probabilistic distributions;
- projection;
- penalties.

Do not impose bounds that are artifacts of one dataset rather than physics.

## 7. Monotonicity

Known monotonic behavior can be useful but may hold only under restricted regimes. For Earth systems, interactions and feedbacks often make naive monotonic constraints too strong.

## 8. Conservation versus empirical balance

Not every empirical relationship is a fundamental conservation law. Clearly distinguish:

- exact physical identity;
- approximate process relation;
- dataset convention;
- statistical correlation.
