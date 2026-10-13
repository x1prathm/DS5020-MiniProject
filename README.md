# DS-5020 Mini-Project 01: Customers Like You

Product recommendations and exploratory customer segmentation for GiftLane using PCA and truncated SVD. Individual submission covering both Data Engineer and ML Engineer roles.

## Success targets
- Reduce storage and measure recommendation runtime.
- Compare hit rate at 10 against best sellers on unseen purchases.
- Compare PCA and SVD at the same component count.
- Describe 3–6 customer groups without exposing customer IDs.

## Data
Download [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) and place the workbook at `data/raw/online_retail_II.xlsx`. Both yearly sheets are required: 1,067,371 invoice lines in total.

Source: Chen, D. (2012). Online Retail II. [DOI](https://doi.org/10.24432/C5CG6D). License: CC BY 4.0. The `data/` folder is excluded from Git.

## Run
Use Python 3.12. From the repository folder:

```bash
python -m pip install -r requirements.txt
```

Open `analysis.ipynb` in VS Code with the Python and Jupyter extensions. Select the environment containing these packages and run every cell from top to bottom. This rebuilds the matrix and exports the reports and figures.

## Approach
Clean invalid transactions and non-product entries. Reserve the last two months for testing. Retain products bought by at least 10 training customers and build a sparse matrix using log-transformed total quantities. Fit SVD and PCA with 50 components and evaluate new-to-customer purchases.

## Results
- Matrix: 5,482 customers × 3,690 products; 97.95% sparse.
- Storage: 161.83 MB dense, 5.00 MB sparse, 3.67 MB SVD factors.
- Hit rate at 10: SVD 22.30%, PCA 22.25%, best sellers 17.38%.
- Evaluation: 1,910 customers; 71.45% of new test pairs were eligible.
- Recommendation generation: 2.29 seconds, excluding preparation, fitting, and saving.
- Four exploratory customer groups; purchasing activity strongly influences the map.

Timings vary by machine and run. New customers and excluded products are not covered by this evaluation.

## Files
- `analysis.ipynb`: complete analysis and export steps.
- `requirements.txt`: package versions.
- `reports/`: profiles, cleaning log, matrix report, evaluation and comparison.
- `figures/`: compression curve and named customer map.
- `data/processed/`: locally generated matrix, index maps and split files.