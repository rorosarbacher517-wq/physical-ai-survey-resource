# Deep-learning Architectures for Scientific Data

## 1. MLP

Input `[B,D] → hidden layers → output`.

Good for tabular/site variables or local parameterization. It has no built-in spatial topology.

## 2. CNN

For grid data:

```text
[B,C,H,W]
→ convolution
→ local feature maps
→ deeper receptive field
```

Inductive bias: local translation-shared filters.

Strengths: efficient spatial learning. Limitations: regular-grid assumption and global interactions may require depth/large kernels.

## 3. U-Net / encoder-decoder

Downsample to capture context, then upsample with skip connections for dense outputs.

Common for segmentation, downscaling, reconstruction and field-to-field prediction.

## 4. Recurrent models

RNN/LSTM/GRU maintain hidden state over time.

```text
x_t, h_{t-1} → h_t → y_t
```

Useful for moderate sequence lengths but less parallel than Transformer-style models.

## 5. Transformer

Typical scientific tensor after tokenization:

`[B,N,D]`

Self-attention:

```text
Q = XW_Q
K = XW_K
V = XW_V
Attention = softmax(QK^T / sqrt(d)) V
```

Global pairwise attention is powerful but naive cost scales roughly with `N²`.

Scientific adaptations may use local windows, factorized space/time attention, sparse attention, axial attention or hierarchical tokens.

## 6. GNN

Nodes represent grid cells, mesh vertices, stations or objects; edges encode neighborhood/interaction.

Message passing:

```text
m_ij = φ_e(h_i, h_j, e_ij)
h_i' = φ_v(h_i, aggregate_j m_ij)
```

Useful for irregular geometry and spherical meshes.

## 7. Generative models

Diffusion/score models learn distributions rather than one conditional mean. This is useful for weather ensembles, downscaling and stochastic unresolved processes.

## 8. Architecture selection

Ask:

- data topology?
- local versus long-range interactions?
- temporal horizon?
- resolution/token budget?
- deterministic versus probabilistic output?
- invariance/equivariance requirements?
- rollout stability?
- physical constraints?

Architecture should follow the structure of the scientific problem, not fashion.
