"""Analyze the synthetic tensile-test dataset."""

from pathlib import Path
import sys

import pandas as pd

from plotting import create_all_plots


PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_PATH = PROJECT_DIR / "data" / "raw" / "tensile_test_results.csv"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"


REQUIRED_COLUMNS = {
    "specimen_id",
    "material",
    "test_condition",
    "yield_strength_mpa",
    "ultimate_tensile_strength_mpa",
    "elongation_percent",
    "hardness_hv",
}


def load_data(data_path: Path) -> pd.DataFrame:
    """Load the CSV file and check that the expected columns are present."""
    data = pd.read_csv(data_path)
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"CSV is missing required columns: {missing}")
    return data


def descriptive_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics grouped by material."""
    measurement_columns = [
        "yield_strength_mpa",
        "ultimate_tensile_strength_mpa",
        "elongation_percent",
        "hardness_hv",
    ]
    return data.groupby("material")[measurement_columns].agg(
        ["count", "mean", "median", "std", "min", "max"]
    ).round(2)


def compare_materials(data: pd.DataFrame) -> pd.DataFrame:
    """Return average measurements for a simple material comparison."""
    measurement_columns = [
        "yield_strength_mpa",
        "ultimate_tensile_strength_mpa",
        "elongation_percent",
        "hardness_hv",
    ]
    return data.groupby("material")[measurement_columns].mean().round(2)


def main(data_path: Path = DEFAULT_DATA_PATH) -> None:
    data = load_data(data_path)
    statistics = descriptive_statistics(data)
    comparison = compare_materials(data)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    statistics.to_csv(PROCESSED_DIR / "descriptive_statistics.csv")
    comparison.to_csv(PROCESSED_DIR / "material_comparison.csv")
    create_all_plots(data, PROCESSED_DIR / "plots")

    print("Descriptive statistics by material:")
    print(statistics)
    print("\nAverage material comparison:")
    print(comparison)
    print(f"\nSaved tables and plots to: {PROCESSED_DIR}")


if __name__ == "__main__":
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DATA_PATH
    main(input_path)
