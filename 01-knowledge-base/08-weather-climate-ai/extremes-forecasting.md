# Forecasting Weather Extremes with AI

## 1. Why average metrics are insufficient

Weather models can have strong global RMSE/ACC while missing rare high-impact events. Extreme evaluation must be explicit.

## 2. Event families

Examples include:

- tropical cyclones;
- extreme precipitation;
- heat/cold extremes;
- severe convection;
- atmospheric rivers;
- strong winds;
- compound events.

Each event requires a suitable definition and verification dataset.

## 3. Conditional distribution problem

Extreme forecasting is often about tail probability:

```text
P(event magnitude > threshold | current state)
```

A deterministic conditional-mean forecast can smooth rare peaks even when large-scale evolution is accurate.

## 4. Approaches

- deterministic models with event-specific losses/diagnostics;
- ensemble forecasting;
- probabilistic/generative models;
- calibrated post-processing;
- specialized high-resolution/nowcasting models;
- multi-scale models that preserve local extremes.

## 5. Spatial and temporal scale

Extremes may be localized relative to a global grid. Track:

- native model grid;
- verification grid;
- event-object scale;
- forecast lead time;
- temporal accumulation window.

Heavy precipitation at 1 h and 24 h are different tasks.

## 6. Evaluation

Depending on event type:

- threshold-based precision/recall or threat scores;
- Brier score/reliability;
- CRPS/tail-weighted probabilistic metrics;
- quantile error;
- object track/location error;
- cyclone track/intensity;
- peak magnitude/timing;
- spatial neighborhood/object metrics.

## 7. Distribution shift

A climate-regime shift can change event frequency/intensity beyond the training distribution. Evaluate by time period, region and event intensity.

## 8. Failure modes

- optimizing global RMSE and assuming extremes follow automatically;
- verifying on an overly coarse grid that smooths event structure;
- class imbalance hiding poor rare-event recall;
- unreliable probabilities despite good ensemble mean;
- event definitions that change between train/test evaluation;
- post-processing calibrated only for historical climatology.

## 9. Carbon connection

Weather extremes provide forcing for ecosystem carbon responses. See [Carbon-flux AI under climate extremes](../07-carbon-cycle-ai/extremes-climate-response.md).
