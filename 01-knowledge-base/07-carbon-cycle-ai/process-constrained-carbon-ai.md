# Process-constrained Carbon AI

## 1. Definition

Process-constrained carbon AI incorporates ecological/biophysical relationships into data-driven prediction through inputs, architecture, objectives, hybrid models or evaluation.

The important question is **which process relationship enters where**.

## 2. Integration levels

### Process-derived inputs

Examples: absorbed radiation proxies, VPD, soil moisture, canopy structure, phenology and physical footprint variables.

### Soft objective

```text
L = L_data + λ_balance L_balance + λ_process L_process
```

### Hard parameterization

Construct outputs so selected bounds/balances hold by design.

### Hybrid process + ML

```text
process model output
+ learned residual/correction
→ final prediction
```

or learn uncertain process parameters/closures.

### Observation operator

Use EC footprint weighting to map a predicted spatial field to the tower observation support.

## 3. Carbon balance example

Under the chosen sign convention:

```text
NEE = RECO - GPP
```

A multi-task model can penalize deviations between predicted components. The coefficient should be tuned against predictive and physical-consistency behavior rather than assumed universal.

## 4. Light, temperature and water-response priors

Possible process priors include:

- radiation controls photosynthetic opportunity;
- water stress/atmospheric demand modifies stomatal response;
- temperature and substrate/moisture influence respiration;
- phenology controls active canopy state.

These are mechanistic guides, not globally fixed monotonic equations.

## 5. Architecture example

```text
EO pixels → spatial encoder → latent field
meteorology → temporal forcing encoder
static/site context → context embedding
→ fused spatiotemporal state
→ pixel/field flux heads
→ footprint observation operator
→ tower-scale loss
```

## 6. Training questions

- Is the process term scaled comparably to data loss?
- Does it improve held-out-site performance?
- Does it reduce physical violation only on train data?
- Is the relationship valid across ecosystems/regimes?
- Does the constraint conflict with uncertain labels?

## 7. Evaluation

Report both:

```text
predictive skill
+
physical/process diagnostics
```

Useful diagnostics include balance residuals, response curves by environmental regime, event behavior and OOD site transfer.

## 8. Failure modes

- calling meteorological inputs a physical constraint;
- enforcing an approximate ecological relationship as exact truth;
- improving balance residual while degrading predictive skill;
- using partitioned GPP/RECO as if uncertainty-free;
- ignoring the tower observation operator.

## 9. Connections

Prerequisites: [Physical AI core](../02-physics-ai-core/index.md) and [hard/soft constraints](../03-physics-informed-learning/hard-soft-constraints.md).

Applications: [Footprint-aware AI](footprint-aware-ai.md), [carbon-water-energy coupling](carbon-water-energy-coupling.md), [tower-to-grid upscaling](tower-to-grid-upscaling.md).
