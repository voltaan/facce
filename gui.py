import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("facce - main window")

        # Menu bar
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        # Face detection menu
        fd_menu = menubar.addMenu("Face detection")

        webcam_action = QAction("Open webcam", self)
        webcam_action.triggered.connect(self.fd_webcam)

        fd_menu.addAction(webcam_action)

        # Help menu
        help_menu = menubar.addMenu("Help")

        about_facce = QAction("About facce", self)
        about_facce.triggered.connect(self.show_about)

        about_qt = QAction("About Qt", self)
        about_qt.triggered.connect(self.show_aboutQt)

        help_menu.addAction(about_facce)
        help_menu.addAction(about_qt)

        self.setGeometry(100, 100, 800, 600)
        self.show()

    def show_about(self):
        QMessageBox.information(
            self,
            "About facce",
            "facce version testing \nhttps://github.com/voltaan/facce",
        )

    def show_aboutQt(self):
        QApplication.aboutQt()

    def fd_webcam(self):
        return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
