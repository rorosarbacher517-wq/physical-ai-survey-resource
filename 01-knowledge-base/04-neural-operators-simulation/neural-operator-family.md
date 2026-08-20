# Neural-operator Family

## 1. Operator-learning target

Instead of one fixed vector mapping, learn a mapping between functions/fields:

`G: a(x) → u(x)`

The same learned operator should handle many input functions/initial conditions within its training domain.

## 2. DeepONet

Conceptual form:

```text
branch network: samples of input function a
trunk network: query coordinate x
→ combine
→ u(x)
```

Useful mental model: one network encodes the input function, another encodes where the solution is queried.

Primary: Lu et al., *Nature Machine Intelligence* (2021): https://doi.org/10.1038/s42256-021-00302-5

## 3. Fourier Neural Operator

FNO alternates pointwise transforms with learned spectral convolution.

Conceptual layer:

```text
x-space field
→ FFT
→ learned transform on selected modes
→ inverse FFT
→ nonlinear mixing
```

Global receptive field is efficient on regular grids, while high-frequency/local details and non-periodic/irregular geometry need care.

Primary: Li et al. (2021): https://arxiv.org/abs/2010.08895

## 4. Graph/mesh operators

Represent the domain as nodes/edges and learn field propagation on irregular geometry. Useful for spherical weather grids and finite-element meshes.

## 5. Resolution transfer

Operator learning is often motivated by resolution flexibility, but practical performance can still depend on discretization, training resolution, coordinate encoding and spectral truncation.

Always test cross-resolution behavior rather than assuming invariance.

## 6. One-step versus rollout

A learned operator may map current state to future state repeatedly. Multi-step errors accumulate, so stability and spectral behavior matter.

## 7. Comparison axes

- regular vs irregular geometry;
- local vs global interaction;
- spectral vs spatial computation;
- fixed vs variable resolution;
- deterministic vs probabilistic;
- one-shot field solution vs temporal rollout;
- physics-constrained vs purely data-driven.
