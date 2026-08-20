# Numerical Methods · 从连续方程到可计算问题

## 1. 为什么 AI 研究者也必须懂 numerical methods

如果 physical process 由 PDE/ODE 描述，真实计算通常是：

```text
continuous equation
→ discretization
→ finite-dimensional state
→ numerical solver
→ approximate solution
```

AI 学到的往往不只是“physics”，还可能包含 numerical scheme、grid、analysis/reanalysis bias 和 solver artifacts。

---

## 2. 基本离散化

### Finite Difference

一阶导近似：

```text
f'(x) ≈ [f(x+h)-f(x)] / h
```

二阶中心差分：

```text
f''(x) ≈ [f(x+h)-2f(x)+f(x-h)] / h²
```

### Finite Volume

在 control volume 上保证 flux balance，特别适合 conservation laws。

### Finite Element

用 basis functions 在复杂 geometry 上近似 solution。

### Spectral Methods

在 global basis（如 Fourier / spherical harmonics）中表示 field，对 smooth global fields 很有效。

---

## 3. 三个核心概念

### Consistency
离散方程在 grid refinement 下是否逼近原方程？

### Stability
数值误差是否会失控增长？

### Convergence
grid/timestep 变细时 numerical solution 是否逼近 true solution？

AI surrogate 也应考虑类似问题：不同 resolution、timestep、rollout length 下是否稳定。

---

## 4. Interpolation / Resampling 不是中性操作

Earth AI 经常做：
- nearest neighbor；
- bilinear；
- cubic；
- area-weighted aggregation；
- conservative remapping。

不同方法改变的是数据的 mathematical meaning。

例如 land-cover class 不适合直接 bilinear；precipitation accumulation 与 reflectance 的重采样语义也不同。

---

## 5. Numerical integration

### Explicit Euler

```text
x_{n+1} = x_n + Δt f(x_n)
```

简单但 stability constraint 强。

### Runge–Kutta
通过多次 slope evaluation 提高精度。

### Implicit methods
适合 stiff systems，但每步可能需要求解 nonlinear/linear system。

---

## 6. 与 AI 的连接

- Neural Operator：学习 function-to-function mapping；
- surrogate：替代 expensive solver；
- learned closure：学习 unresolved process；
- differentiable solver：允许 gradient 穿过 simulator；
- weather AI：学习 analysis state 到未来 state 的离散 flow map。

## Sources

- LeVeque, *Finite Volume Methods for Hyperbolic Problems*.
- Trefethen, *Spectral Methods in MATLAB*.
- Hairer, Nørsett & Wanner, *Solving Ordinary Differential Equations I*.
