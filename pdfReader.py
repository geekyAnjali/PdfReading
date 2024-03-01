
import math
import sys

from PyQt5.QtWidgets import (QListWidgetItem,QSplitter, QFileDialog, QMainWindow, QMessageBox,
                               QApplication,QDialog)


from PyQt5.QtCore import QModelIndex, QPoint, QStandardPaths, QUrl ,Qt
from Notes import TextEditor
from browse import PDFViewerWidget
from pdfReader_ui import Ui_MainWindow
import json
import os 

# a = TextEditor()
class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
  
        self.setupUi(self)
        self.add_pdf_bttn.clicked.connect(self.load_pdf)
        # self.gridLayout_2.addWidget(TextEditor(self))
        TextEditor(self.widget_7)
        self.pdfViewWidget =  PDFViewerWidget(self.widget_4)
        # self.gridLayout_3.addWidget( self.pdfViewWidget)
        
        
        # ssplitter1 = QSplitter(Qt.Horizontal)
        # ssplitter1.addWidget(self.listWidget)
        # ssplitter1.addWidget(self.widget_2 )

        # self.gridLayout_3.addWidget(ssplitter1)
        self.book_data = {}
        self.load_all_book()
        
   
    def load_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdfViewWidget.load_pdf(file_path)
            self.add_book(file_path)
            
            # book_item = QListWidgetItem(file_path)
            
    def add_book(self,book_path):
        book_name = book_path.split('/')
        book_name = book_name[len(book_name)-1]
        self.listWidget.addItem(book_name)
        self.store_book(book_name,book_path)
        self.listWidget.itemClicked.connect(self.load_book)
        
    
    def store_book(self,book,path):        
        with open("book_store.json","w") as file : 
            # data = json.load(file)
            self.book_data[book] = path
            json.dump(self.book_data,file,indent=4)
            # print(data)
    def load_book(self,item):
        book_path = self.book_data[item.text()]
        self.pdfViewWidget.load_pdf(book_path)
    
    def load_all_book(self):
        print("loading book..")
        if os.path.exists("book_store.json"):
            with open("book_store.json","r") as file:
                self.book_data = json.load(file)
        for i in list(self.book_data.values()):
            self.add_book(i)
            
            
                     
# if __name__ =="__main__"    :
import sys
app = QApplication(sys.argv)                                 
mWin = MainWindow()
mWin.show()
sys.exit(app.exec_())
        