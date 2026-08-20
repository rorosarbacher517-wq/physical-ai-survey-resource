# 11 · Data Engineering, HPC, Evaluation and Reproducibility

Scientific AI often fails because of data/support/split issues rather than architecture.

## 1. Data pipeline

```text
source discovery
→ download/access
→ provenance + version
→ QC
→ coordinate/time harmonization
→ unit normalization
→ resampling / observation mapping
→ sample construction
→ split definition
→ sharding/cache
→ training
→ prediction archive
→ evaluation/audit
```

## 2. Data engineering principles

Track:

- source URL/provider;
- version/date;
- coordinate reference system;
- units;
- missing-data semantics;
- QC flags;
- native resolution;
- resampling;
- temporal aggregation;
- sample identifiers;
- leakage-safe split membership.

## 3. Large-scale compute

Know the practical bottlenecks:

- remote I/O and chunking;
- raster/time-series sharding;
- CPU preprocessing versus GPU starvation;
- mixed precision;
- gradient checkpointing;
- distributed data/model parallelism;
- communication cost;
- checkpoint/restart;
- deterministic experiment configuration.

Scientific models may be input-bandwidth bound before they are FLOP bound.

## 4. Evaluation hierarchy

### Predictive metrics
RMSE, MAE, R²/correlation where appropriate.

### Probabilistic metrics
NLL, CRPS, Brier, coverage/calibration.

### Physical metrics
conservation, balance error, spectral behavior, stability, constraint violation.

### Generalization
site/region/time/regime/event/OOD.

### Efficiency
training cost, inference latency, memory, energy/compute and speedup versus numerical baseline.

## 5. Paired comparisons

When testing one scientific design choice, hold all other components fixed where possible.

Examples:

- dynamic footprint weighting versus uniform aggregation;
- HLS only versus HLS + LiDAR;
- physics constraint on versus off;
- same architecture and split, different observation operator.

Use paired error differences and uncertainty/statistical testing where appropriate.

## 6. Reproducibility checklist

- exact data versions;
- preprocessing scripts;
- random seeds;
- split manifests;
- model/config commit;
- software environment;
- hardware;
- training epochs/steps;
- checkpoint selection;
- metric implementation;
- failure/bad-case logs.

## 7. Repository resource layer

Use the canonical libraries instead of duplicating resources:

- [datasets](../../04-dataset-library/index.md)
- [benchmarks](../../05-benchmarks-and-evaluation/index.md)
- [code](../../03-code-library/index.md)
- [papers](../../02-paper-library/index.md)
