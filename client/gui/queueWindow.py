#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QMainWindow, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class QueueWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init()

    def init(self):
        columnLayout = QVBoxLayout()
        waitLabel = QLabel("Poczekaj na kolejnego gracza", self)
        waitLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        waitLabel.setAlignment(Qt.AlignCenter)
        waitLabel.setFont(QFont('Arial', 16))
        columnLayout.addWidget(waitLabel)

        self.setLayout(columnLayout)
        self.setGeometry(700, 400, 400, 200)
        self.setWindowTitle("Szachy kolejka")
        self.show()