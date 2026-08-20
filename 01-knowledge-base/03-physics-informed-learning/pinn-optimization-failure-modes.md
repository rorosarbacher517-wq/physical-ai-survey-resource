# PINN Optimization 与 Failure Modes

PINN 最大问题往往不是 formula，而是 optimization。

## 1. Loss imbalance

```text
L = λ_data L_data + λ_pde L_pde + λ_bc L_bc
```

三个 loss 数值相近，不代表 gradient contribution 相近。

检查：
- `||∇L_data||`；
- `||∇L_pde||`；
- `||∇L_bc||`；
- per-variable scale。

可尝试 dynamic weighting、gradient balancing，但不能把 weighting 当作 universal fix。

---

## 2. Spectral bias

标准 neural network 通常更容易先学习低频 smooth component，高频或 sharp gradient 更难。

影响：
- multiscale PDE；
- turbulence；
- wave/high-frequency solution；
- boundary layer。

可用 Fourier features、multi-scale network、domain decomposition 等缓解。

---

## 3. Stiffness

不同时间/空间尺度相差很大时，PDE 与 optimization 都可能 stiff。

表现：
- loss 降不动；
- 某一项先满足、另一项长期不满足；
- gradient magnitude 极不平衡。

---

## 4. Long-time domain

直接在很长时间域上拟合可能失败。

策略：
- time marching；
- causal training；
- sequential windows；
- curriculum。

---

## 5. Boundary / discontinuity

shock、contact discontinuity、sharp front 会让 smooth network 很难表示。

需要考虑：
- weak formulation；
- domain decomposition；
- shock-aware sampling；
- conservative discretization/hybrid solver。

---

## 6. Inverse parameter failure

即使 state fit 很好，parameter 也可能错，因为：
- observations insufficient；
- parameter compensation；
- noise；
- model discrepancy；
- wrong boundary condition。

因此 inverse PINN 必须报告 parameter uncertainty/sensitivity。

---

## 7. 诊断顺序

```text
units/normalization
→ BC/IC
→ residual distribution
→ gradient balance
→ sampling
→ spectral content
→ long-time stability
→ identifiability
```

## Sources

- Wang, Teng & Perdikaris, gradient-pathology work on PINNs.
- Krishnapriyan et al. (2021), *Characterizing possible failure modes in physics-informed neural networks*.
