# Tkinter

## 1. 概要

Tkinterは、PythonでGUI（Graphical User Interface）アプリケーションを作成するための標準ライブラリ。

以下のようなGUIを作成できる。

- ウィンドウ
- ラベル
- ボタン
- テキスト入力
- チェックボックス
- ラジオボタン
- リスト
- プルダウン
- メニュー
- ダイアログ
- キャンバス

基本的には、ウィンドウを作成し、その中に各種Widget（ウィジェット）を配置してGUIを構築する。

---

## 2. インポート

```python
import tkinter as tk

# ファイル選択ダイアログなど、一部の機能は個別にインポートする。
from tkinter import filedialog
from tkinter import messagebox
```

## 3. 基本構造
TkinterでGUIを作成する基本的な流れ。
1. tkinterをインポート
2. メインウィンドウを作成
3. ウィジェットを作成
4. ウィジェットを配置
5. イベント処理を設定
6. mainloop()でGUIを起動

#### 基本コード
```python
import tkinter as tk

# メインウィンドウを作成
root = tk.Tk()

# ウィンドウタイトル
root.title("My App")

# ウィンドウサイズ
root.geometry("400x300")

# ラベルを作成
label = tk.Label(
    root,
    text="Hello World"
)

# ラベルを配置
label.pack()

# イベントループを開始
root.mainloop()
```

## 4. メインウィンドウ

### Tk()
メインウィンドウを作成する。
```python
import tkinter as tk

root = tk.Tk()
```
基本的にアプリケーションごとに1つ作成する。 

### title()
ウィンドウのタイトルを設定する。
```python
root.title("My App")
```

### geometry()
ウィンドウのサイズや位置を指定する。
```python
root.geometry("400x300")
```

以下のように位置も指定できる。
```python
root.geometry("400x300+100+100")
400：幅
300：高さ
100：X座標
100：Y座標
```

### resizable()
ウィンドウサイズの変更可否を設定する。
```python
# 横・縦ともに変更不可
root.resizable(False, False)
```

### mainloop()
Tkinterのイベントループを開始する。
```python
root.mainloop()
```
これにより、ユーザーのクリックやキーボード入力などのイベントを待ち受ける。

## 5. Widget
Tkinterでは、GUIを構成する各部品をWidget（ウィジェット）として扱う。

Widget | 用途
---- | ----
Label | 文字や画像を表示
Button | ボタン
Entry | 1行のテキスト入力
Text | 複数行のテキスト入力
Checkbutton | チェックボックス
Radiobutton | ラジオボタン
Listbox | リスト表示
Frame | Widgetをグループ化
Canvas | 図形や画像を描画

## 6. Label
文字列や画像を表示する。
```python
label = tk.Label(
    root,
    text="Hello World"
)

label.pack()
```

### 主なオプション
オプション	| 用途
----- | -----
text | 表示する文字列
font | フォント
fg | 文字色
bg | 背景色
width | 幅
height | 高さ

### フォントを指定
```python
label = tk.Label(
    root,
    text="Hello World",
    font=("Arial", 20)
)
```

## 7. Button
ボタンを作成する。
```python
def click():
    print("Clicked!")

button = tk.Button(
    root,
    text="Click",
    command=click
)

button.pack()
command
```

ボタンがクリックされたときに実行する関数を指定する。
```python
command=click
```
関数を指定するときは、基本的に `()` を付けない。
```python
# OK
command=click

# NG
command=click()
```
`command=click()` とすると、ボタンをクリックしたときではなく、Buttonを作成した時点で関数が実行される。

## 8. Entry
1行のテキスト入力欄を作成する。
```python
entry = tk.Entry(root)

entry.pack()
```

### get()
入力された値を取得する。
```python
text = entry.get()

print(text)
```

### delete()
入力内容を削除する。
```python
entry.delete(0, tk.END)
```

### insert()
入力欄に文字列を挿入する。
```python
entry.insert(0, "Hello")
```