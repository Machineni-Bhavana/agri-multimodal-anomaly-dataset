# Data Card

## Overview
Describe the derived dataset and research question after implementation is verified.

## Source datasets
- Smart Farming Data 2024 (SF24): https://www.kaggle.com/datasets/datasetengineer/smart-farming-data-2024-sf24
- UAV Weed Dataset 25: https://www.kaggle.com/datasets/datasetengineer/uav-weed-dataset-25
- PlantVillage Dataset (Kaggle mirror): https://www.kaggle.com/datasets/arjuntejaswi/plant-village

## Composition
Fill in only after running the audit: exact source versions, file names, row/image counts, columns, and hashes.

## Pairing and labels
Document whether links are observed or synthetic, pairing criteria, seed, pseudo-label rules, and known limitations. Do not describe heuristic pseudo-labels as ground truth.

## Intended use
Research into weakly supervised agricultural anomaly detection and cross-modal inconsistency, subject to validation.

## Limitations
- Source datasets may not share farm, time, location, or sample identifiers.
- Domain shifts, class imbalance, label noise, and synthetic pairing bias may affect results.
- Results on synthetic pairings do not establish performance on real farm deployments.

## Licensing and access
Record the license and attribution requirements for each source independently. Do not redistribute source files without confirming permission.
