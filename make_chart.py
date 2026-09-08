# /// script
# requires-python = ">=3.13"
# dependencies = ["matplotlib"]
# ///

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

YEARS = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024]
GDP = [450.8, 511.3, 520.1, 503.9, 512.9, 532.6, 539.7, 609.4]

plt.figure(figsize=(9.6, 5.4))
plt.plot(YEARS, GDP, marker="o", linewidth=2.5)
for x, y in zip(YEARS, GDP):
    plt.text(x, y + 7, f"{y:.1f}", ha="center", fontsize=9)
plt.title("Japan Nominal GDP Trend (trillion yen)")
plt.xlabel("Year")
plt.ylabel("Trillion yen")
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(YEARS)
plt.xlim(1989, 2025)
plt.ylim(min(GDP) - 20, max(GDP) + 30)
plt.tight_layout()
plt.savefig("gnp_chart.png", dpi=150)
print("saved gnp_chart.png")
