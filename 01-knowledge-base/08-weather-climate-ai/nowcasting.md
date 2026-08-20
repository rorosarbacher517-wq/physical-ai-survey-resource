# Weather Nowcasting

## 1. Task

Nowcasting predicts weather over short horizons using high-frequency observations, commonly radar and satellite imagery plus numerical/other context.

## 2. Radar sequence view

Input can be represented as:

`[B,T,C,H,W]`

where channels encode reflectivity/rain-rate-related products and auxiliary variables.

## 3. Baseline approaches

- optical-flow/advection extrapolation;
- ConvLSTM;
- U-Net/video prediction;
- Transformer;
- generative/diffusion methods.

## 4. Core challenge

Pure extrapolation can move existing precipitation but cannot create/decay convection realistically. Learned models aim to capture evolution, while uncertainty increases quickly for convective storms.

## 5. Loss design

Pixel MSE can blur intense rain because conditional mean smooths uncertain locations.

Alternatives/complements:

- threshold-weighted losses;
- probabilistic/generative objectives;
- perceptual/structural terms;
- event-centric verification.

## 6. Evaluation

Use lead-time curves and threshold/event metrics:

- CSI-like skill for precipitation thresholds;
- FSS-like neighborhood scores;
- calibration/probability for severe thresholds;
- displacement/intensity diagnostics.

## 7. Observation issues

Radar coverage, beam blockage, attenuation, clutter and conversion from reflectivity to rain rate introduce uncertainty.

## 8. Multi-source nowcasting

Satellite, lightning, surface stations, NWP and radar can be fused. Different latency and spatial support must be recorded.
