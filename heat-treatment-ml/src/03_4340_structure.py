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
# 3. Source distribution
# ==========================================

print("\n" + "=" * 70)
print("AISI-SAE 4340 — SOURCE DISTRIBUTION")
print("=" * 70)

print(steel["Source"].value_counts().to_string())


# ==========================================
# 4. Exact tempering temperatures
# ==========================================

print("\n" + "=" * 70)
print("AISI-SAE 4340 — TEMPERING TEMPERATURES")
print("=" * 70)

temperatures = sorted(
    steel["Tempering temperature (ºC)"].unique()
)

print(temperatures)
print(f"Number of temperatures: {len(temperatures)}")


# ==========================================
# 5. Exact tempering times
# ==========================================

print("\n" + "=" * 70)
print("AISI-SAE 4340 — TEMPERING TIMES")
print("=" * 70)

times = sorted(
    steel["Tempering time (s)"].unique()
)

print(times)
print(f"Number of times: {len(times)}")


# ==========================================
# 6. Convert time to hours for readability
# ==========================================

print("\n" + "=" * 70)
print("TEMPERING TIMES — HOURS")
print("=" * 70)

times_hours = sorted(
    steel["Tempering time (s)"].unique() / 3600
)

for seconds, hours in zip(times, times_hours):
    print(f"{seconds:8.0f} seconds  =  {hours:.3f} hours")


# ==========================================
# 7. Final hardness statistics
# ==========================================

print("\n" + "=" * 70)
print("FINAL HARDNESS — AISI-SAE 4340")
print("=" * 70)

hardness = steel["Final hardness (HRC) - post tempering"]

print(f"Minimum : {hardness.min():.2f} HRC")
print(f"Maximum : {hardness.max():.2f} HRC")
print(f"Mean    : {hardness.mean():.2f} HRC")
print(f"Std     : {hardness.std():.2f} HRC")


# ==========================================
# 8. Temperature × Time combinations
# ==========================================

print("\n" + "=" * 70)
print("TEMPERATURE × TIME COMBINATIONS")
print("=" * 70)

combinations = (
    steel[
        [
            "Tempering temperature (ºC)",
            "Tempering time (s)"
        ]
    ]
    .drop_duplicates()
    .sort_values(
        [
            "Tempering temperature (ºC)",
            "Tempering time (s)"
        ]
    )
)

print(combinations.to_string(index=False))


# ==========================================
# 9. Initial hardness availability
# ==========================================

print("\n" + "=" * 70)
print("INITIAL HARDNESS AVAILABILITY")
print("=" * 70)

initial = steel["Initial hardness (HRC) - post quenching"]

print(f"Known values : {(initial != '?').sum()}")
print(f"Unknown (?)  : {(initial == '?').sum()}")