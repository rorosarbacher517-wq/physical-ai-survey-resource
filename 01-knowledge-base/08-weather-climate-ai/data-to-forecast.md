# Data-to-Forecast：从 Observations 直接走向 Forecast System

## 1. 为什么这是独立问题

多数 early AI weather forecast workflow：

```text
ERA5 / operational analysis
→ AI forecast model
```

而完整 operational pipeline：

```text
raw/processed observations
→ QC / DA / analysis
→ forecast
```

所以 forecast-core speedup 并不自动代表整个 NWP pipeline 已被替代。

---

## 2. Aardvark Weather

Nature 2025：

```text
remote-sensing + in-situ observations
→ observation-processing/analysis module
→ global gridded forecast
→ local station forecast
```

论文明确：deployment/test-time forecast 不依赖 conventional NWP products；training/pretraining 利用了 ERA5/reanalysis information。

Primary: https://doi.org/10.1038/s41586-025-08897-0

---

## 3. FuXi Weather

Nature Communications 2025：

```text
raw observations
→ FuXi-DA cycling analysis
→ fine-tuned FuXi forecast
→ repeat every 6 h
```

论文描述的重要设计：
- variable/instrument-specific satellite encoders；
- sparse observation encoding；
- cycling DA；
- monthly replay-based incremental updates；
- 0.25° ERA5 reference during training。

Primary: https://doi.org/10.1038/s41467-025-62024-1

---

## 4. 与传统 DA 的区别

传统：明确 `B/R/H/M`、variational/ensemble update。

ML data-to-forecast：可能把其中部分关系隐式学习。

因此需要问：
- observation error 如何处理？
- 新 sensor/instrument 上线怎么办？
- missing observation 怎么办？
- cycling stability？
- bias drift？
- analysis 是否 physically balanced？

---

## 5. Remote Sensing 的连接

这条路线让 EO 不再只是 downstream map：satellite radiance / remote-sensing observations 直接成为 atmospheric state estimation 的上游。

这是 Earth Observation AI 与 Weather AI 最重要的交叉点之一。

---

## 6. Evaluation

应拆成：

```text
observation → analysis skill
analysis → forecast skill
end-to-end station/grid skill
cycling stability
sensor robustness
compute / latency
```

只报 forecast RMSE 不足以诊断 data-to-forecast system。
