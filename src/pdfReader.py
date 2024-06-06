
import math
import sys

from PyQt5.QtWidgets import (QListWidgetItem,QSplitter, QFileDialog, QMainWindow, QMessageBox,
                               QApplication,QDialog)


from PyQt5.QtCore import QModelIndex, QPoint, QStandardPaths, QUrl ,Qt
from PyQt5.QtGui import QIcon, QPalette,QColor
from src.modules.Notes import TextEditor
from src.modules.browse import PDFViewerWidget
from src.ui.pdfReader_ui import Ui_MainWindow
import json
import os 
import src.res_rc_rc
from englisttohindi.englisttohindi import EngtoHindi
import threading
from src.modules.FocusTimer import FocusTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from src.modules.read_stats import GraphOptionsWindow

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
        self.read_stats_bttn.clicked.connect(self.showGraphOptions)
        self.dark_mode_bttn.clicked.connect(self.set_dark_theme)
        self.is_timer_active = None
        self.isPlaying = False
        self.media_player = QMediaPlayer()
        self.records = self.load_records()
        self.is_dark = False
        self.set_light_theme()
        

    def load_records(self):
        if os.path.exists("read_records.json"):
            with open("read_records.json", "r") as file:
                return json.load(file)
        return {}

    def ShowFocusTimer(self):
        """
        The ShowFocusTimer is called to show the focus timer : 
        This will start calculating the time from 00:00:00 to+1 , 
        This sends the value of the center of the mainwindows , center positons.
        """
        if self.is_timer_active is None: 
            x_pos = self.x() + self.width()//2 # this position will always be at the top center of the main windows size
            y_pos = self.y()
            self.Focus_timer = FocusTimer(x_pos=x_pos, y_pos=y_pos)
            
            self.Focus_timer.show()
            self.is_timer_active = None
    

    def playFocusMusic(self):
        """ 
            This Focus Music palys a single focus music each time 
            When we click
            This will  Start and stop the music on the same button click , simultaneously
            TO DO: Add different icon to stop the music playing 
        """
        
        if not self.isPlaying:    
            filename = "melody-of-nature-main.mp3"
            current_directory = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(current_directory, "calmMusic", "melody-of-nature-main.mp3")
            print(file_path )
            audio_url = QUrl.fromLocalFile(file_path)
            media_content = QMediaContent(audio_url)
            self.media_player.setMedia(media_content)
            self.media_player.play()
            self.isPlaying = True
            if os.path.exists(file_path):
                print("File exists")
            else:
                print("File does not exist")
        else:
            self.media_player.pause()
            self.isPlaying = False

    def load_pdf(self):
        """
        shows a qfiledialog to openfile 
        and shows the pdf in to the pdfwidget 
        """

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
        """
        This Functions Basically use to store the book name, and it's address to a .json file 
        book --> it's just a .pdf name
        path --> location of the pdf file
        """      
        with open("book_store.json","w") as file : 
            # data = json.load(file)
            self.book_data[book] = path
            json.dump(self.book_data,file,indent=4)
            # print(data)
        
    def load_book(self,item):
        book_path = self.book_data[item.text()]
        self.pdfViewWidget.load_pdf(book_path)
   
    def load_books_to_listWidget(self):        
        if os.path.exists("book_store.json"):
            with open("book_store.json","r", encoding="utf-8") as file:
                print("inside ")
                self.book_data = json.load(file)
                print(self.book_data)
            keys = list(self.book_data.keys())
            if len(keys) > 0:
                self.pdfViewWidget.load_pdf(self.book_data[keys[0]])
                for i in list(self.book_data.values()):
                    self.add_book(i)
        else : 
            print("book doesn't exists")
        keys = list(self.book_data.keys())
        # print(keys)
            
    def remove_book_from_listwidget(self):
        # self.listWidget.item
        try :
            book_name = self.listWidget.item(0).text()
            listItem = self.listWidget.takeItem(0)
            
            del listItem
            with open("book_store.json","r+",encoding="utf-8") as file :
                self.book_data = json.load(file)
                print(self.book_data[book_name])
                # del self.book_data[book_name]
                # json.dump(self.book_data,file,indent=4)
        except Exception as e : 
            print(e)
            QMessageBox.about(self,"Error","No book to remove")
            return

            
        # self.listWidget.removeItemWidget(curItem)
    
    def translate_english_to_hindi(self):
        def translate_th():
            word = self.lineEdit.text()
            self.res = EngtoHindi(word)
            self.label.setText(self.res.convert)

        tTh =threading.Thread(target=translate_th)
        tTh.start()

    def showGraphOptions(self):
        """
        The show Graph Options show a dialog box to select to types of graph mode 
        1) Books and Read timer 
        2) Date and Total book read in particular date
        """
        self.graphOptionsWindow = GraphOptionsWindow(self.records)
        self.graphOptionsWindow.show()
    
    def closeEvent(self,event):
        """
            When the main window will be closed , it will help in closing the another windows.
        """
        try: 
            self.Focus_timer.close()
        except AttributeError as e : 
            print(e)
        # return res.convert
    def set_light_theme(self):
        
        print("light theme set")
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        # palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        # palette.setColor(QPalette.Base, QColor(240, 240, 240))
        # palette.setColor(QPalette.AlternateBase, QColor(255, 255, 255))
        # palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        # palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        # palette.setColor(QPalette.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.Button, QColor(255, 255, 255))
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
        # palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        self.setStyleSheet("""
        QWidget {
                background-color: #cbabd4;
               
            }
            QLabel {
                 background-color: #cbabd4;
                }
                QTextEdit{
                    background-color: #fbefff;
                }
                    QPushButton:hover {
border:1px solid #ac91b4;
background-color : #ac91b4;
   
    }

    QPushButton:pressed {
        background-color: #b66fd4;
    }
                """)
        self.is_dark = False
        QApplication.instance().setPalette(palette)
    
    def set_dark_theme(self):
        if not self.is_dark: 
            palette = QPalette()
            print("dark theme set")
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            # palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
            # palette.setColor(QPalette.Base, QColor(35, 35, 35))
            # palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            # palette.setColor(QPalette.ToolTipBase, QColor(12, 0, 255))
            # palette.setColor(QPalette.ToolTipText, QColor(12, 0, 255))
            # palette.setColor(QPalette.Text, QColor(155, 155, 255))
            # palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
            palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
            
            QApplication.instance().setPalette(palette)
            self.setStyleSheet("""
            QWidget {
                background-color: #313535;
               
            }
            QLabel {
                 background-color: #313535;
                }
                  QTextEdit{
                    background-color:#8d8d8d ;
                }
                    QPushButton:hover {
border:1px solid #797979;
background-color : #797979;
   
    }

    QPushButton:pressed {
        background-color: #5d5d5d;
    }

        """)
            self.is_dark = True 
        else :
            self.set_light_theme()

def main():
    import sys
    app = QApplication(sys.argv)                                 
    mWin = MainWindow()
    mWin.setWindowIcon(QIcon("stationery.ico"))
    mWin.setWindowTitle("PDFNoteFusion")
    mWin.show()
    sys.exit(app.exec_())

if __name__ =="__main__"    :
    main()
            