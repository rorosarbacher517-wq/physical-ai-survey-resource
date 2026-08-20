# Eddy Covariance for Carbon-flux AI

## 1. Measurement principle

Eddy covariance estimates turbulent vertical flux from covariance between fluctuations in vertical wind and scalar concentration.

A simplified scalar-flux form:

`F ≈ ρ · covariance(w', c')`

where `w'` is vertical-wind fluctuation and `c'` scalar-concentration fluctuation, with processing conventions depending on the flux variable/system.

## 2. Typical time support

Flux networks commonly distribute half-hourly or hourly processed products. Each record integrates turbulent exchange over the averaging period and a dynamic upwind source area.

## 3. EC does not directly measure every carbon component

NEE is derived from turbulent CO₂ exchange processing (with storage/quality considerations depending on site/product). GPP and RECO are obtained through partitioning methods/assumptions.

Therefore GPP/RECO should not be described as directly observed tower fluxes.

## 4. Quality control

Potential issues include:

- low turbulence;
- instrument failure;
- spikes;
- coordinate rotation;
- density corrections;
- storage flux;
- gap filling;
- friction-velocity filtering;
- non-stationarity.

Use the official network/product QC variables rather than inventing thresholds.

## 5. Sign convention

Always confirm whether positive NEE means atmosphere-to-ecosystem or ecosystem-to-atmosphere in the specific dataset.

## 6. Spatial support

The tower coordinate is only the sensor location. The flux measurement integrates an upwind footprint that changes with wind and turbulence.

## 7. Machine-learning sample design

Avoid random splitting of half-hours from the same site across train/test when evaluating spatial generalization. Site-blocked splits prevent direct site leakage.

## 8. Target uncertainty

Prediction error contains both model error and uncertainty in processed/partitioned flux targets. Interpret small component-level improvements in that context.

## 9. Primary data sources

Use verified records in the repository dataset library for FLUXNET/AmeriFlux and follow their data policies/documentation.
