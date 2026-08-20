# Remote-sensing Time-series Learning

## 1. Earth observation is irregular in time

Satellite sequences differ from evenly sampled video. Acquisitions depend on orbit, clouds, sensor availability and compositing rules.

Represent each observation as:

```text
(x_t, timestamp_t, sensor_t, quality_t)
```

rather than assuming an implicit constant frame rate.

## 2. Temporal signals to separate

A sequence can contain:

- diurnal variation;
- phenology/seasonality;
- weather-driven anomalies;
- disturbance;
- long-term trend;
- sensor/geometry artifacts;
- missing-observation patterns.

## 3. Input representations

### Regularized sequence

Interpolate/composite to a fixed interval:

```text
[B,T,C,H,W]
```

Convenient, but interpolation assumptions become part of the data-generating process.

### Irregular-event sequence

Use actual acquisition times and masks:

```text
features: [B,T,D]
times:    [B,T]
mask:     [B,T]
```

### Patch-token sequence

```text
[B,T,P,D]
```

where `P` is the number of spatial tokens.

## 4. Model families

- temporal CNN;
- RNN/LSTM/GRU;
- temporal Transformer;
- spatial-temporal attention;
- state-space sequence models;
- latent ODE/state-space models;
- masked sequence reconstruction.

## 5. Time encoding

Useful signals include:

- elapsed time between observations;
- day-of-year;
- local solar time;
- sensor identifier;
- acquisition geometry;
- event/management metadata where available.

Do not let day-of-year become a shortcut that replaces actual environmental response when OOD climate transfer matters.

## 6. Reconstruction versus prediction

### Reconstruction/gap filling

Estimate missing observations within a sequence.

### Forecasting

Predict future state using only information available before the forecast origin.

### Smoothing

Use observations before and after a target time.

These are different tasks and require different leakage rules.

## 7. Multi-sensor densification

Harmonized or fused records can improve temporal coverage, but cross-sensor calibration and spectral-response differences must be tracked.

## 8. Evaluation

Use splits that test the intended generalization:

- future time blocks;
- held-out regions/sites;
- held-out sensors;
- disturbance/extreme periods;
- long missing intervals.

## 9. Failure modes

- interpolation using future data in a forecasting task;
- random date splitting that leaks seasonal signatures from the same site;
- cloud masks correlated with target conditions;
- treating reconstructed values as independent observations;
- ignoring sensor changes in long records.

## 10. Related pages

See [Temporal modeling](../05-spatiotemporal-multiscale-ai/temporal-modeling.md), [EO preprocessing](eo-preprocessing-quality.md) and [super-resolution/reconstruction](super-resolution-reconstruction.md).
