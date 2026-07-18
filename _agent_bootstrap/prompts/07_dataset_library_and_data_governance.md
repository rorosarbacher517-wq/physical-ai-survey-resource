# Phase 07 — Dataset Library and Data Governance

## Goal

Create verified dataset cards and lawful download/preprocessing guidance without storing large or restricted raw data.

## Dataset card requirements

Each dataset card must include:

- official name and stable ID;
- provider;
- official landing page;
- DOI or provider identifier;
- domain and supported tasks;
- modalities and variables;
- spatial and temporal coverage, only when verified;
- spatial and temporal resolution, only when verified;
- access procedure;
- license or terms-of-use link;
- redistribution policy;
- citation requirement;
- known quality flags and missing-data considerations;
- related paper, code, and benchmark IDs;
- small-sample or fixture policy;
- last verification date.

## Priority coverage

Include verified resources across:

- synthetic PDE datasets;
- fluid simulation;
- energy/materials;
- climate and geoscience;
- remote sensing;
- eddy covariance and carbon flux;
- robotics and physical interaction.

For the geoscience track, cover relevant official providers such as flux networks, meteorological reanalysis, satellite harmonization products, land-cover products, fluorescence, soil moisture, lidar, and thermal data only where their inclusion is scientifically justified.

## Download guides

- Use official APIs and download portals.
- Never embed credentials.
- Use environment variables and `.env.example`.
- Respect authentication, rate limits, terms, and citation requirements.
- Provide checksum verification for small test fixtures.
- Provide resumable workflows when reasonable.
- Separate raw, interim, and processed data paths.
- Add a storage estimate before any large download.
- Do not auto-download very large data during CI.

## Data governance

Create:

- `data-governance.md`
- `data-directory-convention.md`
- `restricted-data-policy.md`
- `data-citation-guide.md`

Explain that public availability does not automatically permit redistribution.

## Acceptance criteria

- Every public dataset record has an official source.
- License/access status is explicit; unknown is not treated as open.
- No large raw dataset is committed.
- Download examples contain no secrets.
- Dataset relationships resolve.
- Phase report status is `PASS`.

## Commit

`phase(07): add verified dataset cards and governance`
