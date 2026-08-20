# Uncertainty and Calibration

## 1. Sources of uncertainty

### Aleatoric
Noise/irreducible variability in observations/processes.

### Epistemic
Uncertainty from limited data/model knowledge.

### Structural
Wrong/incomplete equations, architecture or observation operator.

### Parameter
Uncertain physical/model parameters.

### Support/representativeness
Mismatch between observation and model scale/location.

## 2. Predictive distributions

A model can output:

- mean + variance;
- quantiles;
- mixture distribution;
- ensemble members;
- samples from diffusion/generative model.

## 3. Proper scoring

Probabilistic models should be evaluated with scores that reward both calibration and sharpness, e.g. NLL/CRPS/Brier where appropriate.

## 4. Coverage

For a nominal 90% predictive interval, empirical coverage should be near 90% under the evaluated distribution.

Coverage alone is insufficient if intervals are extremely wide.

## 5. Deep ensembles

Train multiple independently initialized models. Effective practical baseline for epistemic variation, but compute-heavy and not a full Bayesian posterior.

## 6. Conformal prediction

Can provide finite-sample coverage under exchangeability-type assumptions. Spatial/temporal/OOD scientific data can violate these assumptions, so calibration design matters.

## 7. OOD uncertainty

A useful uncertainty system should often become less confident in unseen regimes, but many neural predictors are overconfident. Test by site/region/extreme/sensor shift.

## 8. Error propagation

For carbon or EO, propagate upstream uncertainty where possible:

`measurement → retrieval/QC → spatial support → model → product`.

## 9. Calibration is task-specific

A model can be calibrated globally and miscalibrated for rare extremes or one biome. Report stratified reliability.
