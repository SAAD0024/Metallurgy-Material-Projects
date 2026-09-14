# Machine Learning Prediction of Tempered Hardness in AISI-SAE 4340 Steel

A materials-engineering machine-learning project for predicting the final hardness of AISI-SAE 4340 steel after tempering using tempering temperature and time.

## Project overview

This project investigates the relationship between tempering temperature, tempering time, and final Rockwell C hardness (HRC). The workflow compares interpretable regression models with tree-based machine-learning models and uses grouped temperature validation to test generalization across unseen tempering temperatures.

The final selected model is an interaction linear regression using:

- Tempering temperature (°C)
- `log10(tempering time)` (s)
- Temperature × `log10(tempering time)` interaction

## Dataset

- Material: AISI-SAE 4340 steel
- Observations: 51
- Tempering temperatures: 100–700 °C
- Tempering times: 10–86,400 s
- Target: Final hardness after tempering (HRC)
- Primary subset: Penha (2010)

The model-ready processed subset is provided in `data/processed/4340_Penha2010_processed.csv`. The broader Raiipa dataset is documented in `data/README.md`; the full raw source file is not duplicated in this repository.

## Methodology

1. Data inspection and cleaning
2. Exploratory analysis of hardness versus temperature and time
3. Log transformation of tempering time
4. Temperature × log-time interaction feature engineering
5. Baseline linear regression comparison
6. Decision Tree comparison
7. Random Forest comparison
8. Gradient Boosting comparison
9. Hyperparameter tuning of tree-based models
10. Grouped temperature cross-validation
11. Pooled grouped-CV model comparison
12. Residual and largest-error analysis
13. Marginal-effect and interaction-response analysis
14. Final model selection

## Model comparison

Grouped temperature cross-validation was used as the primary robustness evaluation because individual observations at the same tempering temperature are related. The final comparison was:

| Model | Grouped MAE (HRC) | Grouped RMSE (HRC) | Grouped R² |
|---|---:|---:|---:|
| Gradient Boosting | 2.364 | 3.605 | 0.897 |
| Tuned Gradient Boosting | 2.403 | 3.615 | 0.896 |
| **Model C — Interaction Linear Regression** | **2.404** | **2.990** | **0.929** |
| Random Forest | 2.419 | 3.754 | 0.888 |
| Tuned Random Forest | 2.423 | 3.754 | 0.888 |
| Temperature + log10(Time) | 2.889 | 3.978 | 0.875 |
| Decision Tree | 2.914 | 4.275 | 0.855 |
| Temperature + Raw Time | 3.584 | 4.721 | 0.823 |

Model C achieved the highest grouped-CV R² and the lowest grouped-CV RMSE among the evaluated models, while maintaining a highly interpretable analytical form. Gradient Boosting achieved a slightly lower grouped-CV MAE, so Model C is selected for the project because of the combined accuracy, interpretability, and interaction insight rather than because it is best on every metric.

## Final model

**Model C — Interaction Linear Regression**

Features:

`Temperature + log10(Time) + Temperature × log10(Time)`

Regression equation:

```text
HRC = 62.109275
      - 0.021445 × Temperature
      + 0.041507 × log10(Time)
      - 0.009068 × Temperature × log10(Time)
```

### Validation performance

| Evaluation | MAE (HRC) | RMSE (HRC) | R² |
|---|---:|---:|---:|
| Random 80/20 test | 1.977 | 2.291 | 0.944 |
| Pooled grouped-temperature CV | **2.404** | **2.990** | **0.929** |

The grouped-temperature CV result is treated as the more informative estimate of generalization because each test fold contains an entire tempering temperature that was excluded from model fitting.

## Metallurgical interpretation

The model indicates that hardness decreases with increasing tempering temperature and that the effect of tempering time depends on temperature. The temperature coefficient becomes increasingly negative as `log10(time)` increases, demonstrating a temperature–time interaction rather than two independent additive effects.

The interaction-response analysis shows progressively lower predicted hardness for longer tempering times, with the separation between time conditions increasing as temperature rises.

These model relationships describe the observed dataset and should not be interpreted as a replacement for metallurgical theory, experimental validation, standards, or process qualification.

## Error analysis

Across the 51 pooled grouped-CV predictions:

- Mean absolute error: approximately 2.404 HRC
- Maximum absolute error: approximately 8.049 HRC
- Largest errors occur mainly at the high-temperature end, particularly around 700 °C.

This indicates that the model captures the overall tempering trend well but has greater difficulty with some high-temperature observations and extreme hardness changes.

## Figures

The project includes six final figures:

1. Hardness versus tempering temperature
2. Hardness versus log10(tempering time)
3. Actual versus predicted hardness
4. Residuals versus tempering temperature
5. Model C interaction response
6. Model comparison using pooled grouped-CV MAE

## Results

Final result tables are provided under `data/results/`:

- `final_model_comparison.csv`
- `final_model_summary.csv`
- `model_comparison.csv`
- `model_C_grouped_CV_predictions.csv`
- `model_C_residuals_by_temperature.csv`
- `model_C_largest_errors.csv`

## Project structure

```text
heat-treatment-ml/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── README.md
│   ├── processed/
│   │   └── 4340_Penha2010_processed.csv
│   ├── raw/
│   └── results/
│       ├── final_model_comparison.csv
│       ├── final_model_summary.csv
│       ├── model_C_grouped_CV_predictions.csv
│       ├── model_C_largest_errors.csv
│       ├── model_C_residuals_by_temperature.csv
│       └── model_comparison.csv
├── figures/
├── notebooks/
│   └── 4340_heat_treatment_ML.ipynb
└── src/
```

## Technologies

Python · NumPy · pandas · Matplotlib · scikit-learn · Jupyter Notebook

## Reproducibility

1. Create a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Place the permitted source dataset in the appropriate local data directory if reproducing the full preprocessing workflow.
4. Open `notebooks/4340_heat_treatment_ML.ipynb`.
5. Run the notebook from top to bottom.

Generated result tables are stored in `data/results/`, and recruiter-facing figures are stored in `figures/`.

## Status

**Completed:** exploratory analysis, feature engineering, model comparison, tree-model tuning, grouped temperature validation, residual diagnostics, marginal-effect analysis, interaction-response analysis, final model selection, result tables, figures, and reproducibility documentation.

## Disclaimer

For educational, analytical, and research purposes. Predictions should not replace experimental testing, engineering standards, heat-treatment specifications, or qualified metallurgical judgment.
