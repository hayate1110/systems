# これまでに関わったシステムや作品、アプリ制作活動
## リポジトリの説明
`movie_recommendation`は映画推薦RAGシステムを実装したノートブックが置かれています。Google  Colaboratory上でひらけば動作すると思います。
ただし、GeminiのAPIキーは、Google Colaboratoryのシークレットキーに、自分のものを設定する必要があります。

`time_table`は、タイムテーブル最適化システムです。`time_table`ディレクトリ直下に移動してもらい、`time_table.py`を実行すると、ショーケースの出演順が出力されます。  
実行にあたって、特にライブラリのインストールは必要ありません。


## フォルダ構成
```
.
├── README.md                           
├── movie_recommendation                映画推薦RAGシステム
│   └── chura_intern_gemini_rag.ipynb   ノートブック
└── time_table                          タイムテーブル最適化システム
    ├── teams.txt                       ダミーデータ
    └── time_table.py                   Pythonスクリプト
```