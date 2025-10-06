import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QPushButton, QVBoxLayout, QLineEdit, \
    QLabel, QHBoxLayout, QWidget


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("facce - main window")
        self.setFixedSize(800, 600)

        self.create_menus()

    # Create app menus
    def create_menus(self):
        # Initialize menubar as the main window menu bar
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        # Exit action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        fd_menu = menubar.addMenu("Face detection")
        webcam_action = QAction("Open face detection webcam", self)
        webcam_action.triggered.connect(self.fd_webcam_dialog)
        fd_menu.addAction(webcam_action)

        webcam_eyes_action = QAction("Open eye detection webcam", self)
        webcam_eyes_action.triggered.connect(self.fd_webcam_eyes)
        fd_menu.addAction(webcam_eyes_action)

        help_menu = menubar.addMenu("Help")
        about_facce = QAction("About facce", self)
        about_facce.triggered.connect(self.show_about)
        help_menu.addAction(about_facce)

        about_qt = QAction("About Qt")
        about_qt.triggered.connect(QApplication.aboutQt)
        help_menu.addAction(about_qt)

    def show_about(self):
        QMessageBox.information(self, "About facce", "facce version testing \nhttps://github.com/voltaan/facce")

    def fd_webcam_dialog(self):
        return 0

    def fd_webcam_eyes(self):
        return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Gui()
    mainWindow.show()
    sys.exit(app.exec())
