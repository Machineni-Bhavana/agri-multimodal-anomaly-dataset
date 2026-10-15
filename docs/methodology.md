# Methodology

Complete this document after implementation and evaluation are verified.

## Randomness
The intended seed is 42 for all stochastic operations. Record every operation where randomness is used and verify that the seed is applied consistently.

## Pairing
Specify source fields used, compatibility rules, sampling algorithm, handling of unmatched records, and whether each pair is real or synthetic.

## Pseudo-label generation
Document each rule, threshold, source variable, and rationale. Avoid circular evaluation where labels are derived from the same features that the model is evaluated on.

## Data splitting
Specify train/validation/test strategy. Keep source images and duplicate/derived records grouped to prevent cross-split leakage. Fit preprocessing on training data only.

## Hyperparameters
Provide all model and training hyperparameters in the paper and in a machine-readable config.

## Reproducibility
Record dependency versions, source hashes, generated artifact hashes, and exact commands.
