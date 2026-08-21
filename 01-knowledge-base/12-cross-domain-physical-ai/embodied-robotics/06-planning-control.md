# Planning & Control

## 1. 不要把 planning 和 control 混成一个概念

### Task planning
决定“做什么”：

```text
open drawer
→ grasp cup
→ move cup
→ place cup
```

### Motion planning
决定 robot configuration 如何从 A 到 B，同时满足 collision/kinematic constraints。

### Control
在真实 dynamics 下跟踪 target trajectory / pose / force。

实际机器人通常是 hierarchy：

```text
language goal
→ task/subgoal
→ motion target
→ trajectory
→ low-level controller
→ actuator
```

---

## 2. Classical planning 仍然重要

常见方法族：
- graph/search；
- sampling-based motion planning，如 RRT family；
- trajectory optimization；
- constrained optimization；
- Model Predictive Control (MPC)。

Learned policy 并不自动替代 collision checking、kinematic feasibility 或 hard safety constraints。

---

## 3. MPC

一般形式：

```text
min_{a_t:t+H} Σ cost(x_k,a_k)
subject to x_{k+1}=f(x_k,a_k)
           constraints(x_k,a_k) ≤ 0
```

只执行优化序列的一小段，然后重新观测和优化。

优点：持续 feedback；缺点：依赖 model、solver 与 latency。

如果 `f` 是 learned world model，就形成 learned-model MPC。

---

## 4. Feedback control

### PID
适合很多 low-level tracking 问题。

### Operational-space / Cartesian control
在 end-effector space 控 pose/wrench。

### Impedance control
让 robot 对接触具有 compliance，而不是只强制位置跟踪。

### Whole-body control
同时满足 balance、contact、joint limit、end-effector task 等多个约束。

VLA 通常不会直接取代这些所有层；很多系统是 VLA 输出 target/action chunk，再由 lower-level controller 执行。

---

## 5. Planning with foundation models

VLM/LLM/embodied reasoning model 可用于：
- object/task semantic understanding；
- subgoal decomposition；
- tool selection；
- code/API calling；
- success/failure interpretation。

但语言上合理的 plan 仍可能：
- kinematically infeasible；
- collide；
- require unknown force；
- violate balance；
- use an unavailable tool。

因此需要 geometry/dynamics/safety layer 做 grounding。

---

## 6. Replanning 与 failure recovery

真实环境中 open-loop trajectory 很容易失效。需要：

```text
execute
→ observe progress
→ detect deviation/failure
→ update state
→ replan / retry / request help
```

这也是 embodied agent 与普通 static QA 的关键区别。

---

## 7. Metrics

- planning success；
- path length/time；
- constraint violation；
- collision rate；
- control tracking error；
- energy/torque；
- completion time；
- replanning frequency；
- recovery success；
- real-time latency。

## Sources

- OMPL documentation: https://ompl.kavrakilab.org/
- Modern Robotics: https://modernrobotics.northwestern.edu/
- MuJoCo documentation: https://mujoco.readthedocs.io/
