import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QPushButton, QVBoxLayout, QLineEdit, \
    QLabel, QHBoxLayout, QWidget
import faceDetection, webbrowser


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("facce - main window")
        self.setFixedSize(800, 600)

        self.create_menus()

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
        webcam_eyes_action.triggered.connect(self.fd_eye_webcam_dialog)
        fd_menu.addAction(webcam_eyes_action)

        webcam_smile_action = QAction("Open smile detection webcam", self)
        webcam_smile_action.triggered.connect(self.fd_smile_webcam_dialog)
        fd_menu.addAction(webcam_smile_action)

        help_menu = menubar.addMenu("Help")

        open_issue = QAction("Open a new issue...", self)
        open_issue.triggered.connect(self.open_issue)
        help_menu.addAction(open_issue)

        about_facce = QAction("About facce", self)
        about_facce.triggered.connect(self.show_about)
        help_menu.addAction(about_facce)

        about_qt = QAction("About Qt", self)
        about_qt.triggered.connect(QApplication.aboutQt)
        help_menu.addAction(about_qt)

    def show_about(self):
        QMessageBox.information(self, "About facce", "facce version testing \nhttps://github.com/voltaan/facce")

    def fd_webcam_dialog(self):
        faceDetectionOptions = QDialog(self)
        faceDetectionOptions.setFixedSize(500, 300)
        faceDetectionOptions.setWindowTitle("face detection options")

        # Main layout
        layouts = QWidget(faceDetectionOptions)
        layout = QVBoxLayout(layouts)

        # Width
        widthInput = self.add_label_and_input(layout, "Width",
                                              "(e.g. 1280)")

        # Height
        heightInput = self.add_label_and_input(layout, "Height",
                                               "(e.g. 720)")

        # Flip
        flipInput = self.add_label_and_input(layout, "Flip", "If unsure, set to 1")

        redInput, blueInput, greenInput = self.add_color(layout, "Select the color (RGB) to mark the faces detected.")

        # Submit button
        submit = QPushButton("Submit")
        submit.clicked.connect(
            lambda: self.submit_fd(faceDetectionOptions, widthInput.text(), heightInput.text(), flipInput.text(),
                                   redInput.text(), greenInput.text(), blueInput.text()))
        layout.addWidget(submit)

        faceDetectionOptions.setLayout(layout)
        faceDetectionOptions.show()

    def fd_eye_webcam_dialog(self):
        eyeDetectionOptions = QDialog(self)
        eyeDetectionOptions.setFixedSize(500, 300)
        eyeDetectionOptions.setWindowTitle("eye detection options")

        layout = QVBoxLayout(self)

        widthInput = self.add_label_and_input(layout, "Width", "(e.g. 1280)")

        heightInput = self.add_label_and_input(layout, "Height", "(e.g. 720)")

        flipInput = self.add_label_and_input(layout, "Flip", "If unsure set to 1")

        redInput, greenInput, blueInput = self.add_color(layout, "Select the color (RGB) to mark the faces detected.")

        eyeRedInput, eyeGreenInput, eyeBlueInput = self.add_color(layout,
                                                                  "Select the color (RGB) to mark the eyes detected.")

        submit = QPushButton("Submit")
        submit.clicked.connect(
            lambda: self.submit_fd_eye(eyeDetectionOptions, widthInput.text(), heightInput.text(), flipInput.text(),
                                       redInput.text(), greenInput.text(), blueInput.text(), eyeRedInput.text(),
                                       eyeGreenInput.text(), eyeBlueInput.text()))
        layout.addWidget(submit)
        eyeDetectionOptions.setLayout(layout)
        eyeDetectionOptions.show()

    def fd_smile_webcam_dialog(self):
        smileDetectionOptions = QDialog(self)
        smileDetectionOptions.setFixedSize(500, 300)
        smileDetectionOptions.setWindowTitle("smile detection options")

        layouts = QWidget(self)
        layout = QVBoxLayout(layouts)

        widthInput = self.add_label_and_input(layout, "Width", "(e.g. 1280)")

        heightInput = self.add_label_and_input(layout, "Height", "(e.g. 720)")

        flipInput = self.add_label_and_input(layout, "Flip", "If unsure set to 1")

        redInput, greenInput, blueInput = self.add_color(layout, "Select the color (RGB) to mark the faces detected.")

        smileRedInput, smileGreenInput, smileBlueInput = self.add_color(layout,
                                                                        "Select the color (RGB) to mark the smiles detected.")

        submit = QPushButton("Submit")
        submit.clicked.connect(
            lambda: self.submit_fd_smile(smileDetectionOptions, widthInput.text(), heightInput.text(), flipInput.text(),
                                         redInput.text(), greenInput.text(), blueInput.text(), smileRedInput.text(),
                                         smileGreenInput.text(), smileBlueInput.text()))
        layout.addWidget(submit)

        smileDetectionOptions.setLayout(layout)
        smileDetectionOptions.show()

    @staticmethod
    def add_color(layout, message):
        # Color label
        colorLabel = QLabel(message)
        layout.addWidget(colorLabel)

        # Color
        colorLayout = QHBoxLayout()

        redInput = QLineEdit("0")
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
        return redInput, greenInput, blueInput

    @staticmethod
    def add_label_and_input(layout, placeholder, message):
        input_field = QLineEdit("")
        input_field.setPlaceholderText(placeholder)
        label = QLabel(message)
        layout.addWidget(label)
        layout.addWidget(input_field)
        return input_field

    @staticmethod
    def submit_fd(dialog, widthText, heightText, flipText, redText, greenText, blueText):
        try:
            width = int(widthText)
            height = int(heightText)
            flip = int(flipText)
            red = int(redText)
            green = int(greenText)
            blue = int(blueText)
            dialog.hide()
            faceDetection.detectFace(width, height, flip, red, green, blue)
        except Exception as e:
            QMessageBox.critical(dialog, "Error", f"Error: {e}")

    @staticmethod
    def submit_fd_eye(dialog, widthText, heightText, flipText, redText, greenText, blueText, eyeRedText,
                      eyeGreenText, eyeBlueText):
        try:
            width = int(widthText)
            height = int(heightText)
            flip = int(flipText)
            red = int(redText)
            green = int(greenText)
            blue = int(blueText)
            eyeRed = int(eyeRedText)
            eyeGreen = int(eyeGreenText)
            eyeBlue = int(eyeBlueText)
            dialog.hide()
            faceDetection.detectEye(width, height, flip, red, green, blue, eyeRed, eyeGreen, eyeBlue)
        except Exception as e:
            QMessageBox.critical(dialog, "Error", f"Error: {e}")

    @staticmethod
    def submit_fd_smile(dialog, widthText, heightText, flipText, redText, greenText, blueText, smileRedText,
                        smileGreenText, smileBlueText):
        try:
            width = int(widthText)
            height = int(heightText)
            flip = int(flipText)
            red = int(redText)
            green = int(greenText)
            blue = int(blueText)
            smileRed = int(smileRedText)
            smileGreen = int(smileGreenText)
            smileBlue = int(smileBlueText)
            dialog.hide()
            faceDetection.detectSmile(width, height, flip, red, green, blue, smileRed, smileGreen, smileBlue)
        except Exception as e:
            QMessageBox.critical(dialog, "Error", f"Error: {e}")

    @staticmethod
    def open_issue():
        webbrowser.open_new("https://github.com/voltaan/facce/issues")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Gui()
    mainWindow.show()
    sys.exit(app.exec())
