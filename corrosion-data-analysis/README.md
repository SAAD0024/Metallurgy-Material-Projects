# Corrosion Data Analysis

Machine-learning analysis of the **NIST CORR-DATA** corrosion database using Python, pandas, scikit-learn, and Jupyter.

## Project goal

Build a transparent baseline model for predicting NIST corrosion-resistance ratings (**A, B, C, D**) and investigate how material, environment, concentration, and temperature contribute to classification.

## Data source

The project uses the NIST CORR-DATA database:

- NIST PDR: https://data.nist.gov/pdr/lps/54AE54FB37AC022DE0531A570681D4291851
- Official dataset archive: https://opendata.nist.gov/1851/CORR-DATA_Database.zip
- Field definitions: https://opendata.nist.gov/od/ds/54AE54FB37AC022DE0531A570681D4291851/CORR-DATA-fields.txt

The database contains more than 24,000 corrosion observations from more than 250 source documents.

The raw CSV is intentionally not committed to this repository. Download it from the official NIST source and place it at `data/CORR-DATA_Database.csv` before running the notebook.

## Workflow

1. Inspect the raw NIST data.
2. Clean material/environment text fields.
3. Extract clear A/B/C/D corrosion ratings.
4. Preserve the original NIST values while creating safe numerical features.
5. Parse clear numerical temperature and concentration ranges.
6. Treat concentration values above 100 as unavailable for the numerical Vol-% feature rather than changing the source values.
7. Use training-set medians for missing numerical values and add missing-value indicators.
8. Train Random Forest classification models.
9. Compare random stratified validation with a strict unseen-reference holdout.

## Model results

| Model | Accuracy | Macro F1 | Weighted F1 |
|---|---:|---:|---:|
| Baseline | 63.84% | 0.541 | 0.658 |
| + Concentration | 66.04% | 0.543 | 0.672 |
| + Concentration + Temperature | **78.35%** | **0.701** | **0.789** |

Adding temperature produced the largest improvement in the random stratified split.

### Important validation finding

The random split is not enough to estimate generalization to a new source document. **Reference #253 accounts for 79.35% of all rated observations.**

A strict holdout was therefore performed:

- Train on 3,436 observations from all other known references.
- Test on all 13,210 observations from Reference #253.
- The strict test achieved **39.54% accuracy** and **0.26 Macro F1**.

This large gap indicates that the 78.35% random-split result should be interpreted as performance within the overall dataset distribution, not as guaranteed performance on a previously unseen source.

Reference #253 also has a very different composition: only 25 unique materials but 219 unique environments. In the strict test, 72.61% of observations had a material category not seen in the other references, and 39.28% had an unseen environment category.

## Key model finding

For the Model 3 Random Forest, the strongest reported features included:

- `concentration_mid`
- `temperature_mid_c`
- `temperature_missing`
- several specific chemical environments
- material-family indicators

Feature importance is used as a model diagnostic and **does not establish causation**.

## Repository structure

```text
corrosion-data-analysis/
├── data/
│   └── processed/          # generated outputs are created locally
├── notebooks/
│   └── 01_data_exploration.ipynb
├── results/
│   ├── model_comparison.csv
│   ├── model3_feature_importance_top20.csv
│   ├── validation_comparison.csv
│   └── reference_253_diagnostics.csv
├── src/
├── .gitignore
├── README.md
└── requirements.txt
```

## Limitations

- The source database is highly uneven across references.
- A large proportion of concentration and temperature values are missing or qualitative.
- Random-split performance can be optimistic when related observations occur across train and test sets.
- The strict Reference #253 holdout is unusually difficult because the training set is much smaller and has a substantially different category distribution.
- The current Random Forest is a baseline model, not a production corrosion prediction system.

## Status

**Completed:** data cleaning, feature preparation, three-model comparison, feature-importance analysis, and strict reference-based validation.

**Next:** improve validation design and investigate models/features that generalize better across source references.
