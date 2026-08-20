# Audit & Update Policy

> Knowledge baseline: **2026-08-20**.

This repository is maintained by **knowledge stability + scientific value + verifiability**, not by continuously appending model names.

## 1. Three freshness classes

### Stable fundamentals
Math, probability, optimization, PDE/ODE basics, numerical discretization, conservation, classical ML/DL and core remote-sensing physics.

Update when a factual error, conceptual gap, or clearer explanation is identified.

### Evolving scientific-AI methods
PINNs, neural operators, hybrid numerical-ML methods, differentiable simulation, data assimilation, UQ, scientific foundation-model design and multimodal Earth AI.

Update when a method changes the modeling assumptions, training objective, representation, or evaluation practice.

### Fast-moving systems
Operational weather AI, geospatial foundation-model releases, new pretrained checkpoints and rapidly changing software stacks.

These belong primarily in `01-knowledge-base/13-2026-snapshot/`. Stable principles must be moved back into the relevant foundation module instead of being duplicated indefinitely.

## 2. Evidence levels for prose

- **Confirmed**: directly supported by original paper, publisher page, official repository/model card, official institution or dataset provider.
- **Implementation inference**: can be reasonably derived from open source; must be labeled as inference.
- **Unknown**: not publicly disclosed or not verified. Do not guess.

Canonical resource records continue to use the stricter metadata evidence levels defined in `AGENTS.md` and `metadata/taxonomy.yaml`.

## 3. Source hierarchy

Prefer:

1. original paper / DOI / publisher / arXiv / OpenReview;
2. official organization repository or documentation;
3. official dataset/provider page;
4. author project page;
5. secondary material only for discovery.

Do not use press coverage or blog summaries as the sole source for architecture, training data, benchmark or scientific-result claims.

## 4. What deserves a fast-moving entry?

At least one must be true:

- changes the scientific modeling paradigm;
- becomes operational or broadly deployable;
- introduces a meaningful new representation, objective, coupling or evaluation method;
- opens weights/code/data that materially improve reproducibility;
- is especially relevant to Earth observation, carbon cycle, weather/climate or another core Physical-AI domain.

A version bump or leaderboard-only improvement does not automatically deserve a new section.

## 5. Scientific claim checklist

Before adding a claim, ask:

1. What is the physical variable and unit?
2. What exactly is observed versus derived?
3. What is the spatial/temporal support?
4. What physics or prior is actually encoded?
5. What is learned and what remains numerical/analytical?
6. What validation split was used?
7. Is the comparison resolution/support fair?
8. Are uncertainty and failure modes reported?
9. Is the claim source-stated or repository synthesis?

## 6. Earth-system special rules

### Remote sensing
Never equate a satellite signal with the target process without the retrieval/observation chain. Record sensor, band/modalities, resolution, revisit, preprocessing and support.

### Carbon flux
Keep EC observation support, footprint weighting, NEE sign convention, GPP/RECO partitioning assumptions and tower-to-pixel/grid scale mismatch explicit.

### Weather/climate
Separate analysis/reanalysis, data assimilation, deterministic forecast, probabilistic ensemble, nowcasting, downscaling and climate simulation. Do not compare headline scores without matching variable, lead time, grid and verification data.

## 7. Update cadence

- Scheduled CI already verifies repository integrity and external links weekly.
- Fast-moving snapshot: review at least monthly when actively maintained.
- Core modules: review quarterly or when a major conceptual change occurs.
- Canonical metadata: update only after primary-source verification.

Every snapshot must carry an explicit audit date.

## 8. Anti-duplication rule

A concept has one primary home. Domain modules may link back to it, but should explain only the domain-specific interpretation.

Examples:

- FNO math lives in neural operators; weather module explains how operator-style models interact with spherical/global grids.
- uncertainty fundamentals live in UQ; carbon module explains flux-partition and footprint uncertainty.
- Transformer basics belong in ML/DL; EO module explains patch, spectral, temporal and geospatial tokenization.

## 9. Repository checks

Mandatory deterministic checks remain:

```bash
python -m scripts.full_check
```

Network verification remains separate:

```bash
python -m scripts.verify_external_links --respect-cache --report
```

Broken internal links, generated-file drift, fabricated citations, unsupported claims or hidden uncertainty are release blockers.
