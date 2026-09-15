import pandas as pd


# ==========================================
# 1. Load RAW dataset
# ==========================================

file_path = (
    "data/raw/Tempering data for carbon and low alloy steels - Raiipa.csv"
)

df = pd.read_csv(file_path)


# ==========================================
# 2. Select AISI-SAE 4340
# ==========================================

steel = df[df["Steel type"] == "AISI-SAE 4340"].copy()


# ==========================================
# 3. Initial hardness by source
# ==========================================

print("\n" + "=" * 70)
print("INITIAL HARDNESS BY SOURCE")
print("=" * 70)

for source, group in steel.groupby("Source"):

    initial = group["Initial hardness (HRC) - post quenching"]

    known = (initial != "?").sum()
    unknown = (initial == "?").sum()

    print(f"\nSource: {source}")
    print(f"Records : {len(group)}")
    print(f"Known   : {known}")
    print(f"Unknown : {unknown}")


# ==========================================
# 4. Composition consistency
# ==========================================

composition_columns = [
    "C (%wt)",
    "Mn (%wt)",
    "P (%wt)",
    "S (%wt)",
    "Si (%wt)",
    "Ni (%wt)",
    "Cr (%wt)",
    "Mo (%wt)",
    "V (%wt)",
    "Al (%wt)",
    "Cu (%wt)"
]

print("\n" + "=" * 70)
print("COMPOSITION — AISI-SAE 4340")
print("=" * 70)

for column in composition_columns:

    unique_values = steel[column].nunique()
    minimum = steel[column].min()
    maximum = steel[column].max()

    print(
        f"{column:12} | "
        f"Unique: {unique_values:2} | "
        f"Range: {minimum} – {maximum}"
    )


# ==========================================
# 5. Composition consistency by source
# ==========================================

print("\n" + "=" * 70)
print("COMPOSITION VARIATION BY SOURCE")
print("=" * 70)

for source, group in steel.groupby("Source"):

    print(f"\nSOURCE: {source}")

    for column in composition_columns:

        unique_values = group[column].nunique()
        minimum = group[column].min()
        maximum = group[column].max()

        print(
            f"{column:12} | "
            f"Unique: {unique_values:2} | "
            f"Range: {minimum} – {maximum}"
        )


# ==========================================
# 6. Penha (2010) dataset check
# ==========================================

penha = steel[steel["Source"] == "Penha, 2010"].copy()

print("\n" + "=" * 70)
print("PENHA (2010) — FINAL CHECK")
print("=" * 70)

print(f"Records: {len(penha)}")


# ==========================================
# 7. Unique heat-treatment combinations
# ==========================================

unique_combinations = (
    penha[
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


# ==========================================
# 8. Final hardness completeness
# ==========================================

final_hardness = penha[
    "Final hardness (HRC) - post tempering"
]

missing_final = final_hardness.isna().sum()
question_final = (final_hardness == "?").sum()

print(f"Missing final hardness: {missing_final}")
print(f"'?' final hardness: {question_final}")


# ==========================================
# 9. Penha final hardness statistics
# ==========================================

print("\n" + "=" * 70)
print("PENHA (2010) — FINAL HARDNESS STATISTICS")
print("=" * 70)

print(f"Minimum : {final_hardness.min():.2f} HRC")
print(f"Maximum : {final_hardness.max():.2f} HRC")
print(f"Mean    : {final_hardness.mean():.2f} HRC")
print(f"Std     : {final_hardness.std():.2f} HRC")