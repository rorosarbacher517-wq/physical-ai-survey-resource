# Weather and Earth-system Foundation Models

## 1. Foundation-model question

A weather/Earth foundation model aims to learn reusable representations or dynamics from broad geophysical data, then adapt to multiple tasks, domains or resolutions.

This differs from training one forecast model for one fixed variable set and lead-time setup.

## 2. Pretraining data axes

A geophysical pretraining corpus can vary across:

- variables;
- pressure/model levels;
- time resolution;
- spatial grids;
- observation/reanalysis sources;
- atmosphere/land/ocean components;
- forecast versus analysis fields;
- regions and climate regimes.

## 3. Representation

A generic global state may be represented as:

```text
X: [B,T,V,L,H,W]
```

or flattened/embedded into grid, patch, graph or mesh tokens.

A foundation model may need variable identity, vertical position, geolocation and time encodings rather than assuming a fixed RGB-like channel order.

## 4. Pretraining objectives

Possible objectives include:

- masked variable/space-time reconstruction;
- next-state prediction;
- multi-step forecasting;
- cross-variable prediction;
- multi-resolution reconstruction;
- denoising/generative objectives;
- contrastive/geospatial representation learning.

## 5. Adaptation

Common modes:

```text
frozen representation → shallow head
parameter-efficient adaptation
full fine-tuning
task-specific decoder/head
continued pretraining on a new domain
```

Report exactly which adaptation protocol is used.

## 6. Public model pattern

Aurora is a useful public reference for broad geophysical pretraining followed by adaptation across multiple Earth-system forecasting tasks.

Primary: https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/

Operational model families should not automatically be called foundation models unless the training/adaptation design supports that interpretation.

## 7. Evaluation

A foundation-model claim should be tested through transfer:

- new tasks;
- new regions;
- new variables;
- new time periods;
- new resolutions;
- low-label regimes;
- OOD/extreme regimes.

Compare with task-specific models under matched data and compute when possible.

## 8. Failure modes

- broad pretraining but narrow downstream evaluation;
- pretraining/evaluation overlap;
- fixed variable set despite a general-model claim;
- strong average transfer but poor extremes;
- hidden dependence on reanalysis biases;
- adaptation cost similar to training a task model from scratch.

## 9. Cross-domain connection

Earth-system foundation models can connect weather, climate, land and remote sensing, but observation physics differs by modality. See [multimodal Earth representations](../09-earth-foundation-models/multimodal-earth-representations.md).
