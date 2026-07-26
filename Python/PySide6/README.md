# PySide6

## 目次

- [1. 概要](#1-概要)
- [2. インストール](#2-インストール)
- [3. インポート](#3-インポート)
- [4. 基本構造](#4-基本構造)
- [5. QApplication](#5-qapplication)
- [6. QWidget](#6-qwidget)
- [7. QPushButton](#7-qpushbutton)
- [8. QLabel](#8-qlabel)
- [9. QLineEdit](#9-qlineedit)
- [10. QTextEdit](#10-qtextedit)
- [11. レイアウト](#11-レイアウト)
- [12. Signal / Slot](#12-signal--slot)
- [13. Lambdaを使用したイベント処理](#13-lambdaを使用したイベント処理)
- [14. QMessageBox](#14-qmessagebox)
- [15. QFileDialog](#15-qfiledialog)
- [16. 実用例](#16-実用例)
- [17. よく使うwidget一覧](#17-よく使うwidget一覧)
- [18. よく使うlayout一覧](#18-よく使うlayout一覧)
- [19. よく使うSignal / Slot一覧](#19-よく使うsignal--slot一覧)
---

## 1. 概要

PySide6は、Qt for Pythonを利用してGUI（Graphical User Interface）アプリケーションを開発するためのPythonライブラリ。

QtのGUIフレームワークをPythonから利用できる。

主な特徴：

- クロスプラットフォーム対応
- 豊富なGUI Widget
- Signal / Slotによるイベント処理
- レイアウト管理
- ダイアログ
- メニュー
- ファイル操作
- Qt Designerとの連携

---

## 2. インストール

`pip`を使用してインストールする。

```bash
pip install PySide6
```

インストール後、Pythonからインポートして使用する。

---

## 3. インポート

PySide6では、用途に応じて必要なクラスをインポートする。

基本的なGUIアプリケーションでは、`PySide6.QtWidgets`からWidgetをインポートする。

```python
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
)
```

ボタンやラベルなどを使用する場合は、必要なWidgetを追加する。

```python
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QWidget,
)
```

---

## 4. 基本構造

PySide6のGUIアプリケーションは、基本的に以下の流れで作成する。

1. 必要なクラスをインポート
2. `QApplication`を作成
3. ウィンドウを作成
4. Widgetを作成
5. Widgetを配置
6. Signal / Slotを設定
7. ウィンドウを表示
8. イベントループを開始

### 基本コード

```python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
)


# QApplicationを作成
app = QApplication(sys.argv)

# ウィンドウを作成
window = QWidget()

# ウィンドウの設定
window.setWindowTitle("My App")
window.resize(400, 300)

# ウィンドウを表示
window.show()

# イベントループを開始
sys.exit(app.exec())
```

### 実行用サンプル

[基本ウィンドウ](./basic_window.py)

---

## 5. QApplication

`QApplication`は、GUIアプリケーション全体を管理するクラス。

基本的にアプリケーションごとに1つ作成する。

```python
import sys

from PySide6.QtWidgets import QApplication


app = QApplication(sys.argv)
```

イベントループは`exec()`で開始する。

```python
app.exec()
```

一般的には、アプリケーション終了時の終了コードを返すために以下のように記述する。

```python
sys.exit(app.exec())
```

---

## 6. QWidget

`QWidget`は、PySide6におけるGUIの基本となるWidget。

単純なウィンドウとして使用できる。

```python
from PySide6.QtWidgets import QWidget


window = QWidget()

window.setWindowTitle("My App")
window.resize(400, 300)

window.show()
```

主なメソッド：

| メソッド | 用途 |
|---|---|
| `setWindowTitle()` | ウィンドウタイトルを設定 |
| `resize()` | ウィンドウサイズを変更 |
| `setGeometry()` | 位置・サイズを指定 |
| `show()` | Widgetを表示 |
| `close()` | Widgetを閉じる |

---

## 7. QPushButton

`QPushButton`は、ボタンを作成するためのWidget。

```python
from PySide6.QtWidgets import QPushButton


button = QPushButton("Click")

button.show()
```

ボタンのテキストを設定する。

```python
button.setText("Click Me")
```

ボタンがクリックされたときの処理は、`clicked` SignalにSlotを接続する。

```python
def click():
    print("Clicked!")


button.clicked.connect(click)
```

---

## 8. QLabel

`QLabel`は、文字列や画像などを表示するためのWidget。

```python
from PySide6.QtWidgets import QLabel


label = QLabel("Hello World")

label.show()
```

テキストを設定する。

```python
label.setText("Hello")
```

テキストを取得する。

```python
text = label.text()
```

---

## 9. QLineEdit

`QLineEdit`は、1行のテキスト入力欄を作成するためのWidget。

```python
from PySide6.QtWidgets import QLineEdit


line_edit = QLineEdit()

line_edit.show()
```

入力値を取得する。

```python
text = line_edit.text()
```

入力値を設定する。

```python
line_edit.setText("Hello")
```

入力内容を削除する。

```python
line_edit.clear()
```

---

## 10. QTextEdit

`QTextEdit`は、複数行のテキスト入力欄を作成するためのWidget。

```python
from PySide6.QtWidgets import QTextEdit


text_edit = QTextEdit()

text_edit.show()
```

テキストを取得する。

```python
text = text_edit.toPlainText()
```

テキストを設定する。

```python
text_edit.setPlainText("Hello")
```

入力内容を削除する。

```python
text_edit.clear()
```

---

## 11. レイアウト

PySide6では、Layoutを使用してWidgetを配置する。

主なLayout：

- `QVBoxLayout`
- `QHBoxLayout`
- `QGridLayout`
- `QFormLayout`

Layoutを使用することで、ウィンドウサイズの変更に合わせてWidgetを自動的に配置できる。

---

### QVBoxLayout

Widgetを縦方向に配置する。

```python
from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
)


layout = QVBoxLayout()

layout.addWidget(
    QPushButton("Button 1")
)

layout.addWidget(
    QPushButton("Button 2")
)
```

イメージ：

```text
┌──────────────┐
│  Button 1    │
├──────────────┤
│  Button 2    │
└──────────────┘
```

---

### QHBoxLayout

Widgetを横方向に配置する。

```python
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
)


layout = QHBoxLayout()

layout.addWidget(
    QPushButton("Button 1")
)

layout.addWidget(
    QPushButton("Button 2")
)
```

イメージ：

```text
┌──────────┬──────────┐
│ Button 1 │ Button 2 │
└──────────┴──────────┘
```

---

### QGridLayout

Widgetを行と列で配置する。

```python
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
)


layout = QGridLayout()

layout.addWidget(
    QLabel("Name"),
    0,
    0,
)

layout.addWidget(
    QLineEdit(),
    0,
    1,
)
```

イメージ：

```text
Name    [             ]
Age     [             ]
Address [             ]
```

---

### QFormLayout

フォーム形式のUIを作成する場合に使用する。

```python
from PySide6.QtWidgets import (
    QFormLayout,
    QLineEdit,
)


layout = QFormLayout()

layout.addRow(
    "Name",
    QLineEdit(),
)

layout.addRow(
    "Age",
    QLineEdit(),
)
```

---

## 12. Signal / Slot

PySide6では、Signal / Slotを利用してイベント処理を実装する。

Signalは、ボタンのクリックやテキスト変更などのイベントが発生したことを通知する。

Slotは、Signalが発生したときに実行する処理。

### Buttonのクリック

```python
def click():
    print("Clicked!")


button.clicked.connect(click)
```

以下のようにSignalとSlotを接続する。

```text
QPushButton
    ↓
clicked Signal
    ↓
connect()
    ↓
Slot（関数）
    ↓
処理を実行
```

### 基本例

```python
from PySide6.QtWidgets import QPushButton


def click():
    print("Clicked!")


button = QPushButton("Click")

button.clicked.connect(click)
```
### @Slotデコレータ

PySide6では、Slotを`@Slot`デコレータで明示的に定義できる。

```python
from PySide6.QtCore import Slot


@Slot()
def on_button_clicked():
    print("Clicked!")
```

引数がある場合は、型を指定する。
```python
@Slot(str)
def on_text_changed(text):
    print(text)
```

SignalとSlotはconnect()で接続する。
```python
button.clicked.connect(
    on_button_clicked
)
```

`@Slot`デコレータは必須ではなく、通常のPython関数やメソッドもSignalに接続できる。
```python
def on_button_clicked():
    print("Clicked!")


button.clicked.connect(
    on_button_clicked
)
```

---

## 13. Lambdaを使用したイベント処理

Signalに引数を渡したい場合などは、Lambdaを使用できる。

```python
button.clicked.connect(
    lambda: print("Clicked!")
)
```

引数を渡す場合：

```python
button.clicked.connect(
    lambda: show_message("Hello")
)
```

例えば、ボタンごとに異なる値を渡したい場合に使用できる。

```python
def show_message(message):
    print(message)


button1.clicked.connect(
    lambda: show_message("Button 1")
)

button2.clicked.connect(
    lambda: show_message("Button 2")
)
```

---

## 14. QMessageBox

`QMessageBox`は、メッセージボックスを表示するために使用する。

### 情報メッセージ

```python
from PySide6.QtWidgets import QMessageBox


QMessageBox.information(
    window,
    "Info",
    "処理が完了しました",
)
```

### 警告メッセージ

```python
QMessageBox.warning(
    window,
    "Warning",
    "入力内容を確認してください",
)
```

### エラーメッセージ

```python
QMessageBox.critical(
    window,
    "Error",
    "エラーが発生しました",
)
```

### 確認ダイアログ

```python
result = QMessageBox.question(
    window,
    "確認",
    "実行しますか？",
)
```

---

## 15. QFileDialog

`QFileDialog`は、ファイル選択や保存先選択などのダイアログを表示する。

### ファイルを開く

```python
from PySide6.QtWidgets import QFileDialog


file_path, _ = QFileDialog.getOpenFileName(
    window,
    "ファイルを選択",
)
```

戻り値は以下の2つ。

```text
file_path
    ↓
選択されたファイルのパス

_
    ↓
選択されたファイルのフィルタ
```

### 複数ファイルを選択

```python
file_paths, _ = QFileDialog.getOpenFileNames(
    window,
    "ファイルを選択",
)
```

### ファイルを保存

```python
file_path, _ = QFileDialog.getSaveFileName(
    window,
    "ファイルを保存",
)
```

---

## 16. 実用例

### 入力した文字列をLabelに表示

`QLineEdit`に入力した文字列を、ボタンをクリックしたタイミングで`QLabel`に表示する。

```python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def show_text():
    value = line_edit.text()

    label.setText(value)


app = QApplication(sys.argv)

window = QWidget()

layout = QVBoxLayout()

line_edit = QLineEdit()

button = QPushButton("表示")

label = QLabel()


button.clicked.connect(
    show_text
)


layout.addWidget(line_edit)

layout.addWidget(button)

layout.addWidget(label)


window.setLayout(layout)

window.show()

sys.exit(app.exec())
```

### 処理の流れ

```text
QLineEditに文字を入力
        ↓
QPushButtonをクリック
        ↓
clicked Signalが発生
        ↓
show_text()を実行
        ↓
line_edit.text()で入力値を取得
        ↓
label.setText()でLabelを更新
```

### 実行用サンプル

[入力文字列を表示](./input_text.py)

---

## 17. よく使うWidget一覧

| Widget | 用途 |
|---|---|
| `QWidget` | GUIの基本Widget |
| `QMainWindow` | メインウィンドウ |
| `QDialog` | ダイアログ |
| `QLabel` | 文字・画像表示 |
| `QPushButton` | ボタン |
| `QToolButton` | ツールボタン |
| `QLineEdit` | 1行テキスト入力 |
| `QTextEdit` | 複数行テキスト入力 |
| `QPlainTextEdit` | プレーンテキスト入力 |
| `QCheckBox` | チェックボックス |
| `QRadioButton` | ラジオボタン |
| `QComboBox` | コンボボックス |
| `QListWidget` | リスト |
| `QTableWidget` | テーブル |
| `QTreeWidget` | ツリー |
| `QProgressBar` | プログレスバー |
| `QSlider` | スライダー |
| `QSpinBox` | 数値入力 |
| `QDateEdit` | 日付入力 |
| `QTimeEdit` | 時刻入力 |
| `QDateTimeEdit` | 日時入力 |

---

## 18. よく使うLayout一覧

| Layout | 用途 |
|---|---|
| `QVBoxLayout` | Widgetを縦方向に配置 |
| `QHBoxLayout` | Widgetを横方向に配置 |
| `QGridLayout` | Widgetを行・列で配置 |
| `QFormLayout` | フォーム形式で配置 |
| `QStackedLayout` | 複数のWidgetを切り替えて表示 |

### QVBoxLayout

```python
layout = QVBoxLayout()
```

縦方向にWidgetを配置する。

### QHBoxLayout

```python
layout = QHBoxLayout()
```

横方向にWidgetを配置する。

### QGridLayout

```python
layout = QGridLayout()
```

行と列を指定してWidgetを配置する。

### QFormLayout

```python
layout = QFormLayout()
```

ラベルと入力欄など、フォーム形式のUIを作成する。

---

## 19. よく使うSignal / Slot一覧

PySide6では、WidgetのイベントをSignal / Slotで処理する。

### よく使うSignal

| Signal | 用途 |
|---|---|
| `clicked` | ボタンがクリックされた |
| `pressed` | ボタンが押された |
| `released` | ボタンが離された |
| `textChanged` | テキストが変更された |
| `textEdited` | ユーザーによってテキストが編集された |
| `currentIndexChanged` | 選択項目が変更された |
| `currentTextChanged` | 選択中のテキストが変更された |
| `stateChanged` | チェック状態が変更された |
| `valueChanged` | 数値が変更された |

### SignalとSlotを接続

```python
button.clicked.connect(
    function
)
```

### 基本例

```python
def function():
    print("処理を実行")


button.clicked.connect(
    function
)
```

### Lambdaを使用

```python
button.clicked.connect(
    lambda: function("Hello")
)
```

### Signal / Slotのイメージ

```text
Widget
    ↓
Signal
    ↓
connect()
    ↓
Slot
    ↓
処理
```

---