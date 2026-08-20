# Terrestrial Carbon-flux AI 专题路线

## Goal

把 EC、footprint、EO、meteorology、process physics、AI 和 upscaling 放在同一个 observation-aware framework。

## 1. Process

- [Carbon-cycle Processes](../../../01-knowledge-base/07-carbon-cycle-ai/carbon-cycle-processes.md)
- [Carbon–Water–Energy Coupling](../../../01-knowledge-base/07-carbon-cycle-ai/carbon-water-energy-coupling.md)

## 2. Measurement

- [Eddy Covariance](../../../01-knowledge-base/07-carbon-cycle-ai/eddy-covariance.md)
- [Flux Partitioning](../../../01-knowledge-base/07-carbon-cycle-ai/flux-partitioning-uncertainty.md)
- [Flux Footprints](../../../01-knowledge-base/07-carbon-cycle-ai/flux-footprints.md)

## 3. Data / AI

- [Carbon Data Stack](../../../01-knowledge-base/07-carbon-cycle-ai/carbon-data-stack.md)
- [Carbon Modeling Methods](../../../01-knowledge-base/07-carbon-cycle-ai/carbon-modeling-methods.md)
- [Multimodal Carbon AI](../../../01-knowledge-base/07-carbon-cycle-ai/multimodal-carbon-ai.md)

## 4. Physics-aware learning

- [Process-constrained Carbon AI](../../../01-knowledge-base/07-carbon-cycle-ai/process-constrained-carbon-ai.md)
- [Footprint-aware AI](../../../01-knowledge-base/07-carbon-cycle-ai/footprint-aware-ai.md)

核心结构：

```text
pixel/field flux
→ dynamic footprint observation operator
→ tower-scale supervision
```

## 5. Scale / OOD

- [Tower-to-grid Upscaling](../../../01-knowledge-base/07-carbon-cycle-ai/tower-to-grid-upscaling.md)
- [Extremes / Climate Response](../../../01-knowledge-base/07-carbon-cycle-ai/extremes-climate-response.md)
- [Validation / Uncertainty](../../../01-knowledge-base/07-carbon-cycle-ai/validation-uncertainty.md)

## 6. 截至 2026-08-20 的重点问题

- footprint 作为 observation mapping，而非只作为 feature；
- joint NEE/GPP/RECO physical consistency；
- 2D EO + 3D structure + meteorology + SIF/soil moisture；
- process-model parameter optimization；
- EO foundation representation 对 continuous ecohydrology/carbon inference 的真实增益；
- climate/extreme OOD；
- fine-grid output 的 independent validation gap。
