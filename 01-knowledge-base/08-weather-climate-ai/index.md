# 08 · Weather and Climate AI

Weather AI should be understood as a modeling system, not a leaderboard of model names.

## 1. Operational forecasting chain

```text
observations
→ quality control
→ data assimilation
→ analysis / initial atmospheric state
→ forecast model
→ deterministic forecast or ensemble
→ post-processing / downscaling
→ verification and warnings
```

A model may replace only one block or several blocks.

## 2. Classical numerical-weather context

Numerical weather prediction solves discretized physical equations for atmospheric dynamics and parameterizes unresolved processes.

AI can act as:

- full forecast surrogate;
- learned parameterization/closure;
- data-assimilation component;
- bias correction/post-processing;
- probabilistic ensemble generator;
- nowcasting model;
- downscaling/super-resolution model;
- climate emulator.

## 3. Spatial representations

Global weather is not a flat RGB image.

Common choices:

- latitude-longitude grid;
- spherical harmonics/operator representations;
- icosahedral or mesh graph;
- cubed-sphere / HEALPix-like grids;
- patch/token representations.

Important issues: pole distortion, periodic longitude, multi-level vertical structure, vector winds and conservation.

## 4. Forecast paradigms

### Deterministic
One best-estimate trajectory.

### Probabilistic / ensemble
A distribution or multiple plausible trajectories. Evaluate calibration and spread, not only mean error.

### Generative
Diffusion/score or related generative methods can create coherent forecast ensembles and high-resolution fields.

### Hybrid physics-ML
Learn parameterizations or corrections while retaining numerical dynamics, or build differentiable physical components into training.

## 5. Tasks

- medium-range global forecasting;
- short-range / nowcasting;
- tropical cyclone track/intensity;
- precipitation and severe weather;
- data assimilation;
- regional downscaling;
- subseasonal/seasonal prediction;
- climate simulation/emulation.

## 6. Evaluation

### Deterministic
RMSE, MAE, anomaly correlation, variable/level/lead-time stratification.

### Probabilistic
CRPS, Brier score, rank/reliability diagnostics, spread-skill and event probabilities.

### Extremes
Tail/event metrics, cyclone track/intensity, heavy precipitation, heat/cold extremes.

### Physical quality
Mass/energy behavior, spectra, balance relationships and stable rollout.

Always match verification source, grid/resolution, lead time and variable before comparing systems.

## 7. Current systems to know

Stable conceptual anchors include GraphCast, Pangu-Weather, FourCastNet, NeuralGCM, GenCast and Aurora. Current operational/deployment developments are tracked separately in [13 · 2026 Snapshot](../13-2026-snapshot/index.md), including ECMWF AIFS, WeatherNext 2 and NVIDIA Earth-2.

See the [Weather & climate specialty track](../../06-case-studies/geoscience-remote-sensing/weather-and-climate/index.md).
