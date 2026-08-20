# Thermal Infrared and Solar-induced Fluorescence

## 1. Thermal infrared

Thermal sensors observe emitted radiation related to surface temperature and emissivity.

Retrieval is affected by:

- atmospheric absorption/emission;
- surface emissivity;
- viewing geometry;
- mixed pixels;
- cloud contamination.

Land-surface temperature can inform evapotranspiration, energy balance and heat/water stress, but it is not identical to air temperature or canopy temperature in every situation.

## 2. Energy-balance connection

A simplified surface-energy budget:

```text
Rn = H + LE + G + storage terms
```

where net radiation is partitioned among sensible heat, latent heat, ground heat and storage. Thermal observations can constrain parts of this system when combined with meteorology and surface properties.

## 3. Solar-induced chlorophyll fluorescence

SIF is a weak radiative signal emitted by chlorophyll after absorption of sunlight.

It is related to photosynthetic processes but depends on multiple steps:

```text
incident light
→ absorption by chlorophyll
→ photochemical / non-photochemical / fluorescence pathways
→ canopy escape / radiative transfer
→ sensor observation
```

Therefore SIF and GPP can be strongly related without being identical quantities.

## 4. Scale and retrieval

Satellite SIF products often have coarser native footprints than high-resolution optical imagery. Regridding does not create fine-scale independent SIF observations.

## 5. AI uses

- GPP estimation;
- drought/heat response;
- crop stress;
- energy-water-carbon coupling;
- data assimilation;
- multimodal representation learning.

## 6. Fusion

A useful carbon stack can combine:

```text
reflectance → canopy state/phenology
SIF         → photosynthesis-related radiative signal
thermal     → surface energy/stress
meteorology → environmental forcing
LiDAR       → structure
```

Each modality should retain its observation meaning and native support.
