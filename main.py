from PyQt5.QtWidgets import QApplication
from pdfReader import MainWindow

    
if __name__ =="__main__"    :
    import sys
    app = QApplication(sys.argv)                                 
    mWin = MainWindow()
    mWin.show()
    sys.exit(  app.exec_())