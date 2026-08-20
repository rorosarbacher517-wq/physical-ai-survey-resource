# 13 · 2026-08-20 Scientific / Earth AI Snapshot

> This page contains only **fast-moving developments with primary/official sources**. Stable concepts belong in the earlier modules.

## 1. ECMWF AIFS is an operational AI forecasting system, now on v2

ECMWF's Artificial Intelligence Forecasting System includes deterministic **AIFS Single** and probabilistic **AIFS ENS**. ECMWF reports that the deterministic system became operational on 2025-02-25, the ensemble on 2025-07-01, and both were upgraded to v2 on **2026-05-12**.

Why it matters: AI weather forecasting is no longer only an experimental benchmark; it is part of an operational center's production forecasting stack.

Primary: https://www.ecmwf.int/en/forecasts/datasets/aifs-machine-learning-data

## 2. WeatherNext 2 is Google DeepMind/Research's current weather-model family

The official WeatherNext page describes WeatherNext 2 as its most accurate AI weather forecasting technology, with deterministic/probabilistic weather products and cyclone-focused capabilities exposed through research and Google products.

Why it matters: the direction is moving from single research models toward deployable model families and task-specific weather systems.

Primary: https://deepmind.google/science/weathernext/

## 3. NVIDIA Earth-2 is becoming an end-to-end open weather AI stack

NVIDIA announced an expanded Earth-2 family of open models/tools in January 2026, covering global data assimilation, medium-range forecasting, nowcasting and downscaling, together with PhysicsNeMo/Earth2Studio tooling.

Why it matters: the frontier is no longer only the forecast backbone; observation processing, DA, forecast, generative downscaling and deployment are being connected into one stack.

Primary: https://blogs.nvidia.com/blog/nvidia-earth-2-open-models/
Primary platform: https://www.nvidia.com/en-us/high-performance-computing/earth-2/

## 4. Aurora established the Earth-system foundation-model pattern

Microsoft Research's **Aurora** was published in *Nature* in 2025 as a foundation model trained on more than one million hours of geophysical data and fine-tuned to multiple Earth-system forecasting tasks.

Why it matters: pretraining/fine-tuning across heterogeneous geophysical data is a distinct paradigm from training one forecast model on one reanalysis task.

Primary: https://www.microsoft.com/en-us/research/publication/aurora-a-foundation-model-for-the-earth-system/

## 5. AlphaEarth Foundations shifts EO toward global embedding fields

Google DeepMind introduced AlphaEarth Foundations in July 2025 and released annual Satellite Embedding data through Google Earth Engine. The official description emphasizes integrating multi-source Earth observations into a unified geospatial representation.

Why it matters: downstream Earth applications can increasingly consume pretrained geospatial embeddings instead of training every representation from raw imagery.

Primary: https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/ <!-- manual-review: official source URL path -->

## 6. TerraMind pushes EO toward multimodal any-to-any generation

IBM and ESA open-sourced TerraMind in 2025. The official repository describes it as an any-to-any generative foundation model for Earth observation and provides fine-tuning and cross-modal generation workflows.

Why it matters: EO foundation models are evolving from single-modality encoders toward multimodal representation + generation systems.

Primary: https://github.com/IBM/terramind
Paper: https://arxiv.org/abs/2504.11171

## 7. Prithvi-EO-2.0 remains a practical HLS foundation-model reference

NASA-IMPACT's official repository describes Prithvi-EO-2.0 as trained on global HLS time-series samples at 30 m resolution, with released pretrained models and fine-tuning examples.

Why it matters: it directly links a widely used harmonized remote-sensing product to reusable EO pretraining.

Primary: https://github.com/NASA-IMPACT/Prithvi-EO-2.0

## 8. The major methodological trend in weather AI is “forecast-only → full system”

Current official systems increasingly cover multiple stages:

```text
observations
→ learned / hybrid data assimilation
→ deterministic + probabilistic forecast
→ nowcasting / extremes
→ downscaling
→ operational serving
```

Repository synthesis based on the operational AIFS and Earth-2 developments above.

## 9. The major methodological trend in EO is “single sensor encoder → multimodal planetary representation”

The direction visible in Prithvi-EO, TerraMind and AlphaEarth includes:

- larger geographic diversity;
- temporal pretraining;
- multi-sensor/multimodal fusion;
- reusable embedding fields;
- cross-modal generation;
- fewer labeled examples per downstream task.

The open question is how well these representations transfer to process-sensitive targets such as carbon flux, hydrology and extremes rather than only mapping/segmentation benchmarks.

## 10. Carbon-cycle AI: the high-value frontier is observation-aware multimodality

For terrestrial carbon, the most important future integration is not simply a bigger image backbone. The research stack increasingly needs:

```text
2D EO + 3D structure + meteorology + EC observations
→ observation/support matching
→ process constraints
→ spatiotemporal model
→ site/biome/OOD evaluation
→ uncertainty propagation
```

This is a repository synthesis and research agenda, not a claim about one specific model.

## What to track next

1. learned data assimilation from heterogeneous observations;
2. probabilistic/generative weather ensembles;
3. physically constrained Earth foundation models;
4. multimodal EO foundation models with time and 3D structure;
5. Earth-system models that join atmosphere-land-ocean components;
6. carbon/water/energy coupled AI;
7. support-aware observation operators for sparse field observations;
8. high-resolution downscaling with calibrated extremes;
9. OOD/climate-regime evaluation;
10. scientific agents that operate simulators, geospatial tools and reproducible workflows.

### Update discipline

Verify the official paper/repository/product page before changing this snapshot. Do not infer hidden architecture, training data or benchmark details that the primary source does not disclose.
