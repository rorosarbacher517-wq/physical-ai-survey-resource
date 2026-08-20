# 00 · 数学、物理与数值基础

这一层回答一个最基本的问题：**Scientific AI 里的 tensor、loss、PDE、solver、observation operator 到底在数学上是什么。**

如果这层不扎实，后面很容易出现两个问题：一是只会背模型；二是无法判断一个 physics constraint、forecast rollout 或 inverse problem 为什么有效/失效。

## 1. 核心知识图

```text
Linear Algebra
├─ vector / matrix / tensor
├─ eigen / SVD / low rank
└─ linear operator

Probability / Statistics
├─ random variable / distribution
├─ likelihood / prior / posterior
├─ covariance / correlation
└─ uncertainty / calibration

Optimization
├─ gradient / Jacobian / Hessian
├─ SGD / AdamW
├─ constrained optimization
└─ conditioning

Dynamical Systems / PDE
├─ state / tendency / forcing
├─ ODE / PDE
├─ conservation law
└─ boundary / initial condition

Numerical Methods
├─ discretization
├─ interpolation / integration
├─ finite difference / volume / element / spectral
└─ consistency / stability / convergence

Scale / Support
├─ spatial resolution
├─ temporal resolution
├─ observation support
└─ validation support
```

## 2. 为什么 Earth AI 特别需要这些基础

### Remote sensing
一个 raster 可以写成 `X ∈ R^(C×H×W)`，但每个 channel 对应的物理意义、单位、空间响应和 noise model 不一样。

### Weather
大气状态不是 RGB image，而是多变量、多层、球面上的 field：

```text
X ∈ R^(C × L × H × W)
```

其中 `L` 可能是 pressure/model levels。

### Carbon flux
塔观测常见关系可写成：

```text
NEE = RECO - GPP
```

但同时还需要 observation support：

```text
Y_t = Σ_i w_{i,t} F_{i,t} + ε_t
```

这里真正重要的是 `w_{i,t}` 表示什么，而不只是公式本身。

## 3. 推荐学习顺序

1. [Linear Algebra / Probability / Optimization](linear-algebra-probability-optimization.md)
2. [Dynamical Systems / ODE / PDE](dynamical-systems-pde.md)
3. [Numerical Methods](numerical-methods.md)
4. [Dimensional Analysis / Scale / Support](dimensional-analysis-scale-support.md)

## 4. 学完后应该能回答

- 为什么 matrix 可以表示 derivative、interpolation 或 observation operator？
- covariance 为什么是 Data Assimilation 的核心？
- PDE residual 小是否等于解一定正确？
- discretization error 与 model error 有什么区别？
- 30 m output resolution 与 30 m validation support 为什么不是同一件事？
- 为什么 autoregressive rollout 会累积误差？

## 5. Sources

- Gilbert Strang, *Linear Algebra and Learning from Data*.
- Steven L. Brunton & J. Nathan Kutz, *Data-Driven Science and Engineering*.
- Randall J. LeVeque, *Finite Volume Methods for Hyperbolic Problems*.
- Goodfellow, Bengio & Courville, *Deep Learning*: https://www.deeplearningbook.org/

这些来源用于稳定基础；Earth-domain 具体观测物理在各专题页引用对应 primary sources。
