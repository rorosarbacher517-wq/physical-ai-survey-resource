# Earth Foundation-model Pretraining and Adaptation

## 1. Foundation-model criterion

A large model becomes a useful Earth foundation model when pretraining creates transferable capability across tasks/regions/modalities/variables—not merely because parameter count is large.

## 2. Pretraining data axes

Record:

- geography;
- years/seasons;
- sensor/provider;
- spectral/modal variables;
- resolution;
- temporal cadence;
- missing-data policy;
- sampling balance;
- license/access.

## 3. Objectives

### Masked modeling
Hide spatial/spectral/temporal tokens and reconstruct them.

### Contrastive learning
Pull related observations/views/modalities together and separate unrelated examples.

### Temporal prediction
Predict future/neighboring observations or latent states.

### Multimodal generation
Predict one Earth-observation modality from others.

### Forecast pretraining
Predict future physical fields across broad geophysical datasets.

## 4. Tokenization

Possible tokens:

- image patches;
- spectral groups;
- time steps;
- atmospheric grid cells/levels;
- modality-specific latent tokens.

Token design determines compute and what scale is preserved.

## 5. Adaptation

- frozen embeddings;
- linear probe;
- task head;
- LoRA/parameter-efficient tuning;
- full fine-tuning;
- multi-task fine-tuning.

Report which protocol produced each result.

## 6. Geolocation leakage

Location/time embeddings can aid Earth modeling but can also let a model memorize regional priors. Evaluate held-out geography/time.

## 7. Physics after pretraining

Task adaptation can add observation operators, conservation losses, process modules or DA rather than assuming pretraining already encodes all required physical constraints.
