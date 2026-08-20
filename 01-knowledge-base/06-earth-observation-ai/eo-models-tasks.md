# Earth-observation Models and Tasks

## 1. Task taxonomy

### Classification
One label per patch/object/site.

### Semantic segmentation
One class per pixel.

### Object detection
Bounding boxes/object instances.

### Regression/retrieval
Continuous variable such as biomass, temperature, productivity or moisture proxy.

### Change detection
Difference between times/conditions.

### Reconstruction/gap filling
Infer missing/corrupted observations.

### Forecasting
Predict future field/state.

### Super-resolution/downscaling
Produce fine-grid output conditioned on coarse and auxiliary information.

## 2. CNN/U-Net family

Strong local spatial inductive bias and efficient dense prediction.

Useful for segmentation, mapping, reconstruction and downscaling.

## 3. Vision Transformers

Patch/token representation allows global interactions and large-scale pretraining.

EO adaptations must handle multispectral channels, time, resolution and geolocation.

## 4. Temporal models

- ConvLSTM;
- temporal CNN;
- temporal Transformer;
- space-time factorized attention;
- state-space models.

Select based on sequence length, irregularity and required temporal dynamics.

## 5. Self-supervised learning

Common objectives:

- masked image/patch reconstruction;
- temporal prediction;
- contrastive learning;
- cross-modal alignment.

Useful because labeled geospatial data are much smaller than raw satellite archives.

## 6. Multimodal models

Combine optical, SAR, LiDAR, thermal, SIF, weather and static geographic context.

Key design choice: early channel fusion versus modality-specific encoders/cross-attention.

## 7. Scientific target caution

High mapping accuracy on land-cover/segmentation does not prove equal transfer to process variables such as fluxes. Process targets need support-aware labels, environmental forcing and temporal dynamics.

## 8. Evaluation

Report region/time/sensor OOD performance, spatial resolution, label support, class/regime imbalance and uncertainty.
