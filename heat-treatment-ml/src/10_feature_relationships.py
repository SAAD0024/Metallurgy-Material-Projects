import pandas as pd
import numpy as np


# ==========================================
# 1. Load PROCESSED dataset
# ==========================================

file_path = (
    "data/processed/4340_Penha2010_processed.csv"
)

df = pd.read_csv(file_path)


# ==========================================
# 2. Create log10(time)
# ==========================================

df["log10_time"] = np.log10(
    df["Tempering time (s)"]
)


# ==========================================
# 3. Create temperature × log(time)
#    interaction feature
# ==========================================

df["temperature_x_log_time"] = (
    df["Tempering temperature (ºC)"]
    * df["log10_time"]
)


# ==========================================
# 4. Correlation with hardness
# ==========================================

hardness_column = (
    "Final hardness (HRC) - post tempering"
)

correlations = df[
    [
        "Tempering temperature (ºC)",
        "Tempering time (s)",
        "log10_time",
        "temperature_x_log_time",
        hardness_column
    ]
].corr()[hardness_column]


# ==========================================
# 5. Display results
# ==========================================

print("\n" + "=" * 70)
print("FEATURE RELATIONSHIP WITH FINAL HARDNESS")
print("=" * 70)

print(
    correlations
    .sort_values(ascending=False)
    .round(3)
    .to_string()
)


# ==========================================
# 6. Feature ranges
# ==========================================

print("\n" + "=" * 70)
print("CANDIDATE FEATURE RANGES")
print("=" * 70)

print(
    f"Temperature      : "
    f"{df['Tempering temperature (ºC)'].min():.1f} – "
    f"{df['Tempering temperature (ºC)'].max():.1f} °C"
)

print(
    f"Time             : "
    f"{df['Tempering time (s)'].min():.0f} – "
    f"{df['Tempering time (s)'].max():.0f} s"
)

print(
    f"log10(Time)      : "
    f"{df['log10_time'].min():.3f} – "
    f"{df['log10_time'].max():.3f}"
)

print(
    f"Temperature × "
    f"log10(Time)     : "
    f"{df['temperature_x_log_time'].min():.2f} – "
    f"{df['temperature_x_log_time'].max():.2f}"
)


# ==========================================
# 7. Show candidate ML features
# ==========================================

print("\n" + "=" * 70)
print("CANDIDATE ML FEATURE SETS")
print("=" * 70)

print("\nBaseline:")
print("  X = [Temperature, Time]")

print("\nLog-time:")
print("  X = [Temperature, log10(Time)]")

print("\nInteraction:")
print("  X = [Temperature, log10(Time),")
print("       Temperature × log10(Time)]")