# Phase 15 acceptance report — Chinese-first systematic Earth/Scientific AI knowledge base

Status: `PASS`

Date: 2026-08-20

## Objective

将知识层从英文概览型 Scientific/Physical AI 文档进一步重构为**中文主解释、英文专业术语保留、从底层基础到 Earth-system 前沿逐层展开**的系统知识库，同时保持 canonical metadata、taxonomy 和已有资源路径兼容。

## Scope completed

### 1. Repository-wide learning architecture

- 重写根 `README.md`、knowledge-base 总览、learning paths、detailed index 和 MkDocs navigation；
- 明确真实学习依赖：`Math/Numerics → ML/DL → Physical AI Core → Physics-informed/Operators → Inverse/DA/UQ → Spatiotemporal/Multimodal → Earth domains → Foundation Models → Data/HPC/Evaluation → Cross-domain Physical AI`；
- 保留原目录编号以避免破坏已有链接，但明确编号不再代表唯一学习顺序；
- 增强 `KNOWLEDGE_UNIT_STANDARD.md`，要求核心知识页覆盖 scientific problem、observation model、shape/unit、math/physics、architecture、training、inference/rollout、compute、evaluation、failure modes 和 sources。

### 2. Chinese-first content policy

- explanation、comparison、failure modes、research questions 采用中文；
- model names、paper titles、dataset/product names、variables、equations、tensor shapes、code/API/library names、standard metrics 保持英文或原始形式；
- 不为已有稳定英文术语创造生硬中文译名；
- closed/internal architecture 未公开时使用 `unknown / not publicly disclosed` 原则，不补猜测。

### 3. Foundations and Scientific ML

- 重写 linear algebra、probability、optimization、ODE/PDE、numerical methods、dimensional analysis、scale/support；
- 重写 classical ML、deep-learning architectures、Transformer/GNN、PyTorch/JAX/HPC basics；
- 重写 Observation Operator、conservation/symmetry/dimensional priors、hybrid modeling；
- 重写 PINN fundamentals、optimization failure modes、hard/soft constraints；
- 重写 Neural Operator、surrogates/hybrid solvers、differentiable simulation；
- 将 Inverse Problems / Data Assimilation / UQ 在学习依赖上提前到 Earth-system applications 之前；
- 重写 spatiotemporal、multiscale、multimodal 和 support-aware learning。

### 4. Earth Observation / Remote Sensing

形成完整链：

`physical state → sensing physics → product/data stack → QA/preprocessing → retrieval/inverse → time series → multisensor fusion → task model/FM → geospatial/OOD validation`。

新增或系统重写：

- radiative transfer / observation physics；
- EO data stack；
- Optical / Hyperspectral；
- SAR / Microwave；
- LiDAR / 3D；
- Thermal / SIF；
- preprocessing / QA / resampling / leakage；
- remote-sensing time series；
- retrieval / inverse problems；
- multisensor fusion；
- super-resolution / reconstruction；
- EO tasks/models；
- EO foundation models；
- geospatial validation / OOD。

重点区分 downloadable encoder 与 embedding-as-data 两种 foundation-model interface，并覆盖 Prithvi-EO-2.0、TerraMind、AlphaEarth Foundations、TESSERA、MaRS 和 PANGAEA。

### 5. Terrestrial Carbon / Carbon Flux

形成完整链：

`carbon processes → GPP/RECO/NEE → EC → partitioning → dynamic footprint → multimodal predictors → process constraints → footprint observation operator → tower supervision → tower-to-grid → extremes/OOD/UQ`。

系统重写：

- carbon-cycle processes；
- Eddy Covariance；
- flux partitioning uncertainty；
- flux footprints；
- carbon data stack；
- carbon modeling methods；
- carbon–water–energy coupling；
- process-constrained carbon AI；
- tensor-level footprint-aware AI；
- multimodal carbon AI；
- tower-to-grid upscaling；
- climate/extreme response；
- validation/uncertainty。

明确：GPP/RECO 通常是 partitioned/inferred targets；EC tower coordinate 不等于 point-support flux；output grid resolution 不等于 independent validation support。

### 6. Weather / Climate AI

将 weather track 从模型列表扩展为完整 forecast system：

`atmospheric dynamics → observing system → observation operators/QC → DA/analysis → initial state → forecast backbone → rollout → probabilistic ensemble → data-to-forecast → nowcasting/downscaling → extremes → climate/coupling → verification`。

新增：

- Atmospheric State & Dynamics；
- Weather Observing System；
- Weather Rollout & Training；
- Data-to-Forecast。

系统重写：

- NWP basics；
- weather DA；
- AI weather-model families；
- Physics–ML hybrid weather；
- probabilistic/ensemble weather；
- nowcasting；
- downscaling；
- extremes；
- climate AI；
- Earth-system coupling；
- weather foundation models；
- verification/evaluation。

模型按 scientific role 分类而非 leaderboard：FourCastNet、GraphCast、Pangu-Weather、FuXi、FengWu、NeuralGCM、GenCast、AIFS、WeatherNext 2、Aardvark Weather、FuXi Weather、Aurora。

