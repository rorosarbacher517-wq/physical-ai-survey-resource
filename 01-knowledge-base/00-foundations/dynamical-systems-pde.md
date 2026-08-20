# Dynamical Systems、ODE 与 PDE

## 1. 从 state 开始

一个动态系统可以写成：

```text
dx/dt = f(x,t,u,θ)
```

- `x`：system state；
- `u`：external forcing / control；
- `θ`：parameters；
- `f`：dynamics。

离散时间形式：

```text
x_{t+1} = F(x_t, u_t)
```

这与 autoregressive weather model、生态时序模型、world model 的结构直接对应。

---

## 2. PDE 为什么重要

很多自然系统不仅随时间变化，还在空间中 transport / diffuse / interact。

### Advection

```text
∂u/∂t + v·∇u = 0
```

描述 quantity 被 flow 搬运。

### Diffusion

```text
∂u/∂t = κ∇²u
```

描述 gradient 被平滑。

### Conservation law

```text
∂q/∂t + ∇·F(q) = S
```

其中：
- `q`：conserved quantity；
- `F`：flux；
- `S`：source/sink。

weather、fluid、water/energy/carbon balance 都可看到类似结构。

---

## 3. Initial / Boundary Conditions

PDE 不只是方程本身，还需要：
- initial condition；
- Dirichlet boundary；
- Neumann boundary；
- periodic boundary；
- physical constraints。

PINN 常见失败之一就是“residual 看起来小，但 BC/IC 没真正满足”。

---

## 4. Stability 与 chaotic dynamics

### Linearized dynamics

在参考状态附近：

```text
δx_{t+1} ≈ J_F(x_t) δx_t
```

误差是否增长由 local Jacobian 和 system dynamics 决定。

### Weather 的意义

大气具有 chaotic behavior，initial-condition uncertainty 会随 lead time 增长。因此：
- deterministic forecast 不能表达全部 uncertainty；
- ensemble / probabilistic forecast 很重要；
- rollout stability 不能只看 one-step loss。

---

## 5. Discrete model 与 continuous system

神经网络通常训练在离散数据上：

```text
x_t → x_{t+Δt}
```

但它隐含近似的是连续 dynamics。需要区分：
- physical timestep；
- data sampling interval；
- model rollout step；
- solver timestep。

这四个量不一定相同。

---

## 6. Scientific AI 的三种典型任务

### Forward problem
已知 state/parameter，预测未来或场。

### Inverse problem
从 observation 反推 hidden state / parameter。

### System identification
从数据学习 dynamics `F` 或参数结构。

---

## Sources

- Steven L. Brunton & J. Nathan Kutz, *Data-Driven Science and Engineering*.
- Randall J. LeVeque, *Finite Volume Methods for Hyperbolic Problems*.
- Lorenz (1963), *Deterministic Nonperiodic Flow*.
