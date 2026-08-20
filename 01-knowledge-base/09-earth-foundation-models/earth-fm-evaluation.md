# Evaluating Earth and Scientific Foundation Models

## 1. Core principle

A foundation model should be evaluated by **transfer and reuse**, not only by the accuracy of one downstream task.

## 2. Adaptation protocols must be separated

Report whether evaluation uses:

```text
frozen embedding + shallow head
linear probe
parameter-efficient tuning
full fine-tuning
continued pretraining + fine-tuning
zero-shot / retrieval-style use
```

These protocols have different compute and data requirements.

## 3. Transfer axes

A useful benchmark matrix spans:

- task;
- sensor/modality;
- region;
- time period;
- spatial resolution;
- temporal resolution;
- climate/ecological regime;
- label quantity.

## 4. Leakage audit

Check overlap between pretraining and downstream evaluation at the level of:

- imagery/scenes;
- coordinates;
- acquisition dates;
- derived labels;
- benchmark datasets;
- repeated tiles/time series.

Global pretraining makes naive geographic holdout insufficient if the same location/time was already seen during pretraining.

## 5. Label efficiency

A reusable representation should be tested under decreasing labeled-data budgets rather than only full-data fine-tuning.

## 6. OOD evaluation

Useful splits include:

- held-out continent/region;
- held-out biome/climate regime;
- held-out sensor;
- held-out time period;
- extreme/disturbance events;
- resolution shift.

## 7. Scientific metrics

In addition to task error, evaluate:

- physical consistency;
- calibration/uncertainty;
- event/extreme behavior;
- scale/support correctness;
- long-rollout stability for forecasting models.

## 8. Compute accounting

Report:

- pretraining compute/data scale when disclosed;
- downstream adaptation compute;
- inference latency/memory;
- token/pixel/grid count;
- storage cost for global embeddings if relevant.

A representation that requires expensive full fine-tuning for every task should be compared fairly with task-specific baselines.

## 9. Baselines

Compare against:

- simple task-specific ML/DL;
- domain-pretrained encoders;
- same architecture trained without broad pretraining;
- physically informed/task-specific models where appropriate.

## 10. Process-sensitive benchmark question

For this repository, a high-value test is whether Earth representations improve carbon, water, weather and extreme-event tasks under site/region/regime blocking rather than only semantic mapping.

## 11. Related pages

See [Geospatial validation](../06-earth-observation-ai/geospatial-validation.md), [weather foundation models](../08-weather-climate-ai/weather-foundation-models.md) and [evaluation/benchmarking](../11-data-hpc-evaluation/evaluation-benchmarking.md).
