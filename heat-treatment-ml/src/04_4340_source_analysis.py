import pandas as pd


# ==========================================
# 1. Load RAW dataset
# ==========================================

file_path = "data/raw/Tempering data for carbon and low alloy steels - Raiipa.csv"

df = pd.read_csv(file_path)


# ==========================================
# 2. Select AISI-SAE 4340
# ==========================================

steel = df[df["Steel type"] == "AISI-SAE 4340"].copy()


# ==========================================
# 3. Source-wise summary
# ==========================================

print("\n" + "=" * 80)
print("SOURCE-WISE SUMMARY — AISI-SAE 4340")
print("=" * 80)

source_summary = (
    steel.groupby("Source")
    .agg(
        Records=("Final hardness (HRC) - post tempering", "count"),
        Min_Temperature=("Tempering temperature (ºC)", "min"),
        Max_Temperature=("Tempering temperature (ºC)", "max"),
        Unique_Temperatures=("Tempering temperature (ºC)", "nunique"),
        Min_Time=("Tempering time (s)", "min"),
        Max_Time=("Tempering time (s)", "max"),
        Unique_Times=("Tempering time (s)", "nunique"),
    )
)

print(source_summary.to_string())


# ==========================================
# 4. Source-wise temperature values
# ==========================================

print("\n" + "=" * 80)
print("TEMPERATURES BY SOURCE")
print("=" * 80)

for source, group in steel.groupby("Source"):

    temperatures = sorted(
        group["Tempering temperature (ºC)"].unique()
    )

    print(f"\nSOURCE: {source}")
    print(f"Temperatures ({len(temperatures)}):")
    print(temperatures)


# ==========================================
# 5. Source-wise time values
# ==========================================

print("\n" + "=" * 80)
print("TEMPERING TIMES BY SOURCE")
print("=" * 80)

for source, group in steel.groupby("Source"):

    times = sorted(
        group["Tempering time (s)"].unique()
    )

    print(f"\nSOURCE: {source}")
    print(f"Times ({len(times)}):")
    print(times)


# ==========================================
# 6. Source-wise heat-treatment combinations
# ==========================================

print("\n" + "=" * 80)
print("NUMBER OF UNIQUE HEAT-TREATMENT COMBINATIONS BY SOURCE")
print("=" * 80)

for source, group in steel.groupby("Source"):

    combinations = (
        group[
            [
                "Tempering temperature (ºC)",
                "Tempering time (s)"
            ]
        ]
        .drop_duplicates()
        .shape[0]
    )

    print(f"{source}: {combinations} combinations")


# ==========================================
# 7. Hardness statistics by source
# ==========================================

print("\n" + "=" * 80)
print("FINAL HARDNESS BY SOURCE")
print("=" * 80)

hardness_summary = (
    steel.groupby("Source")["Final hardness (HRC) - post tempering"]
    .agg(["count", "min", "max", "mean", "std"])
)

print(hardness_summary.to_string())