# Evaluation, Safety & Deployment

## 1. Robotics evaluation 必须是分层的

一个 model 可以 perception 很强但 control 很差，也可以 simulation 成功但 real deployment 不稳定。

建议至少分：

```text
perception / reasoning
→ action prediction
→ closed-loop simulation
→ real robot task
→ robustness / OOD
→ safety / recovery
→ latency / resource
```

---

## 2. Task metrics

- full task success；
- partial/subtask completion；
- success under repeated trials；
- completion time；
- intervention count；
- recovery success；
- path/action efficiency；
- contact/collision events。

报告平均成功率时还应给 episode count、scene/task distribution 与 confidence interval/variation。

---

## 3. Generalization axes

需要明确 held-out 什么：

- objects；
- backgrounds/lighting；
- scenes/homes/workcells；
- language paraphrases；
- task combinations；
- disturbances；
- embodiment；
- sensor layout；
- dynamics parameters；
- long-horizon duration。

`random episode split` 对很多机器人任务会高估泛化，因为同一 scene/object/task pattern 可同时进入 train/test。

---

## 4. Physical safety 是系统属性

Safety 不只靠 foundation model。完整 stack 可能包括：

```text
semantic/task constraint
→ planner validation
→ collision checking
→ workspace / joint limits
→ force/torque limits
→ low-level controller
→ emergency stop / human override
```

Foundation model 可以帮助识别 hazard 或拒绝不合适的 task，但不应替代 deterministic hardware/low-level safety mechanisms。

---

## 5. Uncertainty 与 abstention

机器人系统应该能够区分：
- confident normal execution；
- ambiguous perception；
- infeasible task；
- unsafe condition；
- model/controller failure。

可能的 response：
- reobserve；
- slow down；
- replan；
- request human help；
- safe stop。

Calibration、OOD detection 与 failure prediction 比单纯 softmax confidence 更重要。

---

## 6. Deployment metrics

- inference latency；
- control frequency；
- onboard memory/compute；
- network dependence；
- power；
- sensor-to-action delay；
- dropped frames；
- uptime；
- safe-stop latency。

一个 offline model accuracy improvement 如果显著增加 control delay，真实系统效果可能相反。

---

## 7. Safety benchmark 的解释边界

2026 `Gemini Robotics 2` 官方介绍中加入 `ASIMOV-Agentic`，用于评估 agentic safety orchestration、unsafe tool/action handling 与 uncertainty resolution。它是当前 embodied-reasoning safety evaluation 的一个例子，但单一 benchmark 不能覆盖完整 robot safety case。

机器人 safety 仍需要 hardware、controller、system validation、operating environment 与 human factors 的共同设计。

---

## 8. Reproducibility checklist

至少记录：

```text
robot hardware / firmware
sensor calibration
controller
model checkpoint
training data version
normalization
prompt/instruction
scene/task setup
random seed if relevant
trial protocol
failure definition
software commit
```

视频 demo 应作为定性证据，而不能替代完整 repeated-trial metrics。

## Cross-links

- [Uncertainty / Calibration](../../10-data-assimilation-inverse-uq/uncertainty-calibration.md)
- [Evaluation / Benchmarking](../../11-data-hpc-evaluation/evaluation-benchmarking.md)

## Sources

- Google DeepMind, Gemini Robotics 2 (2026-07-30): https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Isaac Lab-Arena official release context: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Releases-New-Physical-AI-Models-as-Global-Partners-Unveil-Next-Generation-Robots/default.aspx
