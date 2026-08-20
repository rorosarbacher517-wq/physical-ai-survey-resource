# Audit & Update Policy · 知识审核与更新规则

## 1. 三种知识生命周期

### Stable fundamentals
包括数学、概率、优化、PDE、numerical methods、Bayesian inference 等。更新频率低，重点是准确性和教学清晰度。

### Evolving methods
包括 neural operators、PINN training、multimodal fusion、foundation-model adaptation、hybrid solvers 等。方法会演化，但基本问题相对稳定。

### Fast-moving systems
包括 operational AI weather、最新 EO foundation model、model version、official service、benchmark release。必须带具体日期。

---

## 2. 来源优先级

1. original paper / DOI / publisher / arXiv / OpenReview；
2. official project page / institutional page；
3. official GitHub / model card / dataset provider；
4. author-maintained project page；
5. trusted bibliographic database；
6. secondary article 只用于发现，不单独支持核心事实。

---

## 3. 内容语言

- explanation：中文；
- model / paper / dataset / code / metric / variable / equation：英文或原始形式；
- 首次出现可用 `中文解释（English term）`；
- 不强行翻译专业缩写。

---

## 4. 事实与解释分开

### Source-stated fact
来源明确声明的事实，如发布日期、输入变量、grid、training data、operational status。

### Repository synthesis
本知识库根据多来源形成的结构化总结，例如“ready-made geospatial embedding product 与 downloadable encoder 的使用接口不同”。

### Interpretation
需要推理的判断必须写清这是 interpretation，不写成来源原话。

### Unknown
公开资料没有说明的内部实现：`unknown / not publicly disclosed`。

---

## 5. Remote Sensing 特殊规则

任何精度或模型比较至少检查：
- sensor / modality；
- native spatial resolution；
- spectral/polarization/geometry；
- temporal sampling；
- preprocessing / resampling；
- label support；
- region split；
- downstream task；
- frozen / linear probe / PEFT / full fine-tune。

不能因为 model output 为 10 m/30 m 就声称“10 m/30 m ground-truth accuracy”。

---

## 6. Carbon-flux 特殊规则

- 区分 measured/processed `NEE` 与 partitioned `GPP/RECO`；
- 明确 sign convention；
- EC tower 不是 point support；
- footprint 用作 predictor weighting、output observation operator、disaggregation、representativeness analysis 或 feature 时必须区分；
- random half-hour/day split 不能代替 site-blocked generalization；
- tower-scale accuracy 不自动验证 fine-resolution flux map；
- feature importance 不自动证明 process causality。

---

## 7. Weather / Climate 特殊规则

每个 forecast claim 必须配套：
- initialization / analysis source；
- forecast lead；
- variable；
- vertical level；
- grid/resolution；
- deterministic / ensemble；
- verification reference；
- metric；
- operational / research status。

`ERA5 hindcast skill`、`operational analysis-initialized forecast`、`real-time service` 不能混为同一种证据。

---

## 8. Foundation-model 特殊规则

至少区分：
- pretraining modality；
- pretrained weights vs hosted embeddings；
- spatial/temporal coverage；
- frozen encoder / linear probe / PEFT / full FT；
- label efficiency；
- geographic leakage；
- temporal leakage；
- task mismatch；
- process-sensitive regression vs simple classification。

“foundation model”不是自动优于 task-specific supervised model 的保证。

---

## 9. 时间基线

本仓库当前 fast-moving cutoff：**2026-08-20**。

新增 2026-08-20 之后的信息时：
1. 先进入 dated snapshot；
2. 验证 primary/official source；
3. 只有当知识已经稳定后，才写入 stable concept pages。

---

## 10. CI / audit

内容更新后必须运行：

```bash
python -m scripts.full_check
python -m scripts.verify_external_links --respect-cache --report
```

不通过时不标记 phase `PASS`，也不通过删除规则、跳过检查或修改 schema 来掩盖失败。
