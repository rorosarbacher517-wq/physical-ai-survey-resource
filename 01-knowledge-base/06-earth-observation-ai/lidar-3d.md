# LiDAR and 3D Vegetation Structure

## 1. Measurement principle

LiDAR measures distance from travel time of emitted laser pulses.

```text
laser pulse
→ target interaction
→ returned energy / waveform
→ range
→ 3D point or vertical structure
```

Airborne and spaceborne systems differ in footprint, sampling pattern and waveform/product structure.

## 2. Point-cloud representation

A point may contain:

```text
[x, y, z, intensity, return_number, class, ...]
```

The raw point cloud is irregular and can contain millions of points.

## 3. Derived vegetation structure

Common products/features:

- canopy height;
- height percentiles;
- canopy cover;
- vertical density/profile;
- gap fraction;
- terrain/elevation;
- structural heterogeneity.

These are derived from point/waveform measurements and preprocessing choices.

## 4. AI representations

### Rasterized structure
Convert metrics to `[C,H,W]` and fuse with imagery.

### Point-based
Use point-set networks or local neighborhood models.

### Voxel/sparse 3D
Discretize space and use sparse convolutions.

### Cross-modal latent fusion
Encode 2D optical and 3D structure separately then fuse.

## 5. Temporal mismatch

LiDAR campaigns can be infrequent while optical/meteorological/flux data are continuous. A structure map may be treated as static over a period only if disturbance/growth assumptions are reasonable.

## 6. Spatial alignment

Check:

- CRS;
- horizontal/vertical datum;
- point density;
- ground classification;
- raster cell definition;
- overlap with optical valid pixels;
- footprint/support.

Small geolocation errors can matter near forest edges or heterogeneous patches.

## 7. Carbon-cycle relevance

3D structure provides information related to biomass, canopy height, roughness and vertical organization. It can complement spectral signals, but it does not guarantee better flux prediction when sample size is small or structure varies weakly within the evaluated domain.

## 8. Evaluation design

Compare optical-only versus optical+LiDAR under identical site/time splits and training budgets. Report where 3D helps by ecosystem, structural heterogeneity and sample density.
