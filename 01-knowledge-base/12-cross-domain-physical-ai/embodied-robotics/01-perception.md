# Robot Perception

## 1. Perception 不是 generic token ingestion

机器人传感器来自不同 observation physics：

| Modality | 直接观测 | 主要误差/限制 |
|---|---|---|
| RGB camera | projected radiance/color | illumination、occlusion、motion blur、exposure |
| Depth camera | depth/range estimate | invalid depth、reflective/transparent surface、range limits |
| LiDAR | active range returns | sparsity、incidence angle、reflectance、motion distortion |
| IMU | angular velocity / specific force | bias、drift、noise |
| encoder | joint position/velocity | calibration、backlash、quantization |
| tactile | local contact deformation/pressure | contact locality、sensor hysteresis |
| force/torque | wrench | bias、mounting transform、dynamic coupling |
| audio | acoustic waveform | reverberation、background noise |

如果 sensor model 不清楚，multimodal fusion 很容易把系统误差学成 shortcut。

---

## 2. Calibration

### Intrinsic calibration

相机内参：

```text
K = [[fx, 0, cx],
     [0, fy, cy],
     [0,  0,  1]]
```

### Extrinsic calibration

```text
p_B = T_BA p_A
```

多相机 / camera-LiDAR / camera-robot base fusion 必须知道相对 pose。

### Temporal calibration

除了空间外参，还要检查：
- timestamp；
- hardware/software sync；
- camera exposure time；
- control-to-actuation delay；
- rolling shutter；
- sensor buffering。

---

## 3. Perception tasks

机器人视觉常包含：

- detection / segmentation；
- depth / surface normal；
- keypoint / pose；
- tracking / optical flow；
- 3D reconstruction；
- grasp / affordance；
- object-state estimation；
- scene graph / relation；
- occupancy / free space。

这些 task 的输出不是都需要最终显式 supervision；现代 systems 也可用 pretrained encoder / VLM latent representation。但 deployment 时仍要确认 latent representation 是否保留控制所需的 geometry 和 temporal information。

---

## 4. Multimodal tensors

```text
RGB:             [B,T,V,3,H,W]
Depth:           [B,T,V,1,H,W]
Point cloud:     [B,T,N,3+C]
IMU:             [B,T,6]
Joint state:     [B,T,2n]      # q,dq example
Force/Torque:    [B,T,6]
Tactile:         [B,T,S,C,H,W]
```

融合前至少统一：
- timestamp；
- coordinate frame；
- unit；
- valid mask；
- sampling rate；
- normalization；
- sensor identity。

---

## 5. Fusion strategies

### Early fusion
先对齐到共享 geometry/feature grid 后 concat。

### Encoder-level fusion
各 modality 先用独立 encoder：

```text
RGB encoder ─┐
Depth encoder├→ fusion / attention → state representation
Tactile enc. ┤
Proprio enc. ┘
```

### Cross-attention
适合 variable-length image/point/language tokens。

### Late fusion
各模态先独立预测/估计，再融合 decision。

没有一种 fusion 方案对所有 robot task 都占优；选择取决于 alignment、data volume、missing modality 与 latency。

---

## 6. Physical perception failure modes

- 透明/反光物体导致 depth/range 异常；
- camera view 被手臂或物体遮挡；
- domain shift 改变 lighting/background；
- tactile 只在 contact 后出现，属于 event-conditioned modality；
- training video frame rate 与 real control loop 不一致；
- sensor dropout 没在训练中出现；
- calibration drift 破坏 multi-view geometry。

## Cross-links

- [Observation Operators](../../02-physics-ai-core/observation-operators.md)
- [Multimodal Fusion](../../05-spatiotemporal-multiscale-ai/multiscale-multimodal-fusion.md)
- [LiDAR / 3D](../../06-earth-observation-ai/lidar-3d.md)

## Sources

- OpenCV camera calibration docs: https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html
- ROS REP-103 coordinate conventions: https://www.ros.org/reps/rep-0103.html