### 7. Earth / Geospatial Foundation Models

按 interface 分类：

1. downloadable pretrained encoder；
2. ready-made global embedding field / embedding-as-data；
3. dynamical Earth-system foundation model。

系统重写 pretraining、multimodal representations、model-family guide 和 evaluation，强调 label efficiency、pretraining overlap、geographic/temporal/sensor OOD、process-sensitive regression 和 adaptation protocol。

### 8. Data/HPC/Evaluation and cross-domain breadth

- 重写 scientific data engineering、distributed scientific ML 和 evaluation/benchmarking；
- 强调 sample manifest、units、CRS、chunking、split provenance、foundation-pretraining overlap、compute-normalized evaluation；
- 保留并重写 fluids/aerodynamics、energy/materials、digital twins/embodied Physical AI；
- 新增 Biomedical Mechanics，补齐 taxonomy 中较弱的 biomedical scientific-AI 知识支线。

### 9. Dated 2026-08-20 snapshot

Fast-moving facts 被集中到 `13-2026-snapshot/index.md`，并显式区分：

- `Official`；
- `Peer-reviewed`；
- `Preprint`。

截至 2026-08-20 的重点包括：

- ECMWF AIFS Single v2 / AIFS ENS v2 operational status；
- WeatherNext 2 current/open updates；
- Aurora 1.5；
- NVIDIA Earth-2 open weather stack；
- Aardvark Weather / FuXi Weather data-to-forecast systems；
- NeuralGCM precipitation extension；
- AlphaEarth annual Satellite Embedding dataset；
- TESSERA v2 preprint；
- MaRS AAAI 2026；
- PANGAEA and current Earth-FM evaluation direction；
- WorldTensor；
- Chu et al. 2026 footprint synthesis；
- recent footprint-aware carbon modeling；
- process-constrained joint carbon learning；
- ML-assisted terrestrial-carbon process-model parameter optimization；
- cutoff 前的新 ecohydrology foundation-model preprint，明确标记为 preprint 而非 settled consensus。

## Source and evidence policy applied

- fast-moving claims 优先 original paper、DOI、official institution documentation、official model/project/data pages；
- preprint 与 peer-reviewed publication 分开标记；
- official product/version facts 与 repository synthesis 分开；
- promotional wording 不改写为 scientific conclusion；
- official AlphaEarth URL 中若出现 repository risky-claim regex 词，仅对 URL path 使用 `manual-review` marker；
- canonical paper/code/dataset/benchmark metadata 未因本阶段写作而修改。

## Invariants preserved

- `metadata/*.yaml` 仍是 resource layer source of truth；
- `metadata/taxonomy.yaml` 未改；
- generated paper/code/dataset/benchmark views 未手工修改；
- root README resource-count generated markers 保留；
- existing resource IDs 未改变或复制；
- existing paths 尽量保持兼容，仅新增必要的 knowledge pages。

## Manual review completed

- branch is based on current `main` and remains ahead without known divergence；
- new navigation paths and new-page references were written against the current branch tree；
- risky-claim vocabulary was intentionally avoided in authored prose；
- current/version-specific claims were isolated in the dated snapshot wherever practical；
- output resolution, observation support and validation support are explicitly separated across EO/carbon/weather pages；
- weather pages distinguish reanalysis/analysis initialization, raw observations, forecast core, ensemble and verification；
- carbon pages distinguish processed NEE from partitioned GPP/RECO and distinguish footprint operator from footprint-as-feature；
- Earth FM pages distinguish downloadable weights from hosted/precomputed embedding products。

## CI fixes during PR validation

Initial PR CI run `#55` failed only on two repository risky-claim regex hits:

- `best-quality composite` in `eo-preprocessing-quality.md`；
- `channel-first` in `pytorch-jax-hpc-basics.md`。

They were rewritten to neutral technical wording (`quality-prioritized composite` and `channels-leading/channels-trailing layout`) without changing the scientific meaning。

## Acceptance gates

- [x] root architecture is bottom-up and dependency-based；
- [x] knowledge explanations are Chinese-first while technical names remain English；
- [x] Earth Observation track is systematic from observation physics to FM/OOD；
- [x] Carbon track is systematic from process/EC/footprint to upscaling/extremes/UQ；
- [x] Weather/Climate track is systematic from observing system/DA/NWP to AI forecast/ensemble/climate/evaluation；
- [x] fast-moving snapshot is current through 2026-08-20 and based primarily on original/official sources；
- [x] `python -m scripts.full_check` observed as passing；
- [x] external-link verification observed as passing；
- [x] no broken internal links reported by final CI；
- [x] no generated-file drift reported by final CI；
- [x] no unsupported fast-moving claims reported by final repository checks。

## Validation evidence

PR #2 validation run `#59` (`workflow run ID 32383345850`) completed successfully after the two wording fixes above。

Successful steps included:

- `python -m scripts.full_check` → success；
- `python -m scripts.verify_external_links --respect-cache --report` → success。

This phase therefore satisfies the repository acceptance gates and is marked `PASS`。
