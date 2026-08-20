# Carbon-flux Modeling Methods

## 1. Process and light-use-efficiency models

Represent photosynthesis/respiration using mechanistic or semi-empirical process relationships.

Strengths: interpretable process structure. Limitations: parameters and unresolved processes can introduce bias.

## 2. Classical ML upscaling

Random forest, boosted trees and related methods map environmental/remote-sensing predictors to tower fluxes.

They are strong baselines but often operate on aggregated features and can struggle with extrapolation.

## 3. Deep temporal models

RNN/Transformer-style models can learn sub-daily/seasonal dynamics from meteorology and remote-sensing state.

## 4. Spatial models

CNN/ViT encoders preserve pixel patterns around towers instead of collapsing a patch to mean statistics.

## 5. Hybrid process–ML

Options:

- process model + residual network;
- learned parameterization;
- process-derived features;
- differentiable process layer;
- carbon/water/energy coupling.

## 6. Physics-constrained models

Possible constraints:

- carbon balance relationship;
- nighttime/photosynthesis rules when scientifically justified;
- positivity/bounds;
- radiation/water stress priors;
- observation-operator matching.

Constraint assumptions should be ablated and checked across regimes.

## 7. Footprint-aware models

Use dynamic source-area weights either on predictors, latent classes or model outputs.

The placement of footprint weighting changes what spatial quantity the model learns.

## 8. Foundation representations

EO foundation-model embeddings can replace/augment hand-crafted spectral features, but they still need meteorological forcing, support alignment and OOD evaluation for flux tasks.

## 9. Comparison design

Use identical split/targets/QC and hold model/training constant when testing one method contribution.
