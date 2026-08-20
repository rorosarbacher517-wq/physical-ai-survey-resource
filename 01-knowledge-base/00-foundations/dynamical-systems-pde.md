# Dynamical Systems and PDE Foundations

## 1. State-space view

A physical system can be written as:

```text
state:       x(t)
dynamics:    dx/dt = f(x, u, θ, t)
observation: y(t) = H(x(t)) + ε
```

where `u` is forcing/control, `θ` parameters, `H` an observation operator and `ε` measurement/error terms.

This separation is useful across weather, ecosystem carbon, fluids and robotics.

## 2. ODEs

An ordinary differential equation represents change with respect to one independent variable, commonly time.

Example:

```text
dC/dt = input - loss
```

Questions:

- what is the state?
- what are forcing and parameters?
- what initial condition is required?
- is the system stiff?
- is the state conserved or bounded?

## 3. PDEs

Partial differential equations describe fields changing in space and time.

### Advection

Transport by a velocity field:

`∂u/∂t + v·∇u = 0`

### Diffusion

Smoothing/spreading:

`∂u/∂t = κ ∇²u`

### Advection-diffusion

Combines transport and diffusion.

### Conservation law

A generic local conservation equation:

`∂q/∂t + ∇·F = S`

where `q` is stored quantity, `F` flux and `S` source/sink.

This pattern underlies mass, water, energy and constituent transport.

## 4. Boundary and initial conditions

A PDE is not defined by the differential operator alone.

Common boundary types:

- Dirichlet: value specified;
- Neumann: derivative/flux specified;
- Robin: combination;
- periodic;
- open/radiative boundaries.

Physical-AI models that ignore boundary conditions can fit interior samples yet fail near boundaries or under rollout.

## 5. Stability and chaos

### Stability

Small perturbations remain controlled under the dynamics/numerical scheme.

### Chaotic sensitivity

Weather systems exhibit sensitive dependence on initial conditions. This motivates ensembles and probabilistic prediction rather than interpreting one deterministic trajectory as certainty.

## 6. Linearization

Near state `x0`:

`f(x) ≈ f(x0) + J(x0)(x-x0)`

The Jacobian `J` describes local sensitivity and links dynamical systems to stability, tangent-linear models and gradient-based DA.

## 7. Multi-scale dynamics

Earth systems combine fast and slow processes:

- turbulence: seconds to minutes;
- diurnal flux cycle: hours;
- synoptic weather: days;
- phenology: weeks/months;
- climate: decades.

A model must decide which scales are resolved, parameterized, aggregated or ignored.

## 8. Minimum understanding

You should distinguish state/forcing/parameter/observation, explain local conservation, identify boundary/initial conditions, and understand why chaotic dynamics require lead-time-dependent and probabilistic evaluation.
