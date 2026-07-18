# Phase 04 — Knowledge Base, Templates, and Learning Paths

## Goal

Create a coherent, citation-aware knowledge structure aligned with the survey without copying the survey into multiple locations.

## Required sections

```text
01-knowledge-base/
├── full-survey/
├── chapter-notes/
├── glossary/
├── tutorials/
├── learning-paths/
└── methods-at-a-glance/
```

## Source-of-truth rule

- The complete survey manuscript, when supplied by the user, is the authoritative long-form source.
- Chapter notes link to survey sections and provide study aids; they do not duplicate full paragraphs.
- Generated resource lists come from metadata.
- Handwritten synthesis must contain citations and provenance markers.

## Required templates

Create:

- `templates/paper-note-template.md`
- `templates/code-reproduction-template.md`
- `templates/dataset-card-template.md`
- `templates/benchmark-card-template.md`
- `templates/model-card-template.md`
- `templates/category-index-template.md`
- `templates/tutorial-template.md`
- `templates/claim-evidence-template.yaml`

## Glossary

Create the glossary structure and populate only terms that can be defined from reliable sources. Each term must contain:

- canonical term;
- aliases;
- concise definition;
- branch and method tags;
- closely related terms;
- common confusion;
- source IDs;
- status and verification date.

Initial terms should cover the repository taxonomy, including PINN, neural operator, DeepONet, FNO, differentiable simulator, equivariance, inverse problem, uncertainty quantification, world model, sim-to-real, and vision-language-action model. Do not force consensus where terminology varies; state ambiguity.

## Learning paths

Create role-based paths:

- newcomer to physics-informed AI;
- machine-learning researcher entering scientific computing;
- domain scientist entering AI;
- embodied-AI learner;
- geoscience and remote-sensing learner;
- reproducibility contributor.

Each path must list prerequisites, concepts, recommended resource IDs, and a realistic sequence. Do not present unverified resources.

## Tutorials

Create framework-agnostic foundational tutorials first:

- physical priors and where they enter a model;
- PDE and numerical-method prerequisites;
- loss constraints vs architectural constraints;
- operator learning;
- uncertainty and calibration;
- scientific evaluation beyond prediction error;
- reproducibility and fair comparison.

Tutorials must use original explanations, small lawful examples, and citations. Avoid pretending a toy result validates a real scientific model.

## Acceptance criteria

- Templates enforce provenance and status fields.
- No long duplicated survey passages.
- Glossary links resolve.
- Learning paths only reference verified records or explicitly marked internal tutorials.
- Claim audit passes.
- Phase report status is `PASS`.

## Commit

`phase(04): add knowledge templates and learning paths`
