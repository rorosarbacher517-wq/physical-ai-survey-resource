# Surrogates and Hybrid Solvers

## 1. Surrogate goal

Approximate an expensive mapping so repeated inference becomes cheaper.

Examples:

- CFD parameter sweep;
- atmospheric forecast step;
- radiative transfer emulator;
- land-surface process module;
- material-property simulation.

## 2. Training domain

Define the valid domain explicitly:

- parameter ranges;
- initial/boundary conditions;
- geometry;
- forcing;
- resolution;
- regime/extremes.

A surrogate is unsafe outside an untested domain simply because inputs have the same shape.

## 3. Residual surrogate

`y = solver(x) + NN(x)`

The network learns systematic solver discrepancy rather than the whole process.

## 4. Closure model

Unresolved subgrid effect is predicted from resolved state.

The learned closure enters the dynamics and changes future inputs, so offline accuracy is insufficient.

## 5. Emulator inside inverse/optimization loop

A differentiable/fast surrogate can enable parameter estimation, uncertainty propagation or design optimization that would be too expensive with the original simulator.

## 6. Fidelity levels

Multi-fidelity learning combines cheap/low-resolution simulations with fewer expensive/high-resolution simulations or observations.

## 7. Evaluation

Report:

- predictive error;
- speed/memory;
- physical residual/conservation;
- parameter/regime OOD;
- rollout stability;
- uncertainty;
- failure boundaries.

## 8. Coupling test

For a learned component embedded in a solver, evaluate the entire coupled system—not only the isolated component.
