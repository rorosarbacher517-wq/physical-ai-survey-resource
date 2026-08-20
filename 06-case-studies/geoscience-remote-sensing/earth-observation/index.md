# Earth Observation / Remote Sensing AI 专题路线

## Goal

完整掌握：

```text
sensor physics
→ product/data stack
→ preprocessing/QA
→ spatial-spectral-temporal representation
→ retrieval/inversion
→ multisensor AI
→ foundation models
→ geospatial/OOD evaluation
```

## 1. 先学 observation physics

- [Radiative Transfer / Observation Physics](../../../01-knowledge-base/06-earth-observation-ai/radiative-transfer-observation-physics.md)
- [Optical / Hyperspectral](../../../01-knowledge-base/06-earth-observation-ai/optical-hyperspectral.md)
- [SAR / Microwave](../../../01-knowledge-base/06-earth-observation-ai/sar-microwave.md)
- [LiDAR / 3D](../../../01-knowledge-base/06-earth-observation-ai/lidar-3d.md)
- [Thermal / SIF](../../../01-knowledge-base/06-earth-observation-ai/thermal-sif.md)

## 2. 再学 data pipeline

- [EO Data Stack](../../../01-knowledge-base/06-earth-observation-ai/eo-data-stack.md)
- [Preprocessing / QA](../../../01-knowledge-base/06-earth-observation-ai/eo-preprocessing-quality.md)
- [Remote-sensing Time Series](../../../01-knowledge-base/06-earth-observation-ai/remote-sensing-time-series.md)

## 3. 再学 inference / fusion

- [Retrieval / Inverse](../../../01-knowledge-base/06-earth-observation-ai/retrieval-inversion.md)
- [Multisensor Fusion](../../../01-knowledge-base/06-earth-observation-ai/multisensor-fusion.md)
- [Super-resolution / Reconstruction](../../../01-knowledge-base/06-earth-observation-ai/super-resolution-reconstruction.md)

## 4. Foundation route

- [EO Foundation Models](../../../01-knowledge-base/06-earth-observation-ai/eo-foundation-models.md)
- [Earth Foundation Models](../../../01-knowledge-base/09-earth-foundation-models/index.md)
- [Geospatial Validation / OOD](../../../01-knowledge-base/06-earth-observation-ai/geospatial-validation.md)

截至 2026-08-20 的重点接口：`Prithvi-EO-2.0`, `TerraMind`, `AlphaEarth Foundations`, `TESSERA`, `MaRS`。

## 5. 最终应该能回答

- sensor 真正测到什么？
- product level / correction 做了什么？
- resolution 与 support 是什么？
- modality 为什么互补？
- embedding 保留的是 semantic 还是 quantitative process information？
- geography/time/sensor OOD 怎么验证？
