# Pythonで学ぶ音声コミュニケーション情報処理 サポートページ

このリポジトリには、『[Pythonで学ぶ音声コミュニケーション情報処理](https://www.asakura.co.jp/detail.php?book_code=12302)』各章のプログラムやデータが含まれています。プログラムの動作確認は **Google Colab** で行っていますが、 **Jupyter Notebook** でも動作します。

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sp-au-mu-nl/SpeechComm)

## 動作確認環境

- Google Colab（ https://colab.research.google.com/ ）および Jupyter Notebook
- Python 3.12

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

- `notebook/chapXX.ipynb`: 教科書の各チャプターに対応したサンプルプログラムです。
- `data/chapXX/`: 各チャプターで使用するデータを格納しています。

## このリポジトリの使い方（プログラムの実行方法）

以下の手順にしたがって、ブラウザ上や自分のパソコンでプログラムを実行できます。

### 1. ブラウザで動かしたい場合（インストール不要）

[Google Colab](https://colab.research.google.com/)  を使用して、オンラインでプログラムを実行します。

1. [GitHubのリポジトリページ](https://github.com//sp-au-mu-nl/SpeechComm)を開きます。  
2. [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sp-au-mu-nl/SpeechComm) ボタン（または [Google Colab](https://colab.research.google.com/) 上で「GitHub から開く」）をクリックします。
3. 実行したい章の `.ipynb` ファイルをクリックします。  

### 2. 自分のパソコンにインストールして動かしたい場合

PythonとJupyter Notebookを自分のパソコンにインストールして、オフラインでプログラムを実行します。  
さまざまな方法がありますが、一例として、Pythonのプログラミング環境 Anaconda（PythonとJupyterがセットになったソフト）を使う方法を紹介します。

1. Anaconda をインストール  
　→ [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

2. Anaconda Navigator (Windowsの場合) または ターミナルに `jupyter notebook` と入力して (Macの場合) 、Jupyter Notebook を起動  

3. ブラウザが開いたら、ダウンロードした `.ipynb` ファイルを開いて実行

※ GitHubからZIP形式でダウンロードするには、リポジトリのトップページ右上の「Code」→「Download ZIP」を選んでください。

## 更新履歴

このリポジトリでは、教科書に掲載されているプログラムの最新版を提供しています。以下に、教科書からの変更点（アップデート・修正）を記載します。


| 章・節       | ページ         | 修正内容                                  | 更新日       |
|--------------|--------------------|-------------------------------------------|--------------|
| 各章  |    | Google Colabでの表示のため、適宜 plt.close() を追記 | 2025-05-01   |
| 4章 4.2.1節  | p.56 | プログラム4.4の sr = 8000 の宣言省略 | 2025-05-01   |
| 4章 4.2.2節  | p.57 | プログラム4.5の sr = 8000 の宣言省略 | 2025-05-01   |
| 5章 章末問題6  | p.87 | librosa.display.specshow(SdB, sr=sr, fmax=8000, x_axis='time', y_axis='mel', cmap='viridis') に修正 | 2025-05-01   |
| 6章  |   | chap06_synth_vowel.wav を差し替え（これにより、p.99 で出力される数値が教科書と異なります） | 2025-05-01   |
| 6章  | p.89  | プログラム6.1に不足があったため import scipy を追記 | 2025-05-01   |
| 7章  |   | FOrmantCVTrainShort.csv を差し替え（これにより、図7.4, 7.5, 7.6, 7.8, 7.10 や p.118 で出力される数値が教科書と異なります） | 2025-05-01   |
| 7章 7.2.1節  | p.116 | 描画設定を、より見やすい alpha=0.25 に変更 | 2025-05-01   |
| 7章 7.2.2節  | p.119 | 描画設定を、より見やすい alpha=0.15 に変更 | 2025-05-01   |
| 8章 8.4節  | p.134 | フレームの指定範囲に誤りがあったため x = np.hstack((np.ones((5,1)), np.array([np.arange(5)-2]).T)) に修正 | 2025-05-01   |
| 10章  | p.153 | プログラム10.1に不足があったため from pickle import FRAME を追記 | 2025-05-01   |
| 10章 10.1節  | p.155 | プログラム10.2のフレームの長さを FRAME_LENGTH = int(0.1 * sr) に修正 | 2025-05-01   |

<!-- 
| 各章  | `sample_code.py`   | コメントの文言をより明確に修正            | 2025-04-20   |
| 第3章 3.2節  | `sample_code.py`   | コメントの文言をより明確に修正            | 2025-04-20   |
| 第5章 5.4節  | `example_module.py`| 非推奨メソッドを新しい形式に変更          | 2025-04-21   |
-->

---

プログラムに関するご質問や誤りのご報告は、GitHubの[Issueページ](https://github.com/sp-au-mu-nl/SpeechComm/issues)からお気軽にご連絡ください。
