# Carbon-flux Data Stack

## 1. Tower targets

Typical sources:

- FLUXNET;
- AmeriFlux;
- regional flux networks.

Record target definition, partitioning product, QC and sign convention.

## 2. Optical Earth observation

Potential products:

- HLS;
- Landsat;
- Sentinel-2;
- MODIS/VIIRS.

Useful for canopy state, phenology, spectral traits and disturbance.

## 3. Meteorology / reanalysis

Potential variables:

- air/dew-point temperature;
- pressure;
- radiation;
- precipitation;
- wind;
- soil temperature/moisture;
- boundary-layer/stability variables.

Important: accumulated variables require correct temporal conversion before resampling.

## 4. Soil moisture

In situ, reanalysis or microwave products such as SMAP can provide water-availability information at different supports/resolutions.

## 5. 3D structure

Airborne/spaceborne LiDAR can provide canopy height/profile and terrain structure.

## 6. SIF and thermal

Complement spectral reflectance with photosynthesis-related radiative information and surface-temperature/energy information.

## 7. Static context

- soil properties;
- topography;
- land cover/biome;
- disturbance history;
- management when available.

## 8. Sample unit

A robust dataset defines a unique sample ID such as:

`site + date/time + sensor acquisition + product versions`

For daily optical + half-hour flux modeling, explicitly document how one image is shared/interpolated across sub-daily time steps.

## 9. Alignment checklist

- CRS and pixel grid;
- timezone/UTC;
- temporal support;
- quality masks;
- valid-pixel fraction;
- tower/footprint geometry;
- missing-data policy;
- split membership;
- normalization computed from train data.

## 10. Repository resources

Use [datasets](../../04-dataset-library/index.md) for canonical source records and licenses.
