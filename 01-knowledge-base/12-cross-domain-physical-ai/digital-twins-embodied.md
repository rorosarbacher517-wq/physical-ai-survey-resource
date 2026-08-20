# Digital Twins 与 Embodied Physical AI

## 1. Digital Twin 的闭环

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

如果只有一个静态 simulator，没有 observation update/control loop，通常不应把它泛化成完整 digital twin。

---

## 2. 与 Data Assimilation 的关系

Digital twin 需要持续校正 state：

```text
model forecast + observations → updated state
```

这与 DA 有直接数学共性。

---

## 3. Embodied intelligence

典型链：

```text
perception
→ localization/state estimation
→ world model
→ planning
→ control/action
→ new observation
```

---

## 4. Physical perception

- RGB / depth；
- LiDAR；
- tactile；
- proprioception；
- audio；
- force/torque。

与 EO 一样，sensor modality 有 observation physics，不应只视作 generic tokens。

---

## 5. World Model

学习：

```text
state + action → future state/observation
```

需要：
- dynamics；
- uncertainty；
- multimodal prediction；
- long-horizon consistency。

---

## 6. Planning / Control

- model predictive control；
- reinforcement learning；
- trajectory optimization；
- vision-language-action (VLA) systems。

Physical AI 需要考虑 constraints、contact、stability 与 safety。

---

## 7. Sim-to-real

simulation 与 real world 存在：
- dynamics gap；
- sensor gap；
- appearance gap；
- contact/friction uncertainty。

策略包括 domain randomization、system identification、online adaptation。

---

## 8. 与 Scientific AI 的桥

Scientific AI 更关注“理解/模拟/反演 physical system”；Embodied AI 更关注“感知/决策/行动”。

两者在：
- state estimation；
- world/dynamics model；
- uncertainty；
- differentiable simulation；
- observation operator；
- control

处汇合。
