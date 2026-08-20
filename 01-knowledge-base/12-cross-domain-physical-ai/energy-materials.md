# Energy and Materials AI

## 1. Energy systems

Applications:

- renewable power forecasting;
- grid load/state estimation;
- battery state/health;
- building/thermal control;
- combustion/heat transfer;
- power-system optimization.

Physics can enter through circuit/network equations, conservation, thermal dynamics and control constraints.

## 2. Materials

Applications:

- property prediction;
- atomistic potentials;
- molecular/crystal generation;
- phase/structure modeling;
- mechanics/fracture;
- inverse design.

## 3. Graph/equivariant models

Atoms or components form graphs. Rotational/translational symmetry can be encoded through invariant/equivariant architectures.

## 4. Surrogate simulation

Learn expensive quantum/atomistic/continuum calculations over a bounded domain.

Validation must include configuration/chemistry/temperature/pressure regimes not merely random structures.

## 5. Design optimization

A differentiable/generative model can propose materials/configurations, but candidates require physical constraints and downstream simulation/experimental validation.

## 6. Uncertainty

High extrapolation risk means uncertainty/active learning are central: identify states where the surrogate lacks training support and request new simulations/measurements.

## 7. Connection to Earth AI

Shared methods include graph learning, operator surrogates, differentiable solvers, uncertainty, multi-fidelity data and physically constrained optimization.
