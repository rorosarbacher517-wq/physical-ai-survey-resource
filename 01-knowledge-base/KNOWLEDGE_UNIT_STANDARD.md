# Knowledge-unit Standard

Every deep-dive page in this repository should answer a stable set of questions. The goal is to make a topic usable for learning, research design, paper reading and technical discussion rather than leaving it as a glossary entry.

## 1. One-sentence definition

State what the concept/model/operator is and what problem it solves.

## 2. Physical or scientific problem

Specify:

- system being modeled;
- target variable(s) and units;
- spatial and temporal scale;
- known equations/process relationships;
- what is observed versus latent.

## 3. Inputs, outputs and representation

Track semantics and shape where applicable.

Examples:

```text
EO time series:    [B,T,C,H,W]
weather state:     [B,T,V,L,H,W]
mesh/graph state:  [B,N,D]
flux sequence:     [B,T,F]
point cloud:       [B,N,C]
```

Also record coordinates, masks, missingness, units and normalization.

## 4. Observation model

Ask what the instrument or preprocessing pipeline actually measures.

```text
latent physical state x
→ observation operator H
→ observation y
→ QC/retrieval/resampling
→ learning representation
```

For Earth science, measurement support and resampling belong here rather than being treated as minor preprocessing details.

## 5. Core computation

Explain the forward path at the level needed to reconstruct the method:

```text
input
→ representation
→ interaction / operator / dynamics
→ output field or latent state
→ observation mapping if needed
```

Include equations when they clarify the computation.

## 6. Where physics enters

Use the repository taxonomy:

- data/labels;
- input features;
- representation/architecture;
- loss/objective;
- hard parameterization;
- simulator/operator/data-assimilation loop;
- evaluation/audit.

Do not call a model physics-informed merely because the prediction target is physical.

## 7. Training objective

Document:

- supervision source;
- loss/likelihood/residual;
- masking;
- multi-task weighting;
- constraints;
- regularization;
- train/validation/test split;
- data leakage risks.

## 8. Inference / rollout

Explain what differs from training:

- autoregressive rollout;
- iterative solver calls;
- ensemble sampling;
- observation aggregation;
- uncertainty generation;
- post-processing.

## 9. Compute and memory

Identify the dominant scaling variable: pixels, tokens, graph nodes, vertical levels, sequence length, ensemble members or solver steps.

## 10. Evaluation

Separate:

- predictive error;
- physical consistency;
- calibration/uncertainty;
- spatial-temporal scale/support;
- OOD transfer;
- event/extreme performance;
- computational cost.

## 11. Failure modes

List assumptions that can break and diagnostics that reveal them.

## 12. Primary sources

Stable fundamentals may cite textbooks or classic papers. Fast-moving model details must use original papers, official repositories/model cards or institutional documentation. Unpublished implementation details remain unknown.

## 13. Cross-links

Every deep page should link backward to prerequisites and forward to domain applications. Avoid duplicating the same explanation in several modules.
