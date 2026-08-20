# Carbon-flux Validation and Uncertainty

## 1. Split design

### Site-blocked
Entire tower sites belong to one fold only. Tests transfer to unseen locations.

### Temporal blocked
Tests future periods/events while preserving site identity.

### Biome/climate-region blocked
Tests stronger ecological/domain extrapolation.

Different splits answer different questions and should not be conflated.

## 2. Metrics

Common deterministic metrics:

- RMSE;
- MAE;
- R²/correlation with stated definition;
- bias.

Report units and sample counts.

## 3. Paired model comparison

If models use the same samples, compare sample-wise or site-wise paired errors. This reduces noise from different test sets.

## 4. Component uncertainty

GPP/RECO are partitioned products. Treat their uncertainty separately from NEE and avoid interpreting small differences as direct measurement truth.

## 5. Footprint uncertainty

Sources include:

- turbulence inputs;
- stability assumptions;
- roughness/displacement;
- canopy changes;
- footprint model applicability;
- rasterization/masking.

## 6. Remote-sensing uncertainty

Cloud masks, atmospheric correction, retrieval, temporal gaps and resampling can propagate to flux estimates.

## 7. OOD diagnostics

Stratify by:

- ecosystem;
- climate;
- heterogeneity;
- season/phenology;
- daytime/nighttime;
- heat/drought/extreme conditions;
- footprint variability;
- sensor availability.

## 8. Resolution claim

If the model produces 30 m flux pixels but supervision is tower-scale, describe output as 30 m model resolution/latent field unless independent 30 m flux validation exists.

## 9. Calibration

For probabilistic predictions report interval coverage/reliability and whether uncertainty grows in unseen sites/regimes.
