# Digital Twins 与 Embodied Physical AI：桥接页

这个页面保留原路径兼容，但不再承载完整 robotics 内容。

- **Digital Twin**：重点是 physical system 与 digital model 之间持续 observation update、state estimation、forecast/simulation 与 decision/control 的闭环；
- **Embodied Physical AI / Robotics**：重点是 agent/robot 在环境中 perception、estimation、planning、control、action 与 feedback。

完整机器人学习路径见：

→ [Embodied Physical AI / Robotics](embodied-robotics/index.md)

---

## 1. Digital Twin 闭环

```text
physical system
→ sensors
→ state estimation
→ digital model
→ forecast / simulation
→ decision / control
→ physical system
→ new observations
```

如果只有静态 simulator，没有 observation update 或 operational feedback loop，通常更准确的称呼是 simulation/model，而不是完整 digital twin。

---

## 2. 与 Data Assimilation 的关系

```text
model forecast + observations
→ updated state
```

这与 DA / Bayesian filtering 具有直接数学共性。

→ [Data Assimilation](../10-data-assimilation-inverse-uq/data-assimilation.md)

---

## 3. 与 Embodied Robotics 的关系

Robot loop：

```text
physical world
→ sensor observations
→ state / belief
→ world/dynamics model
→ planning/control
→ action
→ physical world
```

两者共有：
- observation operator；
- state estimation；
- dynamics/world model；
- uncertainty；
- simulation；
- optimization/control。

不同之处是 robotics 通常更强调 embodied action、contact、real-time latency、collision/safety 与 active exploration。

---

## 4. 什么时候 cross-link

- digital twin 的 estimator → [State Estimation](embodied-robotics/03-state-estimation.md)
- digital twin simulator → [Simulation / Sim-to-Real](embodied-robotics/09-simulation-sim2real.md)
- active decision/control → [Planning / Control](embodied-robotics/06-planning-control.md)
- physical deployment risk → [Evaluation / Safety](embodied-robotics/10-evaluation-safety.md)
