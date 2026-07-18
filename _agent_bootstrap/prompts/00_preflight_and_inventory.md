# Phase 00 — Preflight and Inventory

## Goal

Establish a safe, reproducible execution environment and understand the current repository before generating content.

## Required actions

1. Read all repository instructions.
2. Record:
   - operating system;
   - Python and Git versions;
   - available network access;
   - available browser/search/API tools;
   - current branch and remotes;
   - current file tree;
   - existing licenses;
   - existing user source materials;
   - files larger than 10 MB;
   - suspected secrets or private data.
3. Determine whether the repository is:
   - empty;
   - partially scaffolded;
   - already populated and requiring migration.
4. Create an inventory at `audits/repository-inventory.yaml`.
5. Create a migration risk report if existing content is present.
6. Establish `.gitignore` before running tools that may create caches.
7. Create the branch `build/v1-autonomous` unless already on it.
8. Do not generate scientific content in this phase.

## Required files

- `audits/state.yaml`
- `audits/active-plan.md`
- `audits/blockers.md`
- `audits/pending-verification.yaml`
- `audits/repository-inventory.yaml`
- `audits/phases/00-preflight.md`
- `.gitignore`

## Acceptance criteria

- No uncommitted user file has been modified or deleted.
- The inventory lists every top-level item.
- Private or secret-like files are identified and excluded.
- The execution environment and network limitations are documented.
- Git branch policy is active.
- Phase report status is `PASS`.

## Commit

`phase(00): establish safe build inventory`
