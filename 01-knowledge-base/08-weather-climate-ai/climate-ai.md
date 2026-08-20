# Climate AI

## 1. Weather versus climate

Weather forecasting predicts a specific evolving state from an initial condition. Climate modeling focuses on distributions, forced response, variability and long-term statistics under external forcing.

## 2. Climate applications of AI

- emulator of expensive climate simulations;
- parameterization/closure;
- bias correction;
- downscaling;
- extreme-event statistics;
- detection/attribution support;
- surrogate for scenario ensembles;
- Earth-system component coupling.

## 3. Emulator challenge

A climate emulator must reproduce more than short-horizon RMSE. It should represent:

- mean climatology;
- variability;
- trends/forced response;
- teleconnections;
- extremes;
- spatial spectra;
- conservation/balance;
- regime transitions.

## 4. Distribution shift

Future forcing can move the system beyond the historical training distribution. Extrapolation should be tested using held-out scenarios, climates or parameter regimes.

## 5. Coupled components

Climate involves atmosphere, ocean, land, cryosphere and biogeochemistry. Component-wise accuracy does not guarantee stable coupled behavior.

## 6. Carbon-climate connection

Terrestrial carbon responds to radiation, temperature, water stress, CO₂, disturbance and ecosystem structure; carbon changes can feed back to atmospheric composition/climate at larger scales.

## 7. Uncertainty

Separate:

- internal variability;
- scenario/forcing uncertainty;
- model structural uncertainty;
- parameter uncertainty;
- emulator error.

## 8. Evaluation

Use long simulations/statistics when claiming climate fidelity. Short weather-style test windows are insufficient for many climate properties.
