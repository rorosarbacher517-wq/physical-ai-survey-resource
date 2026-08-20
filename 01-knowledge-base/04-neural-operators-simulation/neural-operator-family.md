# Neural Operator Family

## 1. DeepONet

输入 function `u` 通过 branch net 编码；query coordinate `y` 通过 trunk net 编码：

```text
G(u)(y) ≈ Σ_k b_k(u) t_k(y)
```

适合 parameterized PDE/operator learning。

---

## 2. Fourier Neural Operator (FNO)

核心 layer 可概括为：

```text
v_{l+1}(x)=σ(Wv_l(x)+F^{-1}(R·F(v_l))(x))
```

`R` 学习 selected Fourier modes。

优势：
- global receptive field；
- grid field 高效；
- 可做 resolution transfer（但需实际验证）。

---

## 3. Graph / Mesh Operator

适合：
- unstructured mesh；
- adaptive geometry；
- sphere/icosahedral graph；
- irregular domains。

---

## 4. Resolution transfer 要谨慎

“operator 可以跨 resolution”不意味着：
- 任意 resolution 都同样准确；
- high-frequency detail 自动恢复；
- discretization change 没影响。

必须测试：
- train grid vs test grid；
- interpolation method；
- spectral truncation；
- conservation；
- boundary behavior。

---

## 5. Shape 示例

```text
input field:  [B,C_in,H,W]
latent:       [B,D,H,W]
output field: [B,C_out,H,W]
```

3D/atmosphere 可扩展到：

```text
[B,C,L,H,W]
```

---

## 6. 与 weather AI 的关系

`FourCastNet` 使用 spectral/operator-inspired computation，是 operator route 在 global weather 中的重要代表之一；但实际 weather system 还涉及 initial state、rollout、probabilistic uncertainty 与 verification。

## Sources

- DeepONet: https://arxiv.org/abs/1910.03193
- FNO: https://arxiv.org/abs/2010.08895
- FourCastNet: https://arxiv.org/abs/2202.11214
