
import math
import sys

from PyQt5.QtWidgets import (QDialog, QFileDialog, QMainWindow, QMessageBox,
                               QSpinBox)
from PyQt5.QtCore import QModelIndex, QPoint, QStandardPaths, QUrl, Slot

from pdfReader_ui import Ui_MainWindow


class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        
        self.add_pdf_bttn.clicked.connect(self.load_pdf)
        
    def load_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        if file_path:
            pass
                                                 
        
        