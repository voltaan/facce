import sys
from PySide6.QtWidgets import QApplication, QPushButton, QMenuBar, QMenu
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    app.aboutQt()

app = QApplication(sys.argv)

button = QPushButton("Click me")

button.clicked.connect(say_hello)
button.show()

app.exec()