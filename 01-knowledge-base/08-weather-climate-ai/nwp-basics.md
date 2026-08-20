# Numerical Weather Prediction Basics

## 1. Forecasting problem

Weather forecasting evolves an atmospheric state forward in time from an analyzed initial condition.

A simplified state contains fields such as:

```text
wind components
temperature
pressure / geopotential
humidity
surface variables
```

with vertical levels and a global/regional spatial grid.

## 2. Governing structure

Operational NWP is built around discretized equations for:

- momentum;
- mass continuity;
- thermodynamics/energy;
- moisture/constituents;
- equation of state;
- surface/land/ocean coupling.

Processes below grid scale are parameterized.

## 3. Initial condition

The atmosphere is not observed everywhere. Data assimilation combines heterogeneous observations with a background forecast/model to estimate the initial state.

Forecast skill therefore depends on both model dynamics and analysis quality.

## 4. Resolved versus parameterized scales

A model grid does not resolve every cloud/turbulent process. Parameterizations represent effects such as:

- convection;
- cloud microphysics;
- radiation;
- boundary-layer turbulence;
- land-surface exchange.

AI can replace the complete forecast model or learn selected components.

## 5. Time stepping

Numerical models repeatedly update the state. Stability, conservation and balance matter because small errors can grow over many steps.

## 6. Vertical coordinate

Weather tensors often include pressure/model levels:

`[B,T,V,L,H,W]`

where `V` variables and `L` vertical levels. A model that collapses vertical structure too aggressively can lose important dynamics.

## 7. Boundary conditions

Regional models need lateral boundaries; global models need spherical/periodic geometry handling.

## 8. Deterministic versus ensemble

A deterministic run provides one trajectory. An ensemble samples uncertainty in initial conditions/model/learned stochasticity and supports probabilistic forecasts.

## 9. AI connection

Before studying an AI weather model, identify:

- input analysis/reanalysis;
- variable list and levels;
- grid;
- forecast step;
- autoregressive/direct horizon;
- deterministic/probabilistic objective;
- verification dataset.
