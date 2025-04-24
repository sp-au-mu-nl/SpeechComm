# Pythonで学ぶ音声コミュニケーション情報処理 サポートページ

このリポジトリでは、「[Pythonで学ぶ音声コミュニケーション情報処理](https://www.asakura.co.jp/detail.php?book_code=12302)」のサンプルプログラムやデータをまとめています。プログラムの動作確認は **Google Colab** で行っていますが、 **Jupyter Notebook** でも動作します。

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sp-au-mu-nl/SpeechComm)

## 動作確認環境

- Google Colab（ https://colab.research.google.com/ ）
- Python 3.x
- Jupyter Notebook（任意）

## Google Colab の利用方法

1. 本リポジトリを GitHub 上で開きます。
2. 任意の `.ipynb` ファイルをクリックし、`Open in Colab` ボタン（または [Google Colab](https://colab.research.google.com/) 上で「GitHub から開く」）を使って開きます。
3. 初回実行時は、必要に応じて `data/chapXX/` ディレクトリのデータを Colab にアップロードまたはマウントしてください。

## ディレクトリ構成

~~~
.
├── notebook/
│   ├── chap01.ipynb
│   ├── chap02.ipynb
│   └── ...
└── data/
    ├── chap01/
    ├── chap02/
    └── ...
~~~

- `notebook/chapXX.ipynb`: 教科書の各チャプターに対応したサンプルスクリプトです。
- `data/chapXX/`: 各チャプターで使用するデータを格納しています。

## 補足

- 各チャプターのプログラムを実行するために必要なライブラリは、教科書の各章の冒頭に記載しています。
- 不足しているライブラリがある場合は、セル内で `!pip install ライブラリ名` を実行してインストールしてください。
