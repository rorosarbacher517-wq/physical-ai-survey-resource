# Probabilistic and Ensemble Weather

## 1. Why probability is necessary

Atmospheric dynamics are sensitive to initial conditions and model uncertainty. A single trajectory cannot represent the full range of plausible futures.

## 2. Ensemble concept

Generate members:

`x_t^(1), x_t^(2), ..., x_t^(M)`

from perturbed initial conditions, model stochasticity or a learned generative distribution.

## 3. Desired properties

### Accuracy
Ensemble central tendency should be useful.

### Spread
Members should represent forecast uncertainty.

### Reliability/calibration
Events predicted with probability `p` should occur near frequency `p` under appropriate grouping.

### Sharpness
Forecast should be as concentrated as possible subject to calibration.

## 4. Deep ensembles

Train/use multiple models or checkpoints. Simple but expensive and may not capture all sources of uncertainty.

## 5. Generative ensembles

Diffusion/score/generative models learn conditional distributions and can generate many coherent spatial fields.

The model should preserve physical/spatial correlations, not merely pointwise variance.

## 6. Metrics

- CRPS;
- Brier score for events;
- reliability diagrams;
- rank histograms;
- spread-skill relationship;
- probabilistic extreme-event scores.

## 7. Ensemble size

More members improve sampling of the predictive distribution but increase compute/storage. Report member count when comparing systems.

## 8. Extreme events

Tail behavior matters more than average global metrics for hazards. Evaluate threshold exceedance, spatial footprint, timing and intensity.

## 9. Calibration under shift

A model calibrated on historical weather can become overconfident under rare regimes/climate shift. Stratified/OOD calibration is important.
