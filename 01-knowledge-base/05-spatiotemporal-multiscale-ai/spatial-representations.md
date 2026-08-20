# Spatial Representations

## 1. Raster/grid

Tensor `[B,C,H,W]` or `[B,T,C,H,W]`.

Natural for satellite imagery and latitude-longitude fields. CNNs are efficient, but Earth geometry and varying cell area require care.

## 2. Spherical grid

Global data have periodic longitude and polar distortion. Options include spherical harmonics, mesh grids, cubed-sphere/icosahedral representations and geometry-aware positional encoding.

## 3. Graph/mesh

`nodes [N,D]`, edges encode adjacency/geometry.

Useful for irregular numerical meshes, station networks, river networks and global spherical graphs.

## 4. Point set

LiDAR or particle data:

`[B,N,C]`

Order should not change the physical meaning. PointNet-style pooling, local neighborhoods or sparse voxelization can be used.

## 5. Patch/token

Split a large field/image into patches and map each to an embedding.

Token count scales with area/resolution. High-resolution global data require hierarchical/sparse/token-compression strategies.

## 6. Spectral representation

Fourier/spherical-harmonic modes describe large-scale smooth structure compactly. High-frequency local extremes may require spatial/local pathways.

## 7. Coordinate encoding

Potential coordinates:

- x/y/z;
- lat/lon;
- elevation;
- pressure level;
- time;
- sensor geometry.

Coordinate features help geometry but can leak location identity.

## 8. Representation choice

Choose based on topology, resolution, periodicity, local/global interactions, invariance and computational budget.
