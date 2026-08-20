# Differentiable Simulation

## 1. 基本思想

如果 simulator `S` 可微：

```text
x = S(θ)
L = L(x,y)
∂L/∂θ = ∂L/∂x · ∂S/∂θ
```

可直接做 gradient-based inverse / control / optimization。

---

## 2. Autodiff vs adjoint

### Automatic differentiation
记录 computation graph，直接反传。

### Adjoint method
对长时间 dynamics 更节省 memory 的经典 sensitivity 方法之一。

实际系统可能组合 checkpointing、custom VJP/JVP、adjoint。

---

## 3. 用途

- inverse parameter estimation；
- PDE-constrained optimization；
- optimal control；
- learned closure；
- differentiable rendering / radiative model；
- hybrid weather/climate models。

---

## 4. 难点

- chaotic system gradient 爆炸/失真；
- long rollout memory；
- discontinuous/non-differentiable operators；
- solver tolerance；
- implicit solve；
- gradient correctness。

---

## 5. 验证 gradient

不要只相信 autograd。可用：
- finite-difference check；
- manufactured solution；
- analytic gradient on toy problem；
- sensitivity sanity check。

## Earth example

`NeuralGCM` 展示了 differentiable dynamical core 与 learned components 组合用于 weather/climate 的代表路线：
https://www.nature.com/articles/s41586-024-07744-y
