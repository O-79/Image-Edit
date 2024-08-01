import sys
import os
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Manager import Manager
from Styles import Styles

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image-Edit v1.0')
        self.setGeometry(100, 50, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.open_button = QAction('Open', self)
        self.open_button.triggered.connect(self.FND_IMG)
        toolbar.addAction(self.open_button)

        self.pixellation_button = QAction('Pixellation', self)
        self.pixellation_button.triggered.connect(self.SET_PXL_SIZ)
        toolbar.addAction(self.pixellation_button)

        self.blur_button = QAction('Stretch', self)
        self.blur_button.triggered.connect(self.SET_BLR_SIZ)
        toolbar.addAction(self.blur_button)

        self.exp_button = QAction('Export', self)
        self.exp_button.triggered.connect(self.EXP_CALL)
        self.exp_button.setEnabled(False)
        toolbar.addAction(self.exp_button)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        self.setStyleSheet(Styles.MISC_0)

        self.MGR = Manager(1, 1)

    def FND_IMG(self):
        IMG_PATH_FULL, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")
        self.IMG_NAME = os.path.basename(IMG_PATH_FULL)
        if self.IMG_NAME:
            self.exp_button.setEnabled(True)
            PIX_MAP = QPixmap(self.IMG_NAME)
            self.image_label.setPixmap(PIX_MAP.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation))

    def SET_PXL_SIZ(self):
        SIZ, ok = QInputDialog.getInt(self, "Pixellation Size", "Enter pixellation size:", min=1)
        if ok:
            self.MGR.PXL_SIZ = SIZ
            print(f"Pixellation size set to: {self.MGR.PXL_SIZ}")

    def SET_BLR_SIZ(self):
        SIZ, ok = QInputDialog.getInt(self, "Stretch Size", "Enter blur size:", min=1)
        if ok:
            self.MGR.BLR_SIZ = SIZ
            print(f"Stretch size set to: {self.MGR.BLR_SIZ}")

    def EXP_CALL(self):
        self.MGR.EXP(self.IMG_NAME)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    VIEW = ImageViewer()
    VIEW.show()
    sys.exit(app.exec())