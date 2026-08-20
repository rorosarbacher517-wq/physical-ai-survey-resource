# 09 · Earth and Scientific Foundation Models

A scientific foundation model should provide reusable representations, generative capability or forecast dynamics across multiple tasks, regions, variables or modalities—not merely be a large task-specific network.

## Knowledge path

```text
Earth data/observation physics
→ pretraining corpus design
→ spatial/temporal/modality representation
→ self-supervised / predictive / generative objective
→ adaptation protocol
→ task/region/sensor/regime transfer
→ scientific + OOD evaluation
```

## 1. Why Earth foundation models are different

Earth data are georeferenced, multi-resolution, multi-sensor, multi-temporal and physically structured. Labels are sparse and sampling is highly nonuniform.

Natural-image recipes therefore need adaptation for spectral channels, time, geolocation, vertical coordinates, missing modalities and scale.

## 2. Pretraining and adaptation

See [Earth-FM pretraining and adaptation](earth-fm-pretraining.md).

Possible objectives include:

- masked reconstruction;
- contrastive learning;
- temporal prediction;
- multimodal alignment;
- cross-modal generation;
- autoregressive field prediction;
- supervised multi-task pretraining.

## 3. Multimodal representation

See [Multimodal Earth representations](multimodal-earth-representations.md).

A general model may need modality/sensor, wavelength, geolocation, time, vertical-level, resolution/support and quality/missingness metadata.

## 4. Model families

See [Model-family guide](model-family-guide.md).

Useful families include:

- EO encoders;
- multimodal generative EO models;
- global embedding fields;
- weather/Earth-system forecast foundation models;
- scientific models pretrained across simulation/field domains.

Fast-moving named releases belong in the dated [2026 Snapshot](../13-2026-snapshot/index.md).

## 5. Physics and observation operators

Broad pretraining does not remove the need for physics. Important integration routes include:

- physics-aware coordinates/tokens;
- conservation/process constraints;
- observation operators;
- hybrid simulator coupling;
- process-sensitive task heads;
- physically stratified evaluation.

## 6. Evaluation

See [Earth-FM evaluation](earth-fm-evaluation.md).

A foundation-model claim should be tested across tasks, regions, times, modalities/resolutions and labeled-data budgets with explicit pretraining-overlap audits.

## 7. Priority Earth-system connections

```text
EO foundation representation
├→ carbon-cycle / ecosystem process targets
├→ hydrology/agriculture/disaster tasks
└→ multimodal geospatial retrieval

weather/Earth-system foundation representation
├→ atmospheric forecasting
├→ extremes / downscaling
└→ coupled land/ocean/carbon tasks
```

## 8. Failure modes

- benchmark leakage through broad pretraining;
- location/season shortcut instead of process representation;
- strong interpolation but weak OOD transfer;
- sensor/preprocessing dependence hidden by model branding;
- output scale confused with validation scale;
- expensive adaptation omitted from comparisons;
- broad semantic transfer but weak process-sensitive transfer.

Domain view: [Geospatial foundation models](../../06-case-studies/geoscience-remote-sensing/geospatial-foundation-models/index.md).
