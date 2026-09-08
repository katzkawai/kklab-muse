# /// script
# requires-python = ">=3.13"
# dependencies = ["matplotlib"]
# ///

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

YEARS = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024]
GDP = [450.8, 511.3, 520.1, 503.9, 512.9, 532.6, 539.7, 609.4]
# Real GNI (= real GNP), World Bank WDI constant-LCU (yen) series, trillion yen.
# 1990 has no value in that series, so the real line starts at 1995.
NAN = float("nan")
REAL_GNI = [NAN, 502.5, 526.7, 552.9, 542.8, 581.1, 573.9, 608.2]

plt.figure(figsize=(9.6, 5.4))
plt.plot(YEARS, GDP, marker="o", linewidth=2.5, label="Nominal GDP")
plt.plot(YEARS, REAL_GNI, marker="s", linewidth=2.5, label="Real GNI (= Real GNP)")
for x, y in zip(YEARS, GDP):
    plt.text(x, y + 7, f"{y:.1f}", ha="center", fontsize=9)
for x, y in zip(YEARS, REAL_GNI):
    if y == y:  # skip NaN
        plt.text(x, y - 14, f"{y:.1f}", ha="center", fontsize=8)
plt.title("Japan Nominal GDP & Real GNI Trend (trillion yen)")
plt.xlabel("Year")
plt.ylabel("Trillion yen")
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(YEARS)
plt.legend()
plt.xlim(1989, 2025)
plt.ylim(min(GDP) - 20, max(GDP) + 30)
plt.tight_layout()
plt.savefig("gnp_chart.png", dpi=150)
print("saved gnp_chart.png")
