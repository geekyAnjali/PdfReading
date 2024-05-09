
import math
import sys

from PyQt5.QtWidgets import (QListWidgetItem,QSplitter, QFileDialog, QMainWindow, QMessageBox,
                               QApplication,QDialog)


from PyQt5.QtCore import QModelIndex, QPoint, QStandardPaths, QUrl ,Qt
from src.Notes import TextEditor
from src.browse import PDFViewerWidget
from src.ui.pdfReader_ui import Ui_MainWindow
import json
import os 
import src.imagrrsrc_rc
from englisttohindi.englisttohindi import EngtoHindi
import threading
from src.FocusTimer import FocusTimer
# a = TextEditor()
class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
  
        self.setupUi(self)
        self.add_pdf_bttn.clicked.connect(self.load_pdf)
        self.remove_pdf_bttn.clicked.connect(self.remove_book_from_listwidget)
        self.gridLayout_6.addWidget(TextEditor(self))

        self.pdfViewWidget =  PDFViewerWidget(self.widget_4)
        self.gridLayout_3.addWidget( self.pdfViewWidget)

        self.book_data = {}
        self.load_books_to_listWidget()
        self.search_bttn.clicked.connect(self.translate_english_to_hindi)
        self.focus_time_bttn.clicked.connect(self.ShowFocusTimer)
        self.focus_music_bttn.clicked.connect(self.playFocusMusic)
        self.Focus_timer = None
    def ShowFocusTimer(self):
        if self.Focus_timer is None: 
            self.Focus_timer = FocusTimer()
            
            self.Focus_timer.show()
    

    def playFocusMusic(self):
        pass 

        
   
    def load_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdfViewWidget.load_pdf(file_path)
            self.add_book(file_path)
            
    def add_book(self,book_path):
        '''
        adds books in listwidget.
        book_path =  location of the book 
        '''
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
   
    def load_books_to_listWidget(self):
        print("loading book..")
        
        if os.path.exists("book_store.json"):
            with open("book_store.json","r", encoding="utf-8") as file:
                print("inside ")
                self.book_data = json.load(file)
                print(self.book_data)
            keys = list(self.book_data.keys())
            self.pdfViewWidget.load_pdf(self.book_data[keys[0]])
            for i in list(self.book_data.values()):
                self.add_book(i)
        else : 
            print("book doesn't exists")
        keys = list(self.book_data.keys())
        print(keys)
            
    def remove_book_from_listwidget(self):
        # self.listWidget.item
        listItem = self.listWidget.takeItem(0)
        print(listItem)
        del listItem
        # self.listWidget.removeItemWidget(curItem)
    
    def translate_english_to_hindi(self):
        def translate_th():
            word = self.lineEdit.text()
            self.res = EngtoHindi(word)
            print(self.res.convert)
            self.label.setText(self.res.convert)

        tTh =threading.Thread(target=translate_th)
        tTh.start()
        
        # return res.convert
if __name__ =="__main__"    :
    import sys
    app = QApplication(sys.argv)                                 
    mWin = MainWindow()
    mWin.show()
    sys.exit(app.exec_())
            