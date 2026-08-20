# Temporal Modeling

## 1. Task types

### Sequence-to-one
Past observations → current/aggregate target.

### Sequence-to-sequence
Input trajectory → output trajectory.

### Autoregressive forecast
Predict next state and feed it back.

### Direct multi-horizon
Predict several lead times without recursive feedback.

### Continuous-time
Model derivatives or latent dynamics instead of fixed discrete steps.

## 2. Time encoding

Useful features:

- absolute timestamp;
- cyclic hour/day/year encodings;
- elapsed time;
- irregular time gap;
- lead time;
- acquisition/sensor timestamp.

## 3. Missing observations

Earth observation time series are often irregular because of clouds/orbits. Options:

- masks;
- gap-aware attention;
- interpolation with uncertainty;
- latent state models;
- cross-sensor fusion.

Do not treat imputed values as independently observed truth.

## 4. Autoregressive drift

During training, a model may see true states; during inference, it sees its own imperfect predictions.

Mitigations:

- multi-step training;
- noise/perturbation training;
- scheduled/self-conditioning variants;
- stable physical constraints;
- direct multi-horizon outputs.

## 5. Multi-timescale signals

Separate fast weather/turbulence from slow seasonality/climate/structure using hierarchical temporal features or modules when appropriate.

## 6. Evaluation

Report error versus lead time, season/regime/event, and check phase timing/extreme amplitude—not only pooled error.
