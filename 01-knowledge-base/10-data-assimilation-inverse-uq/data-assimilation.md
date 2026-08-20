# Data Assimilation

## 1. State-estimation problem

At time `t`:

```text
background/model forecast xb
observations y
observation operator H
error models
→ analysis xa
```

Then the model advances the analysis to the next cycle.

## 2. Kalman-filter idea

For linear-Gaussian systems, update background using an innovation:

`innovation = y - H xb`

weighted by uncertainty/covariance.

## 3. Extended/ensemble methods

Nonlinear/high-dimensional systems require approximations such as extended, ensemble or variational methods.

## 4. EnKF intuition

An ensemble approximates state uncertainty and cross-variable covariance. Observations update variables that co-vary with the observed quantity.

## 5. Variational DA

Optimize a cost function over state/trajectory using background and observation misfits, often requiring model/adjoint gradients.

## 6. ML integration

- surrogate forecast model;
- observation operator emulator;
- learned covariance/localization;
- learned correction;
- neural analysis map;
- differentiable DA;
- generative state posterior.

## 7. Sparse Earth observations

DA naturally handles observation-space mismatch when `H` and errors are explicit. This connects weather radiances, EC tower footprints and satellite retrievals under one mathematical framework.

## 8. Cycle stability

A model that produces a good one-time analysis can still drift over repeated assimilation/forecast cycles. Evaluate cycling behavior.

## 9. Diagnostics

- innovation statistics;
- analysis increment;
- forecast impact;
- observation-space residual;
- ensemble spread;
- balance/conservation;
- computational latency.
