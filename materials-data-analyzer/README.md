# Materials Data Analyzer

A beginner-friendly Python project for exploring materials engineering tensile-test data.

## Important data notice

The included CSV file is **synthetic example data** created for learning and demonstration. Its values are illustrative only. They are not real experimental measurements and must not be used for engineering design, safety decisions, production release, or material certification.

## Project structure

```text
materials-data-analyzer/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   └── tensile_test_results.csv
│   └── processed/
├── notebooks/
│   └── exploratory_analysis.ipynb
├── analysis.py
└── plotting.py
```

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the requirements:

```bash
pip install -r requirements.txt
```

## Run the analysis

From the project directory, run:

```bash
python analysis.py
```

The script prints descriptive statistics and material comparisons. It also writes summary tables to `data/processed/` and saves plots to `data/processed/plots/`.

To use a different CSV file:

```bash
python analysis.py path\to\your\tensile_test_results.csv
```

Your CSV should include these columns:

- `specimen_id`
- `material`
- `test_condition`
- `yield_strength_mpa`
- `ultimate_tensile_strength_mpa`
- `elongation_percent`
- `hardness_hv`

## Analyses and plots

The project calculates counts, means, medians, standard deviations, minimums, and maximums for each material. It also compares average yield strength, ultimate tensile strength, elongation, and hardness. The strength plots show mean +/- sample standard deviation; SD represents specimen-to-specimen variability, not measurement uncertainty.

It generates:

- Average yield-strength and ultimate-tensile-strength bar charts with mean +/- sample standard deviation and specimen counts
- `measurement_distributions.png`: Four unit-correct panels showing individual specimen points and material means for yield strength, ultimate tensile strength, elongation, and hardness
- A yield-strength versus elongation scatter plot with an exploratory Pearson correlation coefficient and sample count
- A hardness-versus-ultimate-tensile-strength scatter plot with an exploratory Pearson correlation coefficient and sample count

These measurements are summary tensile-test results, so the project does not generate full stress-strain curves. That would require raw force and displacement measurements.

## Notebook

Open `notebooks/exploratory_analysis.ipynb` in VS Code or Jupyter for a step-by-step version of the workflow.
