import pandas as pd


# ==========================================
# 1. Load RAW dataset
# ==========================================

file_path = "data/raw/Tempering data for carbon and low alloy steels - Raiipa.csv"

df = pd.read_csv(file_path)


# ==========================================
# 2. Create material-wise heat-treatment summary
# ==========================================

summary = []

for steel, group in df.groupby("Steel type"):

    unique_temperatures = group["Tempering temperature (ºC)"].nunique()
    unique_times = group["Tempering time (s)"].nunique()

    unique_combinations = (
        group[
            [
                "Tempering temperature (ºC)",
                "Tempering time (s)"
            ]
        ]
        .drop_duplicates()
        .shape[0]
    )

    summary.append({
        "Steel type": steel,
        "Records": len(group),
        "Unique temperatures": unique_temperatures,
        "Unique times": unique_times,
        "Temperature × Time combinations": unique_combinations,
        "Minimum temperature (ºC)": group["Tempering temperature (ºC)"].min(),
        "Maximum temperature (ºC)": group["Tempering temperature (ºC)"].max(),
        "Minimum time (s)": group["Tempering time (s)"].min(),
        "Maximum time (s)": group["Tempering time (s)"].max()
    })


# ==========================================
# 3. Convert summary into DataFrame
# ==========================================

summary_df = pd.DataFrame(summary)


# ==========================================
# 4. Sort by number of heat-treatment
#    combinations
# ==========================================

summary_df = summary_df.sort_values(
    by="Temperature × Time combinations",
    ascending=False
)


# ==========================================
# 5. Display results
# ==========================================

print("\n" + "=" * 100)
print("MATERIAL-WISE HEAT-TREATMENT SUMMARY")
print("=" * 100)

print(
    summary_df.to_string(index=False)
)


# ==========================================
# 6. Display top candidates
# ==========================================

print("\n" + "=" * 100)
print("TOP MATERIALS BY HEAT-TREATMENT COMBINATIONS")
print("=" * 100)

print(
    summary_df.head(15).to_string(index=False)
)