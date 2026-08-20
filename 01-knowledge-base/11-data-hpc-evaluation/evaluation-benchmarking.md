# Scientific Evaluation and Benchmarking

## 1. Benchmark definition

A meaningful benchmark fixes:

- dataset version;
- preprocessing;
- sample unit;
- split;
- target definition;
- metrics;
- evaluation support;
- baseline protocol.

## 2. IID versus OOD

Random IID tests measure interpolation under a familiar distribution. Scientific deployment often requires new regions, sites, regimes, parameters or extremes.

Both can be useful but answer different questions.

## 3. Physical diagnostics

Add to prediction metrics:

- conservation/balance error;
- boundary/constraint violations;
- spectral behavior;
- long-rollout stability;
- extreme-event error;
- uncertainty calibration.

## 4. Paired ablation

To test a component, hold dataset/split/backbone/training fixed and vary one design choice.

## 5. Statistical uncertainty

Report confidence intervals or bootstrap/site-wise variability when sample dependence makes one pooled number misleading.

## 6. Site-level reporting

For multi-site Earth data, pooled metrics can be dominated by large sites. Report site distributions and macro summaries when appropriate.

## 7. Compute-normalized evaluation

A small accuracy gain at much larger compute may or may not be worthwhile. Include parameter count, training/inference cost and memory when the claim is efficiency-related.

## 8. Reproducibility level

Distinguish:

- paper claim only;
- code released;
- data/split available;
- checkpoint available;
- result independently reproduced.

Do not call a result reproduced without running the documented experiment.

## 9. Repository benchmark layer

Use [benchmark library](../../05-benchmarks-and-evaluation/index.md) for canonical cards rather than copying benchmark definitions into multiple modules.
