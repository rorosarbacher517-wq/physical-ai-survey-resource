# Fluids / Aerodynamics AI

## 1. Governing structure

Fluid dynamics 核心来自 mass/momentum/energy conservation。

不可压 Navier–Stokes 概念形式：

```text
∂u/∂t + u·∇u = -∇p/ρ + ν∇²u + f
∇·u = 0
```

---

## 2. AI task

- CFD surrogate；
- flow-field reconstruction；
- turbulence closure；
- aerodynamic coefficient prediction；
- inverse parameter/geometry；
- flow control；
- mesh acceleration。

---

## 3. Representation

- structured grid `[B,C,H,W]` / `[B,C,D,H,W]`；
- unstructured mesh graph；
- point cloud/surface mesh；
- spectral coefficients。

---

## 4. Neural Operator

适合 parameter/initial/boundary condition → field solution。

应测试：
- geometry OOD；
- Reynolds-number OOD；
- resolution transfer；
- conservation；
- force/drag integrated quantities。

---

## 5. Turbulence closure

```text
resolved solver
+ learned subgrid/Reynolds-stress closure
→ rollout
```

offline stress prediction 好不等于 coupled CFD stable。

---

## 6. Control

流场 state estimation + differentiable/RL control 可用于 drag reduction、mixing 等。

需要 safety/stability constraint，而不是只优化 reward。

## Sources

- Brunton, Noack & Koumoutsakos, machine learning for fluid mechanics review.
- FNO/operator-learning literature。
