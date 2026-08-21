# Active plan

## Phase 16 — Embodied Physical AI / Robotics systematic track

Status: `IN_PROGRESS`

Date: 2026-08-20

Objective: 在保持 Earth-system AI 为仓库重点方向的前提下，将 Embodied Physical AI / Robotics 补成 Physical AI 的第二条系统主干，从 physical perception、3D geometry、state estimation、robot dynamics 一路连接到 world models、planning/control、robot learning、VLA、simulation/sim-to-real 与 safety/evaluation。

Scope:

1. 保持现有 `12-cross-domain-physical-ai` 路径兼容，在其中新增 `embodied-robotics/` 系统子模块；
2. 不把机器人模块组织成模型榜单，而按 `perception → state → dynamics → prediction → planning → action → feedback` 的闭环组织；
3. 与已有 Observation Operator、Inverse/DA/UQ、Differentiable Simulation、Spatiotemporal/Multimodal、Foundation Models、HPC/Evaluation 建立 cross-links；
4. 对 RGB/Depth/LiDAR/Tactile/Proprioception/Force-Torque 等 modality 明确 observation physics、calibration、shape 与 latency；
5. 系统补充 geometry/SE(3)、state estimation/SLAM、kinematics/dynamics/contact、planning/control、imitation/RL、robot datasets、VLA、world models、sim-to-real 与 safety；
6. 在 2026 snapshot 中增加截至 2026-08-20 可由 primary/official source 核实的机器人/Physical AI 更新，并区分 official release、paper/preprint 与 repository synthesis；
7. 不修改 canonical resource metadata 或 taxonomy；
8. CI、internal links、generated-file consistency 与 external links 通过后才标记 PASS。
