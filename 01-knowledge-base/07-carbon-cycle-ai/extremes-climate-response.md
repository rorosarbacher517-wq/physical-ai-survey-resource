# Carbon-flux AI under Climate Extremes

## 1. Why extremes need separate evaluation

A model trained to minimize average error can perform poorly during heat, drought, flooding, disturbance or compound events. These periods are scientifically important and often underrepresented.

## 2. Regime definition

Define an event using explicit variables and thresholds, for example combinations of:

- temperature anomaly;
- VPD/relative humidity;
- soil moisture;
- precipitation deficit;
- radiation;
- disturbance/fire/flood indicators.

Avoid defining an extreme using information unavailable at prediction time.

## 3. Carbon response pathways

Extremes can alter:

- photosynthesis;
- respiration;
- stomatal behavior;
- canopy condition/phenology;
- soil moisture and thermal state;
- mortality/disturbance;
- source-area heterogeneity sampled by EC.

The relative response of GPP, RECO and NEE can differ.

## 4. Temporal structure

Separate:

```text
pre-event baseline
→ onset
→ peak event
→ recovery
→ possible legacy effect
```

A model that captures event onset but not recovery has a different failure mode from one that misses peak magnitude.

## 5. OOD learning problem

Extremes often lie in low-density regions of feature space. Useful approaches include:

- regime-balanced sampling;
- event-aware validation splits;
- probabilistic models;
- process constraints;
- domain adaptation;
- ensembles;
- explicit uncertainty/OOD scores.

## 6. Multimodal observations

Different modalities can respond at different times:

- meteorology detects forcing immediately;
- thermal observations capture temperature/stress;
- optical/SIF respond to canopy function/condition;
- SAR/microwave can inform moisture/structure;
- LiDAR mainly captures slower structural state unless repeated frequently.

## 7. Footprint interaction

During heterogeneous conditions, dynamic source-area sampling can change which stressed/unstressed patches contribute to tower observations. Event diagnostics should therefore separate environmental forcing from support mismatch.

## 8. Evaluation

Report:

- event-specific RMSE/MAE/bias;
- peak magnitude/timing;
- recovery error;
- component-specific GPP/RECO/NEE behavior;
- calibration/coverage;
- site/biome transfer;
- paired error relative to non-event periods.

## 9. Failure modes

- extrapolating smooth seasonal patterns through an event;
- treating rare extremes as noise and removing them during QC;
- using global normalization that hides event magnitude;
- interpreting feature importance as causal mechanism;
- claiming climate robustness from IID random splits.

## 10. Connections

See [carbon-water-energy coupling](carbon-water-energy-coupling.md), [weather/climate AI](../08-weather-climate-ai/index.md) and [uncertainty/calibration](../10-data-assimilation-inverse-uq/uncertainty-calibration.md).
