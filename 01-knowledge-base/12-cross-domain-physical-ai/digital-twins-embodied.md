# Digital Twins and Embodied Physical Systems

## 1. Digital-twin loop

A digital twin is a continuously updated model-system loop:

```text
physical system
→ sensors/observations
→ state estimation
→ model/surrogate
→ forecast/scenario
→ decision/control
→ physical system
```

The synchronization/state-estimation loop distinguishes it from a static simulator dashboard.

## 2. Components

- sensor ingestion;
- observation model;
- state/parameter estimation;
- physics/process model;
- ML surrogate/residual;
- uncertainty;
- decision/control;
- monitoring/audit.

## 3. Embodied intelligence

An embodied agent additionally perceives and acts in a physical environment.

Core stack:

```text
perception
→ world/state representation
→ dynamics/world model
→ planning/policy
→ control/action
→ new observation
```

## 4. Connection to Scientific AI

Shared foundations:

- system identification;
- differentiable simulation;
- uncertainty;
- model predictive control;
- 3D/geometry;
- multi-sensor fusion;
- physical constraints.

## 5. Sim-to-real

A policy/model trained in simulation faces mismatch in dynamics, sensors, contacts and environment.

Approaches include domain randomization, adaptation, system identification and real-world fine-tuning with safety constraints.

## 6. Safety

Physical actions create real consequences. Reliable systems need bounds, monitors, fallback controllers, uncertainty/OOD detection and auditable action interfaces.

## 7. Earth-system analogy

Earth digital twins use similar observe→estimate→simulate→update loops, but action/control may be replaced by scenario analysis, forecasting or decision support.
