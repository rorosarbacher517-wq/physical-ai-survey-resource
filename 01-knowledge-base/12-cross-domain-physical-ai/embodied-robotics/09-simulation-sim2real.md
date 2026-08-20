# Simulation, Synthetic Data & Sim-to-Real

## 1. Simulation 在 robotics 中有多个角色

```text
physics engine
→ controller development
→ policy training
→ synthetic data
→ software-in-the-loop
→ evaluation
→ system identification
```

不能把所有 simulator 使用都叫 sim-to-real。

---

## 2. Simulator 需要模拟什么

- rigid-body dynamics；
- collision/contact；
- friction；
- actuator dynamics；
- joints/limits；
- cameras/depth/LiDAR/IMU；
- deformable objects（如果 task 需要）；
- latency/noise（如果用于 deployment validation）。

高 visual fidelity 不等于高 dynamics fidelity，反之亦然。

---

## 3. Sim-to-real gap

主要来源：

```text
dynamics gap
sensor/appearance gap
contact/friction gap
actuator gap
latency gap
object/scene distribution gap
```

如果 simulator 没有建模实际 deployment 的关键变量，policy 可能在 simulation 成功而 real robot 失败。

---

## 4. Domain randomization

训练时随机化：
- mass/inertia；
- friction；
- joint damping；
- camera pose；
- lighting/texture；
- sensor noise；
- object geometry；
- latency。

目的不是“随机越多越好”，而是让 training distribution 覆盖合理的 real uncertainty。过宽 randomization 也会增加 learning difficulty。

---

## 5. System identification

从 real observations 估计 simulator parameters：

```text
real trajectory
→ inverse problem / parameter fitting
→ simulator parameters
→ improved simulation
```

这和仓库的 [Inverse Problems](../../10-data-assimilation-inverse-uq/inverse-problems.md) 直接对应。

---

## 6. Synthetic robot data

合成数据可以：
- 扩充 rare states；
- 生成 camera viewpoints；
- 扩展 object/layout；
- 生成 motion trajectories；
- 预训练 perception/policy；
- 做 counterfactual evaluation。

但 synthetic data 需要标明 generation pipeline 与 filtering，不能自动当成 real demonstration 的等价替代。

---

## 7. Differentiable simulation

如果 simulator/physics components 对 parameters/actions 可微，可用于：
- system identification；
- trajectory optimization；
- controller learning；
- gradient-based design。

Contact discontinuity、solver stability 与 computational cost 仍是主要限制。

---

## 8. 常用开放工具入口

- MuJoCo: https://mujoco.readthedocs.io/
- Isaac Sim: https://docs.isaacsim.omniverse.nvidia.com/
- Isaac Lab: https://isaac-sim.github.io/IsaacLab/main/index.html
- Genesis: https://genesis-world.readthedocs.io/

工具是否适合某一任务取决于 physics coverage、sensor model、parallelism、hardware/deployment interface 与 license，不按单一“更强”结论排序。

## Cross-links

- [Differentiable Simulation](../../04-neural-operators-simulation/differentiable-simulation.md)
- [Inverse Problems](../../10-data-assimilation-inverse-uq/inverse-problems.md)
- [Distributed Scientific ML](../../11-data-hpc-evaluation/distributed-scientific-ml.md)
