# Transformer and GNN for Scientific Data

## 1. Why Transformer helps

Attention can connect distant positions directly, which is useful for atmospheric teleconnections, long temporal dependencies and multimodal fusion.

But a scientific token needs semantics beyond a word token.

Possible token meanings:

- image patch;
- grid cell;
- vertical atmospheric column;
- station;
- mesh node;
- time step;
- sensor observation;
- latent field block.

## 2. Position and geometry

Standard sequence position is insufficient for many Earth tasks. Models may need:

- latitude/longitude;
- spherical distance;
- elevation/pressure level;
- time-of-day/season;
- sensor geometry;
- relative spatial displacement.

Encoding absolute coordinates can also create geographic memorization, so OOD evaluation is required.

## 3. Factorized attention

For tensor `[B,T,N,D]`, full attention over `T×N` can be expensive.

Alternatives:

- spatial then temporal attention;
- temporal then spatial;
- local windows + global tokens;
- hierarchical patching;
- sparse neighborhoods;
- cross-attention between modalities.

## 4. GNN for physical fields

Graphs separate topology from tensor layout.

Applications:

- weather on spherical/icosahedral meshes;
- river networks;
- station networks;
- finite-element meshes;
- molecular/material graphs.

## 5. Message-passing depth

A node receives information from neighbors; multiple layers increase graph receptive field. Too many layers can cause over-smoothing or inefficient propagation over global graphs.

Multi-scale graphs or encoder-process-decode architectures can accelerate long-range interactions.

## 6. Equivariance

A model is equivariant if transforming the input produces a predictable transformation of the output.

This matters for rotations, translations, permutations and 3D physical systems.

## 7. Transformer versus GNN

| Question | Transformer | GNN |
|---|---|---|
| topology | token sequence/set | explicit edges |
| global interaction | direct but expensive | usually multi-hop/hierarchical |
| irregular mesh | possible | natural |
| multimodal fusion | strong | possible but less standard |
| geometry | encoded in positions/bias | encoded in graph/edges |

Hybrid graph-attention systems are common when both irregular geometry and global context matter.
