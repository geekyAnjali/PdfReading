import sys
import json
import os
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QAction, QPushButton, QVBoxLayout, QWidget, QComboBox, QLabel
import matplotlib.pyplot as plt
from collections import defaultdict
import random

class GraphOptionsWindow(QWidget):
    def __init__(self, records):
        super().__init__()
        self.records = records
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Select Graph Type')
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout()

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Date vs Number of Books Read")
        self.comboBox.addItem("Date vs Total Read Time")
        self.comboBox.currentIndexChanged.connect(self.generateGraph)

        layout.addWidget(QLabel("Select the type of graph:"))
        layout.addWidget(self.comboBox)

        self.setLayout(layout)

    def generateGraph(self):
        graphType = self.comboBox.currentText()

        if graphType == "Date vs Number of Books Read":
            self.plotBooksRead()
        elif graphType == "Date vs Total Read Time":
            self.plotReadTime()

    def plotBooksRead(self):
        dates = []
        books_read = []

        for date, records in self.records.items():
            dates.append(date)
            books_read.append(len(records))

        colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(len(dates))]

        plt.figure(figsize=(10, 5))
        plt.bar(dates, books_read, color=colors, width=0.5)
        plt.xlabel('Date', color='white')
        plt.ylabel('Number of Books Read', color='white')
        plt.title('Date vs Number of Books Read', color='white')
        plt.xticks(rotation=45, color='white')
        plt.yticks(color='white')
        plt.gca().set_facecolor('black')
        plt.gcf().set_facecolor('black')
        plt.tight_layout()
        plt.show()

    def plotReadTime(self):
        dates = []
        total_read_time = []

        for date, records in self.records.items():
            total_time = 0
            for record in records:
                for book, times in record.items():
                    start_time = datetime.strptime(times["start_read_time"], "%Y-%m-%d %H:%M:%S")
                    end_time = datetime.strptime(times["end_read_time"], "%Y-%m-%d %H:%M:%S")
                    total_time += (end_time - start_time).total_seconds()

            dates.append(date)
            total_read_time.append(total_time / 3600)  # Convert seconds to hours

        plt.figure(figsize=(10, 5))
        plt.plot(dates, total_read_time, marker='o', linestyle='-', color='green')
        plt.xlabel('Date', color='white')
        plt.ylabel('Total Read Time (hours)', color='white')
        plt.title('Date vs Total Read Time', color='white')
        plt.xticks(rotation=45, color='white')
        plt.yticks(color='white')
        plt.gca().set_facecolor('black')
        plt.gcf().set_facecolor('black')
        plt.tight_layout()
        plt.show()