import sys
import os
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from Manager import Manager
from Styles import Styles

class ImageEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image-Edit v1.0')
        self.setGeometry(100, 50, 800, 600)

        WGT_MAIN = QWidget()
        self.setCentralWidget(WGT_MAIN)
        LAY_MAIN = QVBoxLayout(WGT_MAIN)

        TBR = QToolBar()
        self.addToolBar(TBR)

        self.BUT_OPN = QAction('Open', self)
        self.BUT_OPN.triggered.connect(self.IMG_FND)
        TBR.addAction(self.BUT_OPN)

        self.BUT_HUE = QAction('Hues', self)
        self.BUT_HUE.triggered.connect(self.SET_HUE_SIZ)
        TBR.addAction(self.BUT_HUE)

        self.BUT_PXL = QAction('Pixellation', self)
        self.BUT_PXL.triggered.connect(self.SET_PXL_SIZ)
        TBR.addAction(self.BUT_PXL)

        self.BUT_BLR = QAction('Blur', self)
        self.BUT_BLR.triggered.connect(self.SET_BLR_SIZ)
        TBR.addAction(self.BUT_BLR)

        self.BUT_EXP = QAction('Export', self)
        self.BUT_EXP.triggered.connect(self.EXP_CALL)
        self.BUT_EXP.setEnabled(False)
        TBR.addAction(self.BUT_EXP)

        self.LBL_IMG = QLabel()
        self.LBL_IMG.setAlignment(Qt.AlignmentFlag.AlignCenter)
        LAY_MAIN.addWidget(self.LBL_IMG)

        self.setStyleSheet(Styles.MISC_0)

        self.MGR = Manager(6, 1, 1)

    def IMG_FND(self):
        self.OLD_PATH, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if self.OLD_PATH:
            self.BUT_EXP.setEnabled(True)
            PIX_MAP = QPixmap(self.OLD_PATH)
            self.LBL_IMG.setPixmap(PIX_MAP.scaled(self.LBL_IMG.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation))

    def SET_HUE_SIZ(self):
        #  15,  30,  45,  60,  75,  90,  105,  120,  135,  150
        #       30,       60,       90,        120,        150
        SIZ, ok = QInputDialog.getInt(self, "Hue Iterations", f"Enter number of hue iterations:", min=2, max=11)
        if ok:
            self.MGR.HUE_SIZ = SIZ
            print(f"[LOG] SETUP -> Hue iteration count set to: {self.MGR.HUE_SIZ}")

    def SET_PXL_SIZ(self):
        SIZ, ok = QInputDialog.getInt(self, "Pixellation Size", "Enter pixellation size:", min=1)
        if ok:
            self.MGR.PXL_SIZ = SIZ
            print(f"[LOG] SETUP -> Pixellation size set to: {self.MGR.PXL_SIZ}")

    def SET_BLR_SIZ(self):
        SIZ, ok = QInputDialog.getInt(self, "Blur Size", "Enter blur size:", min=1)
        if ok:
            self.MGR.BLR_SIZ = SIZ
            print(f"[LOG] SETUP -> Blur size set to: {self.MGR.BLR_SIZ}")

    def EXP_CALL(self):
        self.MGR.EXP(self.OLD_PATH)

if __name__ == '__main__':
    APP = QApplication(sys.argv)
    VIEW = ImageEdit()
    VIEW.show()
    sys.exit(APP.exec())