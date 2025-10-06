import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

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
    webcam_action.triggered.connect(fd_webcam)

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

    mainWindow.setGeometry(100, 100, 800, 600)
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


def fd_webcam():
    fd.detectFace(1920, 1080)


def fd_webcam_eyes():
    fd.detectEye(1920, 1080)

