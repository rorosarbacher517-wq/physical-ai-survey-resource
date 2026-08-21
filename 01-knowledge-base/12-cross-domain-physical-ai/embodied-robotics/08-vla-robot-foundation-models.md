# Vision-Language-Action & Robot Foundation Models

## 1. VLA 是什么

Vision-Language-Action (VLA) 把视觉、语言与机器人 action 放入同一个 policy framework：

```text
images / video
+ language instruction
+ robot state/history
        ↓
multimodal backbone / policy
        ↓
action tokens / continuous action / action chunk
```

VLA 是 robot learning stack 的上层统一方法之一，不是 robotics fundamentals 的替代品。Geometry、state estimation、dynamics、control interface 与 safety 仍然决定模型能否可靠部署。

---

## 2. 常见 architecture pattern

```text
vision encoder ─┐
language tokens ├→ multimodal backbone → action head → action chunk
robot state ────┘
```

Action head 可能是：
- discrete action tokenizer + autoregressive decoding；
- regression head；
- diffusion / DiT；
- flow matching；
- separate continuous action expert。

---

## 3. 代表性路线

| Model / family | 主要研究接口 | 需要记住什么 |
|---|---|---|
| `RT-1` | Transformer robot policy | large-scale real-robot control data |
| `RT-2` | VLM → action tokens | web-scale VLM knowledge 与 robot action co-training |
| `RT-X` | cross-embodiment | heterogeneous robot datasets / action normalization |
| `Octo` | open generalist policy | Open X-Embodiment pretraining + downstream adaptation |
| `OpenVLA` | open VLA | VLM/vision backbone + robot action fine-tuning |
| `π0 / π0.5` | VLA + continuous action generation | flow-matching action route；π0.5 强调 heterogeneous co-training/open-world generalization |
| `GR00T N` | open humanoid-oriented VLA | VLM/reasoning + continuous action model；版本信息看 dated snapshot |
| `Gemini Robotics` | closed/official robotics model family | VLA 与 embodied-reasoning 分层；公开 capability 不等于 internal architecture fully disclosed |

这里不按 leaderboard 排名，因为不同模型的 robot、task、data、action space 与 evaluation protocol 不统一。

---

## 4. Cross-embodiment 的真正难点

多机器人训练不仅是 dataset concat：

```text
robot A: 7-DoF arm + gripper
robot B: bimanual arms
robot C: mobile manipulator
robot D: humanoid whole body
```

需要处理：
- action dimension；
- coordinate frame；
- control mode；
- morphology；
- camera layout；
- proprioception schema；
- task semantics；
- control frequency。

共享 semantic representation 与 embodiment-specific interface 往往需要同时存在。

---

## 5. High-level reasoning 与 low-level execution

一种清晰的 system decomposition：

```text
Embodied reasoning / VLM
→ task plan / subgoal / tool call
→ VLA / skill policy
→ low-level controller
→ robot
```

另一种是更 end-to-end 的 observation→action policy。

两种路线都有 trade-off。分层系统更容易插入 hard constraints / recovery；end-to-end 系统接口更简洁，但 failure attribution 可能更难。

---

## 6. Training

Robot foundation model 常见数据 mixture：
- internet image/text/video；
- robot demonstrations；
- multi-robot datasets；
- synthetic/simulation trajectories；
- high-level semantic labels/subtasks；
- corrective / intervention data。

需要记录每类数据是否真正参与 action learning，不能因为 backbone 有 web pretraining 就把所有 web knowledge 都写成 robot-control supervision。

---

## 7. Inference

实际系统还受：
- model latency；
- action chunk horizon；
- replan frequency；
- onboard vs remote inference；
- network failure；
- low-level controller frequency；
- observation buffering；
- safety filter

影响。

因此离线 VLA benchmark 与真实 robot deployment 是不同 evaluation layer。

---

## 8. 代表性来源

Stable / historical papers:
- RT-1: https://arxiv.org/abs/2212.06817
- RT-2: https://arxiv.org/abs/2307.15818
- Open X-Embodiment / RT-X: https://robotics-transformer-x.github.io/
- Octo: https://arxiv.org/abs/2405.12213
- OpenVLA: https://arxiv.org/abs/2406.09246
- Physical Intelligence π0 / π0.5: https://www.physicalintelligence.company/blog/pi0 and https://www.physicalintelligence.company/download/pi05.pdf

Current model versions belong in [2026 Snapshot](../../13-2026-snapshot/index.md), not here.
