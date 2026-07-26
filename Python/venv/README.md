# venv

## Pythonインストール
    https://www.python.org/downloads/ から指定のバージョンをインストール
    または Microsoft Storeからインストールを行う

## 仮想環境の作成
    (システムのpythonから作成の場合)
    $ python -m venv .venv

    (バージョン指定して作成する場合)
    $ py -3.12 -m venv .venv

    venv - pythonに標準搭載されている仮想環境作成モジュール。
    py - pythonのバージョンを指定するコマンド。環境変数にLuncherを設定しておく必要あり。

## 仮想環境の実行
    (仮想環境の実行)
    $ .venv\Scripts\activate

    (仮想環境から抜ける)
    $ deactivate


