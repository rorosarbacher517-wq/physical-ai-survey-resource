# Hybrid Numerical–ML Modeling Design

## 1. Why hybridize?

Pure numerical models encode physical structure but can be expensive or contain uncertain parameterizations. Pure ML can be fast and flexible but may extrapolate poorly or violate physics.

Hybrid design keeps reliable structure and learns uncertain/expensive components.

## 2. Common patterns

### Learned parameterization

```text
resolved numerical state
→ ML closure/parameterization
→ tendency/flux
→ numerical time step
```

### Residual correction

`prediction = physical_model + ML_residual`

Useful when the physical model is broadly correct but biased.

### Surrogate component

Replace an expensive submodule while preserving surrounding solver logic.

### Emulator

Learn the complete simulator mapping over a bounded parameter/state domain.

### Differentiable hybrid

Backpropagate through both learned and numerical components.

### DA-coupled model

Use ML inside an observation/state-estimation loop rather than as a standalone predictor.

## 3. Interface design

A hybrid interface must define:

- input/output variables and units;
- time step;
- grid/mesh;
- conserved quantities;
- bounds;
- differentiability;
- fallback behavior;
- uncertainty.

## 4. Training choices

- offline supervised learning from solver/observations;
- online learning inside rollout;
- multi-step loss;
- physical residual loss;
- parameter perturbation for robustness;
- regime-balanced sampling.

## 5. Distribution shift

A closure trained on states from one numerical model can fail when inserted into a coupled model because its own predictions change the future state distribution.

Test closed-loop behavior.

## 6. Error decomposition

Separate:

- observation error;
- numerical-model structural error;
- learned-component approximation error;
- coupling/rollout error;
- parameter uncertainty.

## 7. Selection rule

Use the smallest learned component that addresses the actual bottleneck while preserving trustworthy physics and transparent interfaces.
