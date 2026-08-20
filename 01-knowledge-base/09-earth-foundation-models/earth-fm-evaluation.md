# Earth Foundation Model Evaluation

## 1. 先区分 adaptation protocol

```text
frozen embedding + classical model
linear probe
MLP head
adapter / LoRA / PEFT
partial fine-tuning
full fine-tuning
```

protocol 不同，performance 不应直接横比。

---

## 2. Label efficiency curve

foundation model 的价值之一是 low-label regime：

```text
1% labels
5%
10%
50%
100%
```

应与从头训练 supervised baseline 比曲线，而不是只比 full-data endpoint。

---

## 3. Geographic OOD

建议：
- train continents / test continent；
- biome holdout；
- country/region holdout；
- spatial block。

如果 pretraining 已覆盖 test region，需要明确这是 representation transfer，而不是“never-seen geography”。

---

## 4. Temporal OOD

- unseen year；
- future period；
- disturbance year；
- climate anomaly year。

annual embedding product 还要注意 input year 与 label year 是否一致。

---

## 5. Sensor OOD

一个 optical-pretrained model 不应在未测试情况下声称能自然 transfer 到 SAR/hyperspectral。

multimodal FM 也要报告缺失 modality 时性能。

---

## 6. Task hierarchy

从较容易到更 process-sensitive：

```text
scene classification
→ segmentation
→ object/change mapping
→ biophysical regression
→ flux/process prediction
→ dynamical forecasting
```

后面的任务对 continuous/physical information 保留要求更高。

---

## 7. PANGAEA

`PANGAEA` 的意义在于统一：
- datasets；
- tasks；
- sensors；
- resolutions；
- geography；
- evaluation protocols。

公开结果提醒：geospatial FMs 在所有 downstream conditions 上并不稳定超过 supervised baselines，因此 baseline 不能省略。

Sources:
- https://arxiv.org/abs/2412.04204
- https://github.com/yurujaja/pangaea-bench

---

## 8. Embedding-as-data 的额外评测

`AlphaEarth/TESSERA` 这类 embedding products 应比较：
- embedding + RF/XGBoost/MLP；
- raw EO + same downstream model；
- task-specific handcrafted features；
- different embedding dimensions；
- storage/I/O cost；
- year mismatch。

---

## 9. Carbon / weather transfer

### Carbon
site-blocked、biome/climate OOD、quantitative GPP/NEE regression、footprint support。

### Weather
forecast rollout 与 DA problem 并不是普通 static embedding benchmark，应使用 weather-specific verification。
