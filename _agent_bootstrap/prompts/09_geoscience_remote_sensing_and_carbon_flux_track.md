# Phase 09 — Geoscience, Remote Sensing, and Carbon-Flux Track

## Goal

Build the repository’s distinctive specialty track as a connected scientific resource map rather than a single oversized folder.

## Required structure

```text
06-case-studies/
└── geoscience-remote-sensing/
    ├── index.md
    ├── carbon-flux/
    ├── weather-and-climate/
    ├── earth-observation/
    └── geospatial-foundation-models/
```

The carbon-flux section should connect:

- eddy-covariance measurements;
- flux footprints and observation support;
- remote-sensing upscaling;
- meteorological forcing;
- process constraints;
- spatiotemporal models;
- uncertainty and representativeness;
- cross-site generalization;
- evaluation datasets and protocols.

## User-specific carbon-flux work

Look for approved materials in:

- `inputs/survey-manuscript/`
- `inputs/user-materials/`

Before using them:

1. Check whether they are marked public, publication-approved, draft, or private.
2. Preserve exact authorship and publication status.
3. Do not infer missing metrics or claims.
4. Do not publish code or data not explicitly approved.
5. Clearly distinguish:
   - public literature;
   - repository synthesis;
   - user’s published work;
   - user’s unpublished or in-review work.

If approved source material is absent, create a neutral case-study framework with TODO fields and do not invent a FAT implementation or result.

## Resource chain

Create at least one verified end-to-end map:

```text
scientific question
→ measurement/observation process
→ physical prior
→ model integration mechanism
→ dataset
→ code
→ benchmark/evaluation
→ limitations
```

## Specialty navigation

Generate views for:

- carbon-flux papers by method;
- flux-footprint resources;
- remote-sensing datasets;
- carbon-flux code and reproducibility status;
- observation-operator methods;
- geoscience benchmark gaps.

## Scientific safeguards

- Do not state that EC directly measures GPP or ecosystem respiration; describe partitioning correctly when relevant.
- Distinguish measurement footprint from a fixed pixel/window.
- Distinguish optical observability from causal process control.
- Do not overstate 30 m spatial products as validated field-level truth without evidence.
- Preserve units and sign conventions.
- Document site-level leakage and spatial generalization concerns.
- Avoid presenting a private method as an established community standard.

## Acceptance criteria

- All claims are cited or marked as synthesis.
- User materials are handled according to publication status.
- At least one end-to-end verified resource map exists.
- The specialty track links back to the main taxonomy rather than creating a separate incompatible taxonomy.
- Phase report status is `PASS`.

## Commit

`phase(09): build geoscience and carbon-flux specialty track`
