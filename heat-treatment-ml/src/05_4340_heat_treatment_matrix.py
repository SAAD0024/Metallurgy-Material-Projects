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
# 3. Analyze each source separately
# ==========================================

for source, group in steel.groupby("Source"):

    print("\n" + "=" * 80)
    print(f"SOURCE: {source}")
    print("=" * 80)

    # --------------------------------------
    # Temperature × Time table
    # --------------------------------------

    matrix = pd.crosstab(
        group["Tempering temperature (ºC)"],
        group["Tempering time (s)"]
    )

    print("\nTEMPERATURE × TIME MATRIX")
    print("(1 = observation exists, 0 = no observation)")
    print()

    matrix = (matrix > 0).astype(int)

    print(matrix.to_string())


    # --------------------------------------
    # Number of observations per temperature
    # --------------------------------------

    print("\nOBSERVATIONS PER TEMPERATURE")

    temperature_counts = (
        group["Tempering temperature (ºC)"]
        .value_counts()
        .sort_index()
    )

    print(temperature_counts.to_string())


    # --------------------------------------
    # Number of observations per time
    # --------------------------------------

    print("\nOBSERVATIONS PER TIME")

    time_counts = (
        group["Tempering time (s)"]
        .value_counts()
        .sort_index()
    )

    print(time_counts.to_string())