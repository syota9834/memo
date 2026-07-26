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