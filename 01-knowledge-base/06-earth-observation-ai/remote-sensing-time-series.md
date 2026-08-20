# Remote-sensing Time-series Learning

## 1. EO time series 为什么特殊

它不是规则 video：
- revisit irregular；
- cloud missingness；
- multi-sensor cadence；
- seasonal cycle；
- geometry variation；
- disturbance/event abrupt change。

---

## 2. 输入设计

推荐显式保留：

```text
X      [B,T,C,H,W]
mask   [B,T,1,H,W] or [B,T]
time   [B,T,*]
sensor [B,T]
```

必要时还包括 sun/view geometry。

---

## 3. Temporal models

### RNN / GRU / LSTM
适合小样本和 compact sequence。

### Temporal CNN / TCN
高效 local temporal receptive field。

### Transformer
适合 long-range temporal interaction，但需要处理 missingness 和 token cost。

### State-space / continuous-time ideas
适合 irregular time gap 的某些场景。

---

## 4. Gap filling vs Forecasting

### Gap filling
利用前后 context 重建已发生但缺测的 observation。

### Forecasting
只允许使用 forecast origin 之前的信息。

若 gap-filling model 在训练/评测中使用 future observation，就不能把结果当 real forecast。

---

## 5. Phenology

seasonal vegetation dynamics 可用：
- DoY encoding；
- harmonic features；
- temporal attention；
- learned seasonal latent。

但 extreme/drought/disturbance 可能偏离正常 phenological cycle。

---

## 6. Evaluation

建议分别测：
- random missing；
- long cloud gaps；
- seasonal gaps；
- unseen year；
- unseen region；
- disturbance/extreme periods。
