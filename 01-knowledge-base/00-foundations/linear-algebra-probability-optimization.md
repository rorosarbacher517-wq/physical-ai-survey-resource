# Linear Algebra、Probability 与 Optimization

## 1. Linear Algebra：Scientific AI 的表示语言

Scientific data 往往是连续场离散后的 vector / matrix / tensor。

```text
scalar:      一个点的 temperature
vector:      wind [u,v,w]
matrix:      2D raster [H,W]
tensor:      [T,C,H,W]
weather:     [T,C,L,H,W]
point cloud: [N,D]
```

### Dot product

```text
x · y = Σ_i x_i y_i
```

常见意义：
- projection / similarity；
- attention score；
- energy-like contraction；
- weighted spatial aggregation。

### Matrix multiplication

若 `A ∈ R^(m×n)`，`x ∈ R^n`：

```text
Ax ∈ R^m
```

在 scientific computing 中，`A` 可以表示：
- derivative operator；
- interpolation operator；
- diffusion operator；
- graph propagation；
- observation operator。

### Eigen decomposition

```text
A v = λ v
```

`λ` 与 `v` 描述系统 characteristic modes。可联系：
- PCA / EOF；
- linear stability；
- graph Laplacian；
- spectral PDE methods。

### SVD

```text
X = U Σ V^T
```

用途：low-rank approximation、reduced-order modeling、compression、effective rank diagnostics。

---

## 2. Probability：从 measurement noise 到 posterior

### Bayes rule

```text
p(x|y) ∝ p(y|x) p(x)
```

- `x`：latent state / parameter；
- `y`：observation；
- `p(x)`：prior；
- `p(y|x)`：likelihood；
- `p(x|y)`：posterior。

这就是 inverse problems 与 Data Assimilation 的统一语言之一。

### Covariance

```text
Cov(X,Y) = E[(X-E[X])(Y-E[Y])]
```

在 weather DA 中，covariance 决定一个 observation 如何影响未观测位置和相关变量。

### Spatial / temporal autocorrelation

Earth data 高度相关，因此 `N` 个样本不等于 `N` 个独立样本。随机切分相邻时间点或同一站点，常会高估 generalization。

---

## 3. Optimization

### Gradient descent

```text
θ_{k+1} = θ_k - η ∇_θ L(θ_k)
```

### Jacobian / Hessian

- Jacobian：多输出对多输入的一阶导；
- Hessian：二阶曲率。

它们在 differentiable simulation、inverse modeling、PINN conditioning 中尤其重要。

### Constrained optimization

```text
min f(θ)
subject to g(θ)=0
           h(θ)≤0
```

physics constraint 可以通过：
- penalty；
- Lagrange multiplier；
- projection；
- reparameterization；
- differentiable solver。

### Conditioning

如果输入微小扰动导致解大幅变化，问题是 ill-conditioned。典型来源：
- variables scale 差异过大；
- inverse problem 不可辨识；
- 多个 loss 梯度冲突；
- PDE stiffness；
- noisy observation。

---

## 4. Scientific AI 中最常见的误区

1. **normalize 后忘记单位。** 网络看到无量纲值，但物理约束仍可能要求真实单位。
2. **correlation 当 causality。** 高 covariance 不等于过程因果关系。
3. **样本数当独立信息量。** 空间/时间自相关会显著降低 effective sample size。
4. **AdamW 能解决所有优化问题。** optimizer 不能替代合理的 loss scaling 与 conditioning。

## 5. 必会推导/解释

- matrix multiplication shape；
- gradient/Jacobian/Hessian dimension；
- Bayes rule；
- covariance matrix；
- weighted mean；
- constrained objective；
- condition number 的直观意义。

## Sources

- Goodfellow, Bengio & Courville, *Deep Learning*: https://www.deeplearningbook.org/
- Tarantola, *Inverse Problem Theory and Methods for Model Parameter Estimation*.
- Evensen, *Data Assimilation: The Ensemble Kalman Filter*.
