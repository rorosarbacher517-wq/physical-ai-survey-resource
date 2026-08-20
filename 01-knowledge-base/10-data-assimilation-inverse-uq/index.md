# 10 · Data Assimilation, Inverse Problems and Uncertainty Quantification

These topics connect models to incomplete/noisy observations and are central to physical science.

## 1. Forward versus inverse problem

```text
forward:
state/parameters x → model/observation operator H → y

inverse:
observations y → infer state/parameters x
```

Inverse problems can be non-unique, ill-conditioned and sensitive to prior assumptions.

## 2. Data assimilation

Goal: combine a dynamical model/prior with observations to estimate the evolving state.

Core ideas to know:

- background/prior state;
- observation operator;
- observation error;
- model error;
- covariance;
- filtering versus smoothing;
- variational versus ensemble methods.

Classical anchors include Kalman filtering, EnKF and variational DA. Modern AI may learn components or replace parts of the pipeline.

## 3. AI roles in DA

- learned observation operator;
- learned background/error covariance;
- learned surrogate forecast model;
- observation-to-state encoder;
- differentiable end-to-end DA;
- generative posterior/state estimation.

For weather, DA determines the initial state. For carbon/ecosystem models, DA can constrain parameters and latent states from flux/remote-sensing observations.

## 4. Uncertainty types

### Aleatoric
Measurement/process variability that remains even with infinite data.

### Epistemic
Model/parameter uncertainty due to limited knowledge/data.

### Structural
Misspecified equations, model form or observation operator.

### Scale/support uncertainty
Mismatch between what is observed and what the model/pixel/grid represents.

## 5. Methods

- ensembles;
- Bayesian models;
- Monte Carlo/dropout approximations;
- Gaussian processes;
- quantile/probabilistic regression;
- deep ensembles;
- diffusion/generative ensembles;
- conformal prediction where assumptions are appropriate.

## 6. Calibration

A sharp predictive distribution is not useful if it is systematically overconfident.

Check:

- coverage;
- reliability;
- calibration curves;
- CRPS/Brier for probabilistic forecasts;
- interval width versus empirical error;
- calibration under OOD regimes.

## 7. Domain-specific uncertainty

### Carbon
EC measurement error, gap filling, GPP/RECO partitioning, footprint uncertainty, satellite retrieval errors and cross-site transfer.

### Weather
initial-condition uncertainty, model uncertainty, ensemble spread, extremes and observation verification uncertainty.

### Remote sensing
sensor noise, atmospheric correction, cloud masking, retrieval inversion and label uncertainty.

Next: [11 Data/HPC/Evaluation](../11-data-hpc-evaluation/index.md).
