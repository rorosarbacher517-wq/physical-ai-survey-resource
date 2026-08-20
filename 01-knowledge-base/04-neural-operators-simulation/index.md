# 04 · Neural Operators, Surrogates and Differentiable Simulation

A standard neural network often learns a mapping between fixed-dimensional tensors. **Operator learning** aims to learn mappings between functions/fields, which is central to repeated PDE and Earth-system prediction.

## 1. Problem view

```text
input field / forcing / parameters a(x)
        ↓
operator G
        ↓
solution field u(x)
```

Examples:

- initial atmospheric state → future state;
- boundary/forcing field → fluid solution;
- material properties → stress/temperature field;
- environmental drivers → flux field.

## 2. Major approaches

### DeepONet
Represents an operator through branch/trunk networks that encode input functions and query locations.

### Fourier Neural Operator (FNO)
Learns global interactions in Fourier space through spectral convolution/operator layers.

Important questions:

- how modes are truncated;
- grid/resolution dependence;
- periodic/spherical/irregular geometry;
- local high-frequency information;
- rollout stability.

### Graph / mesh neural operators
Useful for irregular meshes, spherical grids and changing geometry.

### Local/global operator mixtures
Combine local convolutions with long-range spectral/attention interactions.

## 3. Surrogate modeling

A surrogate replaces an expensive simulator for repeated inference, optimization, uncertainty analysis or ensemble generation.

A good surrogate should report more than speedup:

- domain of validity;
- parameter ranges;
- conservation/physical error;
- extrapolation behavior;
- uncertainty;
- inference cost versus original solver.

## 4. Hybrid numerical + ML

Common patterns:

```text
numerical core + learned closure
numerical core + learned parameterization
physics model + learned residual correction
learned surrogate inside optimization/DA
ML forecast + physical post-processing
```

This is often more robust than replacing the entire simulator.

## 5. Differentiable simulation

If a simulation/observation operator is differentiable, gradients can flow through it for:

- parameter estimation;
- control;
- inverse problems;
- learning closures;
- end-to-end calibration.

Automatic differentiation does not guarantee numerically stable or physically meaningful gradients; solver conditioning still matters.

## 6. Rollout failure

Autoregressive field prediction can accumulate error:

```text
x_t → model → x_{t+1}
             ↓
          reused input
             ↓
          distribution drift
```

Evaluate long-horizon stability, spectra, conservation and extreme events, not just one-step error.

## 7. Read next

- [Spatiotemporal & Multiscale AI](../05-spatiotemporal-multiscale-ai/index.md)
- [Data Assimilation / Inverse / UQ](../10-data-assimilation-inverse-uq/index.md)
- [Weather & Climate AI](../08-weather-climate-ai/index.md)
