# Robot Learning & Data

## 1. Robot learning 的训练对象

目标通常是 policy：

```text
a_t = πθ(o_≤t, goal)
```

或 action chunk：

```text
A_t = [a_t, a_{t+1}, ..., a_{t+H-1}]
```

输入可能包含 images、language、robot state、history；输出可以是 joint/end-effector actions 或 higher-level skills。

---

## 2. Behavior Cloning / Imitation Learning

Behavior Cloning 直接拟合 demonstrations：

```text
L = distance(πθ(o_t), a_t^expert)
```

优点：简单、稳定、无需在线探索。

主要问题是 covariate shift：deployment 时一个小错误会把 robot 带到 training distribution 之外，后续误差继续累积。

改进方向包括：
- intervention / corrective data；
- dataset aggregation；
- diverse demonstrations；
- temporal/action chunking；
- generative/multimodal action distributions。

---

## 3. Reinforcement Learning

RL 通过 interaction 优化 expected return。

### Online RL
需要真实/模拟环境交互，sample cost 与 safety 是机器人中的核心限制。

### Offline RL
只使用固定 dataset，减少在线交互，但要处理 out-of-distribution action 与 value extrapolation。

### RL + demonstrations
可将 imitation initialization、reward learning、RL fine-tuning 组合。

---

## 4. Generative action policy

Robot action 往往是 multimodal：同一个任务可能存在多条合理 trajectory。

因此出现：
- diffusion policy；
- flow-matching action head；
- autoregressive action tokens；
- continuous action expert。

这类方法的重点不是“生成”本身，而是表达多峰 action distribution 与 temporal coherence。

---

## 5. Robot data schema

一个 trajectory 至少应明确：

```text
episode_id
robot / embodiment
instruction / goal
camera observations
robot state
ordered actions
timestamps
success / termination
calibration metadata
```

对 cross-embodiment data 还要记录：
- morphology；
- joint/action definition；
- coordinate frame；
- gripper semantics；
- control frequency；
- normalization statistics。

---

## 6. Large-scale robot datasets

### Open X-Embodiment
由多机构汇集不同 robot datasets，用 standardized format 支持 cross-embodiment policy research。

### DROID
2024 发布的大规模 in-the-wild manipulation dataset，强调跨场景、任务和采集者的数据多样性。

这些数据集说明 robot foundation policy 的 data problem 与 LLM 不同：robot trajectories 昂贵、embodiment-specific，而且 physical execution quality 会影响 label quality。

---

## 7. Data quality

需要检查：
- failed demonstrations 是否保留；
- teleoperation delay；
- camera/action time alignment；
- reset policy；
- instruction consistency；
- success label quality；
- duplicate trajectory；
- embodiment imbalance；
- scene/task leakage。

数据量增加不能自动解决 low-quality control signal 或 train/test overlap。

---

## 8. Evaluation split

至少考虑：

```text
seen task / seen scene
unseen object
unseen scene
unseen instruction
unseen task composition
unseen embodiment
long-horizon task
```

Robot generalization 不能只用 random trajectory split 说明。

## Sources

- Open X-Embodiment: https://robotics-transformer-x.github.io/
- DROID: https://arxiv.org/abs/2403.12945
- Diffusion Policy: https://arxiv.org/abs/2303.04137
