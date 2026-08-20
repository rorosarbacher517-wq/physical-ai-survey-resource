# Fluids and Aerodynamics AI

## 1. Physical backbone

Fluid problems involve conservation of mass/momentum/energy and often Navier–Stokes-like dynamics.

Key regimes depend on dimensionless ratios such as Reynolds number.

## 2. AI task families

- flow-field surrogate;
- turbulence closure;
- super-resolution/reconstruction;
- drag/lift prediction;
- inverse parameter/boundary inference;
- geometry optimization;
- flow control.

## 3. Representations

- structured CFD grid;
- finite-element/volume mesh;
- point cloud;
- graph;
- signed-distance/geometry field.

## 4. Physics-informed routes

- PINN for inverse/sparse-observation tasks;
- neural operator for repeated PDE solutions;
- GNN/mesh model for geometry variation;
- learned turbulence closure inside solver;
- differentiable simulation for design/control.

## 5. Turbulence challenge

Unresolved scales and broad spectra make naive regression difficult. A learned closure must be tested in closed-loop simulation because small tendency errors can destabilize dynamics.

## 6. Generalization

Test across:

- Reynolds regime;
- geometry;
- boundary conditions;
- grid/resolution;
- transient flow states.

## 7. Evaluation

Beyond RMSE:

- conservation;
- force coefficients;
- spectra;
- coherent structures;
- stability;
- computational speedup.
