# Machine Learning Prediction of Steel Yield Strength

A materials-focused machine learning project for predicting steel yield strength from alloy chemistry, processing conditions, heat-treatment states, and validated temperature information.

## Project Status

Completed core modeling and validation workflow.

## Dataset

- 1,943 unique records after cleaning and deduplication
- Target: Yield strength (MPa)
- Core model: 28 engineered features
- Temperature-augmented model: 32 features
- Independent holdout: 1,554 training samples / 389 testing samples

## Methodology

1. Data cleaning and duplicate removal
2. Processing-condition feature engineering
3. Heat-treatment state encoding
4. Temperature extraction and missing-value handling
5. Baseline model comparison
6. Random Forest hyperparameter optimization
7. 5-fold cross-validation
8. Independent holdout evaluation
9. Residual and strength-range error analysis
10. Random Forest and permutation feature-importance analysis

## Final Model

The final model is a temperature-augmented Random Forest regressor. The optimized parameters were:

- `n_estimators = 495`
- `max_depth = 30`
- `max_features = 0.75`
- `min_samples_leaf = 1`
- `min_samples_split = 7`

## Final Independent Holdout Performance

| Metric | Result |
|---|---:|
| MAE | **89.03 MPa** |
| RMSE | **138.46 MPa** |
| R² | **0.7993** |

## Leakage-Free 5-Fold Cross-Validation

| Metric | Mean | Std. Dev. |
|---|---:|---:|
| MAE | **91.27 MPa** | 2.25 MPa |
| RMSE | **139.61 MPa** | 3.61 MPa |
| R² | **0.7878** | 0.0181 |

## Temperature Feature Impact

Compared with the core Random Forest on the same independent holdout, adding temperature-related features produced:

- MAE improvement: **2.21 MPa (2.42%)**
- RMSE improvement: **0.91 MPa (0.65%)**
- R² improvement: **0.0026 (0.33%)**

The improvement is modest, indicating that heat-treatment state and alloy chemistry carry most of the predictive signal in this dataset, while explicit temperature information provides additional but limited information.

## Most Important Features

The leading Random Forest features in the final temperature-augmented model were:

1. `is_tempered`
2. `Fe`
3. `P`
4. `is_aged`
5. `Mo`
6. `Mn`
7. `C`
8. `is_quenched`
9. `Ni`
10. `Si`

Permutation importance also identified tempering state, Fe, C, P, quenching state, and aging state among the strongest contributors.

## Interpretation

The model captures a meaningful relationship between steel chemistry, processing state, and yield strength. Performance is strongest in the lower and mid-strength ranges and becomes less consistent for sparsely represented high-strength materials. Error analysis shows that limited high-strength samples are an important source of prediction uncertainty.

## Technologies

Python, pandas, NumPy, scikit-learn, Matplotlib, Jupyter Notebook

## Disclaimer

This project is intended for educational, analytical, and research purposes. Predictions should not replace experimental testing, engineering standards, or qualified materials-engineering judgment.
