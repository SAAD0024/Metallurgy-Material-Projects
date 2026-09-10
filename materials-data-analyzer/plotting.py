"""Plots for tensile-test measurements."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


sns.set_theme(style="whitegrid")


def create_all_plots(data: pd.DataFrame, output_dir: Path) -> None:
    """Create and save the project's standard engineering plots."""
    output_dir.mkdir(parents=True, exist_ok=True)
    _save_bar_chart(
        data,
        "yield_strength_mpa",
        "Average Yield Strength (mean +/- sample SD)",
        "Yield Strength (MPa)",
        output_dir / "average_yield_strength.png",
    )
    _save_bar_chart(
        data,
        "ultimate_tensile_strength_mpa",
        "Average Ultimate Tensile Strength (mean +/- sample SD)",
        "Ultimate Tensile Strength (MPa)",
        output_dir / "average_ultimate_tensile_strength.png",
    )
    _save_distribution_panels(data, output_dir / "measurement_distributions.png")
    _save_scatter_plot(data, "yield_strength_mpa", "elongation_percent", "Yield Strength (MPa)", "Elongation (%)", output_dir / "yield_strength_vs_elongation.png")
    _save_scatter_plot(data, "hardness_hv", "ultimate_tensile_strength_mpa", "Hardness (HV)", "Ultimate Tensile Strength (MPa)", output_dir / "hardness_vs_ultimate_strength.png")


def _save_bar_chart(data: pd.DataFrame, value_column: str, title: str, y_label: str, output_path: Path) -> None:
    summary = data.groupby("material")[value_column].agg(["mean", "std", "count"]).reset_index()
    figure, axis = plt.subplots(figsize=(9, 5))
    bars = axis.bar(
        summary["material"],
        summary["mean"],
        yerr=summary["std"],
        capsize=5,
        color=sns.color_palette("deep", n_colors=len(summary)),
        edgecolor="black",
        linewidth=0.5,
    )
    axis.set_title(title)
    axis.set_xlabel("Material")
    axis.set_ylabel(y_label)
    axis.text(
        0.01,
        0.99,
        "Error bars: sample SD (specimen-to-specimen variability), not measurement uncertainty",
        transform=axis.transAxes,
        ha="left",
        va="top",
        fontsize=8,
    )
    axis.tick_params(axis="x", rotation=20)
    for bar, count in zip(bars, summary["count"]):
        axis.annotate(
            f"n = {count}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 7),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)


def _save_distribution_panels(data: pd.DataFrame, output_path: Path) -> None:
    measurements = [
        ("yield_strength_mpa", "Yield Strength (MPa)"),
        ("ultimate_tensile_strength_mpa", "Ultimate Tensile Strength (MPa)"),
        ("elongation_percent", "Elongation (%)"),
        ("hardness_hv", "Hardness (HV)"),
    ]
    materials = data["material"].unique()
    palette = dict(zip(materials, sns.color_palette("deep", n_colors=len(materials))))
    figure, axes = plt.subplots(2, 2, figsize=(13, 9))

    for axis, (value_column, y_label) in zip(axes.flat, measurements):
        sns.stripplot(
            data=data,
            x="material",
            y=value_column,
            hue="material",
            palette=palette,
            legend=False,
            jitter=0.12,
            size=7,
            alpha=0.8,
            ax=axis,
        )
        means = data.groupby("material")[value_column].mean().reindex(materials)
        axis.scatter(
            range(len(means)),
            means,
            color="black",
            marker="D",
            s=55,
            label="Material mean",
            zorder=3,
        )
        axis.set_title(y_label)
        axis.set_xlabel("Material")
        axis.set_ylabel(y_label)
        axis.tick_params(axis="x", rotation=25)

    axes[0, 0].legend(loc="upper left")
    figure.suptitle("Tensile-Test Measurement Distributions", fontsize=14)
    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)


def _save_scatter_plot(data: pd.DataFrame, x_column: str, y_column: str, x_label: str, y_label: str, output_path: Path) -> None:
    figure, axis = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=data, x=x_column, y=y_column, hue="material", s=90, ax=axis)
    correlation = data[x_column].corr(data[y_column], method="pearson")
    axis.set_title(f"{y_label} vs. {x_label} (exploratory)")
    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)
    axis.text(
        0.02,
        0.98,
        f"Exploratory Pearson r = {correlation:.2f}\nn = {len(data)}",
        transform=axis.transAxes,
        ha="left",
        va="top",
        bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"},
    )
    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)
