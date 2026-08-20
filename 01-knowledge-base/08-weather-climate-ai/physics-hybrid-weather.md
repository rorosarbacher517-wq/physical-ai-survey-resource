# Physics–ML Hybrid Weather

## 1. 为什么 hybrid

传统 NWP 的 resolved dynamics 很成熟，但 subgrid physics、parameterizations 与 compute 仍是主要挑战。

Hybrid route：

```text
physical dynamical core
+ learned components
→ forecast/climate model
```

---

## 2. NeuralGCM

概念：

```text
spectral/differentiable dynamical core
+ neural parameterization
→ global atmospheric model
```

它可用于 medium-range weather 与 longer climate-like simulations。

Primary: https://doi.org/10.1038/s41586-024-07744-y

---

## 3. Learned parameterization

可学习：
- convection/cloud tendencies；
- radiation-like effects；
- precipitation/subgrid process；
- correction terms。

但 learned tendency 必须在 closed-loop model 中稳定，而不是只在 offline target 上准确。

---

## 4. Differentiability

如果 dynamical core 可微：
- end-to-end training；
- inverse parameter tuning；
- sensitivity；
- data assimilation integration

更容易实现。

但 chaotic long-horizon gradient 仍有困难。

---

## 5. 2026 precipitation extension

Google 2026 报告的 NeuralGCM precipitation extension 使用 satellite-based precipitation observations 帮助训练 learned physics，并强调 precipitation mean/extreme/daily-cycle representation。

Source: https://research.google/blog/neuralgcm-harnesses-ai-to-better-simulate-long-range-global-precipitation/

---

## 6. Hybrid 的评价维度

不仅看 weather RMSE：
- conservation/balance；
- precipitation distribution；
- spectrum；
- multi-year stability；
- forcing response；
- computational cost；
- parameterization interpretability。

---

## 7. Failure modes

- offline learned physics 在 coupled rollout unstable；
- neural closure compensates dynamical-core bias；
- training climate 之外 response 不合理；
- conservation violation；
- coarse-grid parameterization 无法 transfer 到 new resolution。
