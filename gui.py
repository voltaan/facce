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
        faceDetectionOptions = QDialog(self)
        faceDetectionOptions.setFixedSize(500, 400)
        faceDetectionOptions.setWindowTitle("face detection options")

        # Main layout
        layouts = QWidget(faceDetectionOptions)
        layout = QVBoxLayout(layouts)

        # Width
        widthInput = self.add_label_and_input(layout, "Width",
                                              "If unsure, set to the maximum width resolution of your webcam (e.g., 1280)")

        # Height
        heightInput = self.add_label_and_input(layout, "Height",
                                               "If unsure, set to the maximum height resolution of your webcam (e.g., 720)")

        # Flip
        flipInput = self.add_label_and_input(layout, "Flip", "If unsure, set to +1")

        # Scale factor
        scaleFactorInput = self.add_label_and_input(layout, "Scale factor", "If unsure, set to 1.0")

        # Minimum neighbors
        self.add_label_and_input(layout, "Minimum neighbors", "If unsure, set to 5")

        # Color
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

        # Add color layout to main layout
        layout.addLayout(colorLayout)

        # Color label
        colorLabel = QLabel("Select the color (RGB) with you want to mark the detected face.")
        layout.addWidget(colorLabel)

        faceDetectionOptions.setLayout(layout)
        faceDetectionOptions.show()


    def add_label_and_input(self, layout, placeholder, message):
        input_field = QLineEdit("")
        input_field.setPlaceholderText(placeholder)
        label = QLabel(message)
        layout.addWidget(input_field)
        layout.addWidget(label)
        return input_field

    def fd_webcam_eyes(self):
        return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Gui()
    mainWindow.show()
    sys.exit(app.exec())
