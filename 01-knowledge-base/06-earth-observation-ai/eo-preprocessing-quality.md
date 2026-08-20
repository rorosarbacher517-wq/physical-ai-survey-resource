# EO Preprocessing、Quality Control 与 Data Leakage

## 1. 一个标准 preprocessing chain

```text
source product
→ QA / cloud / shadow / snow / fill handling
→ calibration/correction check
→ reprojection
→ resampling
→ spatial crop
→ temporal alignment
→ normalization
→ sample manifest
```

---

## 2. QA 不应只当“删坏像素”

QA 本身包含 observation uncertainty 信息。

需要记录：
- valid mask；
- cloud probability / QA bit；
- snow/water flag；
- saturation；
- fill value；
- acquisition geometry。

---

## 3. Reprojection / Resampling

### Continuous variable
可用 bilinear/cubic，但会改变高频结构。

### Categorical label
通常用 nearest neighbor。

### Extensive quantity
可能需要 area/conservative aggregation。

---

## 4. Temporal compositing

mean/median/max-NDVI/quality-prioritized composite 含义不同。

Composite 会改变 temporal support，因此不能把 composite date 简单当 instantaneous observation。

---

## 5. Normalization leakage

错误：先用全 dataset 计算 mean/std，再 split。

正确：

```text
train split → compute μ,σ
val/test → reuse train μ,σ
```

---

## 6. Spatial leakage

随机 pixel split 可能把同一 scene/field/tile 的邻近像元分到 train/test。

应根据任务用：
- tile/block split；
- region split；
- scene split；
- site split。

---

## 7. Provenance

至少保存：
- product ID；
- processing version；
- acquisition time；
- source URL；
- preprocessing code version；
- resampling；
- split assignment。
