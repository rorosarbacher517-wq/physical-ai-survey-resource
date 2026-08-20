# Weather Data Assimilation

## 1. Goal

Estimate the atmospheric state using a model/background and observations with different errors/supports.

```text
background state xb
+ observations y
+ observation operator H
+ error statistics
→ analysis xa
```

## 2. Observation types

Examples:

- surface stations;
- radiosondes;
- aircraft;
- satellite radiances;
- radar;
- GNSS-related measurements;
- scatterometer winds.

Many satellite observations are radiances rather than direct model-state variables, so radiative-transfer observation operators are essential.

## 3. Variational view

A generic objective balances distance from background and observations:

```text
J(x) = background_misfit + observation_misfit
```

weighted by uncertainty/covariance.

## 4. Ensemble view

An ensemble estimates flow-dependent uncertainty/covariance. Observations update the ensemble/state according to expected relationships between observed and unobserved variables.

## 5. AI roles

- learned observation operator/emulator;
- learned quality control;
- learned error covariance;
- direct observation-to-state encoder;
- hybrid DA with neural forecast model;
- differentiable assimilation;
- generative posterior/state estimation.

## 6. Why DA and forecasting should be separated conceptually

A strong forecast model can fail from a poor initial state. Conversely, improved assimilation can improve downstream forecasts without changing the forecast architecture.

## 7. Evaluation

Assess:

- analysis error;
- observation-space fit;
- forecast impact at multiple lead times;
- balance/physical plausibility;
- robustness when observations are missing;
- computational cost/latency.

## 8. End-to-end trend

Modern weather AI increasingly connects learned data assimilation, forecast and probabilistic post-processing. Keep the interfaces explicit so gains can be attributed correctly.
