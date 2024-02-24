# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdfReader.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import imagrrsrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(921, 769)
        MainWindow.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton {\n"
"\n"
"	background-color: rgb(31, 112, 116);\n"
"border-radius:8px;\n"
" }\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPlainTextEdit{\n"
"\n"
"background-color: rgb(255, 255, 255);}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 30))
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.widget.setStyleSheet(u"background-color: rgb(134, 134, 134);\n"
"background-color: rgb(70, 70, 70);")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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

        self.horizontalLayout.addWidget(self.add_pdf_bttn)

        self.remove_pdf_bttn = QPushButton(self.widget)
        self.remove_pdf_bttn.setObjectName(u"remove_pdf_bttn")
        self.remove_pdf_bttn.setMinimumSize(QSize(30, 30))
        self.remove_pdf_bttn.setMaximumSize(QSize(100, 100))
        self.remove_pdf_bttn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Images/book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_pdf_bttn.setIcon(icon1)
        self.remove_pdf_bttn.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.remove_pdf_bttn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget)

        self.widget_pdf = QWidget(self.centralwidget)
        self.widget_pdf.setObjectName(u"widget_pdf")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_pdf)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(self.widget_pdf)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.pdf_widget = QWidget(self.widget_pdf)
        self.pdf_widget.setObjectName(u"pdf_widget")

        self.horizontalLayout_2.addWidget(self.pdf_widget)

        self.search_widget = QWidget(self.widget_pdf)
        self.search_widget.setObjectName(u"search_widget")
        self.search_widget.setMinimumSize(QSize(100, 0))
        self.search_widget.setMaximumSize(QSize(203, 16777215))
        self.gridLayout_4 = QGridLayout(self.search_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.search_bttn = QPushButton(self.search_widget)
        self.search_bttn.setObjectName(u"search_bttn")
        self.search_bttn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Images/find.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_bttn.setIcon(icon2)
        self.search_bttn.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.search_bttn, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.search_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.label = QLabel(self.search_widget)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.search_widget)


        self.verticalLayout.addWidget(self.widget_pdf)

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 250))
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout.addWidget(self.widget_7)

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

