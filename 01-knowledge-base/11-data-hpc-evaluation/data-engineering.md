# Scientific Data Engineering

## 1. Raw → Analysis-ready → ML-ready

建议分层：

```text
raw immutable source
→ calibrated/quality-controlled product
→ harmonized analysis-ready data
→ sample manifest
→ model-ready shards/batches
```

不要把 downloaded raw data 与处理后 training array 混在同一个不可追溯目录。

---

## 2. Sample Manifest

每个样本至少能追到：

```text
sample_id
source IDs
space/time bounds
variables
units
QA/mask
processing version
label source/support
split group
checksum/provenance
```

---

## 3. Chunking

Zarr/NetCDF chunk 应根据 access pattern 设计。

例如：
- time-series training：time chunk 不能过碎；
- random spatial patches：spatial chunk 要减少读放大；
- global forecast：常按 time/variable 分片并做 parallel I/O。

错误 chunking 会让 GPU 等数据。

---

## 4. Missing values

区分：
- true physical zero；
- missing；
- fill value；
- invalid QA；
- outside domain。

不要全部填 0 而不提供 mask。

---

## 5. Coordinate / CRS

Earth data 必须保存：
- CRS；
- affine transform；
- latitude/longitude；
- vertical coordinate；
- calendar/time zone；
- grid cell convention。

---

## 6. Units

建议在 ingestion 层统一 canonical units，并在 metadata 保存原单位。

尤其注意：
- Kelvin vs Celsius；
- Pa vs hPa；
- accumulated precipitation vs rate；
- carbon flux sign/unit；
- radiation energy accumulation vs flux。

---

## 7. Split manifest

split 是 data artifact：

```text
sample_id → train/val/test/fold
```

应 version-control，而不是每次 runtime 随机生成。

---

## 8. Foundation-model data overlap

下游 benchmark 还应记录：
- pretraining time range；
- geography overlap；
- sensor overlap；
- target-label overlap if known。

---

## 9. Data lineage

最终一个 metric 应能反向追踪：

```text
metric
→ predictions
→ checkpoint
→ training manifest
→ processed samples
→ raw source/product version
```
