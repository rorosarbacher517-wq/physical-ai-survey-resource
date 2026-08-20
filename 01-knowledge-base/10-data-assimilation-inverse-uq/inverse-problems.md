# Inverse Problems

## 1. Forward model

`y = H(x, θ) + ε`

Given state/parameters, predict observations.

## 2. Inverse problem

Given observations `y`, infer hidden state `x` or parameters `θ`.

Examples:

- atmospheric state from radiances;
- soil moisture from microwave signals;
- ecosystem parameters from flux observations;
- material properties from response fields;
- source/emission estimation.

## 3. Ill-posedness

An inverse problem can be:

- non-unique;
- noise-sensitive;
- underdetermined;
- poorly conditioned.

A neural network can hide these issues but does not remove them.

## 4. Regularization

Add prior structure:

- smoothness;
- sparsity;
- physical bounds;
- Bayesian prior;
- governing equation;
- learned prior/generative model.

## 5. Bayesian view

`p(x|y) ∝ p(y|x) p(x)`

A posterior distribution is more informative than one point estimate when multiple solutions are plausible.

## 6. Amortized inference

Train a network to map many observations to approximate posterior/state estimates quickly. This shifts expensive optimization into training.

## 7. Physics-informed inverse learning

Use PDE/process residuals or differentiable simulators to constrain latent parameters while fitting observations.

## 8. Identifiability

A low reconstruction error `||H(x)-y||` does not guarantee the inferred parameter/state is physically correct if different solutions produce similar observations.

## 9. Validation

Use synthetic recovery when possible, independent observations, parameter sensitivity and posterior coverage/calibration.
