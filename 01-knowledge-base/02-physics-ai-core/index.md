# 02 · Physical AI Core: How Physics Enters AI

The most important question is not “Is this a physics-informed model?” but **where and how physical knowledge changes the learning problem**.

## 1. Seven integration patterns

### A. Physics in data / labels
Simulation-generated training data, physically corrected observations, retrieval products, derived variables and physically meaningful augmentation.

Risk: the physics may only live upstream; the learned model itself can still violate it.

### B. Physics in inputs
Add forcings, parameters, coordinates, topography, boundary conditions, material properties or physically derived features.

### C. Physics in representation / architecture
Use grids, meshes, graphs, equivariant layers, spectral bases, local conservation structure, periodic boundaries or geometry-aware operators.

### D. Physics in loss/objective
Penalize equation residuals, conservation violation, boundary-condition errors, energy imbalance or impossible states.

### E. Physics as hard constraint
Parameterize output so conservation, positivity, monotonicity, symmetry or boundary conditions are satisfied by construction.

### F. Physics in simulation / operator loop
Couple the network with a numerical solver, differentiable simulator, parameterization, closure, emulator or observation operator.

### G. Physics in evaluation
Check conservation, spectra, extremes, stability, regime transfer and physically meaningful consistency—not only average RMSE.

## 2. Observation physics is a core modeling layer

Many Earth-system tasks are measurement problems before they are prediction problems.

```text
true physical state x
→ sensor / transport / sampling process H
→ observation y
→ preprocessing / retrieval
→ ML input or target
```

Examples:

- satellite reflectance is not GPP;
- EC tower flux is not a point measurement;
- radar reflectivity is not rainfall itself;
- reanalysis is not raw observation.

Therefore `H`, the observation operator/support, belongs in the modeling discussion.

## 3. Soft versus hard physics

**Soft constraint**: violation increases the loss but remains possible.

**Hard constraint**: the parameterization prevents violation by construction.

Hard is not always better: exact enforcement of an approximate or misspecified physical relationship can bias the model.

## 4. Hybrid versus pure data-driven

A useful spectrum:

```text
pure numerical model
↔ ML parameterization/closure
↔ hybrid numerical + ML
↔ physics-constrained ML
↔ pure data-driven predictor
```

Choose based on data availability, known physics, computational cost, uncertainty and required extrapolation.

## 5. Common failure modes

- calling any physical target “physics-informed”;
- adding a physical variable as a feature but claiming physical consistency;
- enforcing a relationship with uncertain parameters as exact truth;
- evaluating only IID RMSE;
- ignoring measurement support;
- hiding numerical instability behind short-horizon metrics;
- conflating correlation with physical mechanism.

## 6. Method comparison template

| Axis | Questions |
|---|---|
| Physics source | equation, conservation, symmetry, process model, observation operator? |
| Integration stage | input, architecture, loss, simulator, DA, evaluation? |
| Strength | soft, hard, hybrid, learned residual? |
| Scale | point, pixel, field, mesh, global? |
| Dynamics | static mapping or rollout? |
| Uncertainty | deterministic, ensemble, Bayesian/probabilistic? |
| Extrapolation | new sites, regimes, parameters, extremes? |

Next: [03 Physics-informed Learning](../03-physics-informed-learning/index.md) and [04 Neural Operators & Simulation](../04-neural-operators-simulation/index.md).
