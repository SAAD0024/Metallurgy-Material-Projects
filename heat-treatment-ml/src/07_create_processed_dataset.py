import pandas as pd
from pathlib import Path


# ==========================================
# 1. File paths
# ==========================================

raw_file = Path(
    "data/raw/Tempering data for carbon and low alloy steels - Raiipa.csv"
)

processed_file = Path(
    "data/processed/4340_Penha2010_processed.csv"
)


# ==========================================
# 2. Load RAW dataset
# ==========================================

df = pd.read_csv(raw_file)


# ==========================================
# 3. Select AISI-SAE 4340
#    from Penha (2010)
# ==========================================

processed = df[
    (df["Steel type"] == "AISI-SAE 4340")
    & (df["Source"] == "Penha, 2010")
].copy()


# ==========================================
# 4. Keep only project-relevant columns
# ==========================================

processed = processed[
    [
        "Steel type",
        "Source",
        "Tempering temperature (ºC)",
        "Tempering time (s)",
        "Final hardness (HRC) - post tempering"
    ]
].copy()


# ==========================================
# 5. Create time in hours
#    while retaining original seconds
# ==========================================

processed["Tempering time (h)"] = (
    processed["Tempering time (s)"] / 3600
)


# ==========================================
# 6. Reorder columns
# ==========================================

processed = processed[
    [
        "Steel type",
        "Source",
        "Tempering temperature (ºC)",
        "Tempering time (s)",
        "Tempering time (h)",
        "Final hardness (HRC) - post tempering"
    ]
]


# ==========================================
# 7. Sort by temperature and time
# ==========================================

processed = processed.sort_values(
    [
        "Tempering temperature (ºC)",
        "Tempering time (s)"
    ]
).reset_index(drop=True)


# ==========================================
# 8. Quality checks
# ==========================================

print("\n" + "=" * 70)
print("PROCESSED DATASET QUALITY CHECK")
print("=" * 70)

print(f"Number of rows: {len(processed)}")
print(f"Number of columns: {len(processed.columns)}")

unique_combinations = (
    processed[
        [
            "Tempering temperature (ºC)",
            "Tempering time (s)"
        ]
    ]
    .drop_duplicates()
    .shape[0]
)

print(
    f"Unique temperature-time combinations: "
    f"{unique_combinations}"
)

missing_target = (
    processed["Final hardness (HRC) - post tempering"]
    .isna()
    .sum()
)

print(f"Missing final hardness: {missing_target}")

question_target = (
    processed["Final hardness (HRC) - post tempering"] == "?"
).sum()

print(f"'?' final hardness: {question_target}")


# ==========================================
# 9. Save PROCESSED dataset
# ==========================================

processed_file.parent.mkdir(
    parents=True,
    exist_ok=True
)

processed.to_csv(
    processed_file,
    index=False
)


# ==========================================
# 10. Display first observations
# ==========================================

print("\n" + "=" * 70)
print("FIRST 10 ROWS OF PROCESSED DATASET")
print("=" * 70)

print(
    processed.head(10).to_string(index=False)
)


# ==========================================
# 11. Confirm output file
# ==========================================

print("\n" + "=" * 70)
print("OUTPUT")
print("=" * 70)

print(f"Saved to: {processed_file}")