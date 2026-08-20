# Dimensional Analysis, Scale and Observation Support

## 1. Units are part of model semantics

Before training, record units for every physical variable.

Examples:

- temperature: K or °C;
- pressure: Pa;
- precipitation: rate versus accumulated depth;
- radiation: instantaneous flux versus accumulated energy;
- carbon flux: µmol CO₂ m⁻² s⁻¹;
- wind: m s⁻¹.

A unit mismatch can create plausible-looking but physically wrong training data.

## 2. Dimensional consistency

Terms added in an equation must have compatible dimensions. Dimension checking is a simple but strong debugging tool for feature engineering, derived variables and physical losses.

## 3. Dimensionless groups

Dimensionless combinations summarize regimes and can improve transfer across scales.

Examples across physics include Reynolds, Peclet, Richardson and other ratios of competing processes.

The key idea is not memorizing names: identify the ratio of characteristic effects and how it partitions regimes.

## 4. Resolution versus support

### Resolution
Nominal spacing of a grid or pixel.

### Support
Physical area/volume/time interval contributing to an observation.

### Coverage
Where/when observations exist.

### Validation support
Scale at which ground truth meaningfully checks a prediction.

These are different.

## 5. Examples

### Eddy covariance
A tower is located at a point, but each flux value integrates an upwind area with dynamic weighting.

### Satellite pixel
A nominal 30 m grid cell represents sensor response over an area and may involve resampling from native observations.

### Weather grid
A model cell represents a resolved-scale atmospheric state, while a station measures a local environment.

## 6. Scale mismatch

A learning pair can be biased when:

```text
predictor support ≠ target support
```

Possible remedies:

- observation operators;
- area/footprint weighting;
- aggregation to common support;
- hierarchical models;
- explicit support metadata;
- uncertainty propagation.

## 7. Temporal support

A half-hour mean, hourly accumulation, daily composite and instantaneous satellite overpass are not interchangeable.

Record:

- timestamp convention;
- interval start/end;
- accumulation versus average;
- timezone/UTC;
- interpolation rule.

## 8. Practical checklist

For every variable document:

`name → physical meaning → unit → native support → grid/resolution → time support → preprocessing → uncertainty`.
