import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import Qt

import faceDetection as fd

app = QApplication(sys.argv)
mainWindow = QMainWindow()


def initUI():
    mainWindow.setWindowTitle("facce - main window")

    # Menu bar
    menubar = mainWindow.menuBar()

    # File menu
    file_menu = menubar.addMenu("File")

    exit_action = QAction("Exit", mainWindow)
    exit_action.triggered.connect(mainWindow.close)

    file_menu.addAction(exit_action)

    # Face detection menu
    fd_menu = menubar.addMenu("Face detection")

    webcam_action = QAction("Open face detection webcam", mainWindow)
    webcam_action.triggered.connect(fd_webcam_dialog)

    webcam_eyes_action = QAction("Open eye detection webcam", mainWindow)
    webcam_eyes_action.triggered.connect(fd_webcam_eyes)

    fd_menu.addAction(webcam_action)
    fd_menu.addAction(webcam_eyes_action)

    # Help menu
    help_menu = menubar.addMenu("Help")

    about_facce = QAction("About facce", mainWindow)
    about_facce.triggered.connect(show_about)

    about_qt = QAction("About Qt", mainWindow)
    about_qt.triggered.connect(show_aboutQt)

    help_menu.addAction(about_facce)
    help_menu.addAction(about_qt)

    mainWindow.setFixedSize(800, 600)
    mainWindow.show()
    sys.exit(app.exec())


def show_about():
    QMessageBox.information(
        mainWindow,
        "About facce",
        "facce version testing \nhttps://github.com/voltaan/facce",
    )


def show_aboutQt():
    QApplication.aboutQt()


def fd_webcam_dialog():
    faceDetectionOptions = QDialog(mainWindow)
    faceDetectionOptions.setFixedSize(400, 300)
    faceDetectionOptions.setWindowTitle("face detection options")

    layout = QVBoxLayout(faceDetectionOptions)



    # Width
    widthInput = QLineEdit("",faceDetectionOptions)
    widthInput.setPlaceholderText("Width")
    widthLabel = QLabel("If unsure, put the max width resolution of your webcam (ex 1280)", faceDetectionOptions)
    layout.addWidget(widthInput)
    layout.addWidget(widthLabel)

    # Height
    heightInput = QLineEdit("", faceDetectionOptions)
    heightInput.setPlaceholderText("Height")
    heightLabel = QLabel("If unsure, put the max height resolution of your webcam (ex 720)", faceDetectionOptions)
    layout.addWidget(heightInput)
    layout.addWidget(heightLabel)

    # Submit button
    submit = QPushButton("Submit", faceDetectionOptions)
    layout.addWidget(submit)


    faceDetectionOptions.show()

def fd_webcam(width, height, flip, scaleFactor, minNeighbors, red, green, blue):
    return 0

def fd_webcam_eyes():
    fd.detectEye(1920, 1080)


initUI()
