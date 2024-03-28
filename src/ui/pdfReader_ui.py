# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdfReader.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QVBoxLayout, QWidget)

import src.imagrrsrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1013, 853)
        MainWindow.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton {\n"
"\n"
"	background-color: transparent;\n"
"\n"
" }\n"
"\n"
"/*  QLineEdit{\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPlainTextEdit{\n"
"\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"*/")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, 0, 0)
        self.add_pdf_bttn = QPushButton(self.widget)
        self.add_pdf_bttn.setObjectName(u"add_pdf_bttn")
        self.add_pdf_bttn.setMinimumSize(QSize(30, 30))
        self.add_pdf_bttn.setMaximumSize(QSize(100, 100))
        self.add_pdf_bttn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Images/book-with-add-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_pdf_bttn.setIcon(icon)
        self.add_pdf_bttn.setIconSize(QSize(50, 50))
        self.add_pdf_bttn.setAutoRepeat(True)

        self.gridLayout_5.addWidget(self.add_pdf_bttn, 0, 0, 1, 1)

        self.remove_pdf_bttn = QPushButton(self.widget)
        self.remove_pdf_bttn.setObjectName(u"remove_pdf_bttn")
        self.remove_pdf_bttn.setMinimumSize(QSize(30, 30))
        self.remove_pdf_bttn.setMaximumSize(QSize(100, 100))
        self.remove_pdf_bttn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Images/book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_pdf_bttn.setIcon(icon1)
        self.remove_pdf_bttn.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.remove_pdf_bttn, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(True)
        self.widget_pdf = QWidget(self.splitter)
        self.widget_pdf.setObjectName(u"widget_pdf")
        self.gridLayout_2 = QGridLayout(self.widget_pdf)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.widget_pdf)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy1)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(True)
        self.listWidget = QListWidget(self.splitter_2)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setMinimumSize(QSize(100, 0))
        self.listWidget.setMaximumSize(QSize(200, 16777215))
        self.listWidget.setTabKeyNavigation(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(True)
        self.splitter_2.addWidget(self.listWidget)
        self.widget_4 = QWidget(self.splitter_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter_2.addWidget(self.widget_4)
        self.search_widget = QWidget(self.splitter_2)
        self.search_widget.setObjectName(u"search_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_widget.sizePolicy().hasHeightForWidth())
        self.search_widget.setSizePolicy(sizePolicy3)
        self.search_widget.setMinimumSize(QSize(100, 0))
        self.search_widget.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_4 = QGridLayout(self.search_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.search_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.search_bttn = QPushButton(self.search_widget)
        self.search_bttn.setObjectName(u"search_bttn")
        sizePolicy4.setHeightForWidth(self.search_bttn.sizePolicy().hasHeightForWidth())
        self.search_bttn.setSizePolicy(sizePolicy4)
        self.search_bttn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_bttn.setStyleSheet(u"background-color:transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Images/find.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_bttn.setIcon(icon2)
        self.search_bttn.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.search_bttn, 0, 1, 1, 1)

        self.label = QLabel(self.search_widget)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 2)

        self.splitter_2.addWidget(self.search_widget)

        self.gridLayout_2.addWidget(self.splitter_2, 0, 1, 1, 1)

        self.splitter.addWidget(self.widget_pdf)
        self.widget_7 = QWidget(self.splitter)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_6 = QGridLayout(self.widget_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.widget_7)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_pdf_bttn.setText("")
        self.remove_pdf_bttn.setText("")
        self.search_bttn.setText("")
        self.label.setText("")
    # retranslateUi

if __name__ =="__main__"    :
    import sys
    app = QApplication(sys.argv)   
    widget = QMainWindow()                              
    mWin = Ui_MainWindow()
    mWin.setupUi(widget)
    widget.show()
    
    sys.exit(app.exec_())
            