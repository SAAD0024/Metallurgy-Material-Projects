import pandas as pd
import numpy as np

from sklearn.model_selection import (
    train_test_split,
    GroupKFold
)


# ==========================================
# 1. Load PROCESSED dataset
# ==========================================

file_path = (
    "data/processed/4340_Penha2010_processed.csv"
)

df = pd.read_csv(file_path)


# ==========================================
# 2. Create candidate features
# ==========================================

df["log10_time"] = np.log10(
    df["Tempering time (s)"]
)


# ==========================================
# 3. Define target
# ==========================================

target = "Final hardness (HRC) - post tempering"

y = df[target]


# ==========================================
# 4. Define feature sets
# ==========================================

X_raw = df[
    [
        "Tempering temperature (ºC)",
        "Tempering time (s)"
    ]
]

X_log = df[
    [
        "Tempering temperature (ºC)",
        "log10_time"
    ]
]

X_interaction = df[
    [
        "Tempering temperature (ºC)",
        "log10_time"
    ]
].copy()

X_interaction["temperature_x_log_time"] = (
    X_interaction["Tempering temperature (ºC)"]
    * X_interaction["log10_time"]
)


# ==========================================
# 5. Random train/test split
# ==========================================

print("\n" + "=" * 70)
print("RANDOM 80/20 TRAIN-TEST SPLIT")
print("=" * 70)

X_train, X_test, y_train, y_test = train_test_split(
    X_log,
    y,
    test_size=0.20,
    random_state=42
)

print(f"Training observations : {len(X_train)}")
print(f"Testing observations  : {len(X_test)}")


# ==========================================
# 6. Display test temperatures
# ==========================================

print("\nTest-set temperatures:")

print(
    sorted(
        X_test["Tempering temperature (ºC)"]
        .unique()
        .tolist()
    )
)


# ==========================================
# 7. GroupKFold by temperature
# ==========================================

print("\n" + "=" * 70)
print("GROUPED CROSS-VALIDATION BY TEMPERATURE")
print("=" * 70)

groups = df["Tempering temperature (ºC)"]

group_kfold = GroupKFold(n_splits=9)


# ==========================================
# 8. Display fold structure
# ==========================================

for fold, (train_index, test_index) in enumerate(
    group_kfold.split(
        X_log,
        y,
        groups=groups
    ),
    start=1
):

    train_temperatures = sorted(
        df.iloc[train_index]
        ["Tempering temperature (ºC)"]
        .unique()
        .tolist()
    )

    test_temperatures = sorted(
        df.iloc[test_index]
        ["Tempering temperature (ºC)"]
        .unique()
        .tolist()
    )

    print(f"\nFold {fold}")
    print(
        f"Training rows : {len(train_index)}"
    )
    print(
        f"Testing rows  : {len(test_index)}"
    )
    print(
        f"Training temperatures : "
        f"{train_temperatures}"
    )
    print(
        f"Testing temperature : "
        f"{test_temperatures}"
    )


# ==========================================
# 9. Final validation summary
# ==========================================

print("\n" + "=" * 70)
print("VALIDATION FRAMEWORK SUMMARY")
print("=" * 70)

print("Random validation:")
print("  80% training / 20% testing")
print("  random_state = 42")

print("\nGrouped validation:")
print("  9 folds")
print("  groups = tempering temperature")
print("  each fold holds out one temperature")


# ==========================================
# 10. Candidate feature sets
# ==========================================

print("\n" + "=" * 70)
print("CANDIDATE FEATURE SETS")
print("=" * 70)

print("\nModel A:")
print("  Temperature + raw time")

print("\nModel B:")
print("  Temperature + log10(time)")

print("\nModel C:")
print("  Temperature + log10(time)")
print("  + Temperature × log10(time)")