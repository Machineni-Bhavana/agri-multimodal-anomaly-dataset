# Agri Multimodal Anomaly Dataset

Reproducible research artifacts for weakly supervised agricultural anomaly detection using three public source datasets:

1. [Smart Farming Data 2024 (SF24)](https://www.kaggle.com/datasets/datasetengineer/smart-farming-data-2024-sf24)
2. [UAV Weed Dataset 25](https://www.kaggle.com/datasets/datasetengineer/uav-weed-dataset-25)
3. [PlantVillage Dataset (Kaggle mirror)](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)

## Research scope

This repository investigates whether cross-modal inconsistencies across smart-farming features, UAV weed-related features, and plant-health imagery can support weakly supervised agricultural anomaly detection.

**Important:** the source datasets do not necessarily describe the same farms, locations, or timestamps. Unless genuine linkage identifiers are available and verified, cross-source pairings must be treated as synthetic pairings, not real-world multimodal observations. Any pseudo-labels must be documented as heuristic labels, not ground truth.

## Repository status

This is a reproducibility scaffold. Replace this notice with the verified implementation details before citing the repository as a completed release. Do not claim results, sample counts, or completed tests until reproduced.

## Data access and licensing

Download each dataset from its original source and follow its current terms, attribution requirements, and redistribution restrictions. This repository does not redistribute raw datasets by default.

## Reproducibility

- Intended random seed: `42`
- Record the seed used for pairing, image sampling, splitting, and model initialization.
- Record package versions, source file hashes, preprocessing configuration, and generated pairing-table hash.
- Use group-aware or source-aware splits where applicable; ensure derived copies of the same source image or record cannot cross splits.
- Fit preprocessing and feature transformations on training data only.

## Expected artifacts

- `reports/dataset_audit.md`: verified source audit
- `data/processed/unified_metadata.csv`: derived metadata and source provenance
- `data/processed/pairing_table.csv`: generated pairing table, if permitted and appropriate
- `configs/dataset_config.yaml`: paths and preprocessing configuration
- `docs/data_card.md`: dataset composition, intended use, limitations, and licensing
- `docs/methodology.md`: pairing, pseudo-labeling, split, and evaluation protocol

## Setup

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the audit

Set local dataset paths in `configs/dataset_config.yaml`, then run:

```bash
python src/audit_sources.py --config configs/dataset_config.yaml
```

## Paper citation

Once the repository is public and the contents are reviewed, cite the stable URL:

`https://github.com/<YOUR-GITHUB-USERNAME>/agri-multimodal-anomaly-dataset`

For a more stable archival citation, create a release and archive the release through Zenodo, then cite its DOI.

## Citation

Please cite the associated paper once its bibliographic details are final. A `CITATION.cff` file should be completed before release.
