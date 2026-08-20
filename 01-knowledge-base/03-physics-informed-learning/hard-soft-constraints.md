# Hard Constraints 与 Soft Constraints

## 1. Soft constraint

把 physics violation 放进 loss：

```text
L = L_data + λ L_physics
```

优点：实现简单、允许 noisy/inexact physics。

缺点：
- constraint 不保证严格满足；
- λ 很敏感；
- gradient 冲突。

---

## 2. Hard parameterization

通过 output construction 直接保证 constraint。

例如 positivity：

```text
y = softplus(z)
```

boundary condition 也可通过特定 parameterization 强制满足。

---

## 3. Projection

先预测 unconstrained state：

```text
x_raw = f_θ(z)
```

再投影到可行集合：

```text
x = P_C(x_raw)
```

适用于某些 conservation / geometry constraints。

---

## 4. Constraint layer / conservative formulation

让网络输出 flux 而非直接输出 state，再通过 divergence/update 构造 conserved field，是更结构化的方法。

---

## 5. 什么时候不要 hard constraint

如果关系：
- 只是 approximate；
- target 有 measurement bias；
- process model 有结构误差；
- regime-dependent；

hard constraint 可能把模型强行压到错误 manifold。

---

## 6. Carbon 示例

如果 dataset convention 是：

```text
NEE = RECO - GPP
```

可以：
- soft balance loss；
- 只预测 GPP/RECO，再计算 NEE；
- 预测三者后 projection。

三种方法的 flexibility 与 consistency 不同。
