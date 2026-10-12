# DS-5020 Mini-Project 01: Customers Like You

Build product recommendations and a customer-group map for GiftLane using retail purchases. Compare PCA and truncated SVD for compression, recommendation quality, storage, and runtime.

## Role
Individual submission covering both Data Engineer and ML Engineer tasks.

## Data
[UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii): both yearly sheets, approximately 1.07 million transaction lines. Place `online_retail_II.xlsx` in `data/raw/`; `data/` is excluded from Git.

Source: Chen, D. (2012). Online Retail II [Dataset]. [DOI](https://doi.org/10.24432/C5CG6D). License: CC BY 4.0.

## Success targets
- Reduce storage compared with the dense purchase matrix; also report sparse storage.
- Measure fit time and nightly recommendation runtime.
- Evaluate hit rate at 10 against a best-seller baseline using held-out purchases.
- Create 3–6 named customer groups without displaying customer IDs.
- Compare PCA and SVD on the same training matrix at the same selected component count.

## Status
Setup complete; analysis pending. Requirements and run instructions will be added when the code is ready.
