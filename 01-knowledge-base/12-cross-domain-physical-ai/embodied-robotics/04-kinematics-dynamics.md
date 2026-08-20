# Kinematics, Dynamics & Contact

## 1. Kinematics：动作几何关系

设机器人有 `n` 个 joints：

```text
q   ∈ R^n   joint position
dq  ∈ R^n   joint velocity
ddq ∈ R^n   joint acceleration
```

Forward Kinematics：

```text
T_EE = FK(q)
```

Inverse Kinematics：

```text
q* such that FK(q*) ≈ T_target
```

IK 通常不是唯一解，还要考虑 joint limits、collision、conditioning 与 preferred posture。

---

## 2. Jacobian

```text
v_EE = J(q) dq
```

Jacobian 把 joint velocity 映射到 end-effector spatial velocity。

它用于：
- differential IK；
- manipulability；
- singularity analysis；
- force/torque mapping；
- operational-space control。

接近 singular configuration 时，小的 Cartesian target 可能需要很大的 joint motion。

---

## 3. Rigid-body dynamics

常见形式：

```text
M(q) ddq + C(q,dq) dq + g(q) + τ_contact = τ
```

其中：
- `M(q)`：mass/inertia matrix；
- `C`：Coriolis/centrifugal terms；
- `g(q)`：gravity；
- `τ_contact`：contact contribution；
- `τ`：actuator torque。

真实系统还会有 friction、gearbox、compliance、delay 等未完全建模效应。

---

## 4. Contact

Manipulation 的难点常在 contact：

```text
no contact
→ impact
→ sticking / sliding
→ release
```

需要考虑：
- collision geometry；
- normal force；
- friction cone；
- complementarity / contact mode；
- deformation/compliance；
- tactile/force feedback。

硬接触会导致 dynamics 非平滑，这也是 differentiable simulation 和 gradient-based planning 的难点之一。

---

## 5. Control spaces

### Joint-space
控制 `q/dq/τ`。

### Cartesian / operational space
控制 end-effector pose/velocity/wrench。

### Impedance control
不只追 position，还规定力-位移关系，让机器人在接触任务中保持一定 compliance。

### Whole-body control
同时协调 base、torso、arms、hands，并满足 balance/contact/kinematic constraints。

---

## 6. Learning 与 dynamics 的关系

Learning 可以：
- 直接预测 action；
- 学 residual dynamics；
- 学 contact model；
- 学 cost/reward；
- 学 inverse dynamics；
- 学 controller parameter；
- 学 simulator-to-real correction。

但 learned policy 的 action 仍然通过真实 rigid-body/contact dynamics 执行，因此 evaluation 不能只看离线 action regression error。

---

## 7. Robot state / action normalization

跨机器人训练必须明确：
- joint ordering；
- joint range；
- position/velocity/torque units；
- end-effector frame；
- gripper convention；
- action horizon；
- absolute vs delta action。

不一致的 normalization 会直接造成 deployment error。

---

## 8. Failure modes

- IK solution 不可达或碰撞；
- Jacobian singularity；
- dynamics model mismatch；
- friction/contact 参数变化；
- actuator saturation；
- latency 导致 controller instability；
- policy 输出频率与 low-level control interface 不匹配。

## Cross-links

- [Dynamical Systems / PDE](../../00-foundations/dynamical-systems-pde.md)
- [Differentiable Simulation](../../04-neural-operators-simulation/differentiable-simulation.md)

## Sources

- Modern Robotics, Lynch & Park: https://modernrobotics.northwestern.edu/
- MuJoCo documentation: https://mujoco.readthedocs.io/
