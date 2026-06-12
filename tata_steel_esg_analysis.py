"""
Tata Steel — ESG Risk & Opportunity Analysis
Source: BRSR FY2024-25 (Ref: SEC/373/2025-26)
Author: Sanjana Sabat
Tools: Python, pandas, matplotlib, seaborn, numpy
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import os

# ── Output folder ──────────────────────────────────────────────────────────────
os.makedirs("charts", exist_ok=True)

# ── Global style ───────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
})

COLORS = {
    "dark_blue": "#003366",
    "med_blue": "#1F5C99",
    "light_blue": "#5B9BD5",
    "green": "#1A6B3C",
    "light_green": "#70AD47",
    "red": "#C00000",
    "amber": "#E36C09",
    "gray": "#595959",
    "light_gray": "#BFBFBF",
}

# ══════════════════════════════════════════════════════════════════════════════
# DATA — extracted directly from Tata Steel BRSR FY2024-25
# ══════════════════════════════════════════════════════════════════════════════

# 1. GHG Emissions (Million Tonnes CO2e) — Standalone
ghg_standalone = pd.DataFrame({
    "Year": ["FY2022-23", "FY2023-24", "FY2024-25"],
    "Scope 1": [57, 59, 61],
    "Scope 2": [5, 5, 5],
    "Scope 3": [21, 23, 23],
})

# 2. GHG Emissions — Consolidated
ghg_consolidated = pd.DataFrame({
    "Year": ["FY2023-24", "FY2024-25"],
    "Scope 1": [77, 78],
    "Scope 2": [5, 6],
    "Scope 3": [25, 29],
})

# 3. Emission Intensity (Tonnes CO2e per tonne crude steel)
emission_intensity = pd.DataFrame({
    "Year": ["FY2022-23", "FY2023-24", "FY2024-25"],
    "Standalone": [3.3, 3.2, 3.2],
    "Consolidated": [None, 2.8, 2.7],
})

# 4. Safety KPIs — Standalone
safety_standalone = pd.DataFrame({
    "Year": ["FY2022-23", "FY2023-24", "FY2024-25"],
    "LTIFR Employees": [0.55, 0.51, 0.39],
    "LTIFR Workers": [0.41, 0.36, 0.29],
    "Fatalities (Employees)": [0, 0, 1],
    "Fatalities (Workers)": [7, 5, 4],
    "High Consequence Injuries (Employees)": [3, 2, 4],
    "High Consequence Injuries (Workers)": [7, 9, 18],
})

# 5. Water Data — Standalone (Million Litres)
water = pd.DataFrame({
    "Year": ["FY2023-24", "FY2024-25"],
    "Total Withdrawal": [110947, 110829],
    "Total Consumption": [96938, 98609],
    "Surface Water": [70121, 69346],
    "Groundwater": [13303, 12377],
    "Third Party": [9864, 10304],
    "Water Intensity (KL/T)": [4.82, 4.76],
})

# 6. Renewable Energy (%)
renewable = pd.DataFrame({
    "Year": ["FY2022-23", "FY2023-24", "FY2024-25"],
    "Standalone (%)": [0.01, 0.02, 0.07],
    "Consolidated (%)": [0.01, 0.03, 0.09],
    "Target 2027 (%)": [15, 15, 15],
})

# 7. Waste — Standalone (Metric Tonnes)
waste = pd.DataFrame({
    "Category": ["Non-Hazardous", "Hazardous", "E-Waste", "Plastic", "Battery", "Bio-Medical", "C&D Waste"],
    "FY2024-25": [16119942, 1227314, 201, 2359, 687, 256, 1714],
    "FY2023-24": [16426097, 1534826, 275, 2362, 272, 23, 3071],
})

# 8. Gender Diversity — Consolidated
diversity = pd.DataFrame({
    "Level": ["Board of Directors", "Senior Leadership", "Permanent Employees", "Permanent Workers"],
    "Female %": [10, 13, 9.1, 6.3],
    "Male %": [90, 87, 90.8, 93.5],
})

# 9. ESG Scorecard
esg_scorecard = pd.DataFrame({
    "Dimension": ["Governance", "Community & CSR", "Circular Economy",
                  "Water", "Climate & Energy", "Safety", "Diversity & Inclusion"],
    "Score": [8.5, 7.5, 7.0, 6.5, 6.0, 6.0, 4.5],
    "Color": ["green", "light_green", "light_green",
              "amber", "amber", "amber", "red"],
})

# 10. Turnover Rate — Standalone Permanent Employees (%)
turnover = pd.DataFrame({
    "Year": ["FY2022-23", "FY2023-24", "FY2024-25"],
    "Male": [9.0, 5.6, 7.0],
    "Female": [12.9, 10.2, 8.4],
    "Total": [9.3, 5.9, 7.1],
})


# ══════════════════════════════════════════════════════════════════════════════
# CHART 1 — GHG Emissions Trend (Scope 1, 2, 3) — Standalone
# ══════════════════════════════════════════════════════════════════════════════
def chart1_ghg_trend():
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(ghg_standalone["Year"]))
    width = 0.25

    b1 = ax.bar(x - width, ghg_standalone["Scope 1"], width, label="Scope 1",
                color=COLORS["dark_blue"], edgecolor="white")
    b2 = ax.bar(x, ghg_standalone["Scope 2"], width, label="Scope 2",
                color=COLORS["med_blue"], edgecolor="white")
    b3 = ax.bar(x + width, ghg_standalone["Scope 3"], width, label="Scope 3",
                color=COLORS["light_blue"], edgecolor="white")

    # Value labels
    for bars in [b1, b2, b3]:
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.5,
                    f"{int(bar.get_height())}",
                    ha="center", va="bottom", fontsize=9, color=COLORS["gray"])

    ax.set_xticks(x)
    ax.set_xticklabels(ghg_standalone["Year"], fontsize=11)
    ax.set_ylabel("Million Tonnes CO₂e", fontsize=11)
    ax.set_title("GHG Emissions Trend — Tata Steel Standalone\n(Scope 1, 2 & 3 | FY2022-23 to FY2024-25)",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], pad=15)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 75)

    # Annotation
    ax.annotate("Scope 1 rose +2 MnT\ndue to Kalinganagar\nPhase-2 commissioning",
                xy=(2 - width, 61), xytext=(1.2, 68),
                arrowprops=dict(arrowstyle="->", color=COLORS["red"]),
                fontsize=8.5, color=COLORS["red"])

    fig.text(0.99, 0.01, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/01_ghg_emissions_trend.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 1 saved — GHG Emissions Trend")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 2 — Emission Intensity (T CO2e / T Crude Steel)
# ══════════════════════════════════════════════════════════════════════════════
def chart2_emission_intensity():
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(emission_intensity["Year"], emission_intensity["Standalone"],
            marker="o", linewidth=2.5, color=COLORS["dark_blue"],
            label="Standalone", markersize=8)
    ax.plot(["FY2023-24", "FY2024-25"],
            [emission_intensity["Consolidated"][1], emission_intensity["Consolidated"][2]],
            marker="s", linewidth=2.5, color=COLORS["light_green"],
            label="Consolidated", markersize=8, linestyle="--")

    # Value labels
    for i, row in emission_intensity.iterrows():
        ax.text(i, row["Standalone"] + 0.03, f'{row["Standalone"]}',
                ha="center", fontsize=10, color=COLORS["dark_blue"], fontweight="bold")

    ax.axhline(y=1.8, color=COLORS["green"], linestyle=":", linewidth=1.5,
               label="Global avg low-emission steel (~1.8)")
    ax.axhline(y=2.3, color=COLORS["amber"], linestyle=":", linewidth=1.5,
               label="SBTi steel sector benchmark (~2.3)")

    ax.set_ylabel("T CO₂e per Tonne Crude Steel", fontsize=11)
    ax.set_title("GHG Emission Intensity — Tata Steel\n(Tonnes CO₂e per Tonne Crude Steel)",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], pad=15)
    ax.legend(fontsize=9)
    ax.set_ylim(1.5, 4.0)

    fig.text(0.99, 0.01, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/02_emission_intensity.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 2 saved — Emission Intensity")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 3 — Safety KPIs: LTIFR Trend
# ══════════════════════════════════════════════════════════════════════════════
def chart3_ltifr_trend():
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(safety_standalone["Year"], safety_standalone["LTIFR Employees"],
            marker="o", linewidth=2.5, color=COLORS["dark_blue"],
            label="LTIFR — Employees", markersize=8)
    ax.plot(safety_standalone["Year"], safety_standalone["LTIFR Workers"],
            marker="s", linewidth=2.5, color=COLORS["amber"],
            label="LTIFR — Workers", markersize=8)

    for i, row in safety_standalone.iterrows():
        ax.text(i, row["LTIFR Employees"] + 0.015,
                f'{row["LTIFR Employees"]}', ha="center", fontsize=10,
                color=COLORS["dark_blue"], fontweight="bold")
        ax.text(i, row["LTIFR Workers"] - 0.03,
                f'{row["LTIFR Workers"]}', ha="center", fontsize=10,
                color=COLORS["amber"], fontweight="bold")

    # Improvement arrows
    ax.annotate("", xy=(2, 0.39), xytext=(1, 0.51),
                arrowprops=dict(arrowstyle="-|>", color=COLORS["green"], lw=1.5))
    ax.text(2.05, 0.42, "↓24%", fontsize=9, color=COLORS["green"], fontweight="bold")

    ax.set_ylabel("LTIFR (per million person-hours)", fontsize=11)
    ax.set_title("Lost Time Injury Frequency Rate (LTIFR) Trend\nTata Steel Standalone — FY2022-23 to FY2024-25",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], pad=15)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 0.75)

    fig.text(0.99, 0.01, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/03_ltifr_trend.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 3 saved — LTIFR Trend")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 4 — High Consequence Injuries vs Fatalities
# ══════════════════════════════════════════════════════════════════════════════
def chart4_safety_divergence():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    years = safety_standalone["Year"]
    x = np.arange(len(years))
    width = 0.35

    # Left: High Consequence Injuries
    ax = axes[0]
    ax.bar(x - width/2, safety_standalone["High Consequence Injuries (Employees)"],
           width, label="Employees", color=COLORS["med_blue"], edgecolor="white")
    ax.bar(x + width/2, safety_standalone["High Consequence Injuries (Workers)"],
           width, label="Workers", color=COLORS["red"], edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=9)
    ax.set_title("High Consequence Injuries\n(Despite improving LTIFR)",
                 fontsize=11, fontweight="bold", color=COLORS["dark_blue"])
    ax.set_ylabel("Number of Incidents", fontsize=10)
    ax.legend(fontsize=9)

    # Annotation — worker injuries doubled
    ax.annotate("Workers: 9 → 18\n(doubled in FY25)",
                xy=(2 + width/2, 18), xytext=(1.5, 20),
                arrowprops=dict(arrowstyle="->", color=COLORS["red"]),
                fontsize=8.5, color=COLORS["red"], fontweight="bold")

    # Right: Fatalities
    ax2 = axes[1]
    ax2.bar(x - width/2, safety_standalone["Fatalities (Employees)"],
            width, label="Employees", color=COLORS["med_blue"], edgecolor="white")
    ax2.bar(x + width/2, safety_standalone["Fatalities (Workers)"],
            width, label="Workers", color=COLORS["red"], edgecolor="white")
    ax2.set_xticks(x)
    ax2.set_xticklabels(years, fontsize=9)
    ax2.set_title("Fatalities\n(Workers fatalities declining)",
                  fontsize=11, fontweight="bold", color=COLORS["dark_blue"])
    ax2.set_ylabel("Number of Fatalities", fontsize=10)
    ax2.legend(fontsize=9)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", alpha=0.3, linestyle="--")
        for bar in ax.patches:
            ax.text(bar.get_x() + bar.get_width()/2,
                    bar.get_height() + 0.1,
                    str(int(bar.get_height())),
                    ha="center", va="bottom", fontsize=9)

    fig.suptitle("Safety Performance — Tata Steel Standalone FY2022-23 to FY2024-25",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], y=1.02)
    fig.text(0.99, -0.02, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/04_safety_divergence.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 4 saved — Safety Divergence")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 5 — Water Consumption & Withdrawal Trend
# ══════════════════════════════════════════════════════════════════════════════
def chart5_water_trend():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left: Withdrawal vs Consumption
    ax = axes[0]
    x = np.arange(len(water["Year"]))
    width = 0.35

    ax.bar(x - width/2, water["Total Withdrawal"] / 1000,
           width, label="Withdrawal", color=COLORS["med_blue"], edgecolor="white")
    ax.bar(x + width/2, water["Total Consumption"] / 1000,
           width, label="Consumption", color=COLORS["light_blue"], edgecolor="white")

    for bar in ax.patches:
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 0.3,
                f"{bar.get_height():.1f}",
                ha="center", va="bottom", fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(water["Year"], fontsize=10)
    ax.set_ylabel("Billion Litres", fontsize=10)
    ax.set_title("Water Withdrawal vs Consumption\n(Standalone, Million Litres ÷ 1000)",
                 fontsize=11, fontweight="bold", color=COLORS["dark_blue"])
    ax.legend(fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    # Right: Water Source Breakdown FY2024-25
    ax2 = axes[1]
    sources = ["Surface Water", "Groundwater", "Third Party", "Others"]
    values = [69346, 12377, 10304, 18802]
    c = [COLORS["dark_blue"], COLORS["med_blue"], COLORS["light_blue"], COLORS["light_gray"]]
    wedges, texts, autotexts = ax2.pie(values, labels=sources, colors=c,
                                        autopct="%1.1f%%", startangle=90,
                                        textprops={"fontsize": 9})
    for at in autotexts:
        at.set_fontsize(9)
        at.set_fontweight("bold")

    ax2.set_title("Water Withdrawal by Source\n(Standalone FY2024-25)",
                  fontsize=11, fontweight="bold", color=COLORS["dark_blue"])

    fig.suptitle("Water Risk Analysis — Tata Steel Standalone",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], y=1.02)
    fig.text(0.99, -0.02, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/05_water_analysis.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 5 saved — Water Analysis")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 6 — Renewable Energy Gap
# ══════════════════════════════════════════════════════════════════════════════
def chart6_renewable_gap():
    fig, ax = plt.subplots(figsize=(9, 5))

    x = np.arange(len(renewable["Year"]))
    width = 0.25

    ax.bar(x - width, renewable["Standalone (%)"], width,
           label="Standalone (Actual)", color=COLORS["dark_blue"], edgecolor="white")
    ax.bar(x, renewable["Consolidated (%)"], width,
           label="Consolidated (Actual)", color=COLORS["med_blue"], edgecolor="white")
    ax.bar(x + width, renewable["Target 2027 (%)"], width,
           label="Recommended Target 2027", color=COLORS["light_green"],
           edgecolor="white", alpha=0.8)

    for bar in ax.patches:
        val = bar.get_height()
        if val > 0.1:
            ax.text(bar.get_x() + bar.get_width()/2,
                    bar.get_height() + 0.2,
                    f"{val}%",
                    ha="center", va="bottom", fontsize=8.5)

    ax.set_xticks(x)
    ax.set_xticklabels(renewable["Year"], fontsize=11)
    ax.set_ylabel("Renewable Energy Share (%)", fontsize=11)
    ax.set_title("Renewable Energy Share vs Recommended Target\nTata Steel — FY2022-23 to FY2024-25",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], pad=15)
    ax.legend(fontsize=9)

    # Gap annotation
    ax.annotate("CRITICAL GAP\n0.07% vs 15% target",
                xy=(2 + width, 15), xytext=(1.3, 12),
                arrowprops=dict(arrowstyle="->", color=COLORS["red"]),
                fontsize=9, color=COLORS["red"], fontweight="bold")

    fig.text(0.99, 0.01, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/06_renewable_energy_gap.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 6 saved — Renewable Energy Gap")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 7 — Gender Diversity Across Levels
# ══════════════════════════════════════════════════════════════════════════════
def chart7_gender_diversity():
    fig, ax = plt.subplots(figsize=(10, 5))

    x = np.arange(len(diversity["Level"]))
    width = 0.35

    ax.bar(x - width/2, diversity["Female %"], width,
           label="Female %", color=COLORS["red"], edgecolor="white")
    ax.bar(x + width/2, diversity["Male %"], width,
           label="Male %", color=COLORS["dark_blue"], edgecolor="white")

    # 30% target line
    ax.axhline(y=30, color=COLORS["amber"], linestyle="--", linewidth=1.5,
               label="30% diversity benchmark")

    for bar in ax.patches:
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 0.5,
                f"{bar.get_height():.0f}%",
                ha="center", va="bottom", fontsize=9, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(diversity["Level"], fontsize=9, wrap=True)
    ax.set_ylabel("Percentage (%)", fontsize=11)
    ax.set_title("Gender Representation Across Levels — Tata Steel Consolidated FY2024-25",
                 fontsize=12, fontweight="bold", color=COLORS["dark_blue"], pad=15)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 110)

    # Gap flag
    ax.text(0, 55, "0% female KMPs\n(Key Managerial Personnel)",
            ha="center", fontsize=8.5, color=COLORS["red"],
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FDECEA", edgecolor=COLORS["red"]))

    fig.text(0.99, 0.01, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/07_gender_diversity.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 7 saved — Gender Diversity")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 8 — ESG Scorecard Heatmap
# ══════════════════════════════════════════════════════════════════════════════
def chart8_esg_scorecard():
    fig, ax = plt.subplots(figsize=(10, 6))

    dimensions = esg_scorecard["Dimension"].tolist()
    scores = esg_scorecard["Score"].tolist()

    # Horizontal bar chart styled as scorecard
    colors = []
    for s in scores:
        if s >= 7.5:
            colors.append(COLORS["green"])
        elif s >= 6.0:
            colors.append(COLORS["amber"])
        else:
            colors.append(COLORS["red"])

    y = np.arange(len(dimensions))
    bars = ax.barh(y, scores, color=colors, edgecolor="white", height=0.6)

    # Score labels
    for bar, score in zip(bars, scores):
        ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
                f"{score}/10", va="center", ha="left", fontsize=11, fontweight="bold")

    # Grade labels
    grades = ["A–", "B+", "B", "B–", "C+", "C+", "D+"]
    for i, (grade, score) in enumerate(zip(grades, scores)):
        ax.text(0.2, i, grade, va="center", ha="left",
                fontsize=11, fontweight="bold", color="white")

    ax.set_yticks(y)
    ax.set_yticklabels(dimensions, fontsize=11)
    ax.set_xlim(0, 12)
    ax.set_xlabel("Score (out of 10)", fontsize=11)
    ax.set_title("ESG Scorecard — Tata Steel FY2024-25\n(Based on BRSR Disclosures Analysis)",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], pad=15)
    ax.axvline(x=7.5, color=COLORS["green"], linestyle=":", linewidth=1.5, alpha=0.7)
    ax.axvline(x=6.0, color=COLORS["amber"], linestyle=":", linewidth=1.5, alpha=0.7)

    # Legend
    legend_patches = [
        mpatches.Patch(color=COLORS["green"], label="Strong (≥7.5)"),
        mpatches.Patch(color=COLORS["amber"], label="Moderate (6.0–7.4)"),
        mpatches.Patch(color=COLORS["red"], label="Weak (<6.0)"),
    ]
    ax.legend(handles=legend_patches, fontsize=9, loc="lower right")

    fig.text(0.99, 0.01, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/08_esg_scorecard.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 8 saved — ESG Scorecard")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 9 — Waste Generation: Hazardous vs Non-Hazardous (FY24 vs FY25)
# ══════════════════════════════════════════════════════════════════════════════
def chart9_waste():
    fig, ax = plt.subplots(figsize=(9, 5))

    categories = ["Non-Hazardous\n(Lakh MT)", "Hazardous\n(Lakh MT)"]
    fy24 = [16426097/100000, 1534826/100000]
    fy25 = [16119942/100000, 1227314/100000]

    x = np.arange(len(categories))
    width = 0.35

    b1 = ax.bar(x - width/2, fy24, width, label="FY2023-24",
                color=COLORS["light_gray"], edgecolor="white")
    b2 = ax.bar(x + width/2, fy25, width, label="FY2024-25",
                color=COLORS["dark_blue"], edgecolor="white")

    for bar in [*b1, *b2]:
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 0.2,
                f"{bar.get_height():.1f}",
                ha="center", va="bottom", fontsize=10, fontweight="bold")

    # Improvement annotation
    ax.annotate("Hazardous waste\n↓20% YoY",
                xy=(1 + width/2, fy25[1]), xytext=(1.5, fy25[1] + 3),
                arrowprops=dict(arrowstyle="->", color=COLORS["green"]),
                fontsize=9, color=COLORS["green"], fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=11)
    ax.set_ylabel("Lakh Metric Tonnes", fontsize=11)
    ax.set_title("Waste Generation Trend — Tata Steel Standalone\nFY2023-24 vs FY2024-25",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], pad=15)
    ax.legend(fontsize=10)

    fig.text(0.99, 0.01, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/09_waste_trend.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 9 saved — Waste Trend")


# ══════════════════════════════════════════════════════════════════════════════
# CHART 10 — Employee Turnover Rate Trend
# ══════════════════════════════════════════════════════════════════════════════
def chart10_turnover():
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(turnover["Year"], turnover["Male"], marker="o", linewidth=2.5,
            color=COLORS["dark_blue"], label="Male", markersize=8)
    ax.plot(turnover["Year"], turnover["Female"], marker="s", linewidth=2.5,
            color=COLORS["red"], label="Female", markersize=8)
    ax.plot(turnover["Year"], turnover["Total"], marker="^", linewidth=2.5,
            color=COLORS["amber"], label="Total", markersize=8, linestyle="--")

    for i, row in turnover.iterrows():
        ax.text(i, row["Male"] + 0.2, f'{row["Male"]}%',
                ha="center", fontsize=9, color=COLORS["dark_blue"])
        ax.text(i, row["Female"] + 0.2, f'{row["Female"]}%',
                ha="center", fontsize=9, color=COLORS["red"])

    ax.set_ylabel("Turnover Rate (%)", fontsize=11)
    ax.set_title("Permanent Employee Turnover Rate — Tata Steel Standalone\n(FY2022-23 to FY2024-25)",
                 fontsize=13, fontweight="bold", color=COLORS["dark_blue"], pad=15)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 16)

    fig.text(0.99, 0.01, "Source: Tata Steel BRSR FY2024-25 | Analysis: Sanjana Sabat",
             ha="right", fontsize=7, color=COLORS["light_gray"])
    plt.tight_layout()
    plt.savefig("charts/10_turnover_trend.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 10 saved — Turnover Trend")


# ══════════════════════════════════════════════════════════════════════════════
# RUN ALL CHARTS
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n── Tata Steel ESG Analysis ──────────────────────")
    print("Generating all charts from BRSR FY2024-25 data...\n")
    chart1_ghg_trend()
    chart2_emission_intensity()
    chart3_ltifr_trend()
    chart4_safety_divergence()
    chart5_water_trend()
    chart6_renewable_gap()
    chart7_gender_diversity()
    chart8_esg_scorecard()
    chart9_waste()
    chart10_turnover()
    print("\n✓ All 10 charts saved to /charts folder")
    print("─────────────────────────────────────────────────\n")
