# Phase 06 — Code Library and Reproduction System

## Goal

Create a code index that distinguishes official implementations, community reproductions, framework examples, and user-originated work, then demonstrate the reproduction standard with safe runnable examples.

## Code categories

Use controlled values:

- `official-implementation`
- `author-maintained`
- `community-reproduction`
- `framework-example`
- `repository-original`
- `reference-only`

Never label a repository official without direct evidence.

## Metadata workflow

For each codebase:

1. Verify canonical URL.
2. Record related paper IDs.
3. Inspect repository license.
4. Record language/framework.
5. Record environment files and installation method.
6. Record latest verified release/commit date without implying active maintenance.
7. Record archived status.
8. Record tests, examples, pretrained weights, and dataset scripts when present.
9. Record reproducibility level:
   - L0 link only;
   - L1 environment documented;
   - L2 demo runs;
   - L3 core result approximately reproduced;
   - L4 full reported result reproduced;
   - L5 independent extension and diagnostic validation.
10. Never assign L2–L5 unless the commands were actually run and logs are stored.

## Reproduction project template

Create a standard project template containing:

```text
README.md
LICENSE
CITATION.cff
pyproject.toml or environment.yml
configs/
src/
scripts/
tests/
results/
assets/
REPRODUCTION.md
KNOWN_ISSUES.md
```

## Runnable examples

Provide at least:

- one small PINN example;
- one small operator-learning example;
- one physics-constrained time-series or spatial example.

Requirements:

- synthetic or clearly licensed tiny data;
- CPU-capable smoke test;
- deterministic seed;
- expected metrics;
- explicit statement that the example is pedagogical and not a reproduction of a full scientific result;
- tests for physical residual or constraint behavior;
- no hard-coded local paths.

## Framework demos

Framework demos must point to official docs and use minimal dependencies. Do not maintain copied vendor tutorials when a link and a small adapter are safer.

## User original work

For carbon-flux or FAT-related code:

- use only user-supplied, publication-approved material;
- otherwise create an interface specification and placeholder case-study page;
- never invent model code, results, author list, paper status, or downloadable weights;
- keep private materials out of Git.

## Acceptance criteria

- All code records have license status.
- Official/community status is evidence-backed.
- Runnable examples pass in a clean environment.
- Reproduction levels match stored evidence.
- No code is copied in violation of license.
- Phase report status is `PASS`.

## Commit

`phase(06): add code index and reproducibility system`
