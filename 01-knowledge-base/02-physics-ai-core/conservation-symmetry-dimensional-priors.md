# Conservation、Symmetry 与 Dimensional Priors

## 1. Conservation

典型 conservation law：

```text
∂q/∂t + ∇·F = S
```

可用于：mass、momentum、energy、water、carbon 等。

### 在 AI 中怎么用
- soft penalty；
- conservative architecture；
- projection；
- flux-form prediction；
- residual correction；
- evaluation diagnostic。

---

## 2. Balance constraint

碳通量常用：

```text
NEE = RECO - GPP
```

如果同时预测三者，可定义：

```text
L_balance = ||NEE_hat - (RECO_hat-GPP_hat)||²
```

但前提是：
- sign convention 一致；
- units 一致；
- target definitions 一致。

---

## 3. Symmetry / Equivariance

如果 transformation `g` 作用在输入上，模型满足：

```text
f(gx) = g f(x)
```

则称为 equivariant（具体定义依 representation 而异）。

常见：
- translation；
- rotation；
- permutation；
- graph/node symmetry。

---

## 4. Dimensional priors

有物理单位的模型应检查：
- nondimensionalization；
- scale separation；
- unit conversion；
- parameter range；
- physically valid bounds。

### Positivity / bounds
例如 concentration、variance、probability 某些情况下必须非负，可用：
- `softplus`；
- bounded transform；
- projection。

---

## 5. 软约束不是越多越好

如果 physics relation 本身：
- 只在某 regime 成立；
- observation definition 与理论变量不同；
- 数据 uncertainty 很高；
- 系数不确定；

过强 constraint 可能降低真实数据适配能力。

## Sources

- Karniadakis et al. (2021), physics-informed machine learning review, Nature Reviews Physics.
- Bronstein et al. (2021), *Geometric Deep Learning*: https://arxiv.org/abs/2104.13478
