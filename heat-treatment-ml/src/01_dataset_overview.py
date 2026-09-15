import pandas as pd

# ==========================================
# 1. Load RAW dataset
# ==========================================

file_path = "data/raw/Tempering data for carbon and low alloy steels - Raiipa.csv"

df = pd.read_csv(file_path)


# ==========================================
# 2. Basic dataset information
# ==========================================

print("\n" + "=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Number of rows    : {df.shape[0]}")
print(f"Number of columns : {df.shape[1]}")


# ==========================================
# 3. Column names and data types
# ==========================================

print("\n" + "=" * 60)
print("COLUMNS AND DATA TYPES")
print("=" * 60)

for column in df.columns:
    print(f"{column}  -->  {df[column].dtype}")


# ==========================================
# 4. Missing values
# ==========================================

print("\n" + "=" * 60)
print("MISSING VALUES (NaN)")
print("=" * 60)

missing_values = df.isna().sum()

print(missing_values)


# ==========================================
# 5. '?' values
# ==========================================

print("\n" + "=" * 60)
print("QUESTION-MARK VALUES (?)")
print("=" * 60)

question_marks = (df == "?").sum()

print(question_marks)


# ==========================================
# 6. Number of steel types
# ==========================================

print("\n" + "=" * 60)
print("STEEL TYPES")
print("=" * 60)

print(f"Number of unique steel types: {df['Steel type'].nunique()}")

print("\nSteel types:")
for steel in sorted(df["Steel type"].unique()):
    print(steel)


# ==========================================
# 7. Number of records per steel
# ==========================================

print("\n" + "=" * 60)
print("RECORDS PER STEEL")
print("=" * 60)

records_per_steel = (
    df["Steel type"]
    .value_counts()
    .sort_values(ascending=False)
)

print(records_per_steel.to_string())


# ==========================================
# 8. Final hardness availability
# ==========================================

print("\n" + "=" * 60)
print("FINAL HARDNESS")
print("=" * 60)

final_hardness = df["Final hardness (HRC) - post tempering"]

print(f"Missing final hardness: {final_hardness.isna().sum()}")
print(f"'?' final hardness    : {(final_hardness == '?').sum()}")