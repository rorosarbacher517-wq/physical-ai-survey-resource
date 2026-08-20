# Flux Partitioning and Target Uncertainty

## 1. EC target hierarchy

Eddy covariance provides a net turbulent CO2 exchange estimate after processing/QC. GPP and ecosystem respiration are then inferred through partitioning assumptions rather than observed as independent direct tower measurements.

A common sign convention is:

```text
NEE = RECO - GPP
```

Always verify the convention used by the specific product.

## 2. Why partitioning matters for AI

If a model is trained on partitioned GPP/RECO, the target already contains:

- EC measurement uncertainty;
- gap-filling assumptions;
- partitioning model assumptions;
- nighttime/daytime method differences;
- environmental-response parameter uncertainty.

Therefore model error and target uncertainty are not the same quantity.

## 3. Latent-variable view

A useful abstraction is:

```text
latent ecosystem processes
→ net CO2 exchange
→ EC measurement/QC
→ partitioning algorithm
→ supervised GPP / RECO target
```

The supervised label is downstream of several transformations.

## 4. Train-time implications

Possible approaches:

- train NEE only and derive components through a process model;
- multi-task NEE/GPP/RECO learning with a balance constraint;
- model target uncertainty through heteroscedastic likelihoods;
- train against alternative partitioning products;
- use weak/latent supervision for components.

## 5. Multi-task consistency

For predictions `ŷ_NEE`, `ŷ_GPP`, `ŷ_RECO`, a soft balance term can be written as:

```text
L_balance = ||ŷ_NEE - (ŷ_RECO - ŷ_GPP)||²
```

This enforces internal consistency only under the chosen sign convention. It does not make partitioned targets exact.

## 6. Evaluation

Report component performance separately because the predictability and label uncertainty differ.

Useful analyses:

- NEE/GPP/RECO paired metrics;
- daytime/nighttime stratification;
- season/phenology;
- alternative partitioning methods if available;
- residual balance error;
- uncertainty/calibration.

## 7. Failure modes

- describing GPP/RECO as directly measured by EC;
- interpreting disagreement with one partitioning product as pure model error;
- applying a carbon-balance penalty with the wrong sign convention;
- leaking partitioning variables that encode the target construction;
- comparing studies using different partitioning products without noting it.

## 8. Related pages

See [Eddy covariance](eddy-covariance.md), [carbon-cycle processes](carbon-cycle-processes.md), [process-constrained carbon AI](process-constrained-carbon-ai.md) and [validation/uncertainty](validation-uncertainty.md).
