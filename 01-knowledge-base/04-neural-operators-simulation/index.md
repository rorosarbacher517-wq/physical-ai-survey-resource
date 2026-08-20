# 04 · Neural Operators、Surrogates 与 Differentiable Simulation

如果任务不是“给一个 coordinate 求一个 solution value”，而是 repeatedly 学习：

```text
input field/function → output field/function
```

Neural Operator 往往比 pointwise PINN 更自然。

## 1. Operator learning

传统 neural network：

```text
R^n → R^m
```

Neural Operator 试图学习：

```text
G: function space → function space
```

例如：

```text
initial condition field
→ future PDE solution field
```

---

## 2. 代表方法

### DeepONet
用 branch net 表示 input function，用 trunk net 表示 query location。

### FNO
在 Fourier space 学 global convolution/operator mapping。

### Graph / Mesh Operator
在 irregular mesh 上做 message passing/operator approximation。

---

## 3. 与 surrogate 的关系

Neural Operator 是 surrogate modeling 的一个重要分支，但 surrogate 不一定是 operator。一个 MLP 也可以做 parameter-to-scalar surrogate。

---

## 4. Differentiable Simulation

如果 solver 可微：

```text
θ → simulator → output → loss
```

gradient 可直接穿过 simulation，用于：
- parameter estimation；
- control；
- inverse design；
- learned parameterization。

---

## 5. 页面

- [Neural Operator Family](neural-operator-family.md)
- [Surrogates / Hybrid Solvers](surrogates-hybrid-solvers.md)
- [Differentiable Simulation](differentiable-simulation.md)

## Primary sources

- Lu et al., DeepONet: https://arxiv.org/abs/1910.03193
- Li et al., Fourier Neural Operator: https://arxiv.org/abs/2010.08895
