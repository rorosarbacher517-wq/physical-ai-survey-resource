# Multimodal Carbon AI: 2D + 3D + Meteorology + Observation Physics

## 1. Modality roles

### 2D optical/SAR/thermal/SIF
Spatial canopy/surface state and sensor-specific physical signals.

### 3D LiDAR
Canopy height/profile, terrain and structural heterogeneity.

### Meteorology
Dynamic forcing of photosynthesis/respiration and footprint/turbulence state.

### EC footprint
Observation support rather than another generic image channel.

## 2. Example architecture

```text
2D EO pixels ─→ spatial encoder ─┐
3D structure ─→ 3D encoder ─────┼→ pixel/site latent features
meteorology ─→ temporal encoder ┘
                              ↓
                       temporal model
                              ↓
                    pixel/field fluxes
                              ↓
                  footprint operator H_t
                              ↓
                       tower-scale loss
```

## 3. Shape example

```text
EO:       [B,T,C,H,W]
LiDAR:    [B,C3,H,W] or point set [B,N,C3]
meteo:    [B,T,P]
footprint:[B,T,H,W]
output:   [B,T,K,H,W] or latent pixel list
```

where `K` may represent NEE/GPP/RECO.

## 4. Static versus dynamic 3D

LiDAR may be much less frequent than optical/weather. Treat it as structural context, not a dynamic daily observation, unless repeated acquisitions support change modeling.

## 5. Missing modality strategy

Use masks/modality dropout and compare performance when 3D/SIF/SAR are unavailable.

## 6. Physics constraints

Potential additions:

- carbon-balance consistency;
- footprint observation mapping;
- phenology/radiation timing;
- water-stress features;
- uncertainty-weighted loss.

## 7. Evaluation

Ablate each modality and report pooled plus site-level behavior. A modality that helps some ecosystems and hurts pooled error can still reveal where its information is useful or where data volume is insufficient.

## 8. Research direction

A valuable Earth foundation model for carbon should learn reusable spatial/spectral/structural state while leaving dynamic meteorology and observation physics explicit.
