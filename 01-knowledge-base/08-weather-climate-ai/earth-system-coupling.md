# Coupled Earth-system AI

## 1. Motivation

Atmosphere, land, ocean, sea ice, hydrology and biogeochemistry exchange energy, water, momentum and carbon. A model that predicts only atmospheric variables can ignore feedbacks important on longer timescales or for coupled applications.

## 2. Component view

```text
Atmosphere
↕ momentum / heat / moisture / radiation
Land
↕ runoff / heat / carbon / moisture
Ocean / sea ice
↕ heat / momentum / freshwater
Biogeochemistry
↕ carbon / ecosystem processes
```

## 3. Modeling approaches

### Separate component models + coupling

Each component has its own model and exchange interface.

### Unified multi-component model

One network processes a combined state with variable/component embeddings.

### Hybrid physical–ML coupling

Numerical components are retained while selected components or exchange terms are learned.

## 4. Representation challenge

Different components have different:

- grids;
- vertical coordinates;
- time steps;
- state variables;
- observation density;
- conservation requirements.

A unified tensor is convenient but can hide these differences.

## 5. Coupling frequency

Fast atmospheric dynamics and slower land/ocean/carbon states evolve on different timescales.

Possible designs:

```text
fast atmosphere step × k
→ exchange update
→ slower component step
```

or asynchronous/multi-rate learned integration.

## 6. Physical constraints

Coupling interfaces should track flux sign, units and conservation. Examples:

- surface energy exchange;
- freshwater balance;
- momentum flux;
- carbon exchange.

## 7. Training data

Sources may include:

- coupled-model simulations;
- reanalysis;
- satellite observations;
- in-situ networks;
- land/ocean analysis products.

Observation support and bias differ across sources.

## 8. Evaluation

Check both component skill and coupled behavior:

- atmosphere forecast;
- land/ocean state;
- cross-component fluxes;
- long-term drift;
- conservation;
- extremes;
- climate distribution.

## 9. Failure modes

- component skill improves while coupled fluxes become inconsistent;
- mismatched time scales cause instability;
- learned coupling violates units/sign conventions;
- observationally sparse components inherit simulator bias;
- short forecast evaluation misses slow drift.

## 10. Connections

This page connects [weather/climate AI](index.md), [carbon–water–energy coupling](../07-carbon-cycle-ai/carbon-water-energy-coupling.md), [hybrid weather](physics-hybrid-weather.md) and [Earth foundation models](../09-earth-foundation-models/index.md).
