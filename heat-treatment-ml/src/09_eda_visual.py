import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# 1. Load PROCESSED dataset
# ==========================================

file_path = (
    "data/processed/4340_Penha2010_processed.csv"
)

df = pd.read_csv(file_path)


# ==========================================
# 2. Define variables
# ==========================================

temperature = df["Tempering temperature (ºC)"]

time_seconds = df["Tempering time (s)"]

hardness = df[
    "Final hardness (HRC) - post tempering"
]


# ==========================================
# 3. Plot 1
# Hardness vs Tempering Temperature
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    temperature,
    hardness,
    s=50
)

plt.xlabel("Tempering Temperature (°C)")
plt.ylabel("Final Hardness (HRC)")
plt.title(
    "AISI-SAE 4340: Hardness vs Tempering Temperature"
)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================
# 4. Plot 2
# Hardness vs Tempering Time
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    time_seconds,
    hardness,
    s=50
)

plt.xlabel("Tempering Time (s)")
plt.ylabel("Final Hardness (HRC)")
plt.title(
    "AISI-SAE 4340: Hardness vs Tempering Time"
)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()
# ==========================================
# 5. Plot 3
# Hardness vs log10(Tempering Time)
# ==========================================

log_time = np.log10(time_seconds)

plt.figure(figsize=(8, 5))

plt.scatter(
    log_time,
    hardness,
    s=50
)

plt.xlabel("log₁₀(Tempering Time (s))")
plt.ylabel("Final Hardness (HRC)")
plt.title(
    "AISI-SAE 4340: Hardness vs log₁₀(Tempering Time)"
)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()
# ==========================================
# 6. Heat-treatment hardness map
# ==========================================

# Create log10(time)
df["log10_time"] = np.log10(
    df["Tempering time (s)"]
)


# Create temperature × log(time) matrix
hardness_matrix = df.pivot(
    index="Tempering temperature (ºC)",
    columns="log10_time",
    values="Final hardness (HRC) - post tempering"
)


# ==========================================
# Plot 4
# Temperature × log(Time) → Hardness
# ==========================================

plt.figure(figsize=(10, 6))

plt.imshow(
    hardness_matrix,
    aspect="auto",
    origin="lower",
    interpolation="none"
)

plt.colorbar(
    label="Final Hardness (HRC)"
)

plt.xticks(
    range(len(hardness_matrix.columns)),
    [f"{x:.2f}" for x in hardness_matrix.columns]
)

plt.yticks(
    range(len(hardness_matrix.index)),
    [f"{x:.1f}" for x in hardness_matrix.index]
)

plt.xlabel("log₁₀(Tempering Time (s))")
plt.ylabel("Tempering Temperature (°C)")

plt.title(
    "AISI-SAE 4340: Heat-Treatment Hardness Map"
)

plt.tight_layout()

plt.show()