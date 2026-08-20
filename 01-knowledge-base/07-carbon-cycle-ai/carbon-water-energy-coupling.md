# Carbon–Water–Energy Coupling for AI

## 1. Why carbon should not be modeled in isolation

Photosynthesis, respiration, evapotranspiration, radiation balance, temperature and water availability interact. Many predictive relationships change across environmental regimes.

A conceptual chain is:

```text
radiation + temperature + water availability + atmospheric demand
→ stomatal/canopy response
→ photosynthesis + transpiration
→ carbon and water fluxes
```

Respiration adds temperature/moisture/substrate dependencies.

## 2. Core variables

Carbon:

- NEE;
- GPP;
- RECO.

Water/atmosphere:

- evapotranspiration / latent heat;
- precipitation;
- soil moisture;
- vapor-pressure deficit / humidity;
- wind/turbulence.

Energy:

- shortwave/longwave radiation;
- sensible/latent heat;
- surface/canopy temperature;
- ground heat where relevant.

## 3. Why multimodal AI benefits

Remote sensing captures vegetation state/structure; meteorology captures forcing; EC captures surface-atmosphere exchange.

```text
EO state      [B,T,C,H,W]
meteorology   [B,T,M]
static context[B,S]
→ spatiotemporal model
→ carbon/water/energy targets
```

The modalities play different causal/observational roles and should not be treated as interchangeable features.

## 4. Multi-task learning

One approach predicts several coupled quantities:

```text
shared encoder
→ GPP head
→ RECO head
→ NEE head
→ ET/energy head(s)
```

Possible benefits include shared representation and consistency checks. Risks include negative transfer when tasks have different noise and support.

## 5. Physical relationships

Useful constraints depend on dataset definitions and closure quality. Examples can include:

- NEE/GPP/RECO balance;
- energy-balance consistency;
- nonnegative component fluxes under selected conventions;
- process-sensitive responses to radiation, moisture and temperature.

Avoid forcing approximate ecological relationships as exact equations.

## 6. Regime dependence

Relationships can change across:

- wet versus dry conditions;
- dormant versus growing season;
- daytime versus nighttime;
- heat/drought extremes;
- forest/crop/grassland/wetland systems.

This motivates conditional diagnostics rather than one global feature-importance ranking.

## 7. Evaluation

Check:

- per-target metrics;
- cross-target physical consistency;
- regime-stratified errors;
- OOD climate transfer;
- calibration;
- whether adding coupled targets improves held-out sites rather than only training fit.

## 8. Research direction

A strong Earth AI system should represent coupled carbon-water-energy responses while preserving the observation support of each target. This connects [multimodal carbon AI](multimodal-carbon-ai.md), [weather/climate forcing](../08-weather-climate-ai/index.md) and [data assimilation/UQ](../10-data-assimilation-inverse-uq/index.md).
