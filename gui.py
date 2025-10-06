import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QPushButton, QVBoxLayout, QLineEdit, \
    QLabel, QHBoxLayout, QWidget

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
    faceDetectionOptions.setFixedSize(500, 400)
    faceDetectionOptions.setWindowTitle("Face Detection Options")

    # Main layout
    layouts = QWidget(faceDetectionOptions)
    layout = QVBoxLayout(layouts)

    # Width
    widthInput = QLineEdit("")
    widthInput.setPlaceholderText("Width")
    widthLabel = QLabel("If unsure, set to the maximum width resolution of your webcam (e.g., 1280)")
    layout.addWidget(widthInput)
    layout.addWidget(widthLabel)

    # Height
    heightInput = QLineEdit("")
    heightInput.setPlaceholderText("Height")
    heightLabel = QLabel("If unsure, set to the maximum height resolution of your webcam (e.g., 720)")
    layout.addWidget(heightInput)
    layout.addWidget(heightLabel)

    # Flip
    flipInput = QLineEdit("")
    flipInput.setPlaceholderText("Flip")
    flipLabel = QLabel("If unsure, set to +1")
    layout.addWidget(flipInput)
    layout.addWidget(flipLabel)

    # Scale factor
    scaleFactorInput = QLineEdit("")
    scaleFactorInput.setPlaceholderText("Scale Factor")
    scaleFactorLabel = QLabel("If unsure, set to 1.0")
    layout.addWidget(scaleFactorInput)
    layout.addWidget(scaleFactorLabel)

    # Minimum neighbors
    minNeighborsInput = QLineEdit("")
    minNeighborsInput.setPlaceholderText("Minimum Neighbors")
    minNeighborsLabel = QLabel("If unsure, set to 5")
    layout.addWidget(minNeighborsInput)
    layout.addWidget(minNeighborsLabel)

    # Red, Green, and Blue
    colorLayout = QHBoxLayout()
    redInput = QLineEdit("255")
    redInput.setPlaceholderText("Red")
    colorLayout.addWidget(redInput)

    greenInput = QLineEdit("0")
    greenInput.setPlaceholderText("Green")
    colorLayout.addWidget(greenInput)

    blueInput = QLineEdit("0")
    blueInput.setPlaceholderText("Blue")
    colorLayout.addWidget(blueInput)

    # Color label
    colorLabel = QLabel("Select the color (RGB) with you want to mark the detected face.")
    layout.addWidget(colorLabel)

    # Add color layout to main layout
    layout.addLayout(colorLayout)

    # Submit button
    submit = QPushButton("Submit", faceDetectionOptions)
    layout.addWidget(submit)

    # Show dialog
    faceDetectionOptions.setLayout(layout)
    faceDetectionOptions.show()


def fd_webcam(width, height, flip, scaleFactor, minNeighbors, red, green, blue):
    fd.detectFace(width, height, flip, scaleFactor, minNeighbors, red, green, blue)

def fd_webcam_eyes():
    fd.detectEye(1920, 1080)


initUI()
