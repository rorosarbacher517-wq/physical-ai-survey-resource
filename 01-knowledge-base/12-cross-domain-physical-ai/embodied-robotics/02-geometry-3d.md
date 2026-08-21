# Geometry & 3D Representation

## 1. Coordinate frame 是机器人 3D 的基础

常见 frame：

```text
world / map
base
end-effector
camera
LiDAR
object
```

同一个点在不同 frame 的坐标不同，因此任何 3D output 都必须带 frame definition。

---

## 2. Rigid transform

三维刚体变换：

```text
T = [[R, t],
     [0, 1]]
```

其中：
- `R ∈ SO(3)`：rotation；
- `t ∈ R^3`：translation；
- `T ∈ SE(3)`：rigid-body pose。

齐次坐标：

```text
p_B = T_BA p_A
```

链式变换：

```text
T_world_camera = T_world_base T_base_camera
```

---

## 3. Camera projection

理想 pinhole model：

```text
s [u,v,1]^T = K [R|t] [X,Y,Z,1]^T
```

从 3D 到 2D 会丢失 depth，因此 monocular image 到 3D state 本质上是 underdetermined inference，通常依赖 multi-view、temporal cues、depth sensor 或 learned prior。

---

## 4. 3D representations

### Point cloud

```text
P: [B,N,3+C]
```

优点：保留原始几何；问题：unordered、density 不均、neighbor search 成本。

### Voxel / sparse voxel

```text
[B,C,X,Y,Z]
```

规则栅格利于 convolution，但 dense 3D memory 成本高；常使用 sparse structure。

### BEV

```text
[B,C,H,W]
```

把 3D 场景投影/聚合到 ground-plane representation，常用于 navigation、mobile manipulation、autonomous systems。

### Occupancy

预测空间 cell 的 occupied/free/unknown，可进一步加入 semantic label。

### Object-centric representation

```text
object_i = {pose, size, category, state, relation}
```

适合 symbolic/task planning，但 object extraction 本身可能不稳定。

### Implicit 3D representation
NeRF / 3D Gaussian Splatting 等可用于 reconstruction/simulation/novel view；是否适合 real-time control 取决于 latency、update speed 与 task interface。

---

## 5. Pose representation

常见 rotation：
- rotation matrix；
- quaternion；
- axis-angle；
- Euler angles；
- continuous learned rotation representations。

Euler angles 直观，但存在 parameterization singularity；quaternion 需要 normalization 且有 sign equivalence。

---

## 6. Geometry 与 learning

网络可以直接学习 pixel→action，但显式 geometry 仍在以下场景有价值：
- calibration；
- grasp pose；
- collision checking；
- motion planning；
- multi-view fusion；
- robot-to-camera transformations；
- transferring action between embodiments。

所以“端到端”不等于 geometry 可以忽略。

---

## 7. 常见错误

- 混淆 camera frame 与 world frame；
- degree/radian 混用；
- quaternion order 不一致；
- left/right-handed convention 混用；
- depth unit mm/m 混用；
- 训练和 deployment extrinsic 不一致；
- point cloud crop/augmentation 后没有同步更新 pose。

## Sources

- Modern Robotics, Lynch & Park: https://modernrobotics.northwestern.edu/
- OpenCV calib3d: https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html
