# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import base64
from pathlib import Path

png = Path("gnp_chart.png").read_bytes()
b64 = base64.b64encode(png).decode("ascii")

rows = [
    (1990, 450.8), (1995, 511.3), (2000, 520.1), (2005, 503.9),
    (2010, 512.9), (2015, 532.6), (2020, 539.7), (2024, 609.4),
]
trs = "\n".join(f"      <tr><td>{y}</td><td>{v:.1f}</td></tr>" for y, v in rows)

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>日本のGNP/GDPの推移</title>
<style>
  body {{ font-family: system-ui, -apple-system, "Hiragino Sans", sans-serif; margin: 0; color: #1a1a1a; background: #fff; }}
  main {{ max-width: 860px; margin: 0 auto; padding: 32px 20px 48px; }}
  h1 {{ font-size: 28px; margin: 0 0 8px; }}
  p.note {{ font-size: 14px; color: #333; margin: 0 0 20px; }}
  figure {{ margin: 0 0 24px; border: 1px solid #ddd; padding: 16px; }}
  img {{ width: 100%; height: auto; display: block; }}
  figcaption {{ font-size: 13px; color: #333; margin-top: 8px; }}
  table {{ border-collapse: collapse; width: 100%; max-width: 420px; }}
  th, td {{ border: 1px solid #ccc; padding: 8px 12px; text-align: right; font-size: 15px; }}
  th {{ background: #f0f0f0; }}
  td:first-child, th:first-child {{ text-align: center; }}
  footer {{ margin-top: 24px; font-size: 13px; color: #333; }}
</style>
</head>
<body>
<main>
  <h1>日本のGNP/GDPの推移</h1>
  <p class="note">GNPは現行の国民経済計算ではGNI（国民総所得）と呼ばれる。グラフは名目GDP（兆円）。GNI端点値：1990年 約466.3兆円、2023年 約625.7兆円（World Bank/CEIC連結系列）。</p>
  <figure>
    <img alt="日本の名目GDP推移グラフ" src="data:image/png;base64,{b64}">
    <figcaption>日本の名目GDP推移（兆円、1990〜2024）。出典：内閣府「国民経済計算」系・World Bank WDI連結系列。</figcaption>
  </figure>
  <table>
    <tr><th>年</th><th>名目GDP（兆円）</th></tr>
{trs}
  </table>
  <footer>1990年→2024年の名目GDP増加率：約35.2%。単一ファイル（画像内包）のためオフラインで表示できる。</footer>
</main>
</body>
</html>
"""
Path("index.html").write_text(html, encoding="utf-8")
print(f"wrote index.html {len(html)} bytes")
