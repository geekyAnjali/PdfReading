
import math
import sys

from PyQt5.QtWidgets import (QDialog, QFileDialog, QMainWindow, QMessageBox,
                               QApplication)
from PyQt5.QtCore import QModelIndex, QPoint, QStandardPaths, QUrl 
from Notes import TextEditor
from browse import PDFViewerWidget
from pdfReader_ui import Ui_MainWindow

# a = TextEditor()
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        
        self.add_pdf_bttn.clicked.connect(self.load_pdf)
        self.gridLayout_2.addWidget(TextEditor(self))
        self.pdfViewWidget = PDFViewerWidget(self)
        self.gridLayout_3.addWidget(self.pdfViewWidget)
        
        
        
    def load_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdfViewWidget.setup_ui(file_path)
                                        
                                        
                                        
                                  
if __name__ =="__main__"    :
    import sys
    app = QApplication(sys.argv)                                 
    mWin = MainWindow()
    mWin.show()
    sys.exit(  app.exec_())
        