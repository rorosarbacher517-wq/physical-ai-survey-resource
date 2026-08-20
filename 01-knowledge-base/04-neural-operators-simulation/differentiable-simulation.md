# Differentiable Simulation

## 1. Definition

A simulator is differentiable when gradients of outputs/objectives can be computed with respect to parameters, controls or inputs.

```text
θ → simulator S(θ) → y → loss L(y)
               ↑ gradient flows backward
```

## 2. Uses

- inverse parameter estimation;
- system identification;
- control/trajectory optimization;
- learned closure training;
- sensor/design optimization;
- end-to-end hybrid modeling.

## 3. Differentiation strategies

- automatic differentiation through solver operations;
- adjoint methods;
- implicit differentiation;
- differentiable surrogate when the original solver is not differentiable/practical.

## 4. Memory challenge

Backpropagating through many time steps can require storing a large trajectory. Checkpointing, recomputation or adjoint methods trade compute for memory.

## 5. Numerical gradient quality

A gradient can be mathematically produced but still be noisy/unstable because of discontinuities, iterative solver tolerances, chaos or ill-conditioning.

Validate gradients when they drive scientific inference.

## 6. Discrete versus continuous gradient

Differentiating the discretized solver is not always identical to deriving a continuous adjoint then discretizing it. The distinction matters in precise inverse/control applications.

## 7. Hybrid learning

A neural component can be optimized by downstream physical loss through the simulator, enabling learning without direct labels for the component output.

## 8. Evaluation

Check forward accuracy, gradient accuracy/sensitivity, optimization convergence, robustness to solver settings and computational overhead.
