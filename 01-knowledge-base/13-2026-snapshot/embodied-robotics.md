# 2026-08-20 Snapshot · Embodied Physical AI / Robotics

> **Knowledge cutoff: 2026-08-20.**  
> 本页只记录快速变化的 robotics / embodied Physical AI release 与研究进展。稳定基础放在 [Embodied Physical AI / Robotics](../12-cross-domain-physical-ai/embodied-robotics/index.md)。  
> 标签：`Official` = 官方 release/文档；`Peer-reviewed` = 已正式发表；`Preprint/Research release` = 尚不按正式发表处理。

---

## 1. Gemini Robotics 2

`Official`, **2026-07-30**。

Google DeepMind 官方发布页将当前 robotics family 分成三个角色：

- `Gemini Robotics 2`：Vision-Language-Action model，用视觉/语言输入产生机器人 motor-control outputs；
- `Gemini Robotics ER 2`：embodied reasoning model，负责高层理解、multi-step orchestration、progress tracking 与 tool/model calling；
- `Gemini Robotics On-Device 2`：面向 local robot-device inference 的 VLA variant。

官方页面展示 whole-body humanoid、bimanual manipulation、multi-robot collaboration 与 on-device adaptation examples。这里应把它们写成 **officially demonstrated/reported capabilities**，而不是没有独立复现实验就改写为一般性 scientific conclusion。

该页面还介绍 `ASIMOV-Agentic` safety benchmark，用于 agentic safety orchestration、unsafe action/tool handling 与 uncertainty resolution。它可作为 embodied safety evaluation 的一个当前例子，但不能代表完整 robot safety certification。

Official source:
- https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/

### 学习意义

当前 closed robotics model family 越来越明显地把：

```text
high-level embodied reasoning
→ subgoal / orchestration
→ VLA execution
→ low-level robot control
```

分层处理。公开 capability 不等于 internal architecture、training mixture 或所有 controller details 均已公开。

---

## 2. GR00T N1.6 与 open robotics stack

`Official/open release`, **2026-01-05**。

NVIDIA 官方 release 可确认：

- `Isaac GR00T N1.6`：open reasoning VLA，面向 humanoid/general robot learning；
- `Cosmos Reason 2`：reasoning VLM；
- `Cosmos Predict 2.5 / Transfer 2.5`：world-model / synthetic-data related tools；
- `Isaac Lab-Arena`：simulation-based robot policy evaluation framework；
- GR00T / Isaac 与 Hugging Face `LeRobot` 的 integration。

NVIDIA documentation 还提供 GR00T N1.6 fine-tuning workflow，描述其 vision-language backbone + Diffusion Transformer action head 的公开实现接口。

Official sources:
- https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Releases-New-Physical-AI-Models-as-Global-Partners-Unveil-Next-Generation-Robots/default.aspx
- https://build.nvidia.com/station/gr00t

### 学习意义

Open robotics stack 正从单一 policy 扩展为：

```text
data / synthetic generation
→ foundation policy
→ simulation training
→ benchmark/evaluation
→ edge deployment
```

但 open weights/framework availability 与在任意 real robot 上可直接泛化是两回事；仍需要 embodiment adaptation、calibration、controller integration 与 repeated real-world evaluation。

---

## 3. V-JEPA 2：world model route

`Preprint/Research release`, 2025；截至 2026-08-20 仍是 embodied world-model 路线的重要公开参考。

Meta 的 `V-JEPA 2` 使用 large-scale self-supervised video pretraining，并在额外 robot interaction data 上训练 action-conditioned predictor。官方研究页面报告其可通过 latent prediction + image-goal planning 在新环境执行 reaching/pick/place 类任务。

Sources:
- https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- https://ai.meta.com/research/vjepa/

### 为什么它和 VLA 不同

```text
VLA:
observation + instruction → action

Action-conditioned world model:
state/observation + candidate action → predicted future
```

两者不是互斥路线，可以组成 planner + executor system。

---

## 4. 2026 对“video model 是否学到 physics”的机制研究

`Peer-reviewed`, ICML 2026，Meta Research page date **2026-07-03**：*Interpreting Physics in Video World Models*。

该工作用 layerwise probing、subspace geometry、attention ablation 等分析 video encoders 中 speed、acceleration、motion direction 的表示。论文结果支持：在所研究 architectures 中，physical variables 可在中间层形成可解码的 distributed representations，而不一定对应显式 classical physics-engine state variables。

Source:
- https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

### 处理边界

这是 mechanistic evidence，不应被泛化成：
- 所有 world models 都具有可靠 physical reasoning；
- latent physics representation 自动保证 long-horizon rollout；
- video benchmark performance 自动转化为 robot task success。

---

## 5. Generalist robot policy 的稳定参照

以下模型更适合放在稳定 VLA 页面作为 architecture/history context：

- `RT-1 / RT-2 / RT-X`；
- `Octo`；
- `OpenVLA`；
- `π0 / π0.5`。

其中：
- Open X-Embodiment 代表 cross-embodiment dataset/policy route；
- OpenVLA 强调开放 VLA fine-tuning/deployment；
- `π0` 使用 continuous action generation / flow-matching route；
- `π0.5` 强调 heterogeneous co-training 与 open-world generalization experiments。

Sources:
- https://robotics-transformer-x.github.io/
- https://arxiv.org/abs/2405.12213
- https://arxiv.org/abs/2406.09246
- https://www.physicalintelligence.company/download/pi05.pdf

这些模型的 evaluation setup 不统一，不能直接根据单篇论文数字建立跨模型绝对排名。

---

## 6. 当前更值得关注的问题

截至 2026-08-20，机器人 Physical AI 的关键研究问题更适合表述为：

1. cross-embodiment action/state representation；
2. long-horizon planning 与 failure recovery；
3. world model 与 VLA 如何组合；
4. synthetic/simulation data 与 real data 的 transfer boundary；
5. tactile/proprioception 等非视觉 modality 如何进入 foundation policy；
6. real-time / on-device inference 与 control latency；
7. unseen scene/object/task/embodiment 的 OOD evaluation；
8. uncertainty、abstention、human intervention 与 physical safety；
9. benchmark success 与 real deployment reliability 的差距；
10. data provenance、robot hardware/configuration 与 reproducibility。

---

## 7. 更新规则

新增 robotics release 时必须：
- 写绝对日期；
- 区分 official release、paper/preprint 与 independent evidence；
- 对 closed system 不猜 internal architecture；
- 不用 vendor comparison 直接推出跨平台一般结论；
- 具体 model version 放本页，稳定概念放 robotics knowledge pages。
