import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSizeGrip
from PyQt5.QtCore import QTimer, QTime, Qt

class FocusTimer(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.initUI()
        
    def initUI(self):
     
        self.setGeometry(100, 100, 250, 200)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background: black; color :white;")
        self.timer_label = QLabel(self)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 40px; font-family: Arial; color: #333;")
        self.timer_label.setText("00:00:00")
        
        self.close_button = QPushButton('X', self)
        self.close_button.setStyleSheet(
            "QPushButton { border: none; font-size: 16px; color: #666;width: 30px; height:30px; }"
            "QPushButton:hover {color: #333; background-color:red; }"
        )

        self.close_button.setCursor(Qt.PointingHandCursor)
        self.close_button.clicked.connect(self.close)
        
        # Layouts
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        
        hbox.addWidget(self.close_button, alignment=Qt.AlignTop | Qt.AlignRight)
        vbox.addLayout(hbox)
        vbox.addWidget(self.timer_label, alignment=Qt.AlignCenter)
        
        # Enable resizing
        self.size_grip = QSizeGrip(self)
        vbox.addWidget(self.size_grip, alignment=Qt.AlignBottom | Qt.AlignRight)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.elapsed_time = QTime(0, 0, 0)
        self.timer.start(1000)  # update timer label every second
       

    def updateTimer(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        time_text = self.elapsed_time.toString('hh:mm:ss')
        self.timer_label.setText(time_text)
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()

app = QApplication(sys.argv)
if __name__ == '__main__':
    widget = FocusTimer()
    widget.show()
    sys.exit(app.exec_())
