import pandas as pd


# ==========================================
# 1. Load PROCESSED dataset
# ==========================================

file_path = (
    "data/processed/4340_Penha2010_processed.csv"
)

df = pd.read_csv(file_path)


# ==========================================
# 2. Basic information
# ==========================================

print("\n" + "=" * 70)
print("BASIC DATASET INFORMATION")
print("=" * 70)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")


# ==========================================
# 3. Descriptive statistics
# ==========================================

print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS")
print("=" * 70)

print(
    df[
        [
            "Tempering temperature (ºC)",
            "Tempering time (s)",
            "Tempering time (h)",
            "Final hardness (HRC) - post tempering"
        ]
    ].describe().to_string()
)


# ==========================================
# 4. Unique temperatures
# ==========================================

print("\n" + "=" * 70)
print("TEMPERATURE DISTRIBUTION")
print("=" * 70)

temperature_counts = (
    df["Tempering temperature (ºC)"]
    .value_counts()
    .sort_index()
)

print(temperature_counts.to_string())


# ==========================================
# 5. Unique times
# ==========================================

print("\n" + "=" * 70)
print("TIME DISTRIBUTION")
print("=" * 70)

time_counts = (
    df["Tempering time (s)"]
    .value_counts()
    .sort_index()
)

print(time_counts.to_string())


# ==========================================
# 6. Hardness statistics
# ==========================================

print("\n" + "=" * 70)
print("FINAL HARDNESS")
print("=" * 70)

hardness = df["Final hardness (HRC) - post tempering"]

print(f"Minimum : {hardness.min():.2f} HRC")
print(f"Maximum : {hardness.max():.2f} HRC")
print(f"Mean    : {hardness.mean():.2f} HRC")
print(f"Median  : {hardness.median():.2f} HRC")
print(f"Std     : {hardness.std():.2f} HRC")


# ==========================================
# 7. Correlation
# ==========================================

print("\n" + "=" * 70)
print("CORRELATION MATRIX")
print("=" * 70)

correlation = df[
    [
        "Tempering temperature (ºC)",
        "Tempering time (s)",
        "Tempering time (h)",
        "Final hardness (HRC) - post tempering"
    ]
].corr()

print(correlation.round(3).to_string())


# ==========================================
# 8. Hardness by temperature
# ==========================================

print("\n" + "=" * 70)
print("HARDNESS BY TEMPERING TEMPERATURE")
print("=" * 70)

temperature_hardness = (
    df.groupby("Tempering temperature (ºC)")
    ["Final hardness (HRC) - post tempering"]
    .agg(["count", "min", "max", "mean", "std"])
)

print(
    temperature_hardness
    .round(2)
    .to_string()
)


# ==========================================
# 9. Hardness by tempering time
# ==========================================

print("\n" + "=" * 70)
print("HARDNESS BY TEMPERING TIME")
print("=" * 70)

time_hardness = (
    df.groupby("Tempering time (s)")
    ["Final hardness (HRC) - post tempering"]
    .agg(["count", "min", "max", "mean", "std"])
)

print(
    time_hardness
    .round(2)
    .to_string()
)