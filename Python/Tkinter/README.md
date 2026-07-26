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
サンプルコードは`basic_window.py`を参照

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

## 9. Text
複数行のテキスト入力欄を作成する。
```python
text = tk.Text(
    root,
    width=40,
    height=10
)

text.pack()
```

### get()

入力されたテキストを取得する。
```python
value = text.get("1.0", tk.END)
```

`Text`では、開始位置と終了位置を指定する。
```
"1.0" → 1行目の0文字目
tk.END → 最後まで
```

## 10. Frame
Widgetをグループ化するためのコンテナ。
```python
frame = tk.Frame(root)

frame.pack()
```
Frameの中にWidgetを配置することができる。
```python
frame = tk.Frame(root)
frame.pack()

label = tk.Label(
    frame,
    text="Name"
)

label.pack()
```
複雑なGUIを作成するときは、Frameで画面を分割すると管理しやすい。

## 11. レイアウト
Tkinterでは、Widgetを配置するために主に以下の3種類のGeometry Managerを使用する。
- pack()
- grid()
- place()

### pack()
Widgetを上下・左右方向に配置する。
```python
label = tk.Label(
    root,
    text="Hello"
)

label.pack()
```
#### side
配置方向を指定できる。
```python
label.pack(side="left")
label.pack(side="right")
label.pack(side="top")
label.pack(side="bottom")
```

### grid()
Widgetを行と列で配置する。
```python
label = tk.Label(
    root,
    text="名前"
)

label.grid(
    row=0,
    column=0
)
```
フォームのようなGUIに向いている。
```python
label = tk.Label(
    root,
    text="名前"
)

label.grid(
    row=0,
    column=0
)

entry = tk.Entry(root)

entry.grid(
    row=0,
    column=1
)
```
```
イメージ：

名前    [          ]
年齢    [          ]
住所    [          ]
```

## place()
座標を指定してWidgetを配置する。
```python
button.place(
    x=100,
    y=50
)
```
細かい位置指定ができる。  
ただし、ウィンドウサイズを変更した場合にレイアウトが崩れやすいため、一般的なGUIでは pack() や grid() が使いやすい。

## 12. イベント処理
Tkinterでは、ユーザーの操作に応じて関数を実行できる。

### Buttonのクリック
```python
def click():
    print("Clicked!")


button = tk.Button(
    root,
    text="Click",
    command=click
)

button.pack()
```

### bind()
特定のイベントが発生したときに関数を実行する。
```python
def key_event(event):
    print(event.keysym)


root.bind(
    "<Key>",
    key_event
)
```

### よく使うイベント
イベント | 説明
----- | -----
`<Button-1>` | 左クリック
`<Button-2>` | 中クリック
`<Button-3>` | 右クリック
`<Double-Button-1>` | 左ダブルクリック
`<Key>` | キー入力
`<Return>` | Enterキー
`<Escape>` | Escapeキー

イベント情報は`event`オブジェクトから取得できる。
```python
def key_event(event):
    print(event.keysym)
```

## 13. Variable
Tkinterでは、Widgetの値を管理するために専用のVariableクラスを使用できる。

### 主なクラス：
- StringVar
- IntVar
- DoubleVar
- BooleanVar

### StringVar
```python
name = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=name
)

entry.pack()
```
値を取得する。
```python
value = name.get()
```
値を設定する。
```python
name.set("Hello")
```

## 14. Checkbutton
チェックボックスを作成する。
```python
checked = tk.BooleanVar()

checkbutton = tk.Checkbutton(
    root,
    text="同意する",
    variable=checked
)

checkbutton.pack()
```
チェック状態を取得する。
```python
value = checked.get()
```

## 15. Radiobutton
複数の選択肢から1つを選択する。
```python
selected = tk.StringVar()

radio1 = tk.Radiobutton(
    root,
    text="Python",
    value="python",
    variable=selected
)

radio2 = tk.Radiobutton(
    root,
    text="JavaScript",
    value="javascript",
    variable=selected
)

radio1.pack()
radio2.pack()
```
選択された値を取得する。
```python
value = selected.get()
```

## 16. ダイアログ
### filedialog
ファイル選択ダイアログを表示する。
```python
from tkinter import filedialog

file_path = filedialog.askopenfilename()

print(file_path)
```
複数ファイルを選択する場合。
```python
file_paths = filedialog.askopenfilenames()
```
保存先を選択する場合。
```python
file_path = filedialog.asksaveasfilename()
```

### messagebox
メッセージボックスを表示する。
```python
from tkinter import messagebox

messagebox.showinfo(
    "Info",
    "処理が完了しました"
)
```
警告を表示する。
```python
messagebox.showwarning(
    "Warning",
    "入力内容を確認してください"
)
```
エラーを表示する。
```python
messagebox.showerror(
    "Error",
    "エラーが発生しました"
)
```

## 17. 実用例
入力した文字列をLabelに表示。
```python
import tkinter as tk


def show_text():
    value = entry.get()

    label.config(
        text=value
    )


root = tk.Tk()

root.title("入力テスト")
root.geometry("300x200")


entry = tk.Entry(root)
entry.pack()


button = tk.Button(
    root,
    text="表示",
    command=show_text
)

button.pack()


label = tk.Label(root)
label.pack()


root.mainloop()
```
サンプルコードは`input_text.py`を参照。
### 処理の流れ
Entryに文字を入力  
        ↓  
Buttonをクリック  
        ↓
show_text()を実行  
        ↓  
entry.get()で入力値を取得  
        ↓  
label.config()でLabelを更新  

## 18. 活用例
### ファイル選択ダイアログ
#### 用途
ユーザーにファイルを選択してもらう場合に使用。
```python
from tkinter import filedialog

file_path = filedialog.askopenfilename()

print(file_path)
```

#### Pathlibと組み合わせる
ファイルパスを扱う場合は、`pathlib.Path`と組み合わせると扱いやすい。
```python
from pathlib import Path
from tkinter import filedialog


file_path = filedialog.askopenfilename()

path = Path(file_path)

print(path.name)
print(path.suffix)
```

#### 注意点
`askopenfilename()`の戻り値は文字列。  
必要に応じて`Path`オブジェクトに変換する。

## 19. よく使うWidget一覧
Widget | 用途
----- | -----
Label | 文字や画像を表示
Button | ボタン
Entry | 1行入力
Text | 複数行入力
Checkbutton | チェックボックス
Radiobutton | ラジオボタン
Listbox | リスト
Frame | Widgetのグループ化
Canvas | 図形・画像の描画

## 20. よく使うメソッド一覧
メソッド | 用途
----- | -----
pack() | Widgetを配置
grid() | 行・列で配置
place() | 座標で配置
config() | Widgetの設定を変更
get() | 値を取得
set() | 値を設定
insert() | 値を挿入
delete() | 値を削除
bind() | イベントを登録
