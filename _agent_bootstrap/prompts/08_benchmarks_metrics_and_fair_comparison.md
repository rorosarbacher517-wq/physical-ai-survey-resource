# Phase 08 — Benchmarks, Metrics, and Fair Comparison

## Goal

Add the missing evaluation layer that connects methods, code, datasets, tasks, splits, and metrics.

## Benchmark model

A benchmark is not merely a dataset. Each benchmark record must define:

- scientific or control task;
- inputs and outputs;
- dataset version;
- preprocessing;
- train/validation/test split;
- boundary or initial conditions when relevant;
- evaluation metrics;
- physical-consistency metrics;
- uncertainty metrics where relevant;
- computational reporting requirements;
- baseline definitions;
- comparability limitations;
- official evaluation code when available.

## Metric taxonomy

Cover:

- predictive accuracy;
- physical residuals;
- conservation errors;
- stability over rollout;
- boundary/initial-condition compliance;
- cross-resolution generalization;
- cross-domain and out-of-distribution generalization;
- data efficiency;
- uncertainty calibration;
- robustness;
- runtime, memory, energy, and hardware reporting.

Do not claim metrics are interchangeable. Explain units, directionality, and aggregation.

## Fair comparison rules

Create a mandatory comparison checklist:

- same dataset version;
- same split;
- same preprocessing;
- same evaluation mask;
- same target definition;
- compatible resolution;
- comparable parameter/computation reporting;
- repeated seeds or uncertainty intervals where appropriate;
- distinction between interpolation and extrapolation;
- distinction between forward simulation, surrogate modeling, inversion, and control.

Flag leaderboard entries as non-comparable when these conditions are not met.

## Leaderboards

Generated leaderboards may only include scores that are:

- tied to a source;
- tied to a precise benchmark version;
- tied to a metric definition;
- not extracted ambiguously from plots;
- accompanied by hardware/runtime context when relevant.

Do not create a universal ranking across incompatible tasks.

## Acceptance criteria

- Benchmarks are schema-valid and reference existing entities.
- Metric definitions include units and direction.
- Comparability warnings render visibly.
- No unsourced score is displayed.
- Phase report status is `PASS`.

## Commit

`phase(08): add benchmark and fair-comparison framework`
