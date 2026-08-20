# PINN Fundamentals

## 1. Forward problem

已知 PDE 参数和条件，求 solution `u(x,t)`。

```text
(x,t)
→ neural network u_θ
→ automatic differentiation
→ PDE residual
→ optimize θ
```

### 输入/输出

```text
input:  [B,D_coord]
output: [B,D_state]
```

例如 2D transient field：

```text
input  [B,3] = [x,y,t]
output [B,K]
```

---

## 2. Inverse problem

不仅学习 `u_θ`，还学习 unknown physical parameter `λ`：

```text
min_{θ,λ} L_data + L_PDE
```

例如 diffusivity、reaction coefficient、material parameter。

关键问题是 **identifiability**：不同参数是否可能产生近似相同 observations？

---

## 3. Collocation points

PINN 通常需要：
- data points；
- interior collocation points；
- boundary points；
- initial-condition points。

采样可用：
- uniform/random；
- Latin Hypercube；
- adaptive residual sampling；
- domain decomposition。

---

## 4. Automatic differentiation

如果：

```text
u = network(x,t)
```

可通过 autograd 得到：

```text
∂u/∂t, ∂u/∂x, ∂²u/∂x² ...
```

但 higher-order derivatives 会增加 memory 与 numerical difficulty。

---

## 5. Normalization

坐标和变量尺度差异大时，training 会恶化。

建议明确：
- coordinate normalization；
- state normalization；
- derivative 如何恢复 physical scale；
- loss weights 是否随 units 改变。

---

## 6. PINN ≠ numerical solver 的免费替代

需要比较：
- accuracy；
- wall-clock；
- repeated-query cost；
- boundary complexity；
- parameter sweep；
- training instability。

## Sources

- Raissi et al. (2019): https://doi.org/10.1016/j.jcp.2018.10.045
- Karniadakis et al. (2021), *Physics-informed machine learning*, Nature Reviews Physics.
