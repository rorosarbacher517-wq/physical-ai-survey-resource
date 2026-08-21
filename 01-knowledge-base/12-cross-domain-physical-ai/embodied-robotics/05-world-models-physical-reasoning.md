# World Models & Physical Reasoning

## 1. World model 的核心定义

机器人需要预测 action 的后果：

```text
x_{t+1} = f(x_t, a_t)
```

如果 state 不可直接观测，也可在 latent space 学：

```text
z_t = encoder(o_1:t)
z_{t+1} = fθ(z_t,a_t)
```

World model 不等于 video generator。它可以预测：
- explicit state；
- latent embedding；
- future image/video；
- occupancy；
- object/contact state；
- reward/cost/task progress。

是否有用取决于 prediction 是否保留 planning/control 所需信息，而不是画面是否视觉逼真。

---

## 2. 三种常见路线

### Explicit dynamics model

```text
(q,dq,object state,a) → next state
```

可结合 analytical physics / residual learning。

### Latent predictive model

```text
observation → latent z
(z,a) → z_next
```

降低 pixel prediction burden，但 latent metric 必须与 task/planning 对齐。

### Generative observation model

```text
images/video + action → future images/video
```

可用于 synthetic data、counterfactual rollout、policy evaluation，但需要警惕 visual plausibility 与 physical correctness 不等价。

---

## 3. Physical reasoning 应拆开评价

“会看视频”并不自动意味着懂物理。可以分成：

- object permanence；
- support / containment；
- collision / contact；
- motion / velocity / acceleration；
- gravity / stability；
- affordance；
- causal effect of action；
- counterfactual prediction；
- task progress / success detection。

这些能力的 benchmark 与 robot task success 应分开报告。

---

## 4. World model 如何用于 planning

Model-predictive route：

```text
current state z_t
→ sample candidate action sequences
→ world-model rollout
→ score predicted outcomes
→ execute short prefix
→ observe again
→ replan
```

这与 MPC 的思想一致，只是 dynamics/cost 可能由 learned model 提供。

---

## 5. V-JEPA 2 是什么例子

Meta 2025 的 `V-JEPA 2` 采用 self-supervised video representation + predictor，并在额外 action-conditioned robot data 上训练 predictor。官方论文报告其 action-conditioned variant 可在新环境中进行 image-goal planning。

这个例子说明 world-model route 与 VLA route 不完全相同：

```text
VLA: observation + language → action
World model: observation/state + candidate action → predicted future
```

两者可以组合：high-level VLM/VLA 负责 task semantics，world model 负责 consequence prediction / planning。

2026 的 physics-interpretability 工作进一步研究 video encoders 内部如何表示 speed、acceleration、motion direction 等变量；其结果支持“模型可能使用分布式 representation，而非显式 classical state variable”的解释。这个结论来自特定 architectures/experiments，不应泛化成所有 world models 的内部机制。

---

## 6. Training objectives

可能包括：
- next-state regression；
- latent prediction；
- contrastive/predictive loss；
- image/video reconstruction；
- diffusion / flow matching；
- reward/value prediction；
- consistency across time scales。

Long-horizon rollout 还要关注 compounding error。

---

## 7. Evaluation

至少区分：

1. representation quality；
2. short-horizon prediction；
3. long-horizon prediction；
4. physical consistency；
5. counterfactual/action-conditioned accuracy；
6. planning usefulness；
7. real robot task success。

只评 future-frame quality 不能证明 model 对 control 有用。

## Sources

- V-JEPA 2: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- V-JEPA 2 project: https://ai.meta.com/research/vjepa/
- 2026 physics interpretability study: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
