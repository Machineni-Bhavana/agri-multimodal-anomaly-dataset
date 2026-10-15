# Agri-Multimodal Anomaly Dataset

**A Reproducible Research Framework for Weakly Supervised Agricultural Anomaly Detection**

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Research%20in%20Progress-orange)]()
[![Reproducibility](https://img.shields.io/badge/Random%20Seed-42-brightgreen)]()

## Overview

This repository provides a research framework for investigating weakly supervised agricultural anomaly detection using three publicly available Kaggle datasets covering smart farming, UAV-based weed observations, and plant disease imagery.

The objective is to investigate whether information from heterogeneous agricultural data sources can support the identification of potentially anomalous patterns through reproducible data integration, carefully documented pairing strategies, and machine learning experiments.

The datasets originate from independent sources and are not assumed to represent the same farms, locations, or timestamps. Consequently, any cross-source pairings must be supported by verified linkage information or explicitly identified as synthetic.

**Research status:** The repository currently provides the initial project scaffold. Dataset auditing, integration, pairing-table generation, and experimental validation are intended development stages and must be completed before the corresponding artifacts are considered released.

## Source Datasets

### 1. Smart Farming Data 2024 (SF24)

- **Platform:** Kaggle
- **Source:** https://www.kaggle.com/datasets/datasetengineer/smart-farming-data-2024-sf24
- **Role:** Source of structured smart-farming observations and associated agricultural features, subject to verification of the downloaded schema.

### 2. UAV Weed Dataset 25

- **Platform:** Kaggle
- **Source:** https://www.kaggle.com/datasets/datasetengineer/uav-weed-dataset-25
- **Role:** Source of weed-related observations and UAV imagery or associated annotations, depending on the actual dataset structure.

### 3. PlantVillage Dataset (Kaggle mirror)

- **Platform:** Kaggle
- **Source:** https://www.kaggle.com/datasets/arjuntejaswi/plant-village
- **Role:** Source of plant leaf imagery and associated health or disease labels.

### Data access and licensing

Download the datasets from their respective sources. Review each dataset's license, attribution requirements, and redistribution permissions independently.

Raw source files are not included in this repository by default. Dataset users should follow the original providers' terms.

## Research Objectives

The project is intended to investigate the following questions:

1. How can heterogeneous agricultural datasets be represented through a consistent metadata and provenance schema?
2. Can documented cross-source pairing strategies support meaningful weakly supervised anomaly-detection experiments?
3. How sensitive are experimental findings to pairing assumptions, pseudo-label generation, and source-specific biases?
4. Can the resulting experimental pipeline be reproduced under a fixed random seed and documented configuration?

These are research questions, not established findings. Their validity will be assessed through implementation and evaluation.

## Methodology

The planned workflow consists of the following stages:

1. **Source auditing:** Inspect file formats, schemas, dimensions, labels, missing values, duplicates, and source versions.
2. **Source-specific preprocessing:** Clean structured data and inspect image files and their associated annotations without discarding source provenance.
3. **Metadata standardization:** Create consistent identifiers and source-specific feature representations.
4. **Pairing strategy:** Determine whether verified cross-source links exist. Where they do not, any synthetic pairing must be explicitly documented.
5. **Weak-label generation:** Define and record the rules used to derive heuristic labels, including thresholds and assumptions.
6. **Dataset splitting:** Create reproducible training, validation, and test manifests while preventing duplicate or derived samples from crossing split boundaries.
7. **Model evaluation:** Evaluate appropriate baselines and report metrics, limitations, and sensitivity to pairing and labeling assumptions.

No cross-source relationship is treated as a real-world observation unless supported by verified evidence.

## Repository Structure

```text
agri-multimodal-anomaly-dataset/
├── README.md
├── CITATION.cff
├── .gitignore
├── requirements.txt
├── configs/
│   └── dataset_config.yaml
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── splits/
├── docs/
│   ├── data_card.md
│   └── methodology.md
├── notebooks/
├── reports/
│   └── dataset_audit.md
├── src/
│   ├── audit_sources.py
│   └── build_unified_dataset.py
└── tests/
```

The `notebooks/` directory is reserved for exploratory analysis and may be added as implementation progresses.

## Installation

### Prerequisites

- Python 3.12 or later, subject to dependency compatibility
- Git
- Access to the source datasets

### 1. Clone the repository

```bash
git clone https://github.com/Machineni-Bhavana/agri-multimodal-anomaly-dataset.git
cd agri-multimodal-anomaly-dataset
```

### 2. Create a virtual environment

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Dataset Configuration and Audit

Download the three source datasets and place them in the corresponding local directories:

```text
data/raw/sf24/
data/raw/uav_weed_25/
data/raw/plantvillage/
```

Update `configs/dataset_config.yaml` if your local paths differ.

Run the source audit:

```bash
python src/audit_sources.py --config configs/dataset_config.yaml
```

The audit script inventories source files and inspects supported tabular files for dimensions, column names, missing values, duplicate rows, and file hashes.

Review `reports/dataset_audit.md` before defining the integration or pairing procedure.

**Note:** The current audit script is an initial utility, not a complete validation pipeline for every possible dataset format. Image-level checks and source-specific validation may require additional implementation.

## Reproducibility

The intended random seed is **42** for stochastic operations, including pairing, image sampling, data splitting, and model initialization.

Reproducibility requires more than specifying a seed. The completed implementation should also record:

- Source dataset versions and file hashes.
- Package and dependency versions.
- Pairing and pseudo-label generation rules.
- Preprocessing configuration.
- Train, validation, and test split manifests.
- Model hyperparameters and evaluation settings.
- Hashes or version identifiers for generated artifacts.

The implementation must be verified to use the seed consistently before full reproducibility is claimed.

## Data Integrity and Evaluation

The project will follow these principles:

- Preserve original source identifiers and labels.
- Distinguish observed relationships from synthetic pairings.
- Document heuristic pseudo-labels and their limitations.
- Prevent duplicates and related samples from leaking across data splits.
- Fit learned preprocessing transformations on training data only.
- Avoid circular evaluation in which labels are generated directly from the same features used to claim predictive performance.
- Report class imbalance, appropriate evaluation metrics, and sensitivity to methodological assumptions.

Synthetic pairings and heuristic labels do not constitute independently verified ground truth. Performance on such data alone cannot establish effectiveness in real agricultural deployments.

## Current Development Status

| Component | Status |
|---|---|
| Repository scaffold | Available |
| Source dataset references | Documented |
| Configuration template | Available |
| Initial tabular source-audit utility | Available |
| Complete source-specific preprocessing | In progress |
| Validated cross-source pairing pipeline | Not yet completed |
| Pairing table | Not yet released |
| Fully validated experimental results | Not yet established |

This status should be updated as each component is implemented, tested, and published.

## Citation

If you use the source datasets, cite the original providers according to their requirements.

For research that uses this repository, cite the associated publication once its bibliographic information is available.

**Repository:** https://github.com/Machineni-Bhavana/agri-multimodal-anomaly-dataset

## Limitations

The source datasets were collected independently and may differ in domain, collection procedure, labeling conventions, and representation. They may not share common farm identifiers, geographic coordinates, or timestamps.

Any synthetic integration may introduce assumptions and biases that affect downstream evaluation. Findings must therefore be interpreted in light of source provenance, pairing validity, label quality, and experimental design.

## Contributing

Contributions should preserve source attribution, document methodological decisions, include reproducible instructions, and add validation tests where appropriate.

## License

The repository's software license and the redistribution status of derived artifacts should be finalized after reviewing the terms of all source datasets. No blanket redistribution permission is implied by the public availability of the source datasets.
