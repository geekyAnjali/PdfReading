import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCoreApplication, QUrl
from pdfReader import MainWindow

if __name__=="__main__":
    a = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(QCoreApplication.exec())