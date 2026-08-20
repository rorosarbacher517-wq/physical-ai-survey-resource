# 03 · Physics-informed Learning

Physics-informed learning 的核心不是“加一个 physics loss”，而是把已知 equation、constraint、boundary condition 或 physical structure 放进 learning problem。

## 1. 典型 PINN 形式

设 PDE：

```text
N[u(x,t); λ] = 0
```

神经网络近似：

```text
u_θ(x,t) ≈ u(x,t)
```

通过 automatic differentiation 得到 derivative，并构造 residual：

```text
r_θ(x,t)=N[u_θ(x,t);λ]
```

典型 loss：

```text
L = λ_data L_data
  + λ_pde L_residual
  + λ_bc L_boundary
  + λ_ic L_initial
```

真正困难的是：**不同 loss 是否同尺度、collocation points 是否合理、PDE 是否 stiff、optimization 是否能同时满足多个目标。**

---

## 2. 适合什么问题

PINN 更自然适合：
- sparse observation + known PDE；
- inverse parameter estimation；
- moderately sized domains；
- differentiable equation residual；
- boundary/initial information 明确。

不一定适合：
- 大量高质量 simulator data 已存在；
- repeated field-to-field prediction；
- high-dimensional turbulent dynamics；
- very stiff / multiscale PDE；
- complex discontinuity/shock。

这些场景可能更适合 Neural Operator、surrogate、hybrid solver 或 learned closure。

---

## 3. Constraint 不只有 PDE

- conservation；
- positivity；
- monotonicity（仅在物理上确实成立时）；
- symmetry/equivariance；
- balance relationship；
- boundary/initial condition；
- constitutive relation。

---

## 4. 评测不能只看 RMSE

还要看：
- PDE residual on unseen points；
- BC/IC satisfaction；
- conservation error；
- parameter recovery；
- gradient/spectral behavior；
- long-horizon stability；
- OOD parameter regime。

## 页面
- [PINN Fundamentals](pinn-fundamentals.md)
- [PINN Optimization / Failure Modes](pinn-optimization-failure-modes.md)
- [Hard / Soft Constraints](hard-soft-constraints.md)

## Primary source

Raissi, Perdikaris & Karniadakis (2019), *Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations*, JCP: https://doi.org/10.1016/j.jcp.2018.10.045
