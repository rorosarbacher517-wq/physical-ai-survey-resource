# Scientific Data Engineering

## 1. Data is part of the model

Scientific ML quality depends on provenance, coordinate/time alignment, units, QC and sampling as much as architecture.

## 2. Canonical pipeline

```text
source registry
→ raw access/version
→ validation/QC
→ coordinate harmonization
→ temporal harmonization
→ physical-unit conversion
→ observation/support mapping
→ sample manifest
→ split manifest
→ shards/cache
→ training/evaluation
```

## 3. Immutable raw layer

Preserve original product identifiers/versions and avoid silent in-place modification. Derived datasets should record transformation lineage.

## 4. Sample manifest

For each sample store enough identifiers to reconstruct inputs/targets:

- site/tile/grid;
- timestamp/time interval;
- source product/version;
- sensor;
- QC status;
- split;
- preprocessing version.

## 5. Chunking

Large Earth arrays are read by chunks. Chunk shape should match access patterns:

- spatial tiles;
- time windows;
- variable groups.

Poor chunking can make GPU training I/O-bound.

## 6. Missing data

Use masks and explicit missing semantics. Distinguish:

- not observed;
- invalid/QC rejected;
- outside coverage;
- physically zero.

## 7. Reprocessing

Satellite/reanalysis products can be reprocessed. Pin versions/dates and record changes when rebuilding datasets.

## 8. Leakage-safe splits

Generate split manifests before normalization/statistics. Site/time/region boundaries must be reproducible.

## 9. Data audits

Check distributions by split, site, sensor, season, label and missingness. Many apparent model improvements are sampling differences.
