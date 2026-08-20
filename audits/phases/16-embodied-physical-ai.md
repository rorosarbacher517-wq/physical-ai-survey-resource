# Phase 16 acceptance report — Embodied Physical AI / Robotics

Status: `PENDING_CI`

Date: 2026-08-20

## Objective

将 Embodied Physical AI / Robotics 从 cross-domain overview 扩展为独立、可学习、可维护的 Physical AI 第二主干，同时保持 Earth Observation / Carbon / Weather 为仓库的重点特色方向。

## Scope completed

### 1. Bottom-up robotics knowledge chain

已建立：

```text
robot/environment/task
→ sensor observation physics
→ geometry / 3D / SE(3)
→ state estimation / sensor fusion / SLAM
→ kinematics / dynamics / contact
→ world models / physical reasoning
→ planning / control
→ robot learning / data
→ VLA / robot foundation models
→ simulation / sim-to-real
→ evaluation / safety / deployment
```

### 2. Stable knowledge pages

新增 `12-cross-domain-physical-ai/embodied-robotics/`，包含：

- foundations / POMDP / control loop；
- RGB/Depth/LiDAR/IMU/Tactile/Proprioception/Force-Torque perception；
- calibration、coordinate frame、camera model、SO(3)/SE(3)、point/voxel/BEV/occupancy；
- Bayesian filtering、Kalman intuition、factor graph、SLAM；
- FK/IK、Jacobian、rigid-body dynamics、contact、impedance/whole-body control；
- explicit/latent/generative world models 与 physical reasoning；
- task planning、motion planning、MPC、feedback/replanning；
- behavior cloning、imitation、online/offline RL、generative action policy；
- cross-embodiment data、Open X-Embodiment、DROID；
- RT/RT-X、Octo、OpenVLA、π0/π0.5、GR00T、Gemini Robotics 等 VLA/foundation-policy context；
- MuJoCo / Isaac / Genesis、system identification、domain randomization、sim-to-real；
- closed-loop/OOD/safety/deployment/reproducibility evaluation。

### 3. Cross-domain integration

明确连接已有：

- Observation Operator ↔ robot sensor model；
- Data Assimilation / Bayesian inverse ↔ robot state estimation / SLAM；
- Differentiable Simulation ↔ system identification / planning / sim-to-real；
- Multimodal Fusion ↔ camera/depth/LiDAR/tactile/proprioception；
- Optimization / MPC ↔ planning/control；
- UQ / calibration ↔ abstention / failure detection / safe stop；
- Data/HPC/Evaluation ↔ large-scale robot trajectories / simulation / benchmarks。

### 4. Repository navigation

已更新：

- root `README.md`：改成 Scientific/Earth AI + Embodied Physical AI 两条主干；
- `01-knowledge-base/index.md`：加入 shared state-observation-action framework；
- `DETAILED_INDEX.md`：增加 XI-A robotics section；
- `learning-paths/index.md`：增加 Route H；
- `12-cross-domain-physical-ai/index.md`：明确两类 Physical AI problem；
- `digital-twins-embodied.md`：保留旧路径但降为 bridge page；
- `mkdocs.yml`：加入完整 robotics navigation；
- 2026 snapshot navigation：Earth/Scientific 与 Embodied/Robotics 分开。

### 5. 2026-08-20 robotics snapshot

新增 `13-2026-snapshot/embodied-robotics.md`，区分 `Official / Peer-reviewed / Preprint/Research release`，覆盖：

- Gemini Robotics 2 official release（2026-07-30）；
- GR00T N1.6 / Cosmos / Isaac Lab-Arena open stack（2026-01-05）；
- V-JEPA 2 action-conditioned world-model route；
- ICML 2026 *Interpreting Physics in Video World Models*；
- RT-X / Octo / OpenVLA / π0 / π0.5 作为稳定 architecture/context；
- current research questions：cross-embodiment、long-horizon recovery、world model + VLA、sim-real transfer、nonvisual modalities、on-device latency、OOD、uncertainty/safety 与 reproducibility。

## Evidence policy

- current releases 优先 official institution/project pages；
- paper 与 official product/demo 分开描述；
- vendor-reported capability 只写成 official report/demonstration，不自动改写为 independent scientific conclusion；
- closed architecture 未公开时不猜；
- 不建立跨 robot/model 的绝对 leaderboard，因为 task/data/action/evaluation protocol 不统一；
- 避免 `first / best / state-of-the-art / unprecedented` 等仓库 claim-audit 风险词。

## Acceptance gates

- [x] robotics track is organized bottom-up rather than as a model list；
- [x] perception, geometry, estimation, dynamics, world models, planning/control, learning, VLA, simulation and safety are covered；
- [x] stable concepts are separated from dated 2026 releases；
- [x] current claims use primary/official sources and avoid unsupported generalization；
- [x] existing Scientific AI / Earth AI cross-links are explicit；
- [ ] `python -m scripts.full_check` observed as passing for final branch head；
- [ ] external-link verification observed as passing for final branch head；
- [ ] no broken internal links / generated drift reported by final CI。

## Current validation limitation

Branch `kb-v4-embodied-physical-ai` is based on the current `main` and is ahead without known divergence. The GitHub connector available in this session does not expose a generic branch Actions-run listing endpoint, and its commit-workflow helper only surfaces pull-request-triggered runs. A local clone/check attempt is unavailable because the current container cannot resolve `github.com`.

Therefore the content, sourcing and navigation work is complete, but Phase 16 remains `PENDING_CI` / `IN_PROGRESS` until a pull-request CI run verifies the final branch head. No passing CI result is inferred.
