# 12 · Cross-domain Physical AI

The Earth-system tracks are the repository priority, but the underlying methods generalize across scientific and embodied physical systems.

## 1. Fluids and aerodynamics

Key problems:

- surrogate CFD;
- turbulence closure;
- flow reconstruction;
- drag/lift prediction;
- inverse design;
- control.

Useful methods: neural operators, equivariant networks, learned closures, differentiable solvers and PINNs.

## 2. Energy and materials

Applications:

- battery state/health;
- power-grid forecasting/control;
- renewable energy prediction;
- thermal systems;
- materials/property prediction;
- molecular/atomistic simulation.

Physics may enter through conservation, circuit/electrochemical equations, symmetry/equivariance, differentiable simulators or graph representations.

## 3. Biomedical mechanics

Examples:

- hemodynamics;
- organ/tissue biomechanics;
- physiological parameter inference;
- medical digital twins.

High stakes require explicit uncertainty and domain-shift evaluation.

## 4. Digital twins

A digital twin is not simply a dashboard plus a predictive model.

A strong scientific digital twin contains:

```text
physical asset/system
↔ observations
↔ state estimation / data assimilation
↔ model/surrogate
↔ forecast / scenario / control
↔ continual update
```

## 5. Embodied physical intelligence

This branch emphasizes:

- perception;
- 3D spatial reasoning;
- dynamics/world models;
- planning/control;
- robot learning;
- VLA;
- sim-to-real;
- safety and uncertainty.

The connection to scientific AI is strongest around differentiable simulation, system identification, world dynamics, control and physical consistency.

## 6. Shared method vocabulary

Across domains, classify work using the repository taxonomy:

- physics-constrained objectives;
- physics-embedded architectures;
- differentiable simulation;
- neural operators;
- hybrid numerical-machine learning;
- symmetry/equivariance;
- inverse problems;
- uncertainty quantification;
- scientific foundation models;
- observation-operator methods.

See [metadata/taxonomy.yaml](../../metadata/taxonomy.yaml) and [papers by method](../../02-paper-library/by-method.md).
