# Knowledge-unit Standard · 知识单元统一写作规范

> 目标：像多模态知识库一样，让每个知识点既能从概念讲到实现，也能回到科学问题和来源。

## 1. 语言规则

### 用中文解释
适合中文：
- 概念解释；
- 为什么；
- 方法比较；
- scientific meaning；
- failure modes；
- 学习提示；
- 研究问题。

### 保留英文
以下内容原则上不翻译或首次中英并列后保留英文：
- model / architecture：`Transformer`, `GraphCast`, `FNO`, `U-Net`；
- dataset/product：`ERA5`, `HLS`, `FLUXNET`, `SMAP`；
- variable：`GPP`, `NEE`, `RECO`, `VPD`, `Z500`；
- paper title；
- code/API/library：`PyTorch`, `JAX`, `xarray`, `Dask`；
- tensor shape：`[B,T,C,H,W]`；
- mathematical notation；
- 标准 metric：`RMSE`, `CRPS`, `ACC`, `AUROC`。

不要为了“全中文”创造不常用的中文模型名。

---

## 2. 一个完整知识单元的结构

### A. 这是什么
用 2–5 句话说明问题、对象、使用场景。

### B. Scientific / physical problem
写清：
- latent state；
- target；
- governing process；
- spatial scale；
- temporal scale。

### C. Observation model
优先写成：

```text
state x
→ physical/sensor process
→ observation operator H
→ y = H(x) + ε
```

说明 `H` 是否包含：radiative transfer、footprint、interpolation、retrieval、instrument response、sampling 等。

### D. 输入 / 输出 / shape / unit
示例：

```text
EO sequence:   X  [B,T,C,H,W]
meteorology:   M  [B,T,P]
footprint:     W  [B,T,H,W]
pixel flux:    F  [B,T,K,H,W]
tower target:  Y  [B,T,K]
```

同时写单位和 mask 语义。

### E. 数学核心
给出最重要的 1–5 个公式；解释变量，而不是只贴公式。

### F. Architecture / algorithm
说明每个模块解决什么问题：

```text
encoder → fusion → dynamics/operator → decoder → observation mapping
```

### G. Training
至少写：
- supervision；
- loss；
- sampling；
- normalization；
- augmentation；
- missing data / mask；
- split；
- optimization。

### H. Inference / rollout
说明是否 autoregressive、是否需要 initial condition、是否需要 external forcing、是否生成 ensemble。

### I. Compute / memory
关键问题：
- complexity；
- token/grid count；
- spatial vs temporal memory；
- mixed precision；
- distributed strategy；
- rollout cost。

### J. Evaluation
至少区分：
- interpolation / IID；
- temporal OOD；
- spatial/site/region OOD；
- climate/biome/regime OOD；
- extreme events；
- deterministic vs probabilistic；
- physical consistency；
- calibration；
- scale/support consistency。

### K. Failure modes
不要只写“缺点”，要写**为什么失败**。

### L. 与其他知识点的关系
明确 prerequisites 和 next steps。

### M. Sources
分三类：

```text
Primary source        原论文 / DOI / official project
Official implementation  官方 repo / model card / dataset provider
Repository synthesis  本知识库基于多来源形成的结构化解释
```

---

## 3. 事实强度

### Confirmed
原论文或官方来源明确写出。

### Repository synthesis
不是某一篇论文的原句，而是基于多来源得到的结构化总结。

### Implementation inference
根据公开 code 明确可读出的实现推断；需要注明这是 code-level inference。

### Unknown
公开信息不足时直接写：

`unknown / not publicly disclosed`

不根据 blog 截图、营销图或 secondary summary 补架构细节。

---

## 4. Earth AI 的额外检查

### Remote sensing
- native sensor resolution；
- spectral response / polarization / geometry；
- atmosphere / BRDF / speckle / emissivity；
- reprojection / resampling；
- temporal revisit；
- cloud/missingness；
- label support。

### Carbon flux
- EC measurement support；
- GPP/RECO partitioning；
- sign convention；
- footprint mapping；
- site-blocked split；
- climate/biome OOD；
- tower-to-grid validation gap。

### Weather/climate
- analysis/reanalysis vs observation；
- forecast initial condition；
- vertical coordinate/levels；
- deterministic vs probabilistic；
- lead time；
- rollout cadence；
- verification reference；
- coupled components；
- climate distribution shift。

---

## 5. 最终标准

一页知识点写完后，读者应该能够回答：

> **它在解决什么科学问题？数据从哪里来？shape 怎么变？物理在哪里？模型怎么训练？推理怎么跑？什么时候会失败？怎么公平评测？原始来源是什么？**
