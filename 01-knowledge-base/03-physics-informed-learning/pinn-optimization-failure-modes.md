# PINN Optimization and Failure Modes

## 1. Multi-objective imbalance

Data, PDE, boundary and initial losses can have different magnitudes and gradient scales.

Symptoms:

- data fit improves while PDE residual stalls;
- boundary conditions are ignored;
- one loss dominates total objective.

Diagnostics: log each term and gradient norm separately.

## 2. Spectral bias

Neural networks often learn smooth/low-frequency structure more easily than high-frequency components. Sharp fronts, turbulence and oscillatory solutions can be difficult.

Possible remedies include Fourier features, adaptive sampling, multi-scale networks or domain decomposition.

## 3. Collocation sampling

Uniform random sampling may waste capacity in easy regions.

Strategies:

- residual-based adaptive sampling;
- boundary-focused sampling;
- regime/feature-aware sampling;
- temporal curriculum.

## 4. Long-time domains

Learning an entire long trajectory simultaneously can be hard.

Approaches:

- time-window decomposition;
- curriculum over temporal horizon;
- causal weighting;
- sequential/solver-coupled training.

## 5. Stiffness

Fast and slow dynamics create gradients on different scales. Standard optimizers may struggle even if the PDE formulation is correct.

## 6. Noisy observations

A strict PDE residual can conflict with noisy real observations or imperfect equations.

Model uncertainty and equation discrepancy rather than assuming both are exact.

## 7. Inverse identifiability

Low residual does not prove recovered parameters are unique/correct. Check posterior/sensitivity and synthetic-recovery experiments.

## 8. Evaluation

Report:

- data error;
- PDE residual;
- boundary/initial error;
- conserved quantities;
- parameter recovery;
- error across space/time;
- sensitivity to random seed/collocation design;
- compute cost.
