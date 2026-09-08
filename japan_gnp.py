# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

"""日本のGNP（現在はGNI：国民総所得）の推移を表示するスクリプト.

データ: 内閣府「国民経済計算」等を基にした名目GDP系列
（World Bank WDI 連結系列・IMFとのクロスチェック値として公開されているもの）、
および World Bank/CEIC の GNI 連結系列の端点値を併記。
- GDP系列 (兆円): 1990-2024 (5年刻み+直近)
  出典: Cabinet Office via IMF cross-checked table / World Bank WDI
- GNI系列 (旧GNP, 兆円): 1990年 約466.3 / 2023年 約625.7
  出典: World Bank via CEIC (JP: Gross National Income: Linked Series)
注: GNPは現在の国民経済計算ではGNIと呼ばれる。
"""

GDP = [
    (1990, 450.8),
    (1995, 511.3),
    (2000, 520.1),
    (2005, 503.9),
    (2010, 512.9),
    (2015, 532.6),
    (2020, 539.7),
    (2024, 609.4),
]

GNI_ENDPOINTS = [
    (1990, 466.3),
    (2023, 625.7),
]


def main() -> None:
    print("日本のGNP/GNI・GDPの推移（名目、兆円）")
    print("※ GNPは現行SNAではGNI（国民総所得）と呼ばれる")
    print()
    print(f"{'年':>6}  {'名目GDP(兆円)':>12}  推移グラフ")
    width = 50
    vmax = max(v for _, v in GDP)
    for year, value in GDP:
        bar = "#" * int(value / vmax * width)
        print(f"{year:>6}  {value:>12.1f}  {bar}")
    print()
    print("参考: GNI（旧GNP）端点値 World Bank/CEIC連結系列")
    for year, value in GNI_ENDPOINTS:
        print(f"  {year}年: {value:.1f} 兆円")
    print()
    inc = (GDP[-1][1] - GDP[0][1]) / GDP[0][1] * 100
    print(f"1990年→2024年の名目GDP増加率: 約{inc:.1f}%")


if __name__ == "__main__":
    main()
