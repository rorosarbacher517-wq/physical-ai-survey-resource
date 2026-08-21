# State Estimation & Sensor Fusion

## 1. 为什么需要 estimator

真实机器人通常不能直接观测完整 state：

```text
x_t = {robot pose, velocity, object states, contacts, map, ...}
o_t = sensor measurements
```

Estimator 的任务是：

```text
history(o,a) → belief / state estimate
```

---

## 2. Bayesian filtering

预测：

```text
p(x_t|o_1:t-1) = ∫ p(x_t|x_{t-1},a_{t-1}) p(x_{t-1}|o_1:t-1) dx
```

更新：

```text
p(x_t|o_1:t) ∝ p(o_t|x_t) p(x_t|o_1:t-1)
```

这和 weather Data Assimilation 的核心结构一致：dynamics prior + observation likelihood → updated state。

---

## 3. Kalman-family intuition

Linear Gaussian model：

```text
x_t = A x_{t-1} + B a_{t-1} + ε
o_t = H x_t + η
```

其中：
- `A/B` 描述 dynamics/control；
- `H` 是 observation mapping；
- process noise 与 observation noise 决定更新权重。

Nonlinear robotics 常见 EKF/UKF 或 factor-graph methods。

---

## 4. SLAM

SLAM 同时估计 robot pose 与 map：

```text
sensor observations
+ motion constraints
+ loop closure
→ trajectory + map
```

典型信息源：
- camera；
- LiDAR；
- IMU；
- wheel odometry；
- GPS/RTK（室外）；
- learned features。

视觉/惯性融合常见原因是 camera 提供 rich geometry/appearance，而 IMU 提供高频 motion information，但各自都有 drift/ambiguity。

---

## 5. Factor graph

把 state variables 与 measurements/constraints 表示成 graph：

```text
state nodes: x_0, x_1, ...
factors: odometry, IMU, visual match, loop closure, prior
```

优化目标通常是多个 residual 的加权和。

这一思想与 Scientific AI 的 multi-observation inverse problem 很接近。

---

## 6. Learned state estimation

可以学习：
- visual odometry；
- depth/pose feature；
- latent filter；
- object state tracker；
- end-to-end history encoder。

但 learned estimator 仍需回答：
- uncertainty 是否 calibrated；
- OOD motion/lighting 是否稳定；
- drift 是否积累；
- failure 是否可检测；
- downstream controller 对 estimate error 多敏感。

---

## 7. Tensor view

```text
camera feature:    [B,T,V,D]
IMU:               [B,T,6]
proprioception:    [B,T,Ds]
latent state:      [B,T,Dz]
covariance:        [B,T,Dx,Dx]  # explicit estimator example
```

异步传感器不能只按 array index 对齐，应根据 timestamp 与 interpolation/integration rule 对齐。

---

## 8. Failure modes

- observability 不足；
- IMU bias 未建模；
- loop closure false positive；
- dynamic objects 被错误当 static map；
- learned features 在新场景失效；
- covariance 低估导致 estimator 过度相信错误信息；
- calibration/time-sync drift。

## Cross-links

- [Data Assimilation](../../10-data-assimilation-inverse-uq/data-assimilation.md)
- [Uncertainty / Calibration](../../10-data-assimilation-inverse-uq/uncertainty-calibration.md)
- [Observation Operators](../../02-physics-ai-core/observation-operators.md)

## Sources

- GTSAM documentation: https://gtsam.org/
- ROS robot_localization docs: https://docs.ros.org/en/ros2_packages/rolling/api/robot_localization/
