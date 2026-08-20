# EO Tasks 与 Model Families

## 1. Classification

```text
patch/tile → class
```

baseline：RF / CNN / ViT / frozen FM + linear probe。

---

## 2. Semantic Segmentation

```text
[B,C,H,W] → [B,K,H,W]
```

常用：U-Net、DeepLab、SegFormer、Mask2Former-style architectures。

---

## 3. Object Detection

任务：ship、building、vehicle、infrastructure、disaster object 等。

注意遥感特性：
- arbitrary orientation；
- small objects；
- huge images；
- class imbalance；
- geographic domain shift。

---

## 4. Change Detection

```text
image_t1 + image_t2 → change map
```

关键难点：season/illumination/geometry difference 不等于真实 land change。

---

## 5. Regression / Retrieval

例如：
- biomass；
- LAI；
- soil moisture；
- carbon/ecological variables。

Regression 比简单 land-cover classification 更能检验 foundation representation 是否保留 quantitative process information。

---

## 6. Time-series modeling

- crop/phenology；
- disturbance；
- gap filling；
- forecasting；
- event detection。

---

## 7. Foundation-model adaptation

按严格程度区分：

```text
frozen embedding + shallow model
linear probe
adapter / LoRA / PEFT
partial fine-tuning
full fine-tuning
```

比较结果时必须明确是哪一种。
