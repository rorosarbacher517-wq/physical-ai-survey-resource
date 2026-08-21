# Embodied AI Foundations

## 1. 基本对象

一个机器人任务至少需要区分：

- **environment**：外部物理环境；
- **robot state**：关节位置、速度、base pose、gripper state 等；
- **world state**：物体位置、形状、接触关系、可达区域等；
- **observation**：sensor 可获得的数据；
- **action**：position / velocity / torque / end-effector command 等；
- **goal / task**：需要达到的状态或行为；
- **reward / cost**：如果使用 optimization/RL，怎样评价 trajectory。

关键区别：`state` 不等于 `observation`。真实机器人通常只能部分观测环境。

---

## 2. POMDP 视角

可用 POMDP 表示：

```text
S: latent physical states
A: actions
O: observations
T(x_{t+1}|x_t,a_t): transition/dynamics
Z(o_t|x_t): observation model
R(x_t,a_t): reward/cost
```

机器人只能看到 `o_t`，因此实际决策常依赖 belief/history：

```text
b_t = p(x_t | o_1:t, a_1:t-1)
```

这就是 state estimation、memory、world model 为什么会进入 robotics stack。

---

## 3. Control loop

```text
sense
→ estimate
→ decide
→ command
→ actuator
→ physical response
→ sense again
```

不同模块运行频率可能差异很大：

- low-level motor/current loop：高频；
- joint/Cartesian controller：中高频；
- visuomotor policy：通常更低；
- language/task planner：可更低频。

因此 end-to-end model 也不能忽略 latency、control frequency 与 asynchronous sensors。

---

## 4. Action space

常见 action representation：

```text
joint position:       a_t ∈ R^n
joint velocity:       a_t ∈ R^n
joint torque:         a_t ∈ R^n
EE delta pose:        [dx,dy,dz,droll,dpitch,dyaw]
gripper:              scalar / discrete state
mobile base:          [v, ω]
whole body:           base + torso + arms + hands
```

不同 action space 对 learning difficulty、safety 与 controller responsibility 有直接影响。

---

## 5. Reactive、model-based 与 hierarchical

### Reactive policy

```text
a_t = π(o_t)
```

优点是直接；缺点是长时程 memory/planning 能力有限。

### State-conditioned policy

```text
a_t = π(z_t, goal)
```

其中 `z_t` 来自 estimator 或 learned representation。

### Model-based

```text
z_{t+1} = f(z_t,a_t)
planner searches actions
```

### Hierarchical

```text
language/task goal
→ subgoal / skill
→ motion target
→ low-level controller
```

很多长时程机器人系统实际上是多时间尺度层级，而不是一个单一 network 以同一频率解决全部问题。

---

## 6. Embodiment

不同 robot embodiment 改变：

- degrees of freedom；
- kinematic reachability；
- sensor placement；
- action dimension；
- dynamics/contact；
- control frequency；
- end-effector capability。

所以 cross-embodiment learning 不是简单的数据合并，需要 action/state normalization、morphology metadata、shared task semantics 或 embodiment-specific adapters。

---

## 7. 与 Scientific AI 的统一视角

```text
Scientific AI:
physical state → observation → inference / prediction

Embodied Physical AI:
physical state → observation → inference / prediction → action → new physical state
```

多出来的 `action → state` 闭环使 distribution shift 变成 endogenous：模型自己的动作会改变后续输入分布。

## Sources

- Sutton & Barto, *Reinforcement Learning: An Introduction*: http://incompleteideas.net/book/the-book-2nd.html
- Modern Robotics, Lynch & Park: https://modernrobotics.northwestern.edu/
