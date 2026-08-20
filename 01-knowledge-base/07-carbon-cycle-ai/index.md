# 07 · Terrestrial Carbon-cycle / Carbon-flux AI

This is a priority track of the repository. The organizing principle is the complete chain from **ecosystem processes → measurement physics → multimodal observations → model → observation operator → scale-aware validation**.

## Knowledge path

```text
Carbon-cycle processes
→ EC measurement
→ flux partitioning / target uncertainty
→ flux footprint / observation support
→ EO + meteorology + structure data stack
→ carbon-water-energy coupling
→ data-driven / hybrid / process-constrained model
→ footprint-aware observation mapping
→ tower validation
→ tower-to-grid upscaling
→ extremes / climate-regime OOD
→ uncertainty propagation
```

## 1. Process foundation

Start with [Carbon-cycle processes](carbon-cycle-processes.md).

Common tower-scale quantities are NEE, GPP and RECO. Under one common sign convention:

```text
NEE = RECO - GPP
```

Always verify the product convention.

Then study [carbon–water–energy coupling](carbon-water-energy-coupling.md) to understand why radiation, temperature, water availability and atmospheric demand interact with carbon exchange.

## 2. Eddy covariance and targets

- [Eddy covariance](eddy-covariance.md): what EC measures and key QC/measurement assumptions.
- [Flux partitioning and target uncertainty](flux-partitioning-uncertainty.md): why GPP/RECO are inferred labels rather than independent direct measurements.
- [Flux footprints](flux-footprints.md): dynamic spatial support of the tower observation.

A half-hourly EC record should be treated as an area-support observation, not a point label automatically aligned with a center pixel.

## 3. Data stack

See [Carbon data stack](carbon-data-stack.md).

Typical inputs:

```text
EO patch:       [B,T,C,H,W]
meteorology:    [B,T,M]
static context: [B,S]
3D structure:   [B,N,C3d] or raster features
footprint:      [B,T,H,W]
target:         [B,T,F]
```

Related EO foundations: [Earth Observation AI](../06-earth-observation-ai/index.md) and [multisensor fusion](../06-earth-observation-ai/multisensor-fusion.md).

## 4. Modeling families

See [Carbon modeling methods](carbon-modeling-methods.md).

The hierarchy includes empirical/process models, classical ML upscaling, deep spatiotemporal learning, hybrid process-ML, physics/process constraints and foundation-model representations.

For explicit physical integration see [Process-constrained carbon AI](process-constrained-carbon-ai.md).

## 5. Footprint-aware learning

See [Footprint-aware AI](footprint-aware-ai.md).

Distinguish:

- input-side predictor aggregation;
- output-side observation-operator aggregation;
- flux disaggregation;
- representativeness analysis;
- footprint descriptors as model features.

These placements are scientifically different.

## 6. Multimodal carbon AI

See [Multimodal carbon AI](multimodal-carbon-ai.md).

A high-value design combines:

```text
2D optical/SAR/thermal/SIF
+ 3D canopy structure
+ meteorological forcing
+ static context
+ EC observation support
→ spatiotemporal model
→ flux field / tower prediction
```

## 7. Tower-to-grid upscaling

See [Tower-to-grid upscaling](tower-to-grid-upscaling.md).

Separate:

- tower-scale predictive validation;
- spatial prediction resolution;
- independent spatial validation scale;
- regional OOD coverage.

## 8. Extremes and climate response

See [Carbon-flux AI under climate extremes](extremes-climate-response.md).

Evaluate onset, peak and recovery under heat/drought/compound events rather than relying only on average seasonal metrics.

## 9. Validation and uncertainty

See [Validation and uncertainty](validation-uncertainty.md).

Prefer:

- site-blocked CV;
- region/biome/climate transfer;
- temporal/event blocking;
- component-specific NEE/GPP/RECO metrics;
- support-aware evaluation;
- uncertainty/calibration;
- process-consistency diagnostics.

## 10. Major scientific traps

- describing partitioned GPP/RECO as direct EC measurements;
- random date splitting within the same sites;
- treating optical predictors as causal controllers of carbon exchange;
- ignoring footprint/pixel mismatch;
- using a fine output grid as evidence of fine-scale validation;
- interpreting one feature-importance ranking as process mechanism;
- ignoring measurement/partitioning uncertainty.

## 11. Research frontier

Priority directions include:

- dynamic observation-operator learning;
- 2D EO + 3D structure + meteorology fusion;
- dense time-series reconstruction with uncertainty;
- coupled carbon-water-energy objectives;
- process-informed Earth foundation models;
- event/extreme/OOD evaluation;
- uncertainty propagation from measurement to regional product.

See the [Carbon-flux specialty track](../../06-case-studies/geoscience-remote-sensing/carbon-flux/index.md) and [papers by method](../../02-paper-library/by-method.md).
