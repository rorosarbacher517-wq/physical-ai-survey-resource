# Evaluation 与 Benchmarking

## 1. Benchmark 的真正作用

一个 benchmark 应固定：

```text
data + preprocessing + split + task + metric + protocol
```

否则不同论文数字不具可比性。

---

## 2. Evaluation hierarchy

### IID / interpolation
测试基本拟合能力。

### Temporal OOD
unseen year / future period。

### Spatial OOD
unseen site/region/domain。

### Regime OOD
unseen climate/parameter/operating condition。

### Extreme
tail/event conditions。

### Physical
conservation、balance、spectrum、stability。

---

## 3. Paired ablation

比较一个 physics/module 是否有效时：

```text
same data
same split
same backbone
same optimizer
same random protocol
only change target component
```

然后在同一样本上比较 paired errors。

---

## 4. Statistical uncertainty

报告 mean metric 不够。可提供：
- bootstrap CI；
- site-level distribution；
- multiple seeds；
- paired significance / effect size；
- subgroup sample count。

---

## 5. Compute-normalized evaluation

同时记录：
- parameter count；
- FLOPs/estimated compute；
- training GPU hours；
- inference latency；
- ensemble member count；
- memory。

不同 compute scale 的 model 只比一个 RMSE 不完整。

---

## 6. Domain-specific benchmark

### EO
`PANGAEA` 等跨 sensor/task/geography benchmark。

### Weather
`WeatherBench 2` + operational verification protocols。

### Carbon
site-blocked / biome OOD + support-aware evaluation；目前仍缺统一覆盖 fine-scale footprint-aware carbon modeling 的公共 benchmark，这应明确写成 gap，而不是假装已有标准答案。

---

## 7. Reproducibility vs Replication

- rerun same code：reproducibility；
- independent implementation/data pipeline 得到相近结论：更强的 replication evidence。

仓库只有在实际运行 commands 并记录 outputs 后才能写“reproduced”。
