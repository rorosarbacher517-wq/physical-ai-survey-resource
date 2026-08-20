# Embodied Physical AI / Robotics

> 这一模块讨论 AI 如何在真实物理环境中形成 **perception → state estimation → prediction → planning → control → action → feedback** 闭环。

它与 Scientific AI 的关系不是“另一个完全独立领域”。两者共享 observation model、dynamics、inverse/state estimation、uncertainty、simulation 与 optimization；区别主要在 system objective：Scientific AI 更常关注解释、反演、模拟与预测，Embodied AI 还必须把结果转成实时动作并承担 action-induced feedback 与 physical safety。

---

## 1. 从下到上的知识链

```text
Robot / Environment / Task
        ↓
Sensors & Observation Physics
RGB / Depth / LiDAR / Tactile / IMU / Proprioception / Force-Torque
        ↓
Geometry & 3D Representation
Coordinate Frames / Camera Model / SE(3) / Point / Voxel / BEV / Occupancy
        ↓
State Estimation
Filtering / Sensor Fusion / SLAM / Factor Graph
        ↓
Kinematics / Dynamics / Contact
q, dq, Jacobian, rigid-body dynamics, friction, constraints
        ↓
World Model / Physical Reasoning
state + action → future state / observation
        ↓
Planning / Control
Task Planning / Motion Planning / MPC / Whole-body / Impedance
        ↓
Robot Learning
Behavior Cloning / Imitation / Offline RL / Online RL / Generative Policy
        ↓
Vision-Language-Action / Robot Foundation Models
        ↓
Simulation / Synthetic Data / Sim-to-Real
        ↓
Evaluation / Safety / Deployment
        ↓
Real-world Feedback
```

---

## 2. 机器人为什么属于 Physical AI

机器人不是只做 visual recognition。执行一个真实任务至少涉及：

- **physical state**：机器人和环境当前状态是什么；
- **observation**：相机、LiDAR、IMU、tactile 等真正测到了什么；
- **geometry**：不同坐标系、深度、姿态、遮挡如何对应；
- **dynamics**：action 会怎样改变 robot/world state；
- **constraints**：关节范围、碰撞、接触、摩擦、稳定性、速度/力限制；
- **decision**：在不确定状态下选择什么 action；
- **feedback**：动作执行后重新观测并纠正。

因此 Physical AI 的机器人问题可以统一写成部分可观测闭环：

```text
hidden physical state x_t
        ↓  observation model h
observation o_t
        ↓  estimator / representation
belief or latent state z_t
        ↓  policy / planner
 action a_t
        ↓  dynamics f
state x_{t+1}
        ↓
new observation
```

---

## 3. 常见 tensor / representation

```text
single RGB image:       [B,C,H,W]
multi-camera RGB:       [B,V,C,H,W]
video / observation:    [B,T,V,C,H,W]
depth:                  [B,T,V,1,H,W]
point cloud:            [B,T,N,Cp]
robot state:            [B,T,Ds]
action:                 [B,T,Da]
tactile image:          [B,T,S,C,H,W]
force/torque:            [B,T,6]
occupancy / voxel:       [B,C,X,Y,Z]
BEV feature:             [B,C,H,W]
```

`B,T,V,S,N` 分别可表示 batch、time、camera view、tactile sensor、point count。实际系统必须额外记录 units、coordinate frame、timestamp、latency 与 calibration version。

---

## 4. 与仓库已有模块的连接

- [Observation Operators](../../02-physics-ai-core/observation-operators.md)：robot sensor 也是 `state → measurement`；
- [Inverse / DA / UQ](../../10-data-assimilation-inverse-uq/index.md)：robot state estimation 与 Bayesian filtering / DA 有共同结构；
- [Differentiable Simulation](../../04-neural-operators-simulation/differentiable-simulation.md)：system identification、control 与 sim-to-real 的桥；
- [Multiscale / Multimodal Fusion](../../05-spatiotemporal-multiscale-ai/multiscale-multimodal-fusion.md)：多相机、depth、LiDAR、tactile、proprioception；
- [Data / HPC / Evaluation](../../11-data-hpc-evaluation/index.md)：large-scale robot data、distributed training、benchmarking、reproducibility。

---

## 5. Pages

1. [Embodied Foundations](00-foundations.md)
2. [Robot Perception](01-perception.md)
3. [Geometry & 3D Representation](02-geometry-3d.md)
4. [State Estimation & Sensor Fusion](03-state-estimation.md)
5. [Kinematics, Dynamics & Contact](04-kinematics-dynamics.md)
6. [World Models & Physical Reasoning](05-world-models-physical-reasoning.md)
7. [Planning & Control](06-planning-control.md)
8. [Robot Learning & Data](07-robot-learning.md)
9. [VLA & Robot Foundation Models](08-vla-robot-foundation-models.md)
10. [Simulation & Sim-to-Real](09-simulation-sim2real.md)
11. [Evaluation, Safety & Deployment](10-evaluation-safety.md)

快速变化的 2026 release 统一放到 [2026-08-20 Snapshot](../../13-2026-snapshot/index.md)。
