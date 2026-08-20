# PINN Fundamentals

## 1. Core formulation

Let a neural network approximate a field:

`u_θ(x,t)`

For PDE residual `R[u]=0`, compute derivatives by automatic differentiation and optimize:

```text
L = λ_data L_data
  + λ_R L_residual
  + λ_B L_boundary
  + λ_I L_initial
```

## 2. Training points

- observed data points;
- interior collocation points;
- boundary points;
- initial-condition points.

They can be sampled differently because each term constrains a different region of the solution.

## 3. Forward problem

Equation parameters are known and the network learns the solution field.

## 4. Inverse problem

Unknown physical parameters are optimized jointly with the network using observations and PDE constraints.

Identifiability matters: multiple parameter combinations can explain the same observations.

## 5. Soft physical constraint

PDE residual is a penalty, so zero violation is not guaranteed. Relative weighting against data/boundary terms determines practical enforcement.

## 6. Advantages

- mesh-free coordinate queries;
- combines sparse observations with equations;
- differentiable inverse estimation;
- flexible treatment of some geometries.

## 7. Limitations

- difficult optimization for stiff/multi-scale systems;
- derivative computation can be expensive;
- loss terms can conflict;
- high-dimensional/time-long domains are challenging;
- strong numerical solvers may be much more efficient for routine forward simulation.

## 8. Appropriate questions

Use PINNs when equations are meaningful, observations are limited, inverse estimation or differentiable constraints matter, and computational scale is compatible.

Do not choose PINN solely because the target is physical.

## 9. Primary anchor

Raissi, Perdikaris & Karniadakis (2019), *Journal of Computational Physics*: https://doi.org/10.1016/j.jcp.2018.10.045
