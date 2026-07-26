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
