# SAR and Microwave Remote Sensing

## 1. Why microwave is different

Synthetic-aperture radar is an active sensor: it transmits microwave energy and measures returned backscatter. The signal depends on surface/volume scattering rather than reflected sunlight.

This gives major advantages for cloud-covered regions and day/night acquisition, while introducing speckle and geometry-specific interpretation.

## 2. Key physical controls

Backscatter depends on:

- wavelength/frequency;
- polarization;
- incidence angle;
- dielectric properties;
- surface roughness;
- vegetation/water structure;
- moisture;
- orientation and geometry.

The same land cover can produce different signals under different moisture or viewing conditions.

## 3. Common polarizations

Examples: VV, VH, HH, HV.

Co- and cross-polarized responses encode different scattering behavior. Do not merge polarization channels without understanding their acquisition/product definitions.

## 4. Speckle

Coherent imaging produces multiplicative-looking granular variation. Processing may use multi-looking, filters, temporal averaging or models trained to exploit the statistical structure.

Over-smoothing can remove real fine-scale information.

## 5. Geometry

SAR-specific effects include:

- foreshortening;
- layover;
- radar shadow;
- terrain effects;
- orbit/view direction differences.

Terrain correction and accurate geolocation are critical before fusion with optical data.

## 6. Passive microwave

Radiometers measure naturally emitted microwave brightness temperatures. They often have coarse spatial resolution but can provide moisture/temperature-related information with frequent temporal coverage.

## 7. AI tasks

- crop/forest/land-cover mapping;
- flood/wetland monitoring;
- soil-moisture-related retrieval;
- biomass/structure estimation;
- change detection;
- optical-SAR fusion;
- gap filling under clouds.

## 8. Multimodal fusion

Optical and SAR contain complementary physics. Useful designs include modality-specific encoders followed by latent fusion or cross-attention instead of forcing the channels to behave identically.

## 9. Carbon relevance

SAR/microwave can add information on canopy structure, moisture and inundation that optical data may miss, especially in cloudy or wet environments. Their contribution should be tested with paired ablations and support-aware validation.
