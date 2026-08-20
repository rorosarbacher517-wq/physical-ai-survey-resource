# Terrestrial Carbon-cycle Processes for AI

## 1. Core ecosystem fluxes

### Gross primary productivity (GPP)
Carbon uptake through photosynthesis before subtracting ecosystem respiration.

### Ecosystem respiration (RECO)
Respiratory carbon release from autotrophic and heterotrophic processes.

### Net ecosystem exchange (NEE)
A commonly used convention is:

`NEE = RECO - GPP`

Negative NEE then indicates net ecosystem uptake. Dataset conventions must always be checked.

## 2. Process controls

### Radiation
Photosynthesis requires absorbed photosynthetically active radiation. Light response can saturate and interacts with canopy structure/phenology.

### Temperature
Influences enzymatic/photosynthetic processes and respiration rates.

### Water availability
Soil moisture and atmospheric dryness can constrain stomatal conductance and photosynthesis; severe water stress can also change respiration/substrate dynamics.

### Phenology and canopy state
Leaf area, greenness, pigment and canopy structure control the capacity to absorb light and exchange carbon/water.

### Disturbance/management
Fire, harvest, mowing, irrigation, fertilization and land-use change can alter fluxes abruptly.

## 3. Carbon-water-energy coupling

Photosynthesis and transpiration share stomatal controls, while surface energy determines temperature and evaporation. Carbon modeling can therefore benefit from coupled meteorological/hydrological information.

## 4. Time scales

- sub-daily light/turbulence response;
- daily weather;
- seasonal phenology;
- interannual climate variability;
- disturbance/recovery;
- long-term ecosystem change.

A model should not infer all scales from one static satellite image.

## 5. Spatial heterogeneity

Neighboring patches can differ in vegetation, soil moisture, management and flux. Dynamic EC footprints change their contribution to the tower measurement.

## 6. AI implication

Useful predictors represent both:

```text
capacity/state: vegetation + structure + soil
forcing: radiation + temperature + moisture + atmosphere
observation support: footprint / measurement mapping
```

This provides a more physical framing than feature-only regression.
