import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

import faceDetectionDialog as fdd

app = QApplication(sys.argv)

mainWindow = QMainWindow()
fdd.fd_webcam_dialog(mainWindow)

mainWindow.show()

app.exec()