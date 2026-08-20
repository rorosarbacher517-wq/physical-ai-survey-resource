# Hybrid Physics–ML Weather Modeling

## 1. Definition

Hybrid weather models retain selected numerical/physical components while learning other components such as parameterizations, corrections, latent dynamics or observation mappings.

They occupy the middle of a spectrum:

```text
numerical model
↔ numerical core + learned parameterization
↔ differentiable hybrid model
↔ learned forecast surrogate
```

## 2. Why hybridize

Atmospheric modeling combines relatively well-understood resolved dynamics with unresolved/subgrid processes and computational approximations.

ML can target:

- moist/convection parameterization;
- radiation/cloud approximations;
- turbulence/mixing closures;
- bias correction;
- learned tendencies;
- solver acceleration;
- observation/data-assimilation components.

## 3. State and tendency view

A numerical model can be written schematically as:

```text
x_(t+Δt) = Solver(x_t, forcing, parameterizations)
```

A learned tendency/closure might provide:

```text
Δx_ml = fθ(x_t, local/global context)
```

and the physical/numerical integrator advances the combined state.

## 4. Tensor example

```text
state:     [B,V,L,H,W]
static:    [B,S,H,W]
forcing:   [B,F,H,W]
ML output: [B,K,L?,H,W]
```

The output may represent tendencies, corrections or subgrid terms rather than the full future atmosphere.

## 5. Differentiable hybrid systems

If the numerical core is differentiable, gradients can propagate through physical time stepping and learned modules.

Potential objectives include:

```text
forecast loss
+ physical consistency
+ long-rollout stability
+ parameterization regularization
```

NeuralGCM is an important public example of a learned/physical hybrid route.

Primary anchor: https://www.nature.com/articles/s41586-024-07744-y

## 6. Training choices

### Offline component training
Train a closure/parameterization on targets produced by observations or high-resolution simulations.

### Coupled training
Train while the component interacts with the evolving model state.

Offline accuracy does not guarantee stable coupled rollout.

## 7. Evaluation

Evaluate at multiple levels:

- local component/tendency error;
- short forecast skill;
- long rollout stability;
- climatology/distribution;
- conservation/balance behavior;
- extremes;
- computational cost.

## 8. Failure modes

- learned closure leaves its training-state distribution during rollout;
- short-step accuracy accumulates into long-term drift;
- physical core and learned component compensate for each other's errors in unstable ways;
- unit/sign convention mismatch;
- evaluation only against the teacher simulator rather than observations;
- exact constraints imposed on approximate parameterizations.

## 9. Connections

See [Neural operators and simulation](../04-neural-operators-simulation/index.md), [differentiable simulation](../04-neural-operators-simulation/differentiable-simulation.md) and [AI weather-model families](ai-weather-models.md).
