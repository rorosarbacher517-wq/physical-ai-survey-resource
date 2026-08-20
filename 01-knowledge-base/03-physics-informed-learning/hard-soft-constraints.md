# Hard and Soft Physical Constraints

## 1. Soft constraint

Add a penalty:

`L = L_data + λ L_physics`

Pros: flexible under noisy/imperfect physics. Cons: constraint can be violated and λ selection matters.

## 2. Hard constraint by parameterization

Construct output so the constraint is satisfied automatically.

Example for a boundary value `u(a)=u_a`:

```text
u(x) = u_a + (x-a) N_θ(x)
```

At `x=a`, the network contribution vanishes.

## 3. Projection

Predict an unconstrained field, then project to a constraint-satisfying space.

Useful for divergence-free, normalization or conservation constraints when an efficient projection exists.

## 4. Conservation layer

Represent transfer as fluxes between cells/nodes so internal transfers cancel, preserving totals except explicit sources/sinks/boundaries.

## 5. Positivity

Use positive-valued output parameterizations when the variable is physically nonnegative.

## 6. Choosing constraint strength

Ask:

- Is the relation exact or approximate?
- Are parameters known?
- Does observation noise conflict with it?
- Does it hold across all regimes?
- Will strict enforcement amplify another modeling error?

## 7. Hybrid strategy

Hard-enforce robust identities/bounds while softly regularizing uncertain process relationships.

## 8. Ablation

A physics constraint should be tested against the same model without it, under identical splits/training budget, and evaluated both predictively and physically.
