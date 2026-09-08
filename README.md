# kklab-muse

Python（uv + PEP 723）と単一ファイルWebページの小さな成果物集。

## 内容

- [hello.py](hello.py) — 「こんにちはセカイ」と表示する最小スクリプト（PEP 723形式）。
- [japan_gnp.py](japan_gnp.py) — 日本のGNP/GNI・GDPの推移（名目、兆円）を
  テキストの表とグラフで表示するスクリプト（PEP 723形式、依存なし）。
  ※ GNPは現行SNAではGNI（国民総所得）と呼ばれる。
- [make_chart.py](make_chart.py) — 名目GDP推移の折れ線グラフ
  [gnp_chart.png](gnp_chart.png) を生成するスクリプト（matplotlib使用）。
- [gen_page.py](gen_page.py) — `gnp_chart.png` をBase64で内包した
  単一ファイルのWebページ [index.html](index.html) を生成するスクリプト。
- [index.html](index.html) — 画像内包・オフライン表示可能な成果物。
  ブラウザで直接開ける。

## 実行方法

```sh
uv run hello.py
uv run japan_gnp.py
uv run make_chart.py   # gnp_chart.png を生成
uv run gen_page.py     # index.html を生成
```

## データ出典

- 内閣府「国民経済計算」系の公開値（World Bank WDI連結系列・IMFとの
  クロスチェック値として公開されている名目GDP系列）
- World Bank via CEIC の GNI連結系列の端点値（1990年 約466.3兆円、
  2023年 約625.7兆円）
