# Results

## Final reported holdout comparison

| Model | MAE (MPa) | RMSE (MPa) | R² |
|---|---:|---:|---:|
| Core Random Forest | 91.24 | 139.37 | 0.7966 |
| Temperature-Augmented Random Forest | **89.03** | **138.46** | **0.7993** |

## Leakage-free 5-fold CV

- MAE: **91.27 ± 2.25 MPa**
- RMSE: **139.61 ± 3.61 MPa**
- R²: **0.7878 ± 0.0181**

## Temperature impact

- MAE improvement: **2.21 MPa (2.42%)**
- RMSE improvement: **0.91 MPa (0.65%)**
- R² improvement: **0.0026 (0.33%)**

The final analysis also includes actual-vs-predicted plots, residual analysis, strength-range error analysis, Random Forest feature importance, and permutation importance.
