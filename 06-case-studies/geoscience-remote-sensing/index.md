# Geoscience / Remote Sensing / Earth-system AI 专题

这是仓库的重点应用入口，用于把底层 Scientific AI 知识重新组合成 Earth-system workflow。

## 1. 总依赖图

```text
Math / PDE / Numerical Methods
→ ML/DL / Scientific Computing
→ Observation Operator / Inverse / DA / UQ
→ Spatiotemporal / Multiscale / Multimodal AI
→ Earth Observation
      ├→ Carbon Cycle / Carbon Flux
      ├→ Weather / Climate
      └→ Geospatial Foundation Models
→ Data / HPC / OOD Evaluation
```

## 2. 四条专题

- [Earth Observation / Remote Sensing](earth-observation/index.md)
- [Terrestrial Carbon Flux](carbon-flux/index.md)
- [Weather & Climate](weather-and-climate/index.md)
- [Geospatial Foundation Models](geospatial-foundation-models/index.md)

---

## 3. 六条共同 scientific principles

1. **Observation ≠ state**：sensor/retrieval/footprint physics 必须明确。
2. **Resolution ≠ support**：output grid 与 observation/validation support 分开。
3. **Space × time 不可拆开**：revisit、composite、moving footprint、rollout 都改变问题。
4. **Random split 通常不够**：site/region/time/event/climate blocking 是核心设计。
5. **Physics 有多种入口**：input、architecture、loss、operator、solver、DA、evaluation 不混写。
6. **Uncertainty 是结果的一部分**：measurement、retrieval、partitioning、model、support、OOD uncertainty 都应考虑。

---

## 4. 主知识入口

- [Earth Observation AI](../../01-knowledge-base/06-earth-observation-ai/index.md)
- [Carbon-cycle AI](../../01-knowledge-base/07-carbon-cycle-ai/index.md)
- [Weather & Climate AI](../../01-knowledge-base/08-weather-climate-ai/index.md)
- [Earth Foundation Models](../../01-knowledge-base/09-earth-foundation-models/index.md)
- [DA / Inverse / UQ](../../01-knowledge-base/10-data-assimilation-inverse-uq/index.md)
- [2026-08-20 Snapshot](../../01-knowledge-base/13-2026-snapshot/index.md)
